# CreateNetworkDrive201Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_drive** | [**NetworkDrive**](NetworkDrive.md) |  | 

## Example

```python
from timeweb_cloud_api.models.create_network_drive201_response import CreateNetworkDrive201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNetworkDrive201Response from a JSON string
create_network_drive201_response_instance = CreateNetworkDrive201Response.from_json(json)
# print the JSON string representation of the object
print CreateNetworkDrive201Response.to_json()

# convert the object into a dict
create_network_drive201_response_dict = create_network_drive201_response_instance.to_dict()
# create an instance of CreateNetworkDrive201Response from a dict
create_network_drive201_response_form_dict = create_network_drive201_response.from_dict(create_network_drive201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


