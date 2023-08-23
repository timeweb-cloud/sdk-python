# AddedSubdomain

Добавленный поддомен.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subdomain** | **object** | Поддомен. | 
**status** | **object** | Результат добавления поддомена. | 

## Example

```python
from timeweb_cloud_api.models.added_subdomain import AddedSubdomain

# TODO update the JSON string below
json = "{}"
# create an instance of AddedSubdomain from a JSON string
added_subdomain_instance = AddedSubdomain.from_json(json)
# print the JSON string representation of the object
print AddedSubdomain.to_json()

# convert the object into a dict
added_subdomain_dict = added_subdomain_instance.to_dict()
# create an instance of AddedSubdomain from a dict
added_subdomain_form_dict = added_subdomain.from_dict(added_subdomain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


