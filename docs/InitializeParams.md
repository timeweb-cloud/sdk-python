# InitializeParams

`params` метода `initialize`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protocol_version** | **object** | Версия протокола MCP, которую поддерживает клиент | 
**capabilities** | **Dict[str, object]** | Возможности клиента | 
**client_info** | [**InitializeParamsClientInfo**](InitializeParamsClientInfo.md) |  | 

## Example

```python
from timeweb_cloud_api.models.initialize_params import InitializeParams

# TODO update the JSON string below
json = "{}"
# create an instance of InitializeParams from a JSON string
initialize_params_instance = InitializeParams.from_json(json)
# print the JSON string representation of the object
print InitializeParams.to_json()

# convert the object into a dict
initialize_params_dict = initialize_params_instance.to_dict()
# create an instance of InitializeParams from a dict
initialize_params_form_dict = initialize_params.from_dict(initialize_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


