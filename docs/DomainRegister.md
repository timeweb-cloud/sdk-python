# DomainRegister

Заявка на регистрацию домена

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **object** | Тип создаваемой заявки. | 
**fqdn** | **object** | Полное имя домена. | 
**is_autoprolong_enabled** | **object** | Это логическое значение, которое показывает, включено ли автопродление домена. | [optional] 
**is_whois_privacy_enabled** | **object** | Это логическое значение, которое показывает, включено ли скрытие данных администратора домена для whois. Опция недоступна для доменов в зонах .ru и .рф. | [optional] 
**ns** | **object** | Name-серверы для регистрации домена. Если не передавать этот параметр, будут использованы наши стандартные name-серверы. Нужно указать как минимум 2 name-сервера. | [optional] 
**period** | [**DomainPaymentPeriod**](DomainPaymentPeriod.md) |  | [optional] 
**person_id** | **object** | Идентификатор администратора, на которого регистрируется домен. | 

## Example

```python
from timeweb_cloud_api.models.domain_register import DomainRegister

# TODO update the JSON string below
json = "{}"
# create an instance of DomainRegister from a JSON string
domain_register_instance = DomainRegister.from_json(json)
# print the JSON string representation of the object
print DomainRegister.to_json()

# convert the object into a dict
domain_register_dict = domain_register_instance.to_dict()
# create an instance of DomainRegister from a dict
domain_register_form_dict = domain_register.from_dict(domain_register_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


