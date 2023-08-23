# UpdateDomain


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_autoprolong_enabled** | **object** | Это логическое значение, которое показывает, включено ли автопродление домена. | [optional] 
**linked_ip** | **object** | Привязанный к домену IP-адрес. | [optional] 

## Example

```python
from timeweb_cloud_api.models.update_domain import UpdateDomain

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDomain from a JSON string
update_domain_instance = UpdateDomain.from_json(json)
# print the JSON string representation of the object
print UpdateDomain.to_json()

# convert the object into a dict
update_domain_dict = update_domain_instance.to_dict()
# create an instance of UpdateDomain from a dict
update_domain_form_dict = update_domain.from_dict(update_domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


