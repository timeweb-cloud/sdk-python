# DomainRequest

Заявка на продление/регистрацию/трансфер домена.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **object** | Идентификатор пользователя | 
**auth_code** | **object** | Код авторизации для переноса домена. | 
**var_date** | **object** | Дата создания заявки. | 
**domain_bundle_id** | **object** | Идентификационный номер бандла, в который входит данная заявка (null - если заявка не входит ни в один бандл). | 
**error_code_transfer** | **object** | Код ошибки трансфера домена. | 
**fqdn** | **object** | Полное имя домена. | 
**group_id** | **object** | Идентификатор группы доменных зон. | 
**id** | **object** | Идентификатор заявки. | 
**is_antispam_enabled** | **object** | Это логическое значение, которое показывает включена ли услуга \&quot;Антиспам\&quot; для домена | 
**is_autoprolong_enabled** | **object** | Это логическое значение, которое показывает, включено ли автопродление домена. | 
**is_whois_privacy_enabled** | **object** | Это логическое значение, которое показывает, включено ли скрытие данных администратора домена для whois. Опция недоступна для доменов в зонах .ru и .рф. | 
**message** | **object** | Информационное сообщение о заявке. | 
**money_source** | **object** | Источник (способ) оплаты заявки. | 
**period** | [**DomainPaymentPeriod**](DomainPaymentPeriod.md) |  | 
**person_id** | **object** | Идентификационный номер персоны для заявки на регистрацию. | 
**prime** | [**DomainPrimeType**](DomainPrimeType.md) |  | 
**soon_expire** | **object** | Количество дней до конца регистрации домена, за которые мы уведомим о необходимости продления. | 
**sort_order** | **object** | Это значение используется для сортировки доменных зон в панели управления. | 
**type** | **object** | Тип заявки. | 

## Example

```python
from openapi_client.models.domain_request import DomainRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DomainRequest from a JSON string
domain_request_instance = DomainRequest.from_json(json)
# print the JSON string representation of the object
print DomainRequest.to_json()

# convert the object into a dict
domain_request_dict = domain_request_instance.to_dict()
# create an instance of DomainRequest from a dict
domain_request_form_dict = domain_request.from_dict(domain_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


