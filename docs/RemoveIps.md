# RemoveIps


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **object** | IP-адрес. | 
**status** | **object** | Результат удаления IP-адреса. | 

## Example

```python
from timeweb_cloud_api.models.remove_ips import RemoveIps

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveIps from a JSON string
remove_ips_instance = RemoveIps.from_json(json)
# print the JSON string representation of the object
print RemoveIps.to_json()

# convert the object into a dict
remove_ips_dict = remove_ips_instance.to_dict()
# create an instance of RemoveIps from a dict
remove_ips_form_dict = remove_ips.from_dict(remove_ips_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


