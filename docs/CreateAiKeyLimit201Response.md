# CreateAiKeyLimit201Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ai_key_entity_limit** | [**AiKeyLimit**](AiKeyLimit.md) |  | 

## Example

```python
from timeweb_cloud_api.models.create_ai_key_limit201_response import CreateAiKeyLimit201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAiKeyLimit201Response from a JSON string
create_ai_key_limit201_response_instance = CreateAiKeyLimit201Response.from_json(json)
# print the JSON string representation of the object
print CreateAiKeyLimit201Response.to_json()

# convert the object into a dict
create_ai_key_limit201_response_dict = create_ai_key_limit201_response_instance.to_dict()
# create an instance of CreateAiKeyLimit201Response from a dict
create_ai_key_limit201_response_form_dict = create_ai_key_limit201_response.from_dict(create_ai_key_limit201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


