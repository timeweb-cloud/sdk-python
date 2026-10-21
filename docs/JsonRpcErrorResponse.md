# JsonRpcErrorResponse

Ответ JSON-RPC 2.0 с ошибкой

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jsonrpc** | **object** | Версия протокола JSON-RPC, всегда &#x60;2.0&#x60; | 
**id** | **object** | ID запроса; &#x60;null&#x60;, если запрос не удалось прочитать | 
**error** | [**JsonRpcError**](JsonRpcError.md) |  | 

## Example

```python
from timeweb_cloud_api.models.json_rpc_error_response import JsonRpcErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of JsonRpcErrorResponse from a JSON string
json_rpc_error_response_instance = JsonRpcErrorResponse.from_json(json)
# print the JSON string representation of the object
print JsonRpcErrorResponse.to_json()

# convert the object into a dict
json_rpc_error_response_dict = json_rpc_error_response_instance.to_dict()
# create an instance of JsonRpcErrorResponse from a dict
json_rpc_error_response_form_dict = json_rpc_error_response.from_dict(json_rpc_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


