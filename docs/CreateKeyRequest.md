# CreateKeyRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **object** | Тело SSH-ключа. | 
**is_default** | **object** | Будет ли выбираться SSH-ключ по умолчанию при создании сервера.   | 
**name** | **object** | Название SSH-ключа. | 

## Example

```python
from timeweb_cloud_api.models.create_key_request import CreateKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateKeyRequest from a JSON string
create_key_request_instance = CreateKeyRequest.from_json(json)
# print the JSON string representation of the object
print CreateKeyRequest.to_json()

# convert the object into a dict
create_key_request_dict = create_key_request_instance.to_dict()
# create an instance of CreateKeyRequest from a dict
create_key_request_form_dict = create_key_request.from_dict(create_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


