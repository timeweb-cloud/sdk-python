# ConnectSkillItem

Навык и версия для подключения

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skill_id** | **object** | ID навыка | 
**version** | **object** | Версия из истории навыка. Если не передано — текущая | [optional] 

## Example

```python
from timeweb_cloud_api.models.connect_skill_item import ConnectSkillItem

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectSkillItem from a JSON string
connect_skill_item_instance = ConnectSkillItem.from_json(json)
# print the JSON string representation of the object
print ConnectSkillItem.to_json()

# convert the object into a dict
connect_skill_item_dict = connect_skill_item_instance.to_dict()
# create an instance of ConnectSkillItem from a dict
connect_skill_item_form_dict = connect_skill_item.from_dict(connect_skill_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


