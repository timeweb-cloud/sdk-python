# CreateFloatingIp201Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | [**FloatingIp**](FloatingIp.md) |  | 

## Example

```python
from timeweb_cloud_api.models.create_floating_ip201_response import CreateFloatingIp201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFloatingIp201Response from a JSON string
create_floating_ip201_response_instance = CreateFloatingIp201Response.from_json(json)
# print the JSON string representation of the object
print CreateFloatingIp201Response.to_json()

# convert the object into a dict
create_floating_ip201_response_dict = create_floating_ip201_response_instance.to_dict()
# create an instance of CreateFloatingIp201Response from a dict
create_floating_ip201_response_form_dict = create_floating_ip201_response.from_dict(create_floating_ip201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


