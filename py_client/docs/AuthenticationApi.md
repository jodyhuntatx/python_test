# conjur.AuthenticationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_password**](AuthenticationApi.md#change_password) | **PUT** /authn/{account}/password | Changes a user’s password.
[**enable_authenticator**](AuthenticationApi.md#enable_authenticator) | **PATCH** /{authenticator}/{account} | Enables or disables authenticator defined without service_id.
[**enable_authenticator_instance**](AuthenticationApi.md#enable_authenticator_instance) | **PATCH** /{authenticator}/{service_id}/{account} | Enables or disables authenticator service instances.
[**get_access_token**](AuthenticationApi.md#get_access_token) | **POST** /authn/{account}/{login}/authenticate | Gets a short-lived access token, which is required in the header of most subsequent API requests. 
[**get_access_token_via_aws**](AuthenticationApi.md#get_access_token_via_aws) | **POST** /authn-iam/{service_id}/{account}/{login}/authenticate | Get a short-lived access token for applications running in AWS.
[**get_access_token_via_azure**](AuthenticationApi.md#get_access_token_via_azure) | **POST** /authn-azure/{service_id}/{account}/{login}/authenticate | Gets a short-lived access token for applications running in Azure.
[**get_access_token_via_gcp**](AuthenticationApi.md#get_access_token_via_gcp) | **POST** /authn-gcp/{account}/authenticate | Gets a short-lived access token for applications running in Google Cloud Platform. 
[**get_access_token_via_jwt**](AuthenticationApi.md#get_access_token_via_jwt) | **POST** /authn-jwt/{service_id}/{account}/authenticate | Gets a short-lived access token for applications using JSON Web Token (JWT) to access the Conjur API. 
[**get_access_token_via_jwt_with_id**](AuthenticationApi.md#get_access_token_via_jwt_with_id) | **POST** /authn-jwt/{service_id}/{account}/{id}/authenticate | Gets a short-lived access token for applications using JSON Web Token (JWT) to access the Conjur API. Covers the case of use of optional URL parameter \&quot;ID\&quot; 
[**get_access_token_via_kubernetes**](AuthenticationApi.md#get_access_token_via_kubernetes) | **POST** /authn-k8s/{service_id}/{account}/{login}/authenticate | Gets a short-lived access token for applications running in Kubernetes.
[**get_access_token_via_ldap**](AuthenticationApi.md#get_access_token_via_ldap) | **POST** /authn-ldap/{service_id}/{account}/{login}/authenticate | Gets a short-lived access token for users and hosts using their LDAP identity to access the Conjur API. 
[**get_access_token_via_oidc**](AuthenticationApi.md#get_access_token_via_oidc) | **POST** /authn-oidc/{service_id}/{account}/authenticate | Gets a short-lived access token for applications using OpenID Connect (OIDC) to access the Conjur API. 
[**get_api_key**](AuthenticationApi.md#get_api_key) | **GET** /authn/{account}/login | Gets the API key of a user given the username and password via HTTP Basic Authentication. 
[**get_api_key_via_ldap**](AuthenticationApi.md#get_api_key_via_ldap) | **GET** /authn-ldap/{service_id}/{account}/login | Gets the Conjur API key of a user given the LDAP username and password via HTTP Basic Authentication. 
[**k8s_inject_client_cert**](AuthenticationApi.md#k8s_inject_client_cert) | **POST** /authn-k8s/{service_id}/inject_client_cert | For applications running in Kubernetes; sends Conjur a certificate signing request (CSR) and requests a client certificate injected into the application&#39;s Kubernetes pod. 
[**rotate_api_key**](AuthenticationApi.md#rotate_api_key) | **PUT** /authn/{account}/api_key | Rotates a role&#39;s API key.


# **change_password**
> change_password(account, body, x_request_id=x_request_id)

Changes a user’s password.

You must provide the login name and current password or API key of the user whose password is to be updated in an HTTP Basic Authentication header. Also replaces the user’s API key with a new securely generated random value. You can fetch the new API key using the Login method.  The Basic authentication-compliant header is formed by: 1. Concatenating the role's name, a literal colon character ':',    and the password or API key to create the authentication string. 2. Base64-encoding the authentication string. 3. Prefixing the authentication string with the scheme: `Basic `    (note the required space). 4. Providing the result as the value of the `Authorization` HTTP header:    `Authorization: Basic <authentication string>`.  Your HTTP/REST client probably provides HTTP basic authentication support. For example, `curl` and all of the Conjur client libraries provide this.  Note that machine roles (Hosts) do not have passwords. They authenticate using their API keys, while passwords are only used by human users. 

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import conjur
from conjur.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = conjur.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = conjur.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with conjur.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = conjur.AuthenticationApi(api_client)
    account = 'account_example' # str | Organization account name
body = 'body_example' # str | New password
x_request_id = 'test-id' # str | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  (optional)

    try:
        # Changes a user’s password.
        api_instance.change_password(account, body, x_request_id=x_request_id)
    except ApiException as e:
        print("Exception when calling AuthenticationApi->change_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| Organization account name | 
 **body** | **str**| New password | 
 **x_request_id** | **str**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The password has been changed |  -  |
**400** | The server cannot process the request due to malformed request syntax |  -  |
**401** | Authentication information is missing or invalid |  -  |
**422** | A request parameter was either missing or invalid. |  -  |
**500** | Malfromed request, rejected by the server |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_authenticator**
> enable_authenticator(authenticator, account, x_request_id=x_request_id, enabled=enabled)

Enables or disables authenticator defined without service_id.

Allows you to either enable or disable a given authenticator that does not have service_id (For example: authn-gcp).  When you enable or disable an authenticator via this endpoint, the status of the authenticator is stored in the Conjur database. The enablement status of the authenticator service may be overridden by setting the `CONJUR_AUTHENTICATORS` environment variable on the Conjur server; in the case where this environment variable is set, the database record of whether the authenticator service is enabled will be ignored.  **This endpoint is part of an early implementation of support for enabling Conjur authenticators via the API, and is currently available at the Community (or early alpha) level. This endpoint is still subject to breaking changes in the future.** 

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import conjur
from conjur.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = conjur.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = conjur.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: conjurAuth
configuration = conjur.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with conjur.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = conjur.AuthenticationApi(api_client)
    authenticator = conjur.ServiceAuthenticators() # ServiceAuthenticators | The authenticator to update
account = 'dev' # str | Organization account name
x_request_id = 'test-id' # str | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  (optional)
enabled = True # bool |  (optional)

    try:
        # Enables or disables authenticator defined without service_id.
        api_instance.enable_authenticator(authenticator, account, x_request_id=x_request_id, enabled=enabled)
    except ApiException as e:
        print("Exception when calling AuthenticationApi->enable_authenticator: %s\n" % e)
```

* Api Key Authentication (conjurAuth):
```python
from __future__ import print_function
import time
import conjur
from conjur.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = conjur.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = conjur.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: conjurAuth
configuration = conjur.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with conjur.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = conjur.AuthenticationApi(api_client)
    authenticator = conjur.ServiceAuthenticators() # ServiceAuthenticators | The authenticator to update
account = 'dev' # str | Organization account name
x_request_id = 'test-id' # str | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  (optional)
enabled = True # bool |  (optional)

    try:
        # Enables or disables authenticator defined without service_id.
        api_instance.enable_authenticator(authenticator, account, x_request_id=x_request_id, enabled=enabled)
    except ApiException as e:
        print("Exception when calling AuthenticationApi->enable_authenticator: %s\n" % e)
```

```python
from __future__ import print_function
import time
import conjur
from conjur.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = conjur.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = conjur.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: conjurAuth
configuration = conjur.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with conjur.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = conjur.AuthenticationApi(api_client)
    authenticator = conjur.ServiceAuthenticators() # ServiceAuthenticators | The authenticator to update
account = 'dev' # str | Organization account name
x_request_id = 'test-id' # str | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  (optional)
enabled = True # bool |  (optional)

    try:
        # Enables or disables authenticator defined without service_id.
        api_instance.enable_authenticator(authenticator, account, x_request_id=x_request_id, enabled=enabled)
    except ApiException as e:
        print("Exception when calling AuthenticationApi->enable_authenticator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authenticator** | [**ServiceAuthenticators**](.md)| The authenticator to update | 
 **account** | **str**| Organization account name | 
 **x_request_id** | **str**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 
 **enabled** | **bool**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [conjurAuth](../README.md#conjurAuth), [conjurKubernetesMutualTls](../README.md#conjurKubernetesMutualTls)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The config was updated properly |  -  |
**400** | The server cannot process the request due to malformed request syntax |  -  |
**401** | Authentication information is missing or invalid |  -  |
**404** | The requested resource does not exist, the authenticated user lacks the required privileges to enumerate this resource, or its value has not been set |  -  |
**500** | Malfromed request, rejected by the server |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_authenticator_instance**
> enable_authenticator_instance(authenticator, service_id, account, x_request_id=x_request_id, enabled=enabled)

Enables or disables authenticator service instances.

Allows you to either enable or disable a given authenticator service instance.  When you enable or disable an authenticator service instance via this endpoint, the status of the authenticator service instance is stored in the Conjur database. The enablement status of the authenticator service instance may be overridden by setting the `CONJUR_AUTHENTICATORS` environment variable on the Conjur server; in the case where this environment variable is set, the database record of whether the authenticator service instance is enabled will be ignored.  **This endpoint is part of an early implementation of support for enabling Conjur authenticators via the API, and is currently available at the Community (or early alpha) level. This endpoint is still subject to breaking changes in the future.** 

### Example

* Api Key Authentication (conjurAuth):
```python
from __future__ import print_function
import time
import conjur
from conjur.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = conjur.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: conjurAuth
configuration = conjur.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with conjur.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = conjur.AuthenticationApi(api_client)
    authenticator = conjur.ServiceAuthenticators() # ServiceAuthenticators | The authenticator to update
service_id = 'prod%2fgke' # str | URL-Encoded authenticator service ID
account = 'dev' # str | Organization account name
x_request_id = 'test-id' # str | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  (optional)
enabled = True # bool |  (optional)

    try:
        # Enables or disables authenticator service instances.
        api_instance.enable_authenticator_instance(authenticator, service_id, account, x_request_id=x_request_id, enabled=enabled)
    except ApiException as e:
        print("Exception when calling AuthenticationApi->enable_authenticator_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authenticator** | [**ServiceAuthenticators**](.md)| The authenticator to update | 
 **service_id** | **str**| URL-Encoded authenticator service ID | 
 **account** | **str**| Organization account name | 
 **x_request_id** | **str**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 
 **enabled** | **bool**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[conjurAuth](../README.md#conjurAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The config was updated properly |  -  |
**400** | The server cannot process the request due to malformed request syntax |  -  |
**401** | Authentication information is missing or invalid |  -  |
**404** | The requested resource does not exist, the authenticated user lacks the required privileges to enumerate this resource, or its value has not been set |  -  |
**500** | Malfromed request, rejected by the server |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_access_token**
> str get_access_token(account, login, body, accept_encoding=accept_encoding, x_request_id=x_request_id)

Gets a short-lived access token, which is required in the header of most subsequent API requests. 

A client can obtain an access token by presenting a valid login name and API key.  The access token is used to communicate to the REST API that the bearer of the token has been authorized to access the API and perform specific actions specified by the scope that was granted during authorization.  The `login` must be URL encoded. For example, `alice@devops` must be encoded as `alice%40devops`.  The `service_id`, if given, must be URL encoded. For example, `prod/gke` must be encoded as `prod%2Fgke`.  For host authentication, the `login` is the host ID with the prefix `host/`. For example, the host webserver would login as `host/webserver`, and would be encoded as `host%2Fwebserver`.  For API usage, the base64-encoded access token is ordinarily passed as an HTTP Authorization header as `Authorization: Token token=<base64-encoded token>`.  This is the default authentication endpoint only. See other endpoints for details on authenticating to Conjur using another method, e.g. for applications running in Azure or Kubernetes. 

### Example

```python
from __future__ import print_function
import time
import conjur
from conjur.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = conjur.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with conjur.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = conjur.AuthenticationApi(api_client)
    account = 'account_example' # str | Organization account name
login = 'login_example' # str | URL-encoded login name. For users, it’s the user ID. For hosts, the login name is `host/<host-id>`
body = 'body_example' # str | API Key
accept_encoding = 'application/json' # str | Setting the Accept-Encoding header to base64 will return a pre-encoded access token (optional) (default to 'application/json')
x_request_id = 'test-id' # str | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  (optional)

    try:
        # Gets a short-lived access token, which is required in the header of most subsequent API requests. 
        api_response = api_instance.get_access_token(account, login, body, accept_encoding=accept_encoding, x_request_id=x_request_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthenticationApi->get_access_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| Organization account name | 
 **login** | **str**| URL-encoded login name. For users, it’s the user ID. For hosts, the login name is &#x60;host/&lt;host-id&gt;&#x60; | 
 **body** | **str**| API Key | 
 **accept_encoding** | **str**| Setting the Accept-Encoding header to base64 will return a pre-encoded access token | [optional] [default to &#39;application/json&#39;]
 **x_request_id** | **str**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response is an access token for conjur |  -  |
**400** | The server cannot process the request due to malformed request syntax |  -  |
**401** | Authentication information is missing or invalid |  -  |
**404** | The requested resource does not exist, the authenticated user lacks the required privileges to enumerate this resource, or its value has not been set |  -  |
**500** | Malfromed request, rejected by the server |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_access_token_via_aws**
> str get_access_token_via_aws(service_id, account, login, body, accept_encoding=accept_encoding, x_request_id=x_request_id)

Get a short-lived access token for applications running in AWS.

The access token is used to communicate to the REST API that the bearer of the token has been authorized to access the API and perform specific actions specified by the scope that was granted during authorization.  For API usage, the base64-encoded access token is ordinarily passed as an HTTP Authorization header as `Authorization: Token token=<base64-encoded token>`.  The `login` must be URL encoded and the host ID must have the prefix `host/`. For example, the host webserver would login as `host/webserver`, and would be encoded as `host%2Fwebserver`.  The `service_id`, if given, must be URL encoded. For example, `prod/gke` must be encoded as `prod%2Fgke`.  For detailed instructions on authenticating to Conjur using this endpoint, reference the documentation: [AWS IAM Authenticator](https://docs.conjur.org/Latest/en/Content/Operations/Services/AWS_IAM_Authenticator.htm) (`authn-iam`). 

### Example

```python
from __future__ import print_function
import time
import conjur
from conjur.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = conjur.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with conjur.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = conjur.AuthenticationApi(api_client)
    service_id = 'prod%2fgke' # str | URL-Encoded authenticator service ID
account = 'account_example' # str | Organization account name
login = 'login_example' # str | URL-encoded login name. For hosts, the login name is `host/<host-id>`
body = 'body_example' # str | AWS Signature header
accept_encoding = 'application/json' # str | Setting the Accept-Encoding header to base64 will return a pre-encoded access token (optional) (default to 'application/json')
x_request_id = 'test-id' # str | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  (optional)

    try:
        # Get a short-lived access token for applications running in AWS.
        api_response = api_instance.get_access_token_via_aws(service_id, account, login, body, accept_encoding=accept_encoding, x_request_id=x_request_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthenticationApi->get_access_token_via_aws: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| URL-Encoded authenticator service ID | 
 **account** | **str**| Organization account name | 
 **login** | **str**| URL-encoded login name. For hosts, the login name is &#x60;host/&lt;host-id&gt;&#x60; | 
 **body** | **str**| AWS Signature header | 
 **accept_encoding** | **str**| Setting the Accept-Encoding header to base64 will return a pre-encoded access token | [optional] [default to &#39;application/json&#39;]
 **x_request_id** | **str**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response is an access token for conjur |  -  |
**400** | The server cannot process the request due to malformed request syntax |  -  |
**401** | Authentication information is missing or invalid |  -  |
**404** | The requested resource does not exist, the authenticated user lacks the required privileges to enumerate this resource, or its value has not been set |  -  |
**500** | Malfromed request, rejected by the server |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_access_token_via_azure**
> str get_access_token_via_azure(service_id, account, login, accept_encoding=accept_encoding, x_request_id=x_request_id, jwt=jwt)

Gets a short-lived access token for applications running in Azure.

The access token is used to communicate to the REST API that the bearer of the token has been authorized to access the API and perform specific actions specified by the scope that was granted during authorization.  For API usage, the base64-encoded access token is ordinarily passed as an HTTP Authorization header as `Authorization: Token token=<base64-encoded token>`.  The `login` must be URL encoded and the host ID must have the prefix `host/`. For example, the host webserver would login as `host/webserver`, and would be encoded as `host%2Fwebserver`.  The `service_id`, if given, must be URL encoded. For example, `prod/gke` must be encoded as `prod%2Fgke`.  To authenticate to Conjur using this endpoint, reference the detailed documentation: [Azure Authenticator](https://docs.conjur.org/Latest/en/Content/Operations/Services/azure_authn.htm) (`authn-azure`). 

### Example

```python
from __future__ import print_function
import time
import conjur
from conjur.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = conjur.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with conjur.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = conjur.AuthenticationApi(api_client)
    service_id = 'prod%2fgke' # str | URL-Encoded authenticator service ID
account = 'account_example' # str | Organization account name
login = 'login_example' # str | URL-encoded login name. For users, it’s the user ID. For hosts, the login name is `host/<host-id>`
accept_encoding = 'application/json' # str | Setting the Accept-Encoding header to base64 will return a pre-encoded access token (optional) (default to 'application/json')
x_request_id = 'test-id' # str | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  (optional)
jwt = 'jwt_example' # str |  (optional)

    try:
        # Gets a short-lived access token for applications running in Azure.
        api_response = api_instance.get_access_token_via_azure(service_id, account, login, accept_encoding=accept_encoding, x_request_id=x_request_id, jwt=jwt)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthenticationApi->get_access_token_via_azure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| URL-Encoded authenticator service ID | 
 **account** | **str**| Organization account name | 
 **login** | **str**| URL-encoded login name. For users, it’s the user ID. For hosts, the login name is &#x60;host/&lt;host-id&gt;&#x60; | 
 **accept_encoding** | **str**| Setting the Accept-Encoding header to base64 will return a pre-encoded access token | [optional] [default to &#39;application/json&#39;]
 **x_request_id** | **str**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 
 **jwt** | **str**|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response is an access token for conjur |  -  |
**400** | The server cannot process the request due to malformed request syntax |  -  |
**401** | Authentication information is missing or invalid |  -  |
**404** | The requested resource does not exist, the authenticated user lacks the required privileges to enumerate this resource, or its value has not been set |  -  |
**500** | Malfromed request, rejected by the server |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_access_token_via_gcp**
> str get_access_token_via_gcp(account, accept_encoding=accept_encoding, x_request_id=x_request_id, jwt=jwt)

Gets a short-lived access token for applications running in Google Cloud Platform. 

Use the GCP Authenticator API to send an authentication request from a Google Cloud service to Conjur.  For more information, see [the documentation](https://docs.conjur.org/Latest/en/Content/Operations/Services/cjr-gcp-authn.htm). 

### Example

```python
from __future__ import print_function
import time
import conjur
from conjur.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = conjur.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with conjur.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = conjur.AuthenticationApi(api_client)
    account = 'dev' # str | Organization account name
accept_encoding = 'accept_encoding_example' # str | Setting the Accept-Encoding header to base64 will return a pre-encoded access token (optional)
x_request_id = 'test-id' # str | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  (optional)
jwt = 'jwt_example' # str |  (optional)

    try:
        # Gets a short-lived access token for applications running in Google Cloud Platform. 
        api_response = api_instance.get_access_token_via_gcp(account, accept_encoding=accept_encoding, x_request_id=x_request_id, jwt=jwt)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthenticationApi->get_access_token_via_gcp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| Organization account name | 
 **accept_encoding** | **str**| Setting the Accept-Encoding header to base64 will return a pre-encoded access token | [optional] 
 **x_request_id** | **str**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 
 **jwt** | **str**|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response body is the API key |  -  |
**400** | The server cannot process the request due to malformed request syntax |  -  |
**401** | Authentication information is missing or invalid |  -  |
**500** | Malfromed request, rejected by the server |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_access_token_via_jwt**
> str get_access_token_via_jwt(account, service_id, x_request_id=x_request_id, jwt=jwt)

Gets a short-lived access token for applications using JSON Web Token (JWT) to access the Conjur API. 

Use the JWT Authenticator to leverage the identity layer provided by JWT to authenticate with Conjur. 

### Example

```python
from __future__ import print_function
import time
import conjur
from conjur.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = conjur.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with conjur.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = conjur.AuthenticationApi(api_client)
    account = 'account_example' # str | Organization account name
service_id = 'prod%2fgke' # str | URL-Encoded authenticator service ID
x_request_id = 'test-id' # str | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  (optional)
jwt = 'jwt_example' # str |  (optional)

    try:
        # Gets a short-lived access token for applications using JSON Web Token (JWT) to access the Conjur API. 
        api_response = api_instance.get_access_token_via_jwt(account, service_id, x_request_id=x_request_id, jwt=jwt)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthenticationApi->get_access_token_via_jwt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| Organization account name | 
 **service_id** | **str**| URL-Encoded authenticator service ID | 
 **x_request_id** | **str**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 
 **jwt** | **str**|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response is an access token for conjur |  -  |
**400** | The server cannot process the request due to malformed request syntax |  -  |
**401** | Authentication information is missing or invalid |  -  |
**404** | The requested resource does not exist, the authenticated user lacks the required privileges to enumerate this resource, or its value has not been set |  -  |
**500** | Malfromed request, rejected by the server |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_access_token_via_jwt_with_id**
> str get_access_token_via_jwt_with_id(account, id, service_id, x_request_id=x_request_id, jwt=jwt)

Gets a short-lived access token for applications using JSON Web Token (JWT) to access the Conjur API. Covers the case of use of optional URL parameter \"ID\" 

Use the JWT Authenticator to leverage the identity layer provided by JWT to authenticate with Conjur. 

### Example

```python
from __future__ import print_function
import time
import conjur
from conjur.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = conjur.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with conjur.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = conjur.AuthenticationApi(api_client)
    account = 'account_example' # str | Organization account name
id = 'id_example' # str | Organization user id
service_id = 'prod%2fgke' # str | URL-Encoded authenticator service ID
x_request_id = 'test-id' # str | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  (optional)
jwt = 'jwt_example' # str |  (optional)

    try:
        # Gets a short-lived access token for applications using JSON Web Token (JWT) to access the Conjur API. Covers the case of use of optional URL parameter \"ID\" 
        api_response = api_instance.get_access_token_via_jwt_with_id(account, id, service_id, x_request_id=x_request_id, jwt=jwt)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthenticationApi->get_access_token_via_jwt_with_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| Organization account name | 
 **id** | **str**| Organization user id | 
 **service_id** | **str**| URL-Encoded authenticator service ID | 
 **x_request_id** | **str**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 
 **jwt** | **str**|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response is an access token for conjur |  -  |
**400** | The server cannot process the request due to malformed request syntax |  -  |
**401** | Authentication information is missing or invalid |  -  |
**404** | The requested resource does not exist, the authenticated user lacks the required privileges to enumerate this resource, or its value has not been set |  -  |
**500** | Malfromed request, rejected by the server |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_access_token_via_kubernetes**
> str get_access_token_via_kubernetes(service_id, account, login, accept_encoding=accept_encoding, x_request_id=x_request_id)

Gets a short-lived access token for applications running in Kubernetes.

The access token is used to communicate to the REST API that the bearer of the token has been authorized to access the API and perform specific actions specified by the scope that was granted during authorization.  For API usage, the base64-encoded access token is ordinarily passed as an HTTP Authorization header as `Authorization: Token token=<base64-encoded token>`.  The `login` must be URL encoded and the host ID must have the prefix `host/`. For example, the host webserver would login as `host/webserver`, and would be encoded as `host%2Fwebserver`.  The `service_id`, if given, must be URL encoded. For example, `prod/gke` must be encoded as `prod%2Fgke`.  To authenticate to Conjur using this endpoint, reference the detailed documentation: [Kubernetes Authenticator](https://docs.conjur.org/Latest/en/Content/Operations/Services/k8s_auth.htm) (`authn-k8s`). 

### Example

```python
from __future__ import print_function
import time
import conjur
from conjur.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = conjur.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with conjur.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = conjur.AuthenticationApi(api_client)
    service_id = 'prod%2fgke' # str | URL-Encoded authenticator service ID
account = 'account_example' # str | Organization account name
login = 'login_example' # str | URL-encoded login name. For users, it’s the user ID. For hosts, the login name is `host/<host-id>`
accept_encoding = 'application/json' # str | Setting the Accept-Encoding header to base64 will return a pre-encoded access token (optional) (default to 'application/json')
x_request_id = 'test-id' # str | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  (optional)

    try:
        # Gets a short-lived access token for applications running in Kubernetes.
        api_response = api_instance.get_access_token_via_kubernetes(service_id, account, login, accept_encoding=accept_encoding, x_request_id=x_request_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthenticationApi->get_access_token_via_kubernetes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| URL-Encoded authenticator service ID | 
 **account** | **str**| Organization account name | 
 **login** | **str**| URL-encoded login name. For users, it’s the user ID. For hosts, the login name is &#x60;host/&lt;host-id&gt;&#x60; | 
 **accept_encoding** | **str**| Setting the Accept-Encoding header to base64 will return a pre-encoded access token | [optional] [default to &#39;application/json&#39;]
 **x_request_id** | **str**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 

### Return type

**str**

### Authorization

[conjurKubernetesMutualTls](../README.md#conjurKubernetesMutualTls)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response is an access token for conjur |  -  |
**400** | The server cannot process the request due to malformed request syntax |  -  |
**401** | Authentication information is missing or invalid |  -  |
**404** | The requested resource does not exist, the authenticated user lacks the required privileges to enumerate this resource, or its value has not been set |  -  |
**500** | Malfromed request, rejected by the server |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_access_token_via_ldap**
> str get_access_token_via_ldap(service_id, account, login, accept_encoding=accept_encoding, x_request_id=x_request_id, body=body)

Gets a short-lived access token for users and hosts using their LDAP identity to access the Conjur API. 

The access token is used to communicate to the REST API that the bearer of the token has been authorized to access the API and perform specific actions specified by the scope that was granted during authorization.  For API usage, the base64-encoded access token is ordinarily passed as an HTTP Authorization header as `Authorization: Token token=<base64-encoded token>`.  The `login` must be URL encoded. For example, `alice@devops` must be encoded as `alice%40devops`.  The `service_id`, if given, must be URL encoded. For example, `prod/gke` must be encoded as `prod%2Fgke`.  For host authentication, the `login` is the host ID with the prefix `host/`. For example, the host webserver would login as `host/webserver`, and would be encoded as `host%2Fwebserver`.  To authenticate to Conjur using a LDAP, reference the detailed documentation: [LDAP Authenticator](https://docs.conjur.org/Latest/en/Content/Integrations/ldap/ldap_authenticator.html) (`authn-ldap`). 

### Example

```python
from __future__ import print_function
import time
import conjur
from conjur.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = conjur.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with conjur.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = conjur.AuthenticationApi(api_client)
    service_id = 'prod%2fgke' # str | URL-Encoded authenticator service ID
account = 'account_example' # str | Organization account name
login = 'login_example' # str | URL-encoded login name. For users, it’s the user ID. For hosts, the login name is `host/<host-id>`
accept_encoding = 'application/json' # str | Setting the Accept-Encoding header to base64 will return a pre-encoded access token (optional) (default to 'application/json')
x_request_id = 'test-id' # str | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  (optional)
body = 'body_example' # str | API key (optional)

    try:
        # Gets a short-lived access token for users and hosts using their LDAP identity to access the Conjur API. 
        api_response = api_instance.get_access_token_via_ldap(service_id, account, login, accept_encoding=accept_encoding, x_request_id=x_request_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthenticationApi->get_access_token_via_ldap: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| URL-Encoded authenticator service ID | 
 **account** | **str**| Organization account name | 
 **login** | **str**| URL-encoded login name. For users, it’s the user ID. For hosts, the login name is &#x60;host/&lt;host-id&gt;&#x60; | 
 **accept_encoding** | **str**| Setting the Accept-Encoding header to base64 will return a pre-encoded access token | [optional] [default to &#39;application/json&#39;]
 **x_request_id** | **str**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 
 **body** | **str**| API key | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response is an access token for conjur |  -  |
**400** | The server cannot process the request due to malformed request syntax |  -  |
**401** | Authentication information is missing or invalid |  -  |
**404** | The requested resource does not exist, the authenticated user lacks the required privileges to enumerate this resource, or its value has not been set |  -  |
**500** | Malfromed request, rejected by the server |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_access_token_via_oidc**
> str get_access_token_via_oidc(service_id, account, x_request_id=x_request_id, id_token=id_token)

Gets a short-lived access token for applications using OpenID Connect (OIDC) to access the Conjur API. 

Use the OIDC Authenticator to leverage the identity layer provided by OIDC to authenticate with Conjur.  For more information see [the documentation](https://docs.conjur.org/Latest/en/Content/OIDC/OIDC.htm). 

### Example

```python
from __future__ import print_function
import time
import conjur
from conjur.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = conjur.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with conjur.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = conjur.AuthenticationApi(api_client)
    service_id = 'prod%2fgke' # str | URL-Encoded authenticator service ID
account = 'account_example' # str | Organization account name
x_request_id = 'test-id' # str | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  (optional)
id_token = 'id_token_example' # str |  (optional)

    try:
        # Gets a short-lived access token for applications using OpenID Connect (OIDC) to access the Conjur API. 
        api_response = api_instance.get_access_token_via_oidc(service_id, account, x_request_id=x_request_id, id_token=id_token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthenticationApi->get_access_token_via_oidc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| URL-Encoded authenticator service ID | 
 **account** | **str**| Organization account name | 
 **x_request_id** | **str**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 
 **id_token** | **str**|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response is an access token for conjur |  -  |
**400** | The server cannot process the request due to malformed request syntax |  -  |
**401** | Authentication information is missing or invalid |  -  |
**404** | The requested resource does not exist, the authenticated user lacks the required privileges to enumerate this resource, or its value has not been set |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_key**
> str get_api_key(account, x_request_id=x_request_id)

Gets the API key of a user given the username and password via HTTP Basic Authentication. 

Passwords are stored in the Conjur database using `bcrypt` with a work factor of 12. Therefore, login is a fairly expensive operation. However, once the API key is obtained, it may be used to inexpensively obtain access tokens by calling the Authenticate method. An access token is required to use most other parts of the Conjur API.  The Basic authentication-compliant header is formed by: 1. Concatenating the role's name, a literal colon character ':',    and the password or API key to create the authentication string. 2. Base64-encoding the authentication string. 3. Prefixing the authentication string with the scheme: `Basic `    (note the required space). 4. Providing the result as the value of the `Authorization` HTTP header:    `Authorization: Basic <authentication string>`.  Your HTTP/REST client probably provides HTTP basic authentication support. For example, `curl` and all of the Conjur client libraries provide this.  Note that machine roles (Hosts) do not have passwords and do not need to use this endpoint. 

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import conjur
from conjur.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = conjur.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = conjur.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with conjur.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = conjur.AuthenticationApi(api_client)
    account = 'account_example' # str | Organization account name
x_request_id = 'test-id' # str | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  (optional)

    try:
        # Gets the API key of a user given the username and password via HTTP Basic Authentication. 
        api_response = api_instance.get_api_key(account, x_request_id=x_request_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthenticationApi->get_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| Organization account name | 
 **x_request_id** | **str**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response body is the API key |  -  |
**400** | The server cannot process the request due to malformed request syntax |  -  |
**401** | Authentication information is missing or invalid |  -  |
**404** | The requested resource does not exist, the authenticated user lacks the required privileges to enumerate this resource, or its value has not been set |  -  |
**422** | A request parameter was either missing or invalid. |  -  |
**500** | Malfromed request, rejected by the server |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_key_via_ldap**
> str get_api_key_via_ldap(service_id, account, x_request_id=x_request_id)

Gets the Conjur API key of a user given the LDAP username and password via HTTP Basic Authentication. 

Exchange your LDAP credentials for a Conjur API key. Once the API key is obtained, it may be used to inexpensively obtain access tokens by calling the Authenticate method. An access token is required to use most other parts of the Conjur API.  The Basic authentication-compliant header is formed by: 1. Concatenating the LDAP username, a literal colon character ':',    and the password to create the authentication string. 2. Base64-encoding the authentication string. 3. Prefixing the authentication string with the scheme: `Basic `    (note the required space). 4. Providing the result as the value of the `Authorization` HTTP header:    `Authorization: Basic <authentication string>`.  Your HTTP/REST client probably provides HTTP basic authentication support. 

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import conjur
from conjur.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = conjur.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = conjur.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with conjur.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = conjur.AuthenticationApi(api_client)
    service_id = 'prod%2fgke' # str | URL-Encoded authenticator service ID
account = 'account_example' # str | Organization account name
x_request_id = 'test-id' # str | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  (optional)

    try:
        # Gets the Conjur API key of a user given the LDAP username and password via HTTP Basic Authentication. 
        api_response = api_instance.get_api_key_via_ldap(service_id, account, x_request_id=x_request_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthenticationApi->get_api_key_via_ldap: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| URL-Encoded authenticator service ID | 
 **account** | **str**| Organization account name | 
 **x_request_id** | **str**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response body is the API key |  -  |
**400** | The server cannot process the request due to malformed request syntax |  -  |
**401** | Authentication information is missing or invalid |  -  |
**404** | The requested resource does not exist, the authenticated user lacks the required privileges to enumerate this resource, or its value has not been set |  -  |
**422** | A request parameter was either missing or invalid. |  -  |
**500** | Malfromed request, rejected by the server |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **k8s_inject_client_cert**
> k8s_inject_client_cert(service_id, body, host_id_prefix=host_id_prefix, x_request_id=x_request_id)

For applications running in Kubernetes; sends Conjur a certificate signing request (CSR) and requests a client certificate injected into the application's Kubernetes pod. 

This request sends a Certificate Signing Request to Conjur, which uses the Kubernetes API to inject a client certificate into the application pod.  This endpoint requires a properly configured Conjur Certificate Authority service alongside a properly configured and enabled Kubernetes authenticator. For detailed instructions, see [the documentation](https://docs.conjur.org/Latest/en/Content/Integrations/kubernetes.htm). 

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import conjur
from conjur.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = conjur.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = conjur.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: conjurAuth
configuration = conjur.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with conjur.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = conjur.AuthenticationApi(api_client)
    service_id = 'prod%2fgke' # str | URL-Encoded authenticator service ID
body = 'body_example' # str | Valid certificate signing request that includes the host identity suffix as the CSR common name 
host_id_prefix = 'host/conjur/authn-k8s/my-authenticator-id/apps' # str | Dot-separated policy tree, prefixed by `host.`, where the application identity is defined (optional)
x_request_id = 'test-id' # str | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  (optional)

    try:
        # For applications running in Kubernetes; sends Conjur a certificate signing request (CSR) and requests a client certificate injected into the application's Kubernetes pod. 
        api_instance.k8s_inject_client_cert(service_id, body, host_id_prefix=host_id_prefix, x_request_id=x_request_id)
    except ApiException as e:
        print("Exception when calling AuthenticationApi->k8s_inject_client_cert: %s\n" % e)
```

* Api Key Authentication (conjurAuth):
```python
from __future__ import print_function
import time
import conjur
from conjur.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = conjur.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = conjur.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: conjurAuth
configuration = conjur.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with conjur.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = conjur.AuthenticationApi(api_client)
    service_id = 'prod%2fgke' # str | URL-Encoded authenticator service ID
body = 'body_example' # str | Valid certificate signing request that includes the host identity suffix as the CSR common name 
host_id_prefix = 'host/conjur/authn-k8s/my-authenticator-id/apps' # str | Dot-separated policy tree, prefixed by `host.`, where the application identity is defined (optional)
x_request_id = 'test-id' # str | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  (optional)

    try:
        # For applications running in Kubernetes; sends Conjur a certificate signing request (CSR) and requests a client certificate injected into the application's Kubernetes pod. 
        api_instance.k8s_inject_client_cert(service_id, body, host_id_prefix=host_id_prefix, x_request_id=x_request_id)
    except ApiException as e:
        print("Exception when calling AuthenticationApi->k8s_inject_client_cert: %s\n" % e)
```

```python
from __future__ import print_function
import time
import conjur
from conjur.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = conjur.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = conjur.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: conjurAuth
configuration = conjur.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with conjur.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = conjur.AuthenticationApi(api_client)
    service_id = 'prod%2fgke' # str | URL-Encoded authenticator service ID
body = 'body_example' # str | Valid certificate signing request that includes the host identity suffix as the CSR common name 
host_id_prefix = 'host/conjur/authn-k8s/my-authenticator-id/apps' # str | Dot-separated policy tree, prefixed by `host.`, where the application identity is defined (optional)
x_request_id = 'test-id' # str | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  (optional)

    try:
        # For applications running in Kubernetes; sends Conjur a certificate signing request (CSR) and requests a client certificate injected into the application's Kubernetes pod. 
        api_instance.k8s_inject_client_cert(service_id, body, host_id_prefix=host_id_prefix, x_request_id=x_request_id)
    except ApiException as e:
        print("Exception when calling AuthenticationApi->k8s_inject_client_cert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| URL-Encoded authenticator service ID | 
 **body** | **str**| Valid certificate signing request that includes the host identity suffix as the CSR common name  | 
 **host_id_prefix** | **str**| Dot-separated policy tree, prefixed by &#x60;host.&#x60;, where the application identity is defined | [optional] 
 **x_request_id** | **str**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [conjurAuth](../README.md#conjurAuth), [conjurKubernetesMutualTls](../README.md#conjurKubernetesMutualTls)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | The injected certificate was accepted. |  -  |
**400** | The server cannot process the request due to malformed request syntax |  -  |
**401** | Authentication information is missing or invalid |  -  |
**404** | The requested resource does not exist, the authenticated user lacks the required privileges to enumerate this resource, or its value has not been set |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rotate_api_key**
> str rotate_api_key(account, role=role, x_request_id=x_request_id)

Rotates a role's API key.

Any role can rotate its own API key. The name and password (for users) or current API key (for hosts and users) of the role must be provided via HTTP Basic Authorization.  To rotate another role's API key, you may provide your name and password (for users) or current API key (for hosts and users) via HTTP Basic Authorization with the request. Alternatively, you may provide your Conjur access token via the standard Conjur `Authorization` header.  The Basic authentication-compliant header is formed by: 1. Concatenating the role's name, a literal colon character ':',    and the password or API key to create the authentication string. 2. Base64-encoding the authentication string. 3. Prefixing the authentication string with the scheme: `Basic `    (note the required space). 4. Providing the result as the value of the `Authorization` HTTP header:    `Authorization: Basic <authentication string>`.  Your HTTP/REST client probably provides HTTP basic authentication support. For example, `curl` and all of the Conjur client libraries provide this.  If using the Conjur `Authorization` header, its value should be set to `Token token=<base64-encoded access token>`.  Note that the body of the request must be the empty string. 

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import conjur
from conjur.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = conjur.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = conjur.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: conjurAuth
configuration = conjur.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with conjur.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = conjur.AuthenticationApi(api_client)
    account = 'account_example' # str | Organization account name
role = 'role_example' # str | (**Optional**) role specifier in `{kind}:{identifier}` format  ##### Permissions required  `update` privilege on the role whose API key is being rotated.  (optional)
x_request_id = 'test-id' # str | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  (optional)

    try:
        # Rotates a role's API key.
        api_response = api_instance.rotate_api_key(account, role=role, x_request_id=x_request_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthenticationApi->rotate_api_key: %s\n" % e)
```

* Api Key Authentication (conjurAuth):
```python
from __future__ import print_function
import time
import conjur
from conjur.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = conjur.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = conjur.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: conjurAuth
configuration = conjur.Configuration(
    host = "http://localhost",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with conjur.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = conjur.AuthenticationApi(api_client)
    account = 'account_example' # str | Organization account name
role = 'role_example' # str | (**Optional**) role specifier in `{kind}:{identifier}` format  ##### Permissions required  `update` privilege on the role whose API key is being rotated.  (optional)
x_request_id = 'test-id' # str | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  (optional)

    try:
        # Rotates a role's API key.
        api_response = api_instance.rotate_api_key(account, role=role, x_request_id=x_request_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthenticationApi->rotate_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| Organization account name | 
 **role** | **str**| (**Optional**) role specifier in &#x60;{kind}:{identifier}&#x60; format  ##### Permissions required  &#x60;update&#x60; privilege on the role whose API key is being rotated.  | [optional] 
 **x_request_id** | **str**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [conjurAuth](../README.md#conjurAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response body is the API key |  -  |
**400** | The server cannot process the request due to malformed request syntax |  -  |
**401** | Authentication information is missing or invalid |  -  |
**422** | A request parameter was either missing or invalid. |  -  |
**500** | Malfromed request, rejected by the server |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

