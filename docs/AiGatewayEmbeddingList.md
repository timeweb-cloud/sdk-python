# AiGatewayEmbeddingList

Эмбеддинги в порядке входных текстов

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **object** | Тип объекта | [optional] 
**model** | **object** | Модель, которая ответила | [optional] 
**data** | **object** | Эмбеддинги | [optional] 
**usage** | [**AiGatewayEmbeddingListUsage**](AiGatewayEmbeddingListUsage.md) |  | [optional] 

## Example

```python
from timeweb_cloud_api.models.ai_gateway_embedding_list import AiGatewayEmbeddingList

# TODO update the JSON string below
json = "{}"
# create an instance of AiGatewayEmbeddingList from a JSON string
ai_gateway_embedding_list_instance = AiGatewayEmbeddingList.from_json(json)
# print the JSON string representation of the object
print AiGatewayEmbeddingList.to_json()

# convert the object into a dict
ai_gateway_embedding_list_dict = ai_gateway_embedding_list_instance.to_dict()
# create an instance of AiGatewayEmbeddingList from a dict
ai_gateway_embedding_list_form_dict = ai_gateway_embedding_list.from_dict(ai_gateway_embedding_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


