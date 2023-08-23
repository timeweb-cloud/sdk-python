# CreatedApiKey

Токен.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **object** | Созданный токен, будет показан только один раз, его необходимо сохранить. | 
**id** | **object** | Уникальный идентификатор токена. | 
**created_at** | **object** | Значение времени, указанное в комбинированном формате даты и времени ISO8601, которое представляет, когда был создан токен. | 
**name** | **object** | Имя токена. | 
**expired_at** | **object** | Значение времени, указанное в комбинированном формате даты и времени ISO8601, которое представляет, когда истекает токен. | 

## Example

```python
from openapi_client.models.created_api_key import CreatedApiKey

# TODO update the JSON string below
json = "{}"
# create an instance of CreatedApiKey from a JSON string
created_api_key_instance = CreatedApiKey.from_json(json)
# print the JSON string representation of the object
print CreatedApiKey.to_json()

# convert the object into a dict
created_api_key_dict = created_api_key_instance.to_dict()
# create an instance of CreatedApiKey from a dict
created_api_key_form_dict = created_api_key.from_dict(created_api_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


