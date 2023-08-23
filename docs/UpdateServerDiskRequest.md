# UpdateServerDiskRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | **object** | Минимальный размер 5120. Максимальный размер 512000. Шаг 5120. Нельзя передавать значение меньше текущего размера диска. | 

## Example

```python
from timeweb_cloud_api.models.update_server_disk_request import UpdateServerDiskRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateServerDiskRequest from a JSON string
update_server_disk_request_instance = UpdateServerDiskRequest.from_json(json)
# print the JSON string representation of the object
print UpdateServerDiskRequest.to_json()

# convert the object into a dict
update_server_disk_request_dict = update_server_disk_request_instance.to_dict()
# create an instance of UpdateServerDiskRequest from a dict
update_server_disk_request_form_dict = update_server_disk_request.from_dict(update_server_disk_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


