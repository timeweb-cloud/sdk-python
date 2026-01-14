# TokenPackage

Пакет токенов

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | Уникальный идентификатор пакета | 
**model_id** | **object** | ID модели, к которой применяется пакет токенов | 
**name** | **object** | Название пакета токенов | 
**package_type** | **object** | Тип пакета (base - базовый, additional - дополнительный, promo - промо) | 
**type** | **object** | Тип сущности, к которой относится пакет (agent - агент, knowledgebase - база знаний) | 
**token_amount** | **object** | Количество токенов в пакете | 
**price** | **object** | Цена пакета в целых единицах | 
**duration_days** | **object** | Продолжительность пакета в днях (null для дополнительных пакетов) | [optional] 
**is_available** | **object** | Флаг, указывающий доступность пакета | 

## Example

```python
from timeweb_cloud_api.models.token_package import TokenPackage

# TODO update the JSON string below
json = "{}"
# create an instance of TokenPackage from a JSON string
token_package_instance = TokenPackage.from_json(json)
# print the JSON string representation of the object
print TokenPackage.to_json()

# convert the object into a dict
token_package_dict = token_package_instance.to_dict()
# create an instance of TokenPackage from a dict
token_package_form_dict = token_package.from_dict(token_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


