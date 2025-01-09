# Provider


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_id** | **object** | ID провайдера. | 
**login** | **object** | Логин пользователя. | 
**provider_type** | [**Providers**](Providers.md) |  | 

## Example

```python
from timeweb_cloud_api.models.provider import Provider

# TODO update the JSON string below
json = "{}"
# create an instance of Provider from a JSON string
provider_instance = Provider.from_json(json)
# print the JSON string representation of the object
print Provider.to_json()

# convert the object into a dict
provider_dict = provider_instance.to_dict()
# create an instance of Provider from a dict
provider_form_dict = provider.from_dict(provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


