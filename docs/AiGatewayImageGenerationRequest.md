# AiGatewayImageGenerationRequest

Запрос генерации изображений

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **object** | ID модели генерации изображений (&#x60;mode: image_generation&#x60; в &#x60;GET /v1/models&#x60;) | 
**prompt** | **object** | Описание изображения | 
**n** | **object** | Количество изображений | [optional] 
**size** | **object** | Размер изображения | [optional] 
**quality** | **object** | Качество изображения | [optional] 
**response_format** | **object** | Формат изображения в ответе. Поддерживается не всеми моделями | [optional] 
**output_format** | **object** | Формат файла изображения | [optional] 

## Example

```python
from timeweb_cloud_api.models.ai_gateway_image_generation_request import AiGatewayImageGenerationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiGatewayImageGenerationRequest from a JSON string
ai_gateway_image_generation_request_instance = AiGatewayImageGenerationRequest.from_json(json)
# print the JSON string representation of the object
print AiGatewayImageGenerationRequest.to_json()

# convert the object into a dict
ai_gateway_image_generation_request_dict = ai_gateway_image_generation_request_instance.to_dict()
# create an instance of AiGatewayImageGenerationRequest from a dict
ai_gateway_image_generation_request_form_dict = ai_gateway_image_generation_request.from_dict(ai_gateway_image_generation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


