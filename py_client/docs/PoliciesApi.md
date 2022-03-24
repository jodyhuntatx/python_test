# conjur.PoliciesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**load_policy**](PoliciesApi.md#load_policy) | **POST** /policies/{account}/policy/{identifier} | Adds data to the existing Conjur policy.
[**replace_policy**](PoliciesApi.md#replace_policy) | **PUT** /policies/{account}/policy/{identifier} | Loads or replaces a Conjur policy document.
[**update_policy**](PoliciesApi.md#update_policy) | **PATCH** /policies/{account}/policy/{identifier} | Modifies an existing Conjur policy.


# **load_policy**
> LoadedPolicy load_policy(account, identifier, body, x_request_id=x_request_id)

Adds data to the existing Conjur policy.

Adds data to the existing Conjur policy. Deletions are not allowed. Any policy objects that exist on the server but are omitted from the policy file will not be deleted and any explicit deletions in the policy file will result in an error.  ##### Permissions required  `create` privilege on the policy.\" 

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
    api_instance = conjur.PoliciesApi(api_client)
    account = 'account_example' # str | Organization account name
identifier = 'root' # str | ID of the policy to update
body = 'body_example' # str | Policy
x_request_id = 'test-id' # str | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  (optional)

    try:
        # Adds data to the existing Conjur policy.
        api_response = api_instance.load_policy(account, identifier, body, x_request_id=x_request_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PoliciesApi->load_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| Organization account name | 
 **identifier** | **str**| ID of the policy to update | 
 **body** | **str**| Policy | 
 **x_request_id** | **str**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 

### Return type

[**LoadedPolicy**](LoadedPolicy.md)

### Authorization

[conjurAuth](../README.md#conjurAuth)

### HTTP request headers

 - **Content-Type**: application/x-yaml, text/plain, text/x-yaml, text/yaml
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Decsribes new data created by a successful policy load |  -  |
**400** | The server cannot process the request due to malformed request syntax |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | The authenticated user lacks the necessary privileges |  -  |
**404** | The requested resource does not exist, the authenticated user lacks the required privileges to enumerate this resource, or its value has not been set |  -  |
**409** | Similar operation already in progress, retry after a delay |  -  |
**422** | A request parameter was either missing or invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_policy**
> LoadedPolicy replace_policy(account, identifier, body, x_request_id=x_request_id)

Loads or replaces a Conjur policy document.

Loads or replaces a Conjur policy document.  **Any policy data which already exists on the server but is not explicitly specified in the new policy file will be deleted!**. 

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
    api_instance = conjur.PoliciesApi(api_client)
    account = 'account_example' # str | Organization account name
identifier = 'root' # str | ID of the policy to load (root if no root policy has been loaded yet)
body = 'body_example' # str | Policy
x_request_id = 'test-id' # str | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  (optional)

    try:
        # Loads or replaces a Conjur policy document.
        api_response = api_instance.replace_policy(account, identifier, body, x_request_id=x_request_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PoliciesApi->replace_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| Organization account name | 
 **identifier** | **str**| ID of the policy to load (root if no root policy has been loaded yet) | 
 **body** | **str**| Policy | 
 **x_request_id** | **str**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 

### Return type

[**LoadedPolicy**](LoadedPolicy.md)

### Authorization

[conjurAuth](../README.md#conjurAuth)

### HTTP request headers

 - **Content-Type**: application/x-yaml, text/plain, text/x-yaml, text/yaml
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Decsribes new data created by a successful policy load |  -  |
**400** | The server cannot process the request due to malformed request syntax |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | The authenticated user lacks the necessary privileges |  -  |
**404** | The requested resource does not exist, the authenticated user lacks the required privileges to enumerate this resource, or its value has not been set |  -  |
**409** | Similar operation already in progress, retry after a delay |  -  |
**422** | A request parameter was either missing or invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_policy**
> LoadedPolicy update_policy(account, identifier, body, x_request_id=x_request_id)

Modifies an existing Conjur policy.

Modifies an existing Conjur policy. Data may be explicitly deleted using the `!delete`, `!revoke`, and `!deny` statements. Unlike `replace` mode, no data is ever implicitly deleted.  ##### Permissions required 

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
    api_instance = conjur.PoliciesApi(api_client)
    account = 'account_example' # str | Organization account name
identifier = 'root' # str | ID of the policy to update
body = 'body_example' # str | Policy
x_request_id = 'test-id' # str | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  (optional)

    try:
        # Modifies an existing Conjur policy.
        api_response = api_instance.update_policy(account, identifier, body, x_request_id=x_request_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PoliciesApi->update_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| Organization account name | 
 **identifier** | **str**| ID of the policy to update | 
 **body** | **str**| Policy | 
 **x_request_id** | **str**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 

### Return type

[**LoadedPolicy**](LoadedPolicy.md)

### Authorization

[conjurAuth](../README.md#conjurAuth)

### HTTP request headers

 - **Content-Type**: application/x-yaml, text/plain, text/x-yaml, text/yaml
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Decsribes new data created by a successful policy load |  -  |
**400** | The server cannot process the request due to malformed request syntax |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | The authenticated user lacks the necessary privileges |  -  |
**404** | The requested resource does not exist, the authenticated user lacks the required privileges to enumerate this resource, or its value has not been set |  -  |
**409** | Similar operation already in progress, retry after a delay |  -  |
**422** | A request parameter was either missing or invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

