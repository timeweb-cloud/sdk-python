# CreateAiKey201Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ai_key** | [**AiKey**](AiKey.md) |  | 
**key** | **object** | Значение ключа для запросов к AI Gateway API. Показывается только в этом ответе — сохраните его | 

## Example

```python
from timeweb_cloud_api.models.create_ai_key201_response import CreateAiKey201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAiKey201Response from a JSON string
create_ai_key201_response_instance = CreateAiKey201Response.from_json(json)
# print the JSON string representation of the object
print CreateAiKey201Response.to_json()

# convert the object into a dict
create_ai_key201_response_dict = create_ai_key201_response_instance.to_dict()
# create an instance of CreateAiKey201Response from a dict
create_ai_key201_response_form_dict = create_ai_key201_response.from_dict(create_ai_key201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


