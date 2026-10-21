# AiGatewayBatchList

Список батчей

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **object** | Тип объекта | [optional] 
**data** | **object** | Батчи | [optional] 
**first_id** | **object** | ID первого батча на странице | [optional] 
**last_id** | **object** | ID последнего батча на странице — передайте его в &#x60;after&#x60; для следующей страницы | [optional] 
**has_more** | **object** | Есть ли следующая страница | [optional] 

## Example

```python
from timeweb_cloud_api.models.ai_gateway_batch_list import AiGatewayBatchList

# TODO update the JSON string below
json = "{}"
# create an instance of AiGatewayBatchList from a JSON string
ai_gateway_batch_list_instance = AiGatewayBatchList.from_json(json)
# print the JSON string representation of the object
print AiGatewayBatchList.to_json()

# convert the object into a dict
ai_gateway_batch_list_dict = ai_gateway_batch_list_instance.to_dict()
# create an instance of AiGatewayBatchList from a dict
ai_gateway_batch_list_form_dict = ai_gateway_batch_list.from_dict(ai_gateway_batch_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


