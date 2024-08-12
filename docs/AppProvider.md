# AppProvider


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | Уникальный идентификатор провайдера. | 
**type** | [**Providers**](Providers.md) |  | 

## Example

```python
from timeweb_cloud_api.models.app_provider import AppProvider

# TODO update the JSON string below
json = "{}"
# create an instance of AppProvider from a JSON string
app_provider_instance = AppProvider.from_json(json)
# print the JSON string representation of the object
print AppProvider.to_json()

# convert the object into a dict
app_provider_dict = app_provider_instance.to_dict()
# create an instance of AppProvider from a dict
app_provider_form_dict = app_provider.from_dict(app_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


