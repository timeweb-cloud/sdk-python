# AiGatewaySpeechRequest

Запрос синтеза речи

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **object** | ID модели синтеза речи (&#x60;mode: audio_speech&#x60; в &#x60;GET /v1/models&#x60;) | 
**input** | **object** | Текст для озвучивания | 
**voice** | **object** | Голос | 
**instructions** | **object** | Инструкции к манере речи — для моделей, которые их поддерживают | [optional] 
**response_format** | **object** | Формат аудио, например &#x60;mp3&#x60;, &#x60;wav&#x60;, &#x60;opus&#x60;. По умолчанию — &#x60;mp3&#x60; | [optional] 
**speed** | **object** | Скорость речи | [optional] 

## Example

```python
from timeweb_cloud_api.models.ai_gateway_speech_request import AiGatewaySpeechRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiGatewaySpeechRequest from a JSON string
ai_gateway_speech_request_instance = AiGatewaySpeechRequest.from_json(json)
# print the JSON string representation of the object
print AiGatewaySpeechRequest.to_json()

# convert the object into a dict
ai_gateway_speech_request_dict = ai_gateway_speech_request_instance.to_dict()
# create an instance of AiGatewaySpeechRequest from a dict
ai_gateway_speech_request_form_dict = ai_gateway_speech_request.from_dict(ai_gateway_speech_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


