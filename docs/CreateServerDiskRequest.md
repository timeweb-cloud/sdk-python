# CreateServerDiskRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | **object** | Минимальный размер 5120. Максимальный размер 512000. Шаг 5120 | 

## Example

```python
from timeweb_cloud_api.models.create_server_disk_request import CreateServerDiskRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateServerDiskRequest from a JSON string
create_server_disk_request_instance = CreateServerDiskRequest.from_json(json)
# print the JSON string representation of the object
print CreateServerDiskRequest.to_json()

# convert the object into a dict
create_server_disk_request_dict = create_server_disk_request_instance.to_dict()
# create an instance of CreateServerDiskRequest from a dict
create_server_disk_request_form_dict = create_server_disk_request.from_dict(create_server_disk_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


