# AddIps


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **object** | IP-адрес. | 
**status** | **object** | Результат добавления IP-адреса. | 

## Example

```python
from openapi_client.models.add_ips import AddIps

# TODO update the JSON string below
json = "{}"
# create an instance of AddIps from a JSON string
add_ips_instance = AddIps.from_json(json)
# print the JSON string representation of the object
print AddIps.to_json()

# convert the object into a dict
add_ips_dict = add_ips_instance.to_dict()
# create an instance of AddIps from a dict
add_ips_form_dict = add_ips.from_dict(add_ips_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


