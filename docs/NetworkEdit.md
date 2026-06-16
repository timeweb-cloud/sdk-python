# NetworkEdit


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_dhcp_enabled** | **object** | Включить или выключить DHCP | 

## Example

```python
from timeweb_cloud_api.models.network_edit import NetworkEdit

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkEdit from a JSON string
network_edit_instance = NetworkEdit.from_json(json)
# print the JSON string representation of the object
print NetworkEdit.to_json()

# convert the object into a dict
network_edit_dict = network_edit_instance.to_dict()
# create an instance of NetworkEdit from a dict
network_edit_form_dict = network_edit.from_dict(network_edit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


