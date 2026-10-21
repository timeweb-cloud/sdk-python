# CreateCrispIntegration

Параметры подключения агента к Crisp

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**website_id** | **object** | Website ID сайта в Crisp (Settings → Website Settings) | 
**token_identifier** | **object** | Identifier API-токена Crisp (Settings → Workspace Settings → Advanced configuration → API Token) | 
**token_key** | **object** | Key API-токена Crisp | 

## Example

```python
from timeweb_cloud_api.models.create_crisp_integration import CreateCrispIntegration

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCrispIntegration from a JSON string
create_crisp_integration_instance = CreateCrispIntegration.from_json(json)
# print the JSON string representation of the object
print CreateCrispIntegration.to_json()

# convert the object into a dict
create_crisp_integration_dict = create_crisp_integration_instance.to_dict()
# create an instance of CreateCrispIntegration from a dict
create_crisp_integration_form_dict = create_crisp_integration.from_dict(create_crisp_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


