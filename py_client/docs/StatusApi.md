# conjur.StatusApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_authenticators**](StatusApi.md#get_authenticators) | **GET** /authenticators | Details about which authenticators are on the Conjur Server
[**get_gcp_authenticator_status**](StatusApi.md#get_gcp_authenticator_status) | **GET** /authn-gcp/{account}/status | Details whether an authentication service has been configured properly
[**get_service_authenticator_status**](StatusApi.md#get_service_authenticator_status) | **GET** /{authenticator}/{service_id}/{account}/status | Details whether an authentication service has been configured properly
[**health**](StatusApi.md#health) | **GET** /health | Health info about conjur
[**info**](StatusApi.md#info) | **GET** /info | Basic information about the Conjur Enterprise server
[**remote_health**](StatusApi.md#remote_health) | **GET** /remote_health/{remote} | Health info about a given Conjur Enterprise server
[**who_am_i**](StatusApi.md#who_am_i) | **GET** /whoami | Provides information about the client making an API request.


# **get_authenticators**
> AuthenticatorsResponse get_authenticators(x_request_id=x_request_id)

Details about which authenticators are on the Conjur Server

Response contains three members: installed, configured, and enabled.  installed: The authenticator is implemented in Conjur and is available for configuration configured: The authenticator has a webservice in the DB that was loaded by policy enabled: The authenticator is enabled (in the DB or in the ENV) and is ready for authentication 

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
    api_instance = conjur.StatusApi(api_client)
    x_request_id = 'test-id' # str | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  (optional)

    try:
        # Details about which authenticators are on the Conjur Server
        api_response = api_instance.get_authenticators(x_request_id=x_request_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatusApi->get_authenticators: %s\n" % e)
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
    api_instance = conjur.StatusApi(api_client)
    x_request_id = 'test-id' # str | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  (optional)

    try:
        # Details about which authenticators are on the Conjur Server
        api_response = api_instance.get_authenticators(x_request_id=x_request_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatusApi->get_authenticators: %s\n" % e)
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
    api_instance = conjur.StatusApi(api_client)
    x_request_id = 'test-id' # str | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  (optional)

    try:
        # Details about which authenticators are on the Conjur Server
        api_response = api_instance.get_authenticators(x_request_id=x_request_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatusApi->get_authenticators: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 

### Return type

[**AuthenticatorsResponse**](AuthenticatorsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [conjurAuth](../README.md#conjurAuth), [conjurKubernetesMutualTls](../README.md#conjurKubernetesMutualTls)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details about authenticators for this Conjur server |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gcp_authenticator_status**
> AuthenticatorStatus get_gcp_authenticator_status(account, x_request_id=x_request_id)

Details whether an authentication service has been configured properly

Once the status webservice has been properly configured and the relevant user groups have been given permissions to access the status webservice, the users in those groups can check the status of the authenticator.  This operation only supports the GCP authenticator  See [Conjur Documentation](https://docs.conjur.org/Latest/en/Content/Integrations/Authn-status.htm) for details on setting up the authenticator status webservice. 

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
    api_instance = conjur.StatusApi(api_client)
    account = 'dev' # str | The organization account name
x_request_id = 'test-id' # str | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  (optional)

    try:
        # Details whether an authentication service has been configured properly
        api_response = api_instance.get_gcp_authenticator_status(account, x_request_id=x_request_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatusApi->get_gcp_authenticator_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| The organization account name | 
 **x_request_id** | **str**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 

### Return type

[**AuthenticatorStatus**](AuthenticatorStatus.md)

### Authorization

[conjurAuth](../README.md#conjurAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response contains info about the result |  -  |
**400** | The server cannot process the request due to malformed request syntax |  -  |
**403** | The authenticated user lacks the necessary privileges |  -  |
**404** | The service was not found |  -  |
**500** | The response contains info about the result |  -  |
**501** | The response contains info about the result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_authenticator_status**
> AuthenticatorStatus get_service_authenticator_status(authenticator, service_id, account, x_request_id=x_request_id)

Details whether an authentication service has been configured properly

Once the status webservice has been properly configured and the relevant user groups have been given permissions to access the status webservice, the users in those groups can check the status of the authenticator.  Supported Authenticators:   - Azure   - OIDC  Not Supported:   - AWS IAM   - Kubernetes   - LDAP  See [Conjur Documentation](https://docs.conjur.org/Latest/en/Content/Integrations/Authn-status.htm) for details on setting up the authenticator status webservice. 

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
    api_instance = conjur.StatusApi(api_client)
    authenticator = 'authn-oidc' # str | The type of authenticator
service_id = 'prod%2fgke' # str | URL-Encoded authenticator service ID
account = 'dev' # str | The organization account name
x_request_id = 'test-id' # str | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  (optional)

    try:
        # Details whether an authentication service has been configured properly
        api_response = api_instance.get_service_authenticator_status(authenticator, service_id, account, x_request_id=x_request_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatusApi->get_service_authenticator_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authenticator** | **str**| The type of authenticator | 
 **service_id** | **str**| URL-Encoded authenticator service ID | 
 **account** | **str**| The organization account name | 
 **x_request_id** | **str**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 

### Return type

[**AuthenticatorStatus**](AuthenticatorStatus.md)

### Authorization

[conjurAuth](../README.md#conjurAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response contains info about the result |  -  |
**400** | The server cannot process the request due to malformed request syntax |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | The authenticated user lacks the necessary privileges |  -  |
**404** | The service was not found |  -  |
**500** | The response contains info about the result |  -  |
**501** | The response contains info about the result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **health**
> object health()

Health info about conjur

You can request health checks against any cluster node using the Conjur API. These routes do not require authentication.  The health check attempts an internal HTTP or TCP connection to each Conjur Enterprise service. It also attempts a simple transaction against all internal databases. 

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
    api_instance = conjur.StatusApi(api_client)
    
    try:
        # Health info about conjur
        api_response = api_instance.health()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatusApi->health: %s\n" % e)
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
    api_instance = conjur.StatusApi(api_client)
    
    try:
        # Health info about conjur
        api_response = api_instance.health()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatusApi->health: %s\n" % e)
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
    api_instance = conjur.StatusApi(api_client)
    
    try:
        # Health info about conjur
        api_response = api_instance.health()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatusApi->health: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth), [conjurAuth](../README.md#conjurAuth), [conjurKubernetesMutualTls](../README.md#conjurKubernetesMutualTls)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The tests were successful |  -  |
**502** | The tests failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **info**
> Info info()

Basic information about the Conjur Enterprise server

Information about the Conjur Enterprise node which was queried against.  Includes authenticator info, release/version info, configuration details, internal services, and role information. 

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
    api_instance = conjur.StatusApi(api_client)
    
    try:
        # Basic information about the Conjur Enterprise server
        api_response = api_instance.info()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatusApi->info: %s\n" % e)
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
    api_instance = conjur.StatusApi(api_client)
    
    try:
        # Basic information about the Conjur Enterprise server
        api_response = api_instance.info()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatusApi->info: %s\n" % e)
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
    api_instance = conjur.StatusApi(api_client)
    
    try:
        # Basic information about the Conjur Enterprise server
        api_response = api_instance.info()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatusApi->info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Info**](Info.md)

### Authorization

[basicAuth](../README.md#basicAuth), [conjurAuth](../README.md#conjurAuth), [conjurKubernetesMutualTls](../README.md#conjurKubernetesMutualTls)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | info |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remote_health**
> object remote_health(remote)

Health info about a given Conjur Enterprise server

Use the remote_health route to check the health of any Conjur Enterprise Server from any other Conjur Enterprise Server. With this route, you can check master health relative to a follower, or follower health relative to a standby, and so on. 

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
    api_instance = conjur.StatusApi(api_client)
    remote = 'conjur.myorg.com' # str | The hostname of the remote to check

    try:
        # Health info about a given Conjur Enterprise server
        api_response = api_instance.remote_health(remote)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatusApi->remote_health: %s\n" % e)
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
    api_instance = conjur.StatusApi(api_client)
    remote = 'conjur.myorg.com' # str | The hostname of the remote to check

    try:
        # Health info about a given Conjur Enterprise server
        api_response = api_instance.remote_health(remote)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatusApi->remote_health: %s\n" % e)
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
    api_instance = conjur.StatusApi(api_client)
    remote = 'conjur.myorg.com' # str | The hostname of the remote to check

    try:
        # Health info about a given Conjur Enterprise server
        api_response = api_instance.remote_health(remote)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatusApi->remote_health: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remote** | **str**| The hostname of the remote to check | 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth), [conjurAuth](../README.md#conjurAuth), [conjurKubernetesMutualTls](../README.md#conjurKubernetesMutualTls)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The tests were successful |  -  |
**502** | The tests failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **who_am_i**
> WhoAmI who_am_i(x_request_id=x_request_id)

Provides information about the client making an API request.

WhoAmI provides information about the client making an API request. It can be used to help troubleshoot configuration by verifying authentication and the client IP address for audit and network access restrictions. For more information, see Host Attributes. 

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
    api_instance = conjur.StatusApi(api_client)
    x_request_id = 'test-id' # str | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  (optional)

    try:
        # Provides information about the client making an API request.
        api_response = api_instance.who_am_i(x_request_id=x_request_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatusApi->who_am_i: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 

### Return type

[**WhoAmI**](WhoAmI.md)

### Authorization

[conjurAuth](../README.md#conjurAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details about the client making the request |  -  |
**401** | Authentication information is missing or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

