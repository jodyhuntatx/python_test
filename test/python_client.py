#!/usr/bin/env python3

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
CONJUR_CERT_FILE = '/config/conjur-cert.pem'
SIMPLE_POLICY_FILE = '/config/policy/simple.yml'
POLICY_FILE = '/config/policy/policy.yml'

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
config.debug = False
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
    accept_encoding = 'base64'

    try:
        # Gets the API key of a user given the username and password via HTTP Basic Authentication. 
        api_key = authn_api.get_api_key(account, x_request_id=x_request_id)
        pprint("API key: " + api_key)
    except ApiException as e:
        print("Exception when calling AuthenticationApi->get_api_key: %s\n" % e)

    try:
        # Gets a short-lived access token, which is required in the header of most subsequent API requests. 
        access_token = authn_api.get_access_token(account, 
							login=LOGIN, body=api_key,
							accept_encoding=accept_encoding,
							x_request_id=x_request_id)
        pprint("Access token: " + access_token)
    except ApiException as e:
        print("Exception when calling AuthenticationApi->get_access_token: %s\n" % e)

    # Add Conjur Token header to client configuration
    token_body = 'token="{}"'.format(access_token)
    api_client.configuration.api_key = {'Authorization': token_body}
    api_client.configuration.api_key_prefix = {'Authorization': 'Token'}

    simple_policy = None
    with open(SIMPLE_POLICY_FILE, "r") as file:
      empty_policy = file.read()
    policy = None
    with open(POLICY_FILE, "r") as file:
      policy = file.read()

    ##############################################
    # Create an instance of the Policies API class
    policies_instance = conjur.PoliciesApi(api_client)

    try:
        # Load simple policy, which only defines an admin user
        api_response = policies_instance.load_policy(account=ACCOUNT_NAME,
						identifier='root', body=empty_policy, x_request_id=x_request_id)
        pprint(api_response)
        print("Empty policy loaded.")

	# Load more complex policy with users
        api_response = policies_instance.load_policy(account=ACCOUNT_NAME,
						identifier='root', body=policy, x_request_id=x_request_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PoliciesApi->load_policy: %s\n" % e)


    ##############################################
    # API key rotation

    # Rotate Alice's API key, uses conjurAuth
    print("\nRotating alice API key...")
    alice_api_key = authn_api.rotate_api_key(
        ACCOUNT_NAME,
        role="user:alice"
    )
    print("New API key:", alice_api_key)

    ##############################################
    # Secret set/get

    secret_id = "sampleSecret"		# secret name
    secret = "initialsecret"		# secret value

    # Store a secret
    print("\nStoring secret...")
    secrets_api = conjur.SecretsApi(api_client)
    print("Secret data: ", secret)
    secrets_api.create_secret(
        ACCOUNT_NAME,
        "variable",
        secret_id,
        body=secret
    )
    print("Secret stored.")

    # Retrieve secrets
    print("\nRetrieving secret...")
    retrieved_secret = secrets_api.get_secret(
        ACCOUNT_NAME,
        "variable",
        secret_id
    )
    print("Retrieved secret: ", retrieved_secret)

    secret = "changedsecret"		# new secret value

    # Store a secret
    print("\nStoring secret...")
    secrets_api = conjur.SecretsApi(api_client)
    print("Secret data: ", secret)
    secrets_api.create_secret(
        ACCOUNT_NAME,
        "variable",
        secret_id,
        body=secret
    )
    print("Secret stored.")

    # Retrieve secrets
    print("\nRetrieving secret...")
    retrieved_secret = secrets_api.get_secret(
        ACCOUNT_NAME,
        "variable",
        secret_id
    )
    print("Retrieved secret: ", retrieved_secret)


    if retrieved_secret != secret:
        print("Secret Malformed.")
        print("Secret stored: ", secret)
        print("Secret retrieved: ", retrieved)
        sys.exit(1)

    print("\nDone!")
