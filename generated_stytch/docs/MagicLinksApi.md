# stytch.MagicLinksApi

All URIs are relative to *https://test.stytch.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_user_magic_link_authenticate**](MagicLinksApi.md#post_user_magic_link_authenticate) | **POST** /magic_links/{token}/authenticate | Authenticate magic link
[**send_email_magic_link**](MagicLinksApi.md#send_email_magic_link) | **POST** /magic_links/send_by_email | Send magic link by email
[**send_magic_link**](MagicLinksApi.md#send_magic_link) | **POST** /magic_links/send | Send magic link


# **post_user_magic_link_authenticate**
> MagicLinkAuthenticateResponse post_user_magic_link_authenticate(token, magic_link_authenticate)

Authenticate magic link

Authenticate a user given a magic link. This endpoint verifies that the link is valid, hasn't expired, and any optional security settings such as ip match or user agent match are satisfied. Not to be confused with the emails verify endpoint meant for initial, one time verification that the correct email was supplied during sign up.

### Example

* Basic Authentication (apiKeyAuth):
```python
from __future__ import print_function
import time
import stytch
from stytch.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://test.stytch.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = stytch.Configuration(
    host = "https://test.stytch.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: apiKeyAuth
configuration = stytch.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with stytch.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = stytch.MagicLinksApi(api_client)
    token = 'token_example' # str | 
magic_link_authenticate = stytch.MagicLinkAuthenticate() # MagicLinkAuthenticate | Magic link object

    try:
        # Authenticate magic link
        api_response = api_instance.post_user_magic_link_authenticate(token, magic_link_authenticate)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MagicLinksApi->post_user_magic_link_authenticate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 
 **magic_link_authenticate** | [**MagicLinkAuthenticate**](MagicLinkAuthenticate.md)| Magic link object | 

### Return type

[**MagicLinkAuthenticateResponse**](MagicLinkAuthenticateResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_email_magic_link**
> MagicLinkSendByEmailResponse send_email_magic_link(magic_link_send_by_email)

Send magic link by email

Send a magic link to the user. You can optionally include additional security measures such as requiring the ip address the link is requested from match the one it's clicked from.

### Example

* Basic Authentication (apiKeyAuth):
```python
from __future__ import print_function
import time
import stytch
from stytch.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://test.stytch.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = stytch.Configuration(
    host = "https://test.stytch.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: apiKeyAuth
configuration = stytch.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with stytch.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = stytch.MagicLinksApi(api_client)
    magic_link_send_by_email = stytch.MagicLinkSendByEmail() # MagicLinkSendByEmail | 

    try:
        # Send magic link by email
        api_response = api_instance.send_email_magic_link(magic_link_send_by_email)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MagicLinksApi->send_email_magic_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **magic_link_send_by_email** | [**MagicLinkSendByEmail**](MagicLinkSendByEmail.md)|  | 

### Return type

[**MagicLinkSendByEmailResponse**](MagicLinkSendByEmailResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_magic_link**
> MagicLinkSendResponse send_magic_link(magic_link_send)

Send magic link

Send a magic link to the user. You can optionally include additional security measures such as requiring the ip address the link is requested from match the one it's clicked from.

### Example

* Basic Authentication (apiKeyAuth):
```python
from __future__ import print_function
import time
import stytch
from stytch.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://test.stytch.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = stytch.Configuration(
    host = "https://test.stytch.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: apiKeyAuth
configuration = stytch.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with stytch.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = stytch.MagicLinksApi(api_client)
    magic_link_send = stytch.MagicLinkSend() # MagicLinkSend | 

    try:
        # Send magic link
        api_response = api_instance.send_magic_link(magic_link_send)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MagicLinksApi->send_magic_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **magic_link_send** | [**MagicLinkSend**](MagicLinkSend.md)|  | 

### Return type

[**MagicLinkSendResponse**](MagicLinkSendResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

