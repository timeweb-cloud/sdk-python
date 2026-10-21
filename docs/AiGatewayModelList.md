# AiGatewayModelList

Список моделей

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **object** | Тип объекта | [optional] 
**data** | **object** | Модели | [optional] 

## Example

```python
from timeweb_cloud_api.models.ai_gateway_model_list import AiGatewayModelList

# TODO update the JSON string below
json = "{}"
# create an instance of AiGatewayModelList from a JSON string
ai_gateway_model_list_instance = AiGatewayModelList.from_json(json)
# print the JSON string representation of the object
print AiGatewayModelList.to_json()

# convert the object into a dict
ai_gateway_model_list_dict = ai_gateway_model_list_instance.to_dict()
# create an instance of AiGatewayModelList from a dict
ai_gateway_model_list_form_dict = ai_gateway_model_list.from_dict(ai_gateway_model_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


