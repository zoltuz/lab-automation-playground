# VerifyResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | The &#x60;username&#x60; of the user. | [optional] 
**user_id** | **str** | The &#x60;userId&#x60; of the user. | [optional] 
**status** | **str** | The status of the authentication request. Will be one of &#x60;MFA_REQUIRED&#x60; or &#x60;SUCCESS&#x60;. &#x60;MFA_REQUIRED&#x60; means that MultiFactor Authentication is activated for the account. A &#x60;passCode&#x60; and &#x60;stateToken&#x60; along with a &#x60;factorId&#x60; must be sent via the &#x60;verify&#x60; endpoint to complete the authentication process. | [optional] 
**api_key** | **str** | An API key, which can be used to access any of the endpoints that support apiKey authentication. The API key will only be displayed once. To generate a new API key go to Riffyn Application and revoke the key in the &#x60;Security Settings&#x60; interface. This field will not appear if an api-key exists for this user. | [optional] 
**api_key_name** | **str** | The default name for the api-key that was generated. The default &#x60;name&#x60; for this key will be &#x60;loginKey&#x60;. To rename the key use the &#x60;updateApiKey&#x60; endpoint. This field will not appear if an api-key exists for this user. | [optional] 
**message** | **str** | A message regarding the API key. | [optional] 
**access_token** | **str** | An access token, which can be used to access any of the endpoints that don&#x27;t require &#x60;basic authentication&#x60;. The &#x60;access-token&#x60; can be used for the same endpoints as &#x60;api-key&#x60;. This access token will expire 30 minutes from generation. | [optional] 
**access_token_expires_at** | **str** | The date and time the &#x60;accessToken&#x60; will expire. The accessToken is set to expire 30 minutes from generation. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

