# Ip

Администратор домена — индивидуальный предприниматель

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **object** | Тип администратора. | 
**name** | **object** | ФИО индивидуального предпринимателя. | 
**is_resident** | **object** | Это логическое значение, которое показывает, является ли администратор резидентом РФ. | 
**birthdate** | **object** | Дата рождения. | 
**passport_date** | **object** | Дата выдачи паспорта. | 
**passport_number** | **object** | Номер паспорта. | 
**passport_place** | **object** | Кем выдан паспорт. | 
**passport_series** | **object** | Серия паспорта. | 
**inn** | **object** | ИНН индивидуального предпринимателя. | 
**postcode** | **object** | Почтовый индекс. | 
**mailing_address** | **object** | Почтовый адрес. | 
**phone** | **object** | Контактный телефон. | 
**email** | **object** | Адрес электронной почты. | 
**country_code** | **object** | Код страны. Только для нерезидентов РФ (&#x60;is_resident: false&#x60;); для резидентов поле передавать не нужно. | [optional] 

## Example

```python
from timeweb_cloud_api.models.ip import Ip

# TODO update the JSON string below
json = "{}"
# create an instance of Ip from a JSON string
ip_instance = Ip.from_json(json)
# print the JSON string representation of the object
print Ip.to_json()

# convert the object into a dict
ip_dict = ip_instance.to_dict()
# create an instance of Ip from a dict
ip_form_dict = ip.from_dict(ip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


