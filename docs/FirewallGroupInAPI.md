# FirewallGroupInAPI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Имя группы правил | 
**description** | **object** | Описание группы правил | [optional] 

## Example

```python
from timeweb_cloud_api.models.firewall_group_in_api import FirewallGroupInAPI

# TODO update the JSON string below
json = "{}"
# create an instance of FirewallGroupInAPI from a JSON string
firewall_group_in_api_instance = FirewallGroupInAPI.from_json(json)
# print the JSON string representation of the object
print FirewallGroupInAPI.to_json()

# convert the object into a dict
firewall_group_in_api_dict = firewall_group_in_api_instance.to_dict()
# create an instance of FirewallGroupInAPI from a dict
firewall_group_in_api_form_dict = firewall_group_in_api.from_dict(firewall_group_in_api_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


