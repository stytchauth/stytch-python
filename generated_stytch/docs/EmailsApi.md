# stytch.EmailsApi

All URIs are relative to *https://test.stytch.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_email**](EmailsApi.md#delete_email) | **DELETE** /emails/{email_id}/users/{user_id} | Delete email
[**send_email_verification**](EmailsApi.md#send_email_verification) | **POST** /emails/{email_id}/send_verification | Send Email Verification
[**verify_email**](EmailsApi.md#verify_email) | **POST** /emails/{token}/verify | Verify Email


# **delete_email**
> UserEmailDeleteResponse delete_email(email_id, user_id)

Delete email

Remove an email from a given user.

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
    api_instance = stytch.EmailsApi(api_client)
    email_id = 'email-test-c1a1d554-a93c-11ea-bb37-0242ac130002' # str | The email_id to be deleted.
user_id = 'user-test-b8797f2c-a93c-11ea-bb37-0242ac130002' # str | The user_id to delete an email from.

    try:
        # Delete email
        api_response = api_instance.delete_email(email_id, user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EmailsApi->delete_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_id** | **str**| The email_id to be deleted. | 
 **user_id** | **str**| The user_id to delete an email from. | 

### Return type

[**UserEmailDeleteResponse**](UserEmailDeleteResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **send_email_verification**
> SendVerificationResponse send_email_verification(user_id, email_id)

Send Email Verification

Prompt for a verification email to be sent to the user to confirm the correct email was entered. The email must be verified before the user needs to login next.

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
    api_instance = stytch.EmailsApi(api_client)
    user_id = 'user-test-b8797f2c-a93c-11ea-bb37-0242ac130002' # str | The user_id for the user to fetch.
email_id = 'email-test-c1a1d554-a93c-11ea-bb37-0242ac130002' # str | The email_id for the given user to verify.

    try:
        # Send Email Verification
        api_response = api_instance.send_email_verification(user_id, email_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EmailsApi->send_email_verification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user_id for the user to fetch. | 
 **email_id** | **str**| The email_id for the given user to verify. | 

### Return type

[**SendVerificationResponse**](SendVerificationResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **verify_email**
> VerifyEmailResponse verify_email(token)

Verify Email

Verify that a user supplied the correct email during signup.

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
    api_instance = stytch.EmailsApi(api_client)
    token = 'KKFa7u0KgAgHGXkZ77gOEd8YjyzzcC1rvMINgsZuIxM' # str | The token used to verify user's email.

    try:
        # Verify Email
        api_response = api_instance.verify_email(token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EmailsApi->verify_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The token used to verify user&#39;s email. | 

### Return type

[**VerifyEmailResponse**](VerifyEmailResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
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

