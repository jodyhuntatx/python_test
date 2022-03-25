#!/usr/bin/env python3

# NOTE: Editing this file in the container changes the file in the host directory.

from __future__ import print_function
import time
import sys
import os
import base64
from pprint import pprint

import conjur
from conjur.rest import ApiException

# pull env vars into global vars
CONJUR_APPLIANCE_HOSTNAME = os.environ["CONJUR_APPLIANCE_HOSTNAME"]
ACCOUNT_NAME = os.environ["CONJUR_ACCOUNT"]
LOGIN = os.environ["CONJUR_AUTHN_LOGIN"]
ADMIN_PASSWORD = os.environ["CONJUR_AUTHN_API_KEY"]
CONJUR_CERT_FILE = './conjur-cert.pem'
SIMPLE_POLICY_FILE = './policy/simple_policy.yml'
ROOT_POLICY_FILE = './policy/root_policy.yml'
DELETE_POLICY_FILE = './policy/delete_policy.yml'
DEBUG = bool(os.environ["DEBUG"] == "True")

if DEBUG:
  print("CONJUR_APPLIANCE_HOSTNAME = " + CONJUR_APPLIANCE_HOSTNAME)
  print("ACCOUNT_NAME = " + ACCOUNT_NAME)
  print("LOGIN = " + LOGIN)
  print("ADMIN_PASSWORD = " + ADMIN_PASSWORD)
  print("CONJUR_CERT_FILE = " + CONJUR_CERT_FILE)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# See configuration.py for a list of all supported configuration parameters.

# Configure HTTP basic authorization: basicAuth
config= conjur.Configuration()
config.host = "https://" + CONJUR_APPLIANCE_HOSTNAME
config.verify_ssl = True
config.ssl_ca_cert = CONJUR_CERT_FILE
config.debug = bool(DEBUG)
config.username = LOGIN
config.password = ADMIN_PASSWORD

