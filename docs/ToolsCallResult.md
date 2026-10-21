# ToolsCallResult

Результат `tools/call`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **object** | Блоки результата | 
**is_error** | **object** | &#x60;true&#x60;, если инструмент завершился ошибкой; в тексте — JSON с полем &#x60;error&#x60; | [optional] 

## Example

```python
from timeweb_cloud_api.models.tools_call_result import ToolsCallResult

# TODO update the JSON string below
json = "{}"
# create an instance of ToolsCallResult from a JSON string
tools_call_result_instance = ToolsCallResult.from_json(json)
# print the JSON string representation of the object
print ToolsCallResult.to_json()

# convert the object into a dict
tools_call_result_dict = tools_call_result_instance.to_dict()
# create an instance of ToolsCallResult from a dict
tools_call_result_form_dict = tools_call_result.from_dict(tools_call_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


