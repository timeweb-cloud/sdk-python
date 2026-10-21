# JsonRpcResultResponse

Успешный ответ JSON-RPC 2.0. Приходит в поле `data` события `message` потока `text/event-stream`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jsonrpc** | **object** | Версия протокола JSON-RPC, всегда &#x60;2.0&#x60; | 
**id** | **object** | ID запроса, выбранный клиентом; ответ приходит с тем же ID | 
**result** | [**InitializeResult**](InitializeResult.md) |  | 

## Example

```python
from timeweb_cloud_api.models.json_rpc_result_response import JsonRpcResultResponse

# TODO update the JSON string below
json = "{}"
# create an instance of JsonRpcResultResponse from a JSON string
json_rpc_result_response_instance = JsonRpcResultResponse.from_json(json)
# print the JSON string representation of the object
print JsonRpcResultResponse.to_json()

# convert the object into a dict
json_rpc_result_response_dict = json_rpc_result_response_instance.to_dict()
# create an instance of JsonRpcResultResponse from a dict
json_rpc_result_response_form_dict = json_rpc_result_response.from_dict(json_rpc_result_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


