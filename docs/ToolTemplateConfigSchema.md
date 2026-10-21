# ToolTemplateConfigSchema

Поля, которые нужно заполнить при установке. `null` — настройка не требуется

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | **object** | Поля настройки | [optional] 

## Example

```python
from timeweb_cloud_api.models.tool_template_config_schema import ToolTemplateConfigSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ToolTemplateConfigSchema from a JSON string
tool_template_config_schema_instance = ToolTemplateConfigSchema.from_json(json)
# print the JSON string representation of the object
print ToolTemplateConfigSchema.to_json()

# convert the object into a dict
tool_template_config_schema_dict = tool_template_config_schema_instance.to_dict()
# create an instance of ToolTemplateConfigSchema from a dict
tool_template_config_schema_form_dict = tool_template_config_schema.from_dict(tool_template_config_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


