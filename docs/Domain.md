# Domain

Домен

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_buy_periods** | **object** | Допустимые периоды продления домена. | 
**days_left** | **object** | Количество дней, оставшихся до конца срока регистрации домена. | 
**domain_status** | **object** | Статус домена. | 
**expiration** | **object** | Дата окончания срока регистрации домена, для доменов без срока окончания регистрации будет приходить 0000-00-00. | 
**fqdn** | **object** | Полное имя домена. | 
**id** | **object** | Уникальный идентификатор домена. | 
**is_autoprolong_enabled** | **object** | Это логическое значение, которое показывает, включено ли автопродление домена. | 
**is_premium** | **object** | Это логическое значение, которое показывает, является ли домен премиальным. | 
**is_prolong_allowed** | **object** | Это логическое значение, которое показывает, можно ли сейчас продлить домен. | 
**is_technical** | **object** | Это логическое значение, которое показывает, является ли домен техническим. | 
**is_whois_privacy_enabled** | **object** | Это логическое значение, которое показывает, включено ли скрытие данных администратора домена для whois. Если приходит null, значит для данной зоны эта услуга не доступна. | 
**linked_ip** | **object** | Привязанный к домену IP-адрес. | 
**paid_till** | **object** | До какого числа оплачен домен. | 
**person_id** | **object** | Идентификатор администратора, на которого зарегистрирован домен. | 
**premium_prolong_cost** | **object** | Стоимость премиального домена. | 
**provider** | **object** | Идентификатор регистратора домена. | 
**request_status** | **object** | Статус заявки на продление/регистрацию/трансфер домена. | 
**subdomains** | **object** | Список поддоменов. | 
**tld_id** | **object** | Идентификатор доменной зоны. | 

## Example

```python
from openapi_client.models.domain import Domain

# TODO update the JSON string below
json = "{}"
# create an instance of Domain from a JSON string
domain_instance = Domain.from_json(json)
# print the JSON string representation of the object
print Domain.to_json()

# convert the object into a dict
domain_dict = domain_instance.to_dict()
# create an instance of Domain from a dict
domain_form_dict = domain.from_dict(domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


