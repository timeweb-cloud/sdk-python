# FirewallGroupOutAPI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | Идентификатор группы правил | 
**created_at** | **object** | Дата и время создания | 
**updated_at** | **object** | Дата и время последнего обновления | 
**name** | **object** | Имя группы правил | 
**description** | **object** | Описание группы правил | 
**policy** | [**Policy**](Policy.md) |  | 

## Example

```python
from timeweb_cloud_api.models.firewall_group_out_api import FirewallGroupOutAPI

# TODO update the JSON string below
json = "{}"
# create an instance of FirewallGroupOutAPI from a JSON string
firewall_group_out_api_instance = FirewallGroupOutAPI.from_json(json)
# print the JSON string representation of the object
print FirewallGroupOutAPI.to_json()

# convert the object into a dict
firewall_group_out_api_dict = firewall_group_out_api_instance.to_dict()
# create an instance of FirewallGroupOutAPI from a dict
firewall_group_out_api_form_dict = firewall_group_out_api.from_dict(firewall_group_out_api_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


