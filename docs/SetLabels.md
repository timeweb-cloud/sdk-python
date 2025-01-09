# SetLabels

Лейбл для группы нод

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **object** | Ключ | 
**value** | **object** | Значение | 

## Example

```python
from timeweb_cloud_api.models.set_labels import SetLabels

# TODO update the JSON string below
json = "{}"
# create an instance of SetLabels from a JSON string
set_labels_instance = SetLabels.from_json(json)
# print the JSON string representation of the object
print SetLabels.to_json()

# convert the object into a dict
set_labels_dict = set_labels_instance.to_dict()
# create an instance of SetLabels from a dict
set_labels_form_dict = set_labels.from_dict(set_labels_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


