# AiGatewayImagesResponse

Сгенерированные изображения

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **object** | Время создания, Unix-время в секундах | [optional] 
**data** | **object** | Изображения | [optional] 
**usage** | **Dict[str, object]** | Расход токенов, если модель его возвращает | [optional] 

## Example

```python
from timeweb_cloud_api.models.ai_gateway_images_response import AiGatewayImagesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AiGatewayImagesResponse from a JSON string
ai_gateway_images_response_instance = AiGatewayImagesResponse.from_json(json)
# print the JSON string representation of the object
print AiGatewayImagesResponse.to_json()

# convert the object into a dict
ai_gateway_images_response_dict = ai_gateway_images_response_instance.to_dict()
# create an instance of AiGatewayImagesResponse from a dict
ai_gateway_images_response_form_dict = ai_gateway_images_response.from_dict(ai_gateway_images_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


