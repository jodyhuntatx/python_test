# conjur.ResourcesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**show_resource**](ResourcesApi.md#show_resource) | **GET** /resources/{account}/{kind}/{identifier} | Shows a description of a single resource.
[**show_resources_for_account**](ResourcesApi.md#show_resources_for_account) | **GET** /resources/{account} | Lists resources within an organization account.
[**show_resources_for_all_accounts**](ResourcesApi.md#show_resources_for_all_accounts) | **GET** /resources | Lists resources within an organization account.
[**show_resources_for_kind**](ResourcesApi.md#show_resources_for_kind) | **GET** /resources/{account}/{kind} | Lists resources of the same kind within an organization account.


# **show_resource**
> Resource show_resource(account, kind, identifier, permitted_roles=permitted_roles, privilege=privilege, check=check, role=role, x_request_id=x_request_id)

Shows a description of a single resource.

Details about a single resource.  If `permitted_roles` and `privilege` are given, Conjur lists the roles with the specified privilege on the resource.  If `check`, `privilege` and `role` are given, Conjur checks if the specified role has the privilege on the resource.  If `permitted_roles` and `check` are both given, Conjur responds to the `check` call ONLY.  ##### Permissions Required 

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
    api_instance = conjur.ResourcesApi(api_client)
    account = 'account_example' # str | Organization account name
kind = 'user' # str | Type of resource
identifier = 'conjur/authn-iam/test' # str | ID of the resource for which to get the information about
permitted_roles = True # bool | Lists the roles which have the named privilege on a resource. (optional)
privilege = 'privilege_example' # str | Level of privilege to filter on. Can only be used in combination with `permitted_roles` or `check` parameter. (optional)
check = True # bool | Check whether a role has a privilege on a resource. (optional)
role = 'myorg:host:host1' # str | Role to check privilege on. Can only be used in combination with `check` parameter. (optional)
x_request_id = 'test-id' # str | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  (optional)

    try:
        # Shows a description of a single resource.
        api_response = api_instance.show_resource(account, kind, identifier, permitted_roles=permitted_roles, privilege=privilege, check=check, role=role, x_request_id=x_request_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ResourcesApi->show_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| Organization account name | 
 **kind** | **str**| Type of resource | 
 **identifier** | **str**| ID of the resource for which to get the information about | 
 **permitted_roles** | **bool**| Lists the roles which have the named privilege on a resource. | [optional] 
 **privilege** | **str**| Level of privilege to filter on. Can only be used in combination with &#x60;permitted_roles&#x60; or &#x60;check&#x60; parameter. | [optional] 
 **check** | **bool**| Check whether a role has a privilege on a resource. | [optional] 
 **role** | **str**| Role to check privilege on. Can only be used in combination with &#x60;check&#x60; parameter. | [optional] 
 **x_request_id** | **str**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 

### Return type

[**Resource**](Resource.md)

### Authorization

[conjurAuth](../README.md#conjurAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response body contains the list of role memberships or permitted roles |  -  |
**204** | Permissions check was successful |  -  |
**400** | The server cannot process the request due to malformed request syntax |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | The authenticated user lacks the necessary privileges |  -  |
**404** | The requested resource does not exist, the authenticated user lacks the required privileges to enumerate this resource, or its value has not been set |  -  |
**422** | A request parameter was either missing or invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_resources_for_account**
> list[Resource] show_resources_for_account(account, kind=kind, search=search, offset=offset, limit=limit, count=count, role=role, acting_as=acting_as, x_request_id=x_request_id)

Lists resources within an organization account.

Lists resources within an organization account.  If a `kind` query parameter is given, narrows results to only resources of that kind.  If a `limit` is given, returns no more than that number of results. Providing an `offset` skips a number of resources before returning the rest. In addition, providing an `offset` will give `limit` a default value of 10 if none other is provided. These two parameters can be combined to page through results.  If the parameter `count` is `true`, returns only the number of items in the list.  ##### Text search  If the `search` parameter is provided, narrows results to those pertaining to the search query. Search works across resource IDs and the values of annotations. It weighs results so that those with matching id or a matching value of an annotation called `name` appear first, then those with another matching annotation value, and finally those with a matching  `kind`. 

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
    api_instance = conjur.ResourcesApi(api_client)
    account = 'account_example' # str | Organization account name
kind = 'user' # str | Type of resource (optional)
search = 'db' # str | Filter resources based on this value by name (optional)
offset = 56 # int | When listing resources, start at this item number. (optional)
limit = 56 # int | When listing resources, return up to this many results. (optional)
count = True # bool | When listing resources, if `true`, return only the count of the results. (optional)
role = 'myorg:host:host1' # str | Retrieves the resources list for a different role if the authenticated role has access (optional)
acting_as = 'myorg:host:host1' # str | Retrieves the resources list for a different role if the authenticated role has access (optional)
x_request_id = 'test-id' # str | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  (optional)

    try:
        # Lists resources within an organization account.
        api_response = api_instance.show_resources_for_account(account, kind=kind, search=search, offset=offset, limit=limit, count=count, role=role, acting_as=acting_as, x_request_id=x_request_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ResourcesApi->show_resources_for_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| Organization account name | 
 **kind** | **str**| Type of resource | [optional] 
 **search** | **str**| Filter resources based on this value by name | [optional] 
 **offset** | **int**| When listing resources, start at this item number. | [optional] 
 **limit** | **int**| When listing resources, return up to this many results. | [optional] 
 **count** | **bool**| When listing resources, if &#x60;true&#x60;, return only the count of the results. | [optional] 
 **role** | **str**| Retrieves the resources list for a different role if the authenticated role has access | [optional] 
 **acting_as** | **str**| Retrieves the resources list for a different role if the authenticated role has access | [optional] 
 **x_request_id** | **str**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 

### Return type

[**list[Resource]**](Resource.md)

### Authorization

[conjurAuth](../README.md#conjurAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response body contains a list of resources |  -  |
**400** | The server cannot process the request due to malformed request syntax |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | The authenticated user lacks the necessary privileges |  -  |
**422** | A request parameter was either missing or invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_resources_for_all_accounts**
> list[Resource] show_resources_for_all_accounts(account=account, kind=kind, search=search, offset=offset, limit=limit, count=count, role=role, acting_as=acting_as, x_request_id=x_request_id)

Lists resources within an organization account.

Lists resources within an organization account.  In the absence of an `account` query parameter, shows results for the account of the authorization token user.  If an `account` query parameter is given, shows results for the specified account.  If a `kind` query parameter is given, narrows results to only resources of that kind.  If a `limit` is given, returns no more than that number of results. Providing an `offset` skips a number of resources before returning the rest. In addition, providing an `offset` will give `limit` a default value of 10 if none other is provided. These two parameters can be combined to page through results.  If the parameter `count` is `true`, returns only the number of items in the list.  ##### Text search  If the `search` parameter is provided, narrows results to those pertaining to the search query. Search works across resource IDs and the values of annotations. It weighs results so that those with matching id or a matching value of an annotation called `name` appear first, then those with another matching annotation value, and finally those with a matching  `kind`.\" 

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
    api_instance = conjur.ResourcesApi(api_client)
    account = 'myorg' # str | Organization account name (optional)
kind = 'user' # str | Type of resource (optional)
search = 'db' # str | Filter resources based on this value by name (optional)
offset = 56 # int | When listing resources, start at this item number. (optional)
limit = 56 # int | When listing resources, return up to this many results. (optional)
count = True # bool | When listing resources, if `true`, return only the count of the results. (optional)
role = 'myorg:host:host1' # str | Retrieves the resources list for a different role if the authenticated role has access (optional)
acting_as = 'myorg:host:host1' # str | Retrieves the resources list for a different role if the authenticated role has access (optional)
x_request_id = 'test-id' # str | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  (optional)

    try:
        # Lists resources within an organization account.
        api_response = api_instance.show_resources_for_all_accounts(account=account, kind=kind, search=search, offset=offset, limit=limit, count=count, role=role, acting_as=acting_as, x_request_id=x_request_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ResourcesApi->show_resources_for_all_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| Organization account name | [optional] 
 **kind** | **str**| Type of resource | [optional] 
 **search** | **str**| Filter resources based on this value by name | [optional] 
 **offset** | **int**| When listing resources, start at this item number. | [optional] 
 **limit** | **int**| When listing resources, return up to this many results. | [optional] 
 **count** | **bool**| When listing resources, if &#x60;true&#x60;, return only the count of the results. | [optional] 
 **role** | **str**| Retrieves the resources list for a different role if the authenticated role has access | [optional] 
 **acting_as** | **str**| Retrieves the resources list for a different role if the authenticated role has access | [optional] 
 **x_request_id** | **str**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 

### Return type

[**list[Resource]**](Resource.md)

### Authorization

[conjurAuth](../README.md#conjurAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response body contains a list of resources |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | The authenticated user lacks the necessary privileges |  -  |
**422** | A request parameter was either missing or invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_resources_for_kind**
> list[Resource] show_resources_for_kind(account, kind, search=search, offset=offset, limit=limit, count=count, role=role, acting_as=acting_as, x_request_id=x_request_id)

Lists resources of the same kind within an organization account.

Lists resources of the same kind within an organization account.  Kinds of resources include: policy, user, host, group, layer, or variable  If a `limit` is given, returns no more than that number of results. Providing an `offset` skips a number of resources before returning the rest. In addition, providing an `offset` will give `limit` a default value of 10 if none other is provided. These two parameters can be combined to page through results.  If the parameter `count` is `true`, returns only the number of items in the list.  ##### Text search  If the `search` parameter is provided, narrows results to those pertaining to the search query. Search works across resource IDs and the values of annotations. It weighs results so that those with matching id or a matching value of an annotation called `name` appear first, then those with another matching annotation value, and finally those with a matching  `kind`. 

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
    api_instance = conjur.ResourcesApi(api_client)
    account = 'account_example' # str | Organization account name
kind = 'user' # str | Type of resource
search = 'db' # str | Filter resources based on this value by name (optional)
offset = 56 # int | When listing resources, start at this item number. (optional)
limit = 56 # int | When listing resources, return up to this many results. (optional)
count = True # bool | When listing resources, if `true`, return only the count of the results. (optional)
role = 'myorg:host:host1' # str | Retrieves the resources list for a different role if the authenticated role has access (optional)
acting_as = 'myorg:host:host1' # str | Retrieves the resources list for a different role if the authenticated role has access (optional)
x_request_id = 'test-id' # str | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  (optional)

    try:
        # Lists resources of the same kind within an organization account.
        api_response = api_instance.show_resources_for_kind(account, kind, search=search, offset=offset, limit=limit, count=count, role=role, acting_as=acting_as, x_request_id=x_request_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ResourcesApi->show_resources_for_kind: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| Organization account name | 
 **kind** | **str**| Type of resource | 
 **search** | **str**| Filter resources based on this value by name | [optional] 
 **offset** | **int**| When listing resources, start at this item number. | [optional] 
 **limit** | **int**| When listing resources, return up to this many results. | [optional] 
 **count** | **bool**| When listing resources, if &#x60;true&#x60;, return only the count of the results. | [optional] 
 **role** | **str**| Retrieves the resources list for a different role if the authenticated role has access | [optional] 
 **acting_as** | **str**| Retrieves the resources list for a different role if the authenticated role has access | [optional] 
 **x_request_id** | **str**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 

### Return type

[**list[Resource]**](Resource.md)

### Authorization

[conjurAuth](../README.md#conjurAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response body contains a list of resources |  -  |
**400** | The server cannot process the request due to malformed request syntax |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | The authenticated user lacks the necessary privileges |  -  |
**422** | A request parameter was either missing or invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

