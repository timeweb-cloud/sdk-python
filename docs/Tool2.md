# Tool2

Инструмент MCP

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Имя инструмента | 
**title** | **object** | Короткое название инструмента | [optional] 
**description** | **object** | Что делает инструмент. Описания изменяющих инструментов, как правило, начинаются с &#x60;[WRITE]&#x60;, у платных добавляется &#x60;[BILLABLE]&#x60; | [optional] 
**input_schema** | **Dict[str, object]** | JSON Schema аргументов инструмента | 
**annotations** | [**Tool2Annotations**](Tool2Annotations.md) |  | [optional] 

## Example

```python
from timeweb_cloud_api.models.tool2 import Tool2

# TODO update the JSON string below
json = "{}"
# create an instance of Tool2 from a JSON string
tool2_instance = Tool2.from_json(json)
# print the JSON string representation of the object
print Tool2.to_json()

# convert the object into a dict
tool2_dict = tool2_instance.to_dict()
# create an instance of Tool2 from a dict
tool2_form_dict = tool2.from_dict(tool2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


