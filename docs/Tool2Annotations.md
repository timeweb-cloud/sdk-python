# Tool2Annotations

Аннотации инструмента

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**read_only_hint** | **object** | &#x60;true&#x60; у инструментов, которые только читают данные. Инструменты без этой аннотации могут что-то изменить и требуют подтверждения | [optional] 

## Example

```python
from timeweb_cloud_api.models.tool2_annotations import Tool2Annotations

# TODO update the JSON string below
json = "{}"
# create an instance of Tool2Annotations from a JSON string
tool2_annotations_instance = Tool2Annotations.from_json(json)
# print the JSON string representation of the object
print Tool2Annotations.to_json()

# convert the object into a dict
tool2_annotations_dict = tool2_annotations_instance.to_dict()
# create an instance of Tool2Annotations from a dict
tool2_annotations_form_dict = tool2_annotations.from_dict(tool2_annotations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


