# WhoAmI

Information about the client making a request
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** | The account attribute of the client provided access token. | [optional] 
**client_ip** | **str** | The request client IP address as determined by Conjur. This same IP address appears in application logs and audit logs. | [optional] 
**token_issued_at** | **str** | The issued timestamp, that is, when the provided access token was created (iat field in the JWT) | [optional] 
**user_agent** | **str** | The incoming request HTTP user agent header. | [optional] 
**username** | **str** | The username attribute of the provided access token. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


