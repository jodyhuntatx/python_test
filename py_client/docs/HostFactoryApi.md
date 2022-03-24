# conjur.HostFactoryApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_host**](HostFactoryApi.md#create_host) | **POST** /host_factories/hosts | Creates a Host using the Host Factory.
[**create_token**](HostFactoryApi.md#create_token) | **POST** /host_factory_tokens | Creates one or more host identity tokens.
[**revoke_token**](HostFactoryApi.md#revoke_token) | **DELETE** /host_factory_tokens/{token} | Revokes a token, immediately disabling it.


# **create_host**
> CreateHost create_host(id, x_request_id=x_request_id, annotations=annotations)

Creates a Host using the Host Factory.

Creates a Host using the Host Factory and returns a JSON description of it.  Requires a host factory token, which can be created using the create tokens API. In practice, this token is usually provided automatically as part of Conjur integration with your host provisioning infrastructure.  Note: If the token was created with a CIDR restriction, you must make this API request from a whitelisted address. 

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
    api_instance = conjur.HostFactoryApi(api_client)
    id = 'id_example' # str | Identifier of the host to be created. It will be created within the account of the host factory.
x_request_id = 'test-id' # str | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  (optional)
annotations = None # object | Annotations to apply to the new host (optional)

    try:
        # Creates a Host using the Host Factory.
        api_response = api_instance.create_host(id, x_request_id=x_request_id, annotations=annotations)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling HostFactoryApi->create_host: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the host to be created. It will be created within the account of the host factory. | 
 **x_request_id** | **str**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 
 **annotations** | [**object**](object.md)| Annotations to apply to the new host | [optional] 

### Return type

[**CreateHost**](CreateHost.md)

### Authorization

[conjurAuth](../README.md#conjurAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The response body contains the newly-created host |  -  |
**401** | Authentication information is missing or invalid |  -  |
**422** | A request parameter was either missing or invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_token**
> list[object] create_token(expiration, host_factory, x_request_id=x_request_id, cidr=cidr, count=count)

Creates one or more host identity tokens.

Creates one or more tokens which can be used to bootstrap host identity. Responds with a JSON document containing the tokens and their restrictions.  If the tokens are created with a CIDR restriction, Conjur will only accept them from the whitelisted IP ranges.  ##### Permissions required # `execute` privilege on the Host Factory.\" 

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
    api_instance = conjur.HostFactoryApi(api_client)
    expiration = 'expiration_example' # str | `ISO 8601 datetime` denoting a requested expiration time.
host_factory = 'host_factory_example' # str | Fully qualified host factory ID
x_request_id = 'test-id' # str | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  (optional)
cidr = 'cidr_example' # list[str] | Number of host tokens to create (optional)
count = 56 # int | Number of host tokens to create (optional)

    try:
        # Creates one or more host identity tokens.
        api_response = api_instance.create_token(expiration, host_factory, x_request_id=x_request_id, cidr=cidr, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling HostFactoryApi->create_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expiration** | **str**| &#x60;ISO 8601 datetime&#x60; denoting a requested expiration time. | 
 **host_factory** | **str**| Fully qualified host factory ID | 
 **x_request_id** | **str**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 
 **cidr** | [**list[str]**](str.md)| Number of host tokens to create | [optional] 
 **count** | **int**| Number of host tokens to create | [optional] 

### Return type

**list[object]**

### Authorization

[conjurAuth](../README.md#conjurAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Zero or more tokens were created and delivered in the response body |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | The authenticated user lacks the necessary privileges |  -  |
**404** | The requested resource does not exist, the authenticated user lacks the required privileges to enumerate this resource, or its value has not been set |  -  |
**422** | A request parameter was either missing or invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_token**
> revoke_token(token, x_request_id=x_request_id)

Revokes a token, immediately disabling it.

Revokes a token, immediately disabling it.  ##### Permissions required  `update` privilege on the host factory.\" 

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
    api_instance = conjur.HostFactoryApi(api_client)
    token = 'token_example' # str | The host factory token to revoke
x_request_id = 'test-id' # str | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  (optional)

    try:
        # Revokes a token, immediately disabling it.
        api_instance.revoke_token(token, x_request_id=x_request_id)
    except ApiException as e:
        print("Exception when calling HostFactoryApi->revoke_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The host factory token to revoke | 
 **x_request_id** | **str**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 

### Return type

void (empty response body)

### Authorization

[conjurAuth](../README.md#conjurAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Token was successfully revoked |  -  |
**400** | The server cannot process the request due to malformed request syntax |  -  |
**401** | Authentication information is missing or invalid |  -  |
**404** | The requested resource does not exist, the authenticated user lacks the required privileges to enumerate this resource, or its value has not been set |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

