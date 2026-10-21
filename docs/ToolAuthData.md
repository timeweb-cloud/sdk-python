# ToolAuthData

Авторизация на MCP-сервере

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **object** | Способ авторизации | 
**data** | [**ToolAuthDataParams**](ToolAuthDataParams.md) |  | [optional] 

## Example

```python
from timeweb_cloud_api.models.tool_auth_data import ToolAuthData

# TODO update the JSON string below
json = "{}"
# create an instance of ToolAuthData from a JSON string
tool_auth_data_instance = ToolAuthData.from_json(json)
# print the JSON string representation of the object
print ToolAuthData.to_json()

# convert the object into a dict
tool_auth_data_dict = tool_auth_data_instance.to_dict()
# create an instance of ToolAuthData from a dict
tool_auth_data_form_dict = tool_auth_data.from_dict(tool_auth_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


