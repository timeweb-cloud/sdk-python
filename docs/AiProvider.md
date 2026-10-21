# AiProvider

Провайдер AI моделей

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID провайдера | 
**name** | **object** | Имя провайдера | 
**type** | **object** | &#x60;external&#x60; — внешний провайдер, &#x60;internal&#x60; — модели, размещённые в Timeweb Cloud | 

## Example

```python
from timeweb_cloud_api.models.ai_provider import AiProvider

# TODO update the JSON string below
json = "{}"
# create an instance of AiProvider from a JSON string
ai_provider_instance = AiProvider.from_json(json)
# print the JSON string representation of the object
print AiProvider.to_json()

# convert the object into a dict
ai_provider_dict = ai_provider_instance.to_dict()
# create an instance of AiProvider from a dict
ai_provider_form_dict = ai_provider.from_dict(ai_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


