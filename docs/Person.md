# Person


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | Уникальный идентификатор администратора домена. | 
**type** | **object** | Тип администратора: &#x60;person&#x60; — физическое лицо, &#x60;org&#x60; — организация, &#x60;ip&#x60; — индивидуальный предприниматель. | 
**name** | **object** | Имя администратора (ФИО или название организации). | 
**name_eng** | **object** | Имя администратора в латинской транслитерации. | 
**email** | **object** | Адрес электронной почты администратора. | 
**phone** | **object** | Контактный телефон администратора. | 
**postcode** | **object** | Почтовый индекс. | 
**mailing_address** | **object** | Почтовый адрес. | 
**country_code** | **object** | Код страны администратора. | 
**is_resident** | **object** | Это логическое значение, которое показывает, является ли администратор резидентом РФ. | 
**is_blank** | **object** | Это логическое значение, которое показывает, заполнены ли данные администратора не полностью. | 
**is_closed** | **object** | Это логическое значение, которое показывает, закрыт ли администратор. | 
**birthdate** | **object** | Дата рождения. Только для типов &#x60;person&#x60; и &#x60;ip&#x60;. | [optional] 
**passport_date** | **object** | Дата выдачи паспорта. Только для типов &#x60;person&#x60; и &#x60;ip&#x60;. | [optional] 
**passport_number** | **object** | Номер паспорта. Только для типов &#x60;person&#x60; и &#x60;ip&#x60;. | [optional] 
**passport_place** | **object** | Кем выдан паспорт. Только для типов &#x60;person&#x60; и &#x60;ip&#x60;. | [optional] 
**passport_series** | **object** | Серия паспорта. Только для типов &#x60;person&#x60; и &#x60;ip&#x60;. | [optional] 
**inn** | **object** | ИНН. Только для типов &#x60;org&#x60; и &#x60;ip&#x60;. | [optional] 
**kpp** | **object** | КПП организации. Только для типа &#x60;org&#x60;. | [optional] 
**legal_address** | **object** | Юридический адрес организации. Только для типа &#x60;org&#x60;. | [optional] 
**contact_name** | **object** | Контактное лицо организации. Только для типа &#x60;org&#x60;. | [optional] 

## Example

```python
from timeweb_cloud_api.models.person import Person

# TODO update the JSON string below
json = "{}"
# create an instance of Person from a JSON string
person_instance = Person.from_json(json)
# print the JSON string representation of the object
print Person.to_json()

# convert the object into a dict
person_dict = person_instance.to_dict()
# create an instance of Person from a dict
person_form_dict = person.from_dict(person_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


