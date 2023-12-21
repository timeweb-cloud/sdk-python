# CreateFloatingIp


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_ddos_guard** | **object** | Это логическое значение, которое показывает, включена ли защита от DDoS. | 
**availability_zone** | [**AvailabilityZone**](AvailabilityZone.md) |  | 

## Example

```python
from timeweb_cloud_api.models.create_floating_ip import CreateFloatingIp

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFloatingIp from a JSON string
create_floating_ip_instance = CreateFloatingIp.from_json(json)
# print the JSON string representation of the object
print CreateFloatingIp.to_json()

# convert the object into a dict
create_floating_ip_dict = create_floating_ip_instance.to_dict()
# create an instance of CreateFloatingIp from a dict
create_floating_ip_form_dict = create_floating_ip.from_dict(create_floating_ip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


