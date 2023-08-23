# UpdateKeyRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **object** | Тело SSH-ключа | [optional] 
**is_default** | **object** | Будет ли выбираться SSH-ключ по умолчанию при создании сервера | [optional] 
**name** | **object** | Название SSH-ключа | [optional] 

## Example

```python
from timeweb_cloud_api.models.update_key_request import UpdateKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateKeyRequest from a JSON string
update_key_request_instance = UpdateKeyRequest.from_json(json)
# print the JSON string representation of the object
print UpdateKeyRequest.to_json()

# convert the object into a dict
update_key_request_dict = update_key_request_instance.to_dict()
# create an instance of UpdateKeyRequest from a dict
update_key_request_form_dict = update_key_request.from_dict(update_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


