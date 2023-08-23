# DomainProlong

Заявка на продление домена

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **object** | Тип создаваемой заявки. | 
**fqdn** | **object** | Полное имя домена. | 
**is_antispam_enabled** | **object** | Это логическое значение, которое показывает включена ли услуга \&quot;Антиспам\&quot; для домена | [optional] 
**is_autoprolong_enabled** | **object** | Это логическое значение, которое показывает, включено ли автопродление домена. | [optional] 
**is_whois_privacy_enabled** | **object** | Это логическое значение, которое показывает, включено ли скрытие данных администратора домена для whois. Опция недоступна для доменов в зонах .ru и .рф. | [optional] 
**period** | [**DomainPaymentPeriod**](DomainPaymentPeriod.md) |  | [optional] 
**person_id** | **object** | Идентификатор администратора, на которого зарегистрирован домен. | [optional] 
**prime** | [**DomainPrimeType**](DomainPrimeType.md) |  | [optional] 

## Example

```python
from timeweb_cloud_api.models.domain_prolong import DomainProlong

# TODO update the JSON string below
json = "{}"
# create an instance of DomainProlong from a JSON string
domain_prolong_instance = DomainProlong.from_json(json)
# print the JSON string representation of the object
print DomainProlong.to_json()

# convert the object into a dict
domain_prolong_dict = domain_prolong_instance.to_dict()
# create an instance of DomainProlong from a dict
domain_prolong_form_dict = domain_prolong.from_dict(domain_prolong_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


