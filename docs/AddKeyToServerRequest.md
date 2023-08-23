# AddKeyToServerRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ssh_key_ids** | **object** | Массив уникальных идентификаторов SSH-ключей | 

## Example

```python
from timeweb_cloud_api.models.add_key_to_server_request import AddKeyToServerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddKeyToServerRequest from a JSON string
add_key_to_server_request_instance = AddKeyToServerRequest.from_json(json)
# print the JSON string representation of the object
print AddKeyToServerRequest.to_json()

# convert the object into a dict
add_key_to_server_request_dict = add_key_to_server_request_instance.to_dict()
# create an instance of AddKeyToServerRequest from a dict
add_key_to_server_request_form_dict = add_key_to_server_request.from_dict(add_key_to_server_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


