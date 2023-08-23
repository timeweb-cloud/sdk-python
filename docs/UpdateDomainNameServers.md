# UpdateDomainNameServers


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name_servers** | **object** | Список новых name-серверов для домена | 

## Example

```python
from openapi_client.models.update_domain_name_servers import UpdateDomainNameServers

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDomainNameServers from a JSON string
update_domain_name_servers_instance = UpdateDomainNameServers.from_json(json)
# print the JSON string representation of the object
print UpdateDomainNameServers.to_json()

# convert the object into a dict
update_domain_name_servers_dict = update_domain_name_servers_instance.to_dict()
# create an instance of UpdateDomainNameServers from a dict
update_domain_name_servers_form_dict = update_domain_name_servers.from_dict(update_domain_name_servers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


