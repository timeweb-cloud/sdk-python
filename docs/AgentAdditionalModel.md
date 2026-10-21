# AgentAdditionalModel

Дополнительная модель агента с настройками

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_id** | **object** | ID модели | 
**width** | **object** | Ширина генерируемого изображения в пикселях (для моделей генерации изображений). Если не передана — значение по умолчанию для модели. | [optional] 
**height** | **object** | Высота генерируемого изображения в пикселях (для моделей генерации изображений). Если не передана — значение по умолчанию для модели. | [optional] 

## Example

```python
from timeweb_cloud_api.models.agent_additional_model import AgentAdditionalModel

# TODO update the JSON string below
json = "{}"
# create an instance of AgentAdditionalModel from a JSON string
agent_additional_model_instance = AgentAdditionalModel.from_json(json)
# print the JSON string representation of the object
print AgentAdditionalModel.to_json()

# convert the object into a dict
agent_additional_model_dict = agent_additional_model_instance.to_dict()
# create an instance of AgentAdditionalModel from a dict
agent_additional_model_form_dict = agent_additional_model.from_dict(agent_additional_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


