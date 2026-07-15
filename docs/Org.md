# Org

Администратор домена — организация

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **object** | Тип администратора. | 
**name** | **object** | Название организации. | 
**is_resident** | **object** | Это логическое значение, которое показывает, является ли администратор резидентом РФ. | 
**contact_name** | **object** | Контактное лицо организации. | 
**inn** | **object** | ИНН организации. | 
**kpp** | **object** | КПП организации. | [optional] 
**legal_address** | **object** | Юридический адрес организации. | 
**postcode** | **object** | Почтовый индекс. | 
**mailing_address** | **object** | Почтовый адрес. | 
**phone** | **object** | Контактный телефон. | 
**email** | **object** | Адрес электронной почты. | 
**country_code** | **object** | Код страны. Только для нерезидентов РФ (&#x60;is_resident: false&#x60;); для резидентов поле передавать не нужно. | [optional] 

## Example

```python
from timeweb_cloud_api.models.org import Org

# TODO update the JSON string below
json = "{}"
# create an instance of Org from a JSON string
org_instance = Org.from_json(json)
# print the JSON string representation of the object
print Org.to_json()

# convert the object into a dict
org_dict = org_instance.to_dict()
# create an instance of Org from a dict
org_form_dict = org.from_dict(org_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


