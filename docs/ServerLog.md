# ServerLog

Лог сервера

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | Уникальный идентификатор диска. | 
**logged_at** | **object** | Дата лога. | 
**event** | **object** | Событие сервера. | 

## Example

```python
from timeweb_cloud_api.models.server_log import ServerLog

# TODO update the JSON string below
json = "{}"
# create an instance of ServerLog from a JSON string
server_log_instance = ServerLog.from_json(json)
# print the JSON string representation of the object
print ServerLog.to_json()

# convert the object into a dict
server_log_dict = server_log_instance.to_dict()
# create an instance of ServerLog from a dict
server_log_form_dict = server_log.from_dict(server_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


