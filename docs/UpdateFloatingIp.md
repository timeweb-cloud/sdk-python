# UpdateFloatingIp


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **object** | Комментарий | [optional] 
**ptr** | **object** | Запись имени узла. | [optional] 

## Example

```python
from timeweb_cloud_api.models.update_floating_ip import UpdateFloatingIp

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFloatingIp from a JSON string
update_floating_ip_instance = UpdateFloatingIp.from_json(json)
# print the JSON string representation of the object
print UpdateFloatingIp.to_json()

# convert the object into a dict
update_floating_ip_dict = update_floating_ip_instance.to_dict()
# create an instance of UpdateFloatingIp from a dict
update_floating_ip_form_dict = update_floating_ip.from_dict(update_floating_ip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


