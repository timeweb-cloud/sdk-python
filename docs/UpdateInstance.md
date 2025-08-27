# UpdateInstance


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Название инстанса базы данных | [optional] 
**description** | **object** | Описание инстанса базы данных | [optional] 

## Example

```python
from timeweb_cloud_api.models.update_instance import UpdateInstance

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateInstance from a JSON string
update_instance_instance = UpdateInstance.from_json(json)
# print the JSON string representation of the object
print UpdateInstance.to_json()

# convert the object into a dict
update_instance_dict = update_instance_instance.to_dict()
# create an instance of UpdateInstance from a dict
update_instance_form_dict = update_instance.from_dict(update_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


