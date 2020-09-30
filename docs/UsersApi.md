# swagger_client.UsersApi

All URIs are relative to *https://sandbox.stytch.io/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user**](UsersApi.md#create_user) | **POST** /users | Create user
[**delete_email**](UsersApi.md#delete_email) | **DELETE** /users/{user_id}/emails/{email_id} | Delete email
[**delete_user**](UsersApi.md#delete_user) | **DELETE** /users/{user_id} | Delete user
[**get_user_by_id**](UsersApi.md#get_user_by_id) | **GET** /users/{user_id} | Get user
[**get_user_email_verify**](UsersApi.md#get_user_email_verify) | **POST** /users/{user_id}/emails/{email_id}/verify | Verify email
[**update_user**](UsersApi.md#update_user) | **PUT** /users/{user_id} | Update user

# **create_user**
> UserCreateResponse create_user(body)

Create user

Add a user to Stytch. A user_id is returned in the response that can then be used to perform other operations within Stytch.

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.UserCreate() # UserCreate | Created user object

try:
    # Create user
    api_response = api_instance.create_user(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserCreate**](UserCreate.md)| Created user object | 

### Return type

[**UserCreateResponse**](UserCreateResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_email**
> UserDeleteResponse delete_email(user_id, email_id)

Delete email

Remove an email from a given user.

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | The user_id to delete an email from
email_id = 'email_id_example' # str | The email_id to be deleted

try:
    # Delete email
    api_response = api_instance.delete_email(user_id, email_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->delete_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user_id to delete an email from | 
 **email_id** | **str**| The email_id to be deleted | 

### Return type

[**UserDeleteResponse**](UserDeleteResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> UserDeleteResponse delete_user(user_id)

Delete user

Remove a user from Stytch.

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | The user_id to be deleted

try:
    # Delete user
    api_response = api_instance.delete_user(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user_id to be deleted | 

### Return type

[**UserDeleteResponse**](UserDeleteResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_by_id**
> UserGetResponse get_user_by_id(user_id)

Get user

Fetch a given user to see what their various attributes are.

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | The user_id for the user to fetch.

try:
    # Get user
    api_response = api_instance.get_user_by_id(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user_id for the user to fetch. | 

### Return type

[**UserGetResponse**](UserGetResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_email_verify**
> EmailVerifyResponse get_user_email_verify(user_id, email_id)

Verify email

Prompt for a verification email to be sent to the user to confirm the correct email was entered. The email must be verified before the user needs to login next.

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | The user_id for the user to fetch.
email_id = 'email_id_example' # str | The email_id for the given user to verify.

try:
    # Verify email
    api_response = api_instance.get_user_email_verify(user_id, email_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_email_verify: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user_id for the user to fetch. | 
 **email_id** | **str**| The email_id for the given user to verify. | 

### Return type

[**EmailVerifyResponse**](EmailVerifyResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> UserUpdateResponse update_user(body, user_id)

Update user

Update a user's attributes. For example, you can add additional emails or change the user's primary email.

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.UserUpdate() # UserUpdate | Updated user object
user_id = 'user_id_example' # str | The user_id to update.

try:
    # Update user
    api_response = api_instance.update_user(body, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserUpdate**](UserUpdate.md)| Updated user object | 
 **user_id** | **str**| The user_id to update. | 

### Return type

[**UserUpdateResponse**](UserUpdateResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

