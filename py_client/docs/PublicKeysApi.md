# conjur.PublicKeysApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**show_public_keys**](PublicKeysApi.md#show_public_keys) | **GET** /public_keys/{account}/{kind}/{identifier} | Shows all public keys for a resource.


# **show_public_keys**
> str show_public_keys(account, kind, identifier, x_request_id=x_request_id)

Shows all public keys for a resource.

Shows all public keys for a resource as newline delimited string for compatibility with the authorized_keys SSH format. Returns an empty string if the resource does not exist, to prevent attackers from determining whether a resource exists. 

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
    api_instance = conjur.PublicKeysApi(api_client)
    account = 'account_example' # str | Organization account name
kind = 'user' # str | Type of resource
identifier = 'admin' # str | ID of the resource for which to get the information about
x_request_id = 'test-id' # str | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  (optional)

    try:
        # Shows all public keys for a resource.
        api_response = api_instance.show_public_keys(account, kind, identifier, x_request_id=x_request_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PublicKeysApi->show_public_keys: %s\n" % e)
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
    api_instance = conjur.PublicKeysApi(api_client)
    account = 'account_example' # str | Organization account name
kind = 'user' # str | Type of resource
identifier = 'admin' # str | ID of the resource for which to get the information about
x_request_id = 'test-id' # str | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  (optional)

    try:
        # Shows all public keys for a resource.
        api_response = api_instance.show_public_keys(account, kind, identifier, x_request_id=x_request_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PublicKeysApi->show_public_keys: %s\n" % e)
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
    api_instance = conjur.PublicKeysApi(api_client)
    account = 'account_example' # str | Organization account name
kind = 'user' # str | Type of resource
identifier = 'admin' # str | ID of the resource for which to get the information about
x_request_id = 'test-id' # str | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  (optional)

    try:
        # Shows all public keys for a resource.
        api_response = api_instance.show_public_keys(account, kind, identifier, x_request_id=x_request_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PublicKeysApi->show_public_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| Organization account name | 
 **kind** | **str**| Type of resource | 
 **identifier** | **str**| ID of the resource for which to get the information about | 
 **x_request_id** | **str**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth), [conjurAuth](../README.md#conjurAuth), [conjurKubernetesMutualTls](../README.md#conjurKubernetesMutualTls)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Public keys for a resource as newline delimited string for compatibility with the authorized_keys SSH format. Empty string if the resource does not exist |  -  |
**400** | The server cannot process the request due to malformed request syntax |  -  |
**404** | The requested resource does not exist, the authenticated user lacks the required privileges to enumerate this resource, or its value has not been set |  -  |
**422** | A request parameter was either missing or invalid. |  -  |
**500** | Malfromed request, rejected by the server |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

