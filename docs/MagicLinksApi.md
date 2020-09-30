# swagger_client.MagicLinksApi

All URIs are relative to *https://sandbox.stytch.io/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_user_magic_link**](MagicLinksApi.md#post_user_magic_link) | **POST** /magic_links/send | Send magic link
[**post_user_magic_link_authenticate**](MagicLinksApi.md#post_user_magic_link_authenticate) | **POST** /magic_links/{magic_link_id}/authenticate | Authenticate magic link

# **post_user_magic_link**
> MagicLinkSendResponse post_user_magic_link(body)

Send magic link

Send a magic link to the user. You can optionally include additional security measures such as requiring the ip address the link is requested from match the one it's clicked from.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: apiKeyAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.MagicLinksApi(swagger_client.ApiClient(configuration))
body = swagger_client.MagicLinkSend() # MagicLinkSend | 

try:
    # Send magic link
    api_response = api_instance.post_user_magic_link(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MagicLinksApi->post_user_magic_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MagicLinkSend**](MagicLinkSend.md)|  | 

### Return type

[**MagicLinkSendResponse**](MagicLinkSendResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_user_magic_link_authenticate**
> MagicLinkAuthenticateResponse post_user_magic_link_authenticate(body, magic_link_id)

Authenticate magic link

Authenticate a user given a magic link. This endpoint verifies that the link is valid, hasn't expired, and any optional security settings such as ip match or user agent match are satisfied. Not to be confused with the emails verify endpoint meant for initial, one time verification that the correct email was supplied during sign up.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: apiKeyAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.MagicLinksApi(swagger_client.ApiClient(configuration))
body = swagger_client.MagicLinkAuthenticate() # MagicLinkAuthenticate | Magic link object
magic_link_id = 'magic_link_id_example' # str | 

try:
    # Authenticate magic link
    api_response = api_instance.post_user_magic_link_authenticate(body, magic_link_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MagicLinksApi->post_user_magic_link_authenticate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MagicLinkAuthenticate**](MagicLinkAuthenticate.md)| Magic link object | 
 **magic_link_id** | **str**|  | 

### Return type

[**MagicLinkAuthenticateResponse**](MagicLinkAuthenticateResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

