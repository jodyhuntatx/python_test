# conjur.RolesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_member_to_role**](RolesApi.md#add_member_to_role) | **POST** /roles/{account}/{kind}/{identifier} | Update or modify an existing role membership
[**remove_member_from_role**](RolesApi.md#remove_member_from_role) | **DELETE** /roles/{account}/{kind}/{identifier} | Deletes an existing role membership
[**show_role**](RolesApi.md#show_role) | **GET** /roles/{account}/{kind}/{identifier} | Get role information


# **add_member_to_role**
> add_member_to_role(account, kind, identifier, members, member, x_request_id=x_request_id)

Update or modify an existing role membership

Updates or modifies an existing role membership.  If a role A is granted to a role B, then role A is said to have role B as a member. These relationships are described in the “members” portion of the returned JSON.  When the `members` query parameter is provided, you will get the members of a role.  When the `members` and `member` query parameters are provided, the role specfified by `member` will be added as a member of the role specified in the endpoint URI. 

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
    api_instance = conjur.RolesApi(api_client)
    account = 'account_example' # str | Organization account name
kind = 'user' # str | Type of resource
identifier = 'admin' # str | ID of the role for which to get the information about
members = 'members_example' # str | Returns a list of the Role's members.
member = 'member_example' # str | The identifier of the Role to be added as a member.
x_request_id = 'test-id' # str | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  (optional)

    try:
        # Update or modify an existing role membership
        api_instance.add_member_to_role(account, kind, identifier, members, member, x_request_id=x_request_id)
    except ApiException as e:
        print("Exception when calling RolesApi->add_member_to_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| Organization account name | 
 **kind** | **str**| Type of resource | 
 **identifier** | **str**| ID of the role for which to get the information about | 
 **members** | **str**| Returns a list of the Role&#39;s members. | 
 **member** | **str**| The identifier of the Role to be added as a member. | 
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
**204** | Member was added to role successfully |  -  |
**400** | The server cannot process the request due to malformed request syntax |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | The authenticated user lacks the necessary privileges |  -  |
**404** | The requested resource does not exist, the authenticated user lacks the required privileges to enumerate this resource, or its value has not been set |  -  |
**422** | A request parameter was either missing or invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_member_from_role**
> remove_member_from_role(account, kind, identifier, members, member, x_request_id=x_request_id)

Deletes an existing role membership

Deletes an existing role membership.  If a role A is granted to a role B, then role A is said to have role B as a member. These relationships are described in the “members” portion of the returned JSON.  When the `members` query parameter is provided, you will get the members of a role.  When the `members` and `member` query parameters are provided, the role specfified by `member` will be removed as a member of the role specified in the endpoint URI. 

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
    api_instance = conjur.RolesApi(api_client)
    account = 'account_example' # str | Organization account name
kind = 'user' # str | Type of resource
identifier = 'admin' # str | ID of the role for which to get the information about
members = 'members_example' # str | Returns a list of the Role's members.
member = 'member_example' # str | The identifier of the Role to be added as a member.
x_request_id = 'test-id' # str | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  (optional)

    try:
        # Deletes an existing role membership
        api_instance.remove_member_from_role(account, kind, identifier, members, member, x_request_id=x_request_id)
    except ApiException as e:
        print("Exception when calling RolesApi->remove_member_from_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| Organization account name | 
 **kind** | **str**| Type of resource | 
 **identifier** | **str**| ID of the role for which to get the information about | 
 **members** | **str**| Returns a list of the Role&#39;s members. | 
 **member** | **str**| The identifier of the Role to be added as a member. | 
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
**204** | Member was deleted from role successfully |  -  |
**400** | The server cannot process the request due to malformed request syntax |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | The authenticated user lacks the necessary privileges |  -  |
**404** | The requested resource does not exist, the authenticated user lacks the required privileges to enumerate this resource, or its value has not been set |  -  |
**422** | A request parameter was either missing or invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_role**
> object show_role(account, kind, identifier, all=all, memberships=memberships, members=members, offset=offset, limit=limit, count=count, search=search, graph=graph, x_request_id=x_request_id)

Get role information

Gets detailed information about a specific role, including the role members.  If a role A is granted to a role B, then role A is said to have role B as a member. These relationships are described in the “members” portion of the returned JSON.  ##### Listing members  If `members` is provided, you will get the members of a role.  If a `kind` query parameter is given, narrows results to only resources of that kind.  If a `limit` is given, returns no more than that number of results. Providing an `offset` skips a number of resources before returning the rest. In addition, providing an `offset` will give limit a default value of 10 if none other is provided. These two parameters can be combined to page through results.  If the parameter `count` is true, returns only the number of items in the list.  ##### Text search  If the search parameter is provided, narrows results to those pertaining to the search query. Search works across resource IDs and the values of annotations. It weights results so that those with matching id or a matching value of an annotation called name appear first, then those with another matching annotation value, and finally those with a matching kind.  ##### Parameter Priority  If Conjur is given any combination of optional parameters, it responds with ONLY results for the parameter of the highest priority.  1. `graph` 2. `all` 3. `memberships` 4. `members` 

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
    api_instance = conjur.RolesApi(api_client)
    account = 'account_example' # str | Organization account name
kind = 'user' # str | Type of resource
identifier = 'admin' # str | ID of the role for which to get the information about
all = 'all_example' # str | Returns an array of Role IDs representing all role memberships, expanded recursively. (optional)
memberships = 'memberships_example' # str | Returns all direct role memberships (members not expanded recursively). (optional)
members = 'members_example' # str | Returns a list of the Role's members. (optional)
offset = 56 # int | When listing members, start at this item number. (optional)
limit = 56 # int | When listing members, return up to this many results. (optional)
count = True # bool | When listing members, if `true`, return only the count of members. (optional)
search = 'user' # str | When listing members, the results will be narrowed to only those matching the provided string (optional)
graph = '' # str | If included in the query returns a graph view of the role (optional)
x_request_id = 'test-id' # str | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  (optional)

    try:
        # Get role information
        api_response = api_instance.show_role(account, kind, identifier, all=all, memberships=memberships, members=members, offset=offset, limit=limit, count=count, search=search, graph=graph, x_request_id=x_request_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RolesApi->show_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| Organization account name | 
 **kind** | **str**| Type of resource | 
 **identifier** | **str**| ID of the role for which to get the information about | 
 **all** | **str**| Returns an array of Role IDs representing all role memberships, expanded recursively. | [optional] 
 **memberships** | **str**| Returns all direct role memberships (members not expanded recursively). | [optional] 
 **members** | **str**| Returns a list of the Role&#39;s members. | [optional] 
 **offset** | **int**| When listing members, start at this item number. | [optional] 
 **limit** | **int**| When listing members, return up to this many results. | [optional] 
 **count** | **bool**| When listing members, if &#x60;true&#x60;, return only the count of members. | [optional] 
 **search** | **str**| When listing members, the results will be narrowed to only those matching the provided string | [optional] 
 **graph** | **str**| If included in the query returns a graph view of the role | [optional] 
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
**200** | The response body contains the requested role(s)/member(s) |  -  |
**400** | The server cannot process the request due to malformed request syntax |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | The authenticated user lacks the necessary privileges |  -  |
**404** | The requested resource does not exist, the authenticated user lacks the required privileges to enumerate this resource, or its value has not been set |  -  |
**422** | A request parameter was either missing or invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

