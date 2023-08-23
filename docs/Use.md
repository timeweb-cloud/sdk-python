# Use

Оплата заявки на продление/регистрацию домена с баланса аккаунта

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**money_source** | **object** | Тип создаваемой заявки. | 
**person_id** | **object** | Идентификатор администратора, на которого зарегистрирован домен. | [optional] 

## Example

```python
from openapi_client.models.use import Use

# TODO update the JSON string below
json = "{}"
# create an instance of Use from a JSON string
use_instance = Use.from_json(json)
# print the JSON string representation of the object
print Use.to_json()

# convert the object into a dict
use_dict = use_instance.to_dict()
# create an instance of Use from a dict
use_form_dict = use.from_dict(use_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


