# JsonRpcNotification

Уведомление JSON-RPC 2.0: без `id`, ответа на него нет. Принимается с HTTP 202

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jsonrpc** | **object** | Версия протокола JSON-RPC, всегда &#x60;2.0&#x60; | 
**method** | **object** | Метод уведомления | 
**params** | **Dict[str, object]** | Параметры уведомления | [optional] 

## Example

```python
from timeweb_cloud_api.models.json_rpc_notification import JsonRpcNotification

# TODO update the JSON string below
json = "{}"
# create an instance of JsonRpcNotification from a JSON string
json_rpc_notification_instance = JsonRpcNotification.from_json(json)
# print the JSON string representation of the object
print JsonRpcNotification.to_json()

# convert the object into a dict
json_rpc_notification_dict = json_rpc_notification_instance.to_dict()
# create an instance of JsonRpcNotification from a dict
json_rpc_notification_form_dict = json_rpc_notification.from_dict(json_rpc_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


