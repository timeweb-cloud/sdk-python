# TopLevelDomain

Доменная зона.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_buy_periods** | **object** | Список доступных периодов для регистрации/продления доменов со стоимостью. | 
**early_renew_period** | **object** | Количество дней до истечение срока регистрации, когда можно продлять домен. | 
**grace_period** | **object** | Количество дней, которые действует льготный период когда вы ещё можете продлить домен, после окончания его регистрации | 
**id** | **object** | ID доменной зоны. | 
**is_published** | **object** | Это логическое значение, которое показывает, опубликована ли доменная зона. | 
**is_registered** | **object** | Это логическое значение, которое показывает, зарегистрирована ли доменная зона. | 
**is_whois_privacy_default_enabled** | **object** | Это логическое значение, которое показывает, включено ли по умолчанию скрытие данных администратора для доменной зоны. | 
**is_whois_privacy_enabled** | **object** | Это логическое значение, которое показывает, доступно ли управление скрытием данных администратора для доменной зоны. | 
**name** | **object** | Имя доменной зоны. | 
**price** | **object** | Цена регистрации домена | 
**prolong_price** | **object** | Цена продления домена. | 
**registrar** | **object** | Регистратор доменной зоны. | 
**transfer** | **object** | Цена услуги трансфера домена. | 
**whois_privacy_price** | **object** | Цена услуги скрытия данных администратора для доменной зоны. | 

## Example

```python
from timeweb_cloud_api.models.top_level_domain import TopLevelDomain

# TODO update the JSON string below
json = "{}"
# create an instance of TopLevelDomain from a JSON string
top_level_domain_instance = TopLevelDomain.from_json(json)
# print the JSON string representation of the object
print TopLevelDomain.to_json()

# convert the object into a dict
top_level_domain_dict = top_level_domain_instance.to_dict()
# create an instance of TopLevelDomain from a dict
top_level_domain_form_dict = top_level_domain.from_dict(top_level_domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


