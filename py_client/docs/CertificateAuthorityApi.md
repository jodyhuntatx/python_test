# conjur.CertificateAuthorityApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sign**](CertificateAuthorityApi.md#sign) | **POST** /ca/{account}/{service_id}/sign | Gets a signed certificate from the configured Certificate Authority service.


# **sign**
> CertificateJson sign(account, service_id, csr, ttl, accept=accept, x_request_id=x_request_id)

Gets a signed certificate from the configured Certificate Authority service.

Gets a signed certificate from the configured Certificate Authority service.  The request must include a valid Certificate Signing Request, and a desired TTL in ISO 8601 format.  *** IMPORTANT *** This endpoint is part of an early implementation of support for using Conjur as a certificate authority, and is currently available at the Community (or early alpha) level. This endpoint is still subject to breaking changes in the future. 

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
    api_instance = conjur.CertificateAuthorityApi(api_client)
    account = 'account_example' # str | Organization account name
service_id = 'ca-service' # str | Name of the Certificate Authority service
csr = 'csr_example' # str | 
ttl = 'ttl_example' # str | 
accept = 'application/x-pem-file' # str | Setting the Accept header to `application/x-pem-file` allows Conjur to respond with a formatted certificate (optional)
x_request_id = 'test-id' # str | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  (optional)

    try:
        # Gets a signed certificate from the configured Certificate Authority service.
        api_response = api_instance.sign(account, service_id, csr, ttl, accept=accept, x_request_id=x_request_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CertificateAuthorityApi->sign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| Organization account name | 
 **service_id** | **str**| Name of the Certificate Authority service | 
 **csr** | **str**|  | 
 **ttl** | **str**|  | 
 **accept** | **str**| Setting the Accept header to &#x60;application/x-pem-file&#x60; allows Conjur to respond with a formatted certificate | [optional] 
 **x_request_id** | **str**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 

### Return type

[**CertificateJson**](CertificateJson.md)

### Authorization

[conjurAuth](../README.md#conjurAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/x-pem-file

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The response body is the newly signed certificate |  -  |
**400** | The server cannot process the request due to malformed request syntax |  -  |
**401** | Authentication information is missing or invalid |  -  |
**403** | Either           - The authenticated role is not a Host role, - The authenticated Host does not have &#x60;sign&#x60; privilege for the CA service, or - The authenticated Host ID does not match the of the CSR Common Name (CN).  |  -  |
**404** | CA Service with the given ID does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

