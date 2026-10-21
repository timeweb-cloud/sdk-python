# AiGatewayModel

Модель

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID модели — передавайте его в поле &#x60;model&#x60; | [optional] 
**object** | **object** | Тип объекта | [optional] 
**created** | **object** | Время добавления, Unix-время в секундах | [optional] 
**owned_by** | **object** | Владелец модели | [optional] 
**mode** | **object** | Назначение модели: &#x60;chat&#x60;, &#x60;responses&#x60;, &#x60;embedding&#x60;, &#x60;image_generation&#x60;, &#x60;audio_speech&#x60;, &#x60;audio_transcription&#x60; и др. У части моделей не задано | [optional] 
**max_input_tokens** | **object** | Контекстное окно, если известно | [optional] 
**max_output_tokens** | **object** | Максимум выходных токенов, если известно | [optional] 

## Example

```python
from timeweb_cloud_api.models.ai_gateway_model import AiGatewayModel

# TODO update the JSON string below
json = "{}"
# create an instance of AiGatewayModel from a JSON string
ai_gateway_model_instance = AiGatewayModel.from_json(json)
# print the JSON string representation of the object
print AiGatewayModel.to_json()

# convert the object into a dict
ai_gateway_model_dict = ai_gateway_model_instance.to_dict()
# create an instance of AiGatewayModel from a dict
ai_gateway_model_form_dict = ai_gateway_model.from_dict(ai_gateway_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


