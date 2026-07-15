# Person2

Администратор домена — физическое лицо

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **object** | Тип администратора. | 
**name** | **object** | ФИО администратора. | 
**is_resident** | **object** | Это логическое значение, которое показывает, является ли администратор резидентом РФ. | 
**birthdate** | **object** | Дата рождения. | 
**passport_date** | **object** | Дата выдачи паспорта. | 
**passport_number** | **object** | Номер паспорта. | 
**passport_place** | **object** | Кем выдан паспорт. | 
**passport_series** | **object** | Серия паспорта. | 
**postcode** | **object** | Почтовый индекс. | 
**mailing_address** | **object** | Почтовый адрес. | 
**phone** | **object** | Контактный телефон. | 
**email** | **object** | Адрес электронной почты. | 
**country_code** | **object** | Код страны. Только для нерезидентов РФ (&#x60;is_resident: false&#x60;); для резидентов поле передавать не нужно. | [optional] 

## Example

```python
from timeweb_cloud_api.models.person2 import Person2

# TODO update the JSON string below
json = "{}"
# create an instance of Person2 from a JSON string
person2_instance = Person2.from_json(json)
# print the JSON string representation of the object
print Person2.to_json()

# convert the object into a dict
person2_dict = person2_instance.to_dict()
# create an instance of Person2 from a dict
person2_form_dict = person2.from_dict(person2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


