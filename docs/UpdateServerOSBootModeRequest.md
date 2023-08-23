# UpdateServerOSBootModeRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**boot_mode** | **object** | Тип загрузки операционной системы. \\  Параметры: &#x60;default&#x60; – стандартный режим, &#x60;single&#x60; – однопользовательский режим, &#x60;recovery_disk&#x60; – загрузка с диска восстановления. | 

## Example

```python
from openapi_client.models.update_server_os_boot_mode_request import UpdateServerOSBootModeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateServerOSBootModeRequest from a JSON string
update_server_os_boot_mode_request_instance = UpdateServerOSBootModeRequest.from_json(json)
# print the JSON string representation of the object
print UpdateServerOSBootModeRequest.to_json()

# convert the object into a dict
update_server_os_boot_mode_request_dict = update_server_os_boot_mode_request_instance.to_dict()
# create an instance of UpdateServerOSBootModeRequest from a dict
update_server_os_boot_mode_request_form_dict = update_server_os_boot_mode_request.from_dict(update_server_os_boot_mode_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


