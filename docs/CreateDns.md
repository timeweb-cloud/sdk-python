# CreateDns


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**priority** | **object** | Приоритет DNS-записи. | [optional] 
**subdomain** | **object** | Полное имя поддомена. | [optional] 
**type** | **object** | Тип DNS-записи. | 
**value** | **object** | Значение DNS-записи. | 

## Example

```python
from timeweb_cloud_api.models.create_dns import CreateDns

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDns from a JSON string
create_dns_instance = CreateDns.from_json(json)
# print the JSON string representation of the object
print CreateDns.to_json()

# convert the object into a dict
create_dns_dict = create_dns_instance.to_dict()
# create an instance of CreateDns from a dict
create_dns_form_dict = create_dns.from_dict(create_dns_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


