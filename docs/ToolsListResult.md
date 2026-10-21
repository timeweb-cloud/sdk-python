# ToolsListResult

Результат `tools/list`. Все инструменты приходят одной страницей

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tools** | **object** | Инструменты сервера | 

## Example

```python
from timeweb_cloud_api.models.tools_list_result import ToolsListResult

# TODO update the JSON string below
json = "{}"
# create an instance of ToolsListResult from a JSON string
tools_list_result_instance = ToolsListResult.from_json(json)
# print the JSON string representation of the object
print ToolsListResult.to_json()

# convert the object into a dict
tools_list_result_dict = tools_list_result_instance.to_dict()
# create an instance of ToolsListResult from a dict
tools_list_result_form_dict = tools_list_result.from_dict(tools_list_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


