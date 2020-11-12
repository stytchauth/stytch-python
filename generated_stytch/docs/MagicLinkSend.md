# MagicLinkSend

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**method_id** | **str** | The method id for where to send the magic link, such as an email_id. | 
**magic_link_url** | **str** | The url the user clicks from the email magic link. This should be a url that your app receives and parses and subsequently send an api request to authenticate the magic link and log in the user. | [optional] 
**expiration_minutes** | **int** | Set the expiration for the email magic link, in minutes. By default, it expires in 1 hour. The minimum expiration is 5 minutes and the maximum is 7 days (10080 mins). | [optional] 
**template_id** | **str** | The template id to use for the magic link, for example the template_id that corresponds to a specific email format. | [optional] 
**attributes** | [**Attributes**](Attributes.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


