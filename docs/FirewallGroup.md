# FirewallGroup


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID группы правил. | 
**created_at** | **object** | Дата и время создания. | 
**updated_at** | **object** | Дата и время последнего обновления. | 
**name** | **object** | Имя группы правил. | 
**description** | **object** | Описание группы правил. | 
**policy** | [**Policy**](Policy.md) |  | 

## Example

```python
from timeweb_cloud_api.models.firewall_group import FirewallGroup

# TODO update the JSON string below
json = "{}"
# create an instance of FirewallGroup from a JSON string
firewall_group_instance = FirewallGroup.from_json(json)
# print the JSON string representation of the object
print FirewallGroup.to_json()

# convert the object into a dict
firewall_group_dict = firewall_group_instance.to_dict()
# create an instance of FirewallGroup from a dict
firewall_group_form_dict = firewall_group.from_dict(firewall_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


