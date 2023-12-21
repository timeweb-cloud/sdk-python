# BindFloatingIp


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_type** | **object** | Тип ресурса. | 
**resource_id** | **object** | Id ресурса. | 

## Example

```python
from timeweb_cloud_api.models.bind_floating_ip import BindFloatingIp

# TODO update the JSON string below
json = "{}"
# create an instance of BindFloatingIp from a JSON string
bind_floating_ip_instance = BindFloatingIp.from_json(json)
# print the JSON string representation of the object
print BindFloatingIp.to_json()

# convert the object into a dict
bind_floating_ip_dict = bind_floating_ip_instance.to_dict()
# create an instance of BindFloatingIp from a dict
bind_floating_ip_form_dict = bind_floating_ip.from_dict(bind_floating_ip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


