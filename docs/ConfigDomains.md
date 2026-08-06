# ConfigDomains

Домены, с которых раздается контент ресурса

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aliases** | **object** | Список доменов ресурса. Первым в списке всегда идет технический домен &#x60;cdn_domain&#x60;, вторым может быть ваш собственный домен. Чтобы собственный домен заработал, направьте на &#x60;cdn_domain&#x60; CNAME-запись. &#x60;null&#x60; — оставить только технический домен. | [optional] 

## Example

```python
from timeweb_cloud_api.models.config_domains import ConfigDomains

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigDomains from a JSON string
config_domains_instance = ConfigDomains.from_json(json)
# print the JSON string representation of the object
print ConfigDomains.to_json()

# convert the object into a dict
config_domains_dict = config_domains_instance.to_dict()
# create an instance of ConfigDomains from a dict
config_domains_form_dict = config_domains.from_dict(config_domains_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


