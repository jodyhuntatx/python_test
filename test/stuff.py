#!/usr/bin/env python3

import base64
import os
import pathlib
import sys
from pprint import pprint

import conjur
from conjur.rest import ApiException

CONJUR_APPLIANCE_HOSTNAME = os.environ["CONJUR_APPLIANCE_HOSTNAME"]
ACCOUNT_NAME = os.environ["CONJUR_ACCOUNT"]
LOGIN = os.environ["CONJUR_AUTHN_LOGIN"]
ADMIN_PASSWORD = os.environ["CONJUR_AUTHN_API_KEY"]
CONJUR_CERT_FILE = '/config/conjur-cert.pem'

print("CONJUR_APPLIANCE_HOSTNAME = " + CONJUR_APPLIANCE_HOSTNAME)
print("ACCOUNT_NAME = " + ACCOUNT_NAME)
print("LOGIN = " + LOGIN)
print("ADMIN_PASSWORD = " + ADMIN_PASSWORD)
print("CONJUR_CERT_FILE = " + CONJUR_CERT_FILE)

# Setup API client config
config = conjur.Configuration()
config.host = "https://" + CONJUR_APPLIANCE_HOSTNAME
config.debug = True
config.username = LOGIN
config.password = ADMIN_PASSWORD
config.verify_ssl = True
config.ssl_ca_cert = CONJUR_CERT_FILE

# Enter a context with an instance of the API client
with conjur.ApiClient(config) as api_client:

    # check for Conjur OSS vs Conjur Enterprise client library
    try:
        status_api = conjur.StatusApi(api_client)
        status_api.info()
    except AttributeError:
        print("Using OSS client")
        exit(1)
    else:
        print("Using Enterprise client")

    # Create an instance of the API class
    api_instance = conjur.AuthenticationApi(api_client)
    login = LOGIN
    account = ACCOUNT_NAME			# str | Organization account name
#    accept_encoding = 'application/json'
    accept_encoding = 'base64'
    api_key = 'init'
    access_token = 'init'
    x_request_id = 'test-id'			# str | Add an ID to the request being made 
						# so it can be tracked in Conjur. 
						# If not provided the server will automatically
						# generate one.  (optional)

    try:
        # Gets the API key of a user given the username and password via HTTP Basic Authentication. 
        api_key = api_instance.get_api_key(account, x_request_id=x_request_id)
        pprint(api_key)
    except ApiException as e:
        print("Exception when calling AuthenticationApi->get_api_key: %s\n" % e)

    try:
        # Gets a short-lived access token, which is required in the header of most subsequent API requests. 
        access_token = api_instance.get_access_token(account,
							login, api_key,
							accept_encoding=accept_encoding,
							x_request_id=x_request_id)
        pprint(access_token)
    except ApiException as e:
        print("Exception when calling AuthenticationApi->get_access_token: %s\n" % e)

# Constants
new_password = "N3w-Passw0rd!"
secret = "supersecretstuff"
secret_id = "sampleSecret"
simple_policy = None
with open("config/policy/simple.yml", "r") as file:
    empty_policy = file.read()
policy = None
with open("config/policy/policy.yml", "r") as file:
    policy = file.read()

# Change admin password, uses basicAuth
print("\nChanging admin password...")
login_api.change_password(
    body=new_password,
    account=ACCOUNT_NAME
)
print("Password change successful.")

api_client.configuration.password = new_password

# Add Conjur Token header to client configuration
token_body = 'token="{}"'.format(access_token)
api_client.configuration.api_key = {'Authorization': token_body}
api_client.configuration.api_key_prefix = {'Authorization': 'Token'}

policy_api = conjur.PoliciesApi(api_client)
login_api = conjur.AuthenticationApi(api_client)

# Load simple policy, which only defines an admin user
# Allows the example to be run multiple times sequentially
# Loading a policy returns data for users CREATED when the policy is loaded. Without loading
# the simple policy, if the user alice already exists due to a prior example run, loading
# the full policy will not respond with alice's api key.
print("\nLoading simple root policy...")
policy_api.replace_policy(
    ACCOUNT_NAME,
    "root",
    empty_policy
)
print("Empty policy loaded.")

# Load a policy using api client
print("\nLoading root policy...")
loaded_results = policy_api.replace_policy(
    ACCOUNT_NAME,
    "root",
    body=policy
)
print("Policy loaded.")

alice_api_key = loaded_results.created_roles["dev:user:alice"]["api_key"]
print("Alice API key: ", alice_api_key)

# Rotate Alice's API key, uses conjurAuth
print("\nRotating alice API key...")
alice_api_key = login_api.rotate_api_key(
    ACCOUNT_NAME,
    role="user:alice"
)
print("New API key:", alice_api_key)

# Store a secret, uses conjurAuth
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

# Retrieve secrets, uses conjurAuth
print("\nRetrieving secret...")
retrieved_secret = secrets_api.get_secret(
    ACCOUNT_NAME,
    "variable",
    secret_id
)
print("Retrieved seceret: ", retrieved_secret)

if retrieved_secret != secret:
    print("Secret Malformed.")
    print("Secret stored: ", secret)
    print("Secret retrieved: ", retrieved)
    sys.exit(1)

print("\nDone!")
