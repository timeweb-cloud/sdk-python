# Bonus

Оплата заявки на продление/регистрацию домена бонусом

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**money_source** | **object** | Тип создаваемой заявки. | 
**person_id** | **object** | Идентификатор администратора, на которого зарегистрирован домен. | [optional] 
**bonus_id** | **object** | Идентификатор бонуса. | 

## Example

```python
from timeweb_cloud_api.models.bonus import Bonus

# TODO update the JSON string below
json = "{}"
# create an instance of Bonus from a JSON string
bonus_instance = Bonus.from_json(json)
# print the JSON string representation of the object
print Bonus.to_json()

# convert the object into a dict
bonus_dict = bonus_instance.to_dict()
# create an instance of Bonus from a dict
bonus_form_dict = bonus.from_dict(bonus_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


