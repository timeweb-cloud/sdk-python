# AiGatewayTranscription

Распознанный текст

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **object** | Текст | [optional] 
**usage** | **Dict[str, object]** | Расход токенов, если модель его возвращает | [optional] 

## Example

```python
from timeweb_cloud_api.models.ai_gateway_transcription import AiGatewayTranscription

# TODO update the JSON string below
json = "{}"
# create an instance of AiGatewayTranscription from a JSON string
ai_gateway_transcription_instance = AiGatewayTranscription.from_json(json)
# print the JSON string representation of the object
print AiGatewayTranscription.to_json()

# convert the object into a dict
ai_gateway_transcription_dict = ai_gateway_transcription_instance.to_dict()
# create an instance of AiGatewayTranscription from a dict
ai_gateway_transcription_form_dict = ai_gateway_transcription.from_dict(ai_gateway_transcription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