# Enter a context with an instance of the API client
with conjur.ApiClient(config) as api_client:

    ##############################################
    # Create an instance of the Authentication API class
    authn_api = conjur.AuthenticationApi(api_client)

    account = ACCOUNT_NAME	# str | Organization account name
    x_request_id = 'test-id'	# str | Add an ID to the request being made so it can be tracked in Conjur.
				# If not provided the server will automatically generate one.  (optional)
    api_key = 'init'
    access_token = 'init'

    try:
        # Gets the API key of a user given the username and password via HTTP Basic Authentication. 
        api_key = authn_api.get_api_key(account, x_request_id=x_request_id)
        pprint("API key: " + api_key)
    except ApiException as e:
        print("Exception when calling AuthenticationApi->get_api_key: %s\n" % e)

    try:
        # Gets a short-lived access token, which is required in the header of most subsequent API requests. 
        access_token = authn_api.get_access_token(account, 
						  login=LOGIN,
						  body=api_key,
						  accept_encoding='base64',
						  x_request_id=x_request_id)
        pprint("Access token: " + access_token)
    except ApiException as e:
        print("Exception when calling AuthenticationApi->get_access_token: %s\n" % e)

    # Add Conjur Authorization Token header to client configuration
    #   Note that the token has a TTL of 8 minutes and would need to be refreshed
    #   by reauthenticating and.
    token_body = 'token="{}"'.format(access_token)
    api_client.configuration.api_key = {'Authorization': token_body}
    api_client.configuration.api_key_prefix = {'Authorization': 'Token'}

    ##############################################
    # API key rotation

    # Rotate Alice user's API key
    print("\nRotating Alice user\'s API key...")
    try:
        # Rotates a role's API key.
        new_api_key = authn_api.rotate_api_key(account=ACCOUNT_NAME,
						role="user:alice",
						x_request_id=x_request_id)
        print("New API key:", new_api_key)
    except ApiException as e:
        print("Exception when calling AuthenticationApi->rotate_api_key: %s\n" % e)

    ##############################################
    # Load policies

    simple_policy = None
    root_policy = None
    delete_policy = None

    # read policy docs
    with open(SIMPLE_POLICY_FILE, "r") as file:
      simple_policy = file.read()
    with open(ROOT_POLICY_FILE, "r") as file:
      root_policy = file.read()
    with open(DELETE_POLICY_FILE, "r") as file:
      delete_policy = file.read()

    policies_instance = conjur.PoliciesApi(api_client)

    try:
        print("\nLoading simple policy...")
        api_response = policies_instance.load_policy(account=ACCOUNT_NAME,
						     identifier='root',
						     body=simple_policy,
						     x_request_id=x_request_id)
        pprint(api_response)
        print("Simple policy loaded.")

        print("\nLoading root policy...")
        api_response = policies_instance.load_policy(account=ACCOUNT_NAME,
						     identifier='root',
						     body=root_policy,
						     x_request_id=x_request_id)
        pprint(api_response)
        print("Root policy loaded.")
    except ApiException as e:
        print("Exception when calling PoliciesApi->load_policy: %s\n" % e)


    ##############################################
    # Secret set/get

    secret_id = "sampleSecret"		# secret name
    secret_value = "initialsecret"	# secret value
    retrieved_secret = 'init'

    secrets_api = conjur.SecretsApi(api_client)

    # Store a secret
    try:
        print("\nStoring secret...")
        print("Secret data: ", secret_value)
        # Creates a secret value within the specified variable.
        secrets_api.create_secret(account=ACCOUNT_NAME,
				  kind='variable',
				  identifier=secret_id,
				  body=secret_value,
				  x_request_id=x_request_id)
        print("Secret stored.")
    except ApiException as e:
        print("Exception when calling SecretsApi->create_secret: %s\n" % e)

    # Retrieve secret
    try:
        print("\nRetrieving secret...")
        # Fetches the value of a secret from the specified Secret.
        retrieved_secret = secrets_api.get_secret(account=ACCOUNT_NAME,
						  kind='variable',
						  identifier=secret_id,
						  x_request_id=x_request_id)
        print("Retrieved secret: ", retrieved_secret)
    except ApiException as e:
        print("Exception when calling SecretsApi->get_secret: %s\n" % e)

    secret_value = "changedsecret"		# new secret value

    # Store a secret
    try:
        print("\nStoring secret...")
        print("Secret data: ", secret_value)
        # Creates a secret value within the specified variable.
        secrets_api.create_secret(account=ACCOUNT_NAME,
                                  kind='variable',
                                  identifier=secret_id,
                                  body=secret_value,
                                  x_request_id=x_request_id)
        print("Secret stored.")
    except ApiException as e:
        print("Exception when calling SecretsApi->create_secret: %s\n" % e)

    # Retrieve secret
    try:
        print("\nRetrieving old version of secret...")
        retrieved_secret = secrets_api.get_secret(account=ACCOUNT_NAME,
                                                kind='variable',
                                                identifier=secret_id,
                                                version=1,
                                                x_request_id=x_request_id)
        print("Retrieved secret: ", retrieved_secret)

        print("\nRetrieving current version of secret...")
        retrieved_secret = secrets_api.get_secret(account=ACCOUNT_NAME,
                                                kind='variable',
                                                identifier=secret_id,
                                                x_request_id=x_request_id)
        print("Retrieved secret: ", retrieved_secret)
    except ApiException as e:
        print("Exception when calling SecretsApi->get_secret: %s\n" % e)


    ##############################################
    # Delete secret w/ delete policy
    try:
        print("\nLoading delete policy...")
        api_response = policies_instance.update_policy(account=ACCOUNT_NAME,
                                                     identifier='root',
                                                     body=delete_policy,
                                                     x_request_id=x_request_id)
        pprint(api_response)
        print("Delete policy loaded.")
    except ApiException as e:
        print("Exception when calling PoliciesApi->load_policy: %s\n" % e)

# end - with conjur.ApiClient()

print("\nDone!")
