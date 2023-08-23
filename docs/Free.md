# Free

Обновление заявки на перенос домена

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**money_source** | **object** | Тип создаваемой заявки. | 
**person_id** | **object** | Идентификатор администратора, на которого зарегистрирован домен. | [optional] 
**auth_code** | **object** | Код авторизации для переноса домена. | 

## Example

```python
from timeweb_cloud_api.models.free import Free

# TODO update the JSON string below
json = "{}"
# create an instance of Free from a JSON string
free_instance = Free.from_json(json)
# print the JSON string representation of the object
print Free.to_json()

# convert the object into a dict
free_dict = free_instance.to_dict()
# create an instance of Free from a dict
free_form_dict = free.from_dict(free_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


