# TokenPackage

Пакет токенов

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID пакета | 
**model_id** | **object** | ID модели, к которой относится пакет | 
**service_type_id** | **object** | ID тарифа пакета в биллинге | 
**name** | **object** | Название пакета | 
**package_type** | **object** | Тип пакета: &#x60;base&#x60; — пакет подписки, &#x60;additional&#x60; — дополнительный пакет, &#x60;promo&#x60; — промо-пакет | 
**type** | **object** | Для чего пакет: &#x60;agent&#x60; — AI агент, &#x60;knowledgebase&#x60; — база знаний | 
**token_amount** | **object** | Количество токенов в пакете | 
**price** | **object** | Цена пакета в рублях | 
**duration_days** | **object** | Период подписки в днях. &#x60;null&#x60; для дополнительных пакетов | 
**is_available** | **object** | Пакет доступен для покупки | 

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


