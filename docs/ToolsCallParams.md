# ToolsCallParams

`params` метода `tools/call`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Имя инструмента | 
**arguments** | **Dict[str, object]** | Аргументы по &#x60;inputSchema&#x60; инструмента. Во втором вызове изменяющего инструмента добавьте &#x60;confirm_token&#x60; | [optional] 

## Example

```python
from timeweb_cloud_api.models.tools_call_params import ToolsCallParams

# TODO update the JSON string below
json = "{}"
# create an instance of ToolsCallParams from a JSON string
tools_call_params_instance = ToolsCallParams.from_json(json)
# print the JSON string representation of the object
print ToolsCallParams.to_json()

# convert the object into a dict
tools_call_params_dict = tools_call_params_instance.to_dict()
# create an instance of ToolsCallParams from a dict
tools_call_params_form_dict = tools_call_params.from_dict(tools_call_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


