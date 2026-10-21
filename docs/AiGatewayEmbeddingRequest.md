# AiGatewayEmbeddingRequest

Запрос эмбеддингов

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **object** | ID модели эмбеддингов (&#x60;mode: embedding&#x60; в &#x60;GET /v1/models&#x60;) | 
**input** | **object** | Текст или список текстов | 
**dimensions** | **object** | Размерность вектора — для моделей, которые её поддерживают | [optional] 
**encoding_format** | **object** | Формат векторов | [optional] 

## Example

```python
from timeweb_cloud_api.models.ai_gateway_embedding_request import AiGatewayEmbeddingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiGatewayEmbeddingRequest from a JSON string
ai_gateway_embedding_request_instance = AiGatewayEmbeddingRequest.from_json(json)
# print the JSON string representation of the object
print AiGatewayEmbeddingRequest.to_json()

# convert the object into a dict
ai_gateway_embedding_request_dict = ai_gateway_embedding_request_instance.to_dict()
# create an instance of AiGatewayEmbeddingRequest from a dict
ai_gateway_embedding_request_form_dict = ai_gateway_embedding_request.from_dict(ai_gateway_embedding_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


