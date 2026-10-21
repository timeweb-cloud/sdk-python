# CreateJivoIntegration

Параметры подключения агента к Jivo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_id** | **object** | Provider ID, который выдала техническая поддержка Jivo | 

## Example

```python
from timeweb_cloud_api.models.create_jivo_integration import CreateJivoIntegration

# TODO update the JSON string below
json = "{}"
# create an instance of CreateJivoIntegration from a JSON string
create_jivo_integration_instance = CreateJivoIntegration.from_json(json)
# print the JSON string representation of the object
print CreateJivoIntegration.to_json()

# convert the object into a dict
create_jivo_integration_dict = create_jivo_integration_instance.to_dict()
# create an instance of CreateJivoIntegration from a dict
create_jivo_integration_form_dict = create_jivo_integration.from_dict(create_jivo_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


