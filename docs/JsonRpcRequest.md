# JsonRpcRequest

Запрос JSON-RPC 2.0. Форма `params` зависит от `method`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jsonrpc** | **object** | Версия протокола JSON-RPC, всегда &#x60;2.0&#x60; | 
**id** | **object** | ID запроса, выбранный клиентом; ответ приходит с тем же ID | 
**method** | **object** | Метод MCP | 
**params** | [**InitializeParams**](InitializeParams.md) |  | [optional] 

## Example

```python
from timeweb_cloud_api.models.json_rpc_request import JsonRpcRequest

# TODO update the JSON string below
json = "{}"
# create an instance of JsonRpcRequest from a JSON string
json_rpc_request_instance = JsonRpcRequest.from_json(json)
# print the JSON string representation of the object
print JsonRpcRequest.to_json()

# convert the object into a dict
json_rpc_request_dict = json_rpc_request_instance.to_dict()
# create an instance of JsonRpcRequest from a dict
json_rpc_request_form_dict = json_rpc_request.from_dict(json_rpc_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


