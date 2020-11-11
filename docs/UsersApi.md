# stytch.UsersApi

All URIs are relative to *https://test.stytch.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user**](UsersApi.md#create_user) | **POST** /users | Create user
[**delete_user**](UsersApi.md#delete_user) | **DELETE** /users/{user_id} | Delete user
[**get_user_by_id**](UsersApi.md#get_user_by_id) | **GET** /users/{user_id} | Get user
[**update_user**](UsersApi.md#update_user) | **PUT** /users/{user_id} | Update user


# **create_user**
> UserCreateResponse create_user(user_create)

Create user

Add a user to Stytch. A user_id is returned in the response that can then be used to perform other operations within Stytch.

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
    api_instance = stytch.UsersApi(api_client)
    user_create = stytch.UserCreate() # UserCreate | Created user object

    try:
        # Create user
        api_response = api_instance.create_user(user_create)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_create** | [**UserCreate**](UserCreate.md)| Created user object | 

### Return type

[**UserCreateResponse**](UserCreateResponse.md)

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

# **delete_user**
> UserDeleteResponse delete_user(user_id)

Delete user

Remove a user from Stytch.

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
    api_instance = stytch.UsersApi(api_client)
    user_id = 'user-test-b8797f2c-a93c-11ea-bb37-0242ac130002' # str | The user_id to be deleted.

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
 **user_id** | **str**| The user_id to be deleted. | 

### Return type

[**UserDeleteResponse**](UserDeleteResponse.md)

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

# **get_user_by_id**
> UserGetResponse get_user_by_id(user_id)

Get user

Fetch a given user to see what their various attributes are.

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
    api_instance = stytch.UsersApi(api_client)
    user_id = 'user-test-b8797f2c-a93c-11ea-bb37-0242ac130002' # str | The user_id for the user to fetch.

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

# **update_user**
> UserUpdateResponse update_user(user_id, user_update)

Update user

Update a user's attributes. For example, you can add additional emails or change the user's primary email.

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
    api_instance = stytch.UsersApi(api_client)
    user_id = 'user-test-b8797f2c-a93c-11ea-bb37-0242ac130002' # str | The user_id to update.
user_update = stytch.UserUpdate() # UserUpdate | Updated user object

    try:
        # Update user
        api_response = api_instance.update_user(user_id, user_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user_id to update. | 
 **user_update** | [**UserUpdate**](UserUpdate.md)| Updated user object | 

### Return type

[**UserUpdateResponse**](UserUpdateResponse.md)

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

