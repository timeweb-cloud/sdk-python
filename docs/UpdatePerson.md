# UpdatePerson


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **object** | Почтовый адрес администратора. | 
**email** | **object** | Адрес электронной почты администратора. | 
**phone** | **object** | Контактный телефон администратора. | 
**postcode** | **object** | Почтовый индекс. | 

## Example

```python
from timeweb_cloud_api.models.update_person import UpdatePerson

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePerson from a JSON string
update_person_instance = UpdatePerson.from_json(json)
# print the JSON string representation of the object
print UpdatePerson.to_json()

# convert the object into a dict
update_person_dict = update_person_instance.to_dict()
# create an instance of UpdatePerson from a dict
update_person_form_dict = update_person.from_dict(update_person_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


