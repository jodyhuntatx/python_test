# conjur.SecretsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_secret**](SecretsApi.md#create_secret) | **POST** /secrets/{account}/{kind}/{identifier} | Creates a secret value within the specified variable.
[**get_secret**](SecretsApi.md#get_secret) | **GET** /secrets/{account}/{kind}/{identifier} | Fetches the value of a secret from the specified Secret.
[**get_secrets**](SecretsApi.md#get_secrets) | **GET** /secrets | Fetch multiple secrets


# **create_secret**
> create_secret(account, kind, identifier, expirations=expirations, x_request_id=x_request_id, body=body)

Creates a secret value within the specified variable.

Creates a secret value within the specified Secret.   Note: Conjur will allow you to add a secret to any resource, but the best practice is to store and retrieve secret data only using Secret resources. 

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
    api_instance = conjur.SecretsApi(api_client)
    account = 'account_example' # str | Organization account name
kind = 'kind_example' # str | Type of resource - in almost all cases this should be `variable`
identifier = 'identifier_example' # str | URL-encoded variable ID
expirations = 'expirations_example' # str | Tells the server to reset the variables expiration date (optional)
x_request_id = 'test-id' # str | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  (optional)
body = 'body_example' # str | Secret data (optional)

    try:
        # Creates a secret value within the specified variable.
        api_instance.create_secret(account, kind, identifier, expirations=expirations, x_request_id=x_request_id, body=body)
    except ApiException as e:
        print("Exception when calling SecretsApi->create_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| Organization account name | 
 **kind** | **str**| Type of resource - in almost all cases this should be &#x60;variable&#x60; | 
 **identifier** | **str**| URL-encoded variable ID | 
 **expirations** | **str**| Tells the server to reset the variables expiration date | [optional] 
 **x_request_id** | **str**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 
 **body** | **str**| Secret data | [optional] 

### Return type

void (empty response body)

### Authorization

[conjurAuth](../README.md#conjurAuth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The secret value was added successfully |  -  |
**400** | The server cannot process the request due to malformed request syntax |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | The authenticated user lacks the necessary privileges |  -  |
**422** | A request parameter was either missing or invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_secret**
> str get_secret(account, kind, identifier, version=version, x_request_id=x_request_id)

Fetches the value of a secret from the specified Secret.

Fetches the value of a secret from the specified Secret. The latest version will be retrieved unless the version parameter is specified. The twenty most recent secret versions are retained.  The secret data is returned in the response body.  Note: Conjur will allow you to add a secret to any resource, but the best practice is to store and retrieve secret data only using Secret resources. 

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
    api_instance = conjur.SecretsApi(api_client)
    account = 'account_example' # str | Organization account name
kind = 'kind_example' # str | Type of resource - in almost all cases this should be `variable`
identifier = 'identifier_example' # str | URL-encoded variable ID
version = 56 # int | (**Optional**) Version you want to retrieve (Conjur keeps the last 20 versions of a secret) (optional)
x_request_id = 'test-id' # str | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  (optional)

    try:
        # Fetches the value of a secret from the specified Secret.
        api_response = api_instance.get_secret(account, kind, identifier, version=version, x_request_id=x_request_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SecretsApi->get_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| Organization account name | 
 **kind** | **str**| Type of resource - in almost all cases this should be &#x60;variable&#x60; | 
 **identifier** | **str**| URL-encoded variable ID | 
 **version** | **int**| (**Optional**) Version you want to retrieve (Conjur keeps the last 20 versions of a secret) | [optional] 
 **x_request_id** | **str**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 

### Return type

**str**

### Authorization

[conjurAuth](../README.md#conjurAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The secret value was added successfully |  -  |
**400** | The server cannot process the request due to malformed request syntax |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | The authenticated user lacks the necessary privileges |  -  |
**404** | The requested resource does not exist, the authenticated user lacks the required privileges to enumerate this resource, or its value has not been set |  -  |
**422** | A request parameter was either missing or invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_secrets**
> object get_secrets(variable_ids, accept_encoding=accept_encoding, x_request_id=x_request_id)

Fetch multiple secrets

Fetches multiple secret values in one invocation. It’s faster to fetch secrets in batches than to fetch them one at a time.

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
    api_instance = conjur.SecretsApi(api_client)
    variable_ids = 'variable_ids_example' # str | Comma-delimited, URL-encoded resource IDs of the variables.
accept_encoding = 'accept_encoding_example' # str | Set the encoding of the response object (optional)
x_request_id = 'test-id' # str | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  (optional)

    try:
        # Fetch multiple secrets
        api_response = api_instance.get_secrets(variable_ids, accept_encoding=accept_encoding, x_request_id=x_request_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SecretsApi->get_secrets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **variable_ids** | **str**| Comma-delimited, URL-encoded resource IDs of the variables. | 
 **accept_encoding** | **str**| Set the encoding of the response object | [optional] 
 **x_request_id** | **str**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 

### Return type

**object**

### Authorization

[conjurAuth](../README.md#conjurAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The batch secret values |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | The authenticated user lacks the necessary privileges |  -  |
**404** | At least one resource was unable to be found |  -  |
**406** | Issue encoding secret into JSON format |  -  |
**422** | A request parameter was either missing or invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

