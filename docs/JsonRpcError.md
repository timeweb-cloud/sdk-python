# JsonRpcError

Ошибка JSON-RPC

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **object** | Код ошибки: &#x60;-32700&#x60; — ошибка разбора, &#x60;-32600&#x60; — некорректный запрос, &#x60;-32601&#x60; — метод не найден, &#x60;-32602&#x60; — некорректные параметры, &#x60;-32603&#x60; — внутренняя ошибка, &#x60;-32000&#x60; — ошибка транспорта, &#x60;-32001&#x60; — запрос не удалось связать с аккаунтом | 
**message** | **object** | Текст ошибки | 
**data** | **Dict[str, object]** | Дополнительные сведения об ошибке | [optional] 

## Example

```python
from timeweb_cloud_api.models.json_rpc_error import JsonRpcError

# TODO update the JSON string below
json = "{}"
# create an instance of JsonRpcError from a JSON string
json_rpc_error_instance = JsonRpcError.from_json(json)
# print the JSON string representation of the object
print JsonRpcError.to_json()

# convert the object into a dict
json_rpc_error_dict = json_rpc_error_instance.to_dict()
# create an instance of JsonRpcError from a dict
json_rpc_error_form_dict = json_rpc_error.from_dict(json_rpc_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


