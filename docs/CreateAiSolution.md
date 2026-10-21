# CreateAiSolution

Параметры создания AI-решения

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **object** | Тип решения. Доступные типы возвращает метод получения типов AI-решений | 
**name** | **object** | Название решения. Используется и как имя сервера | 
**description** | **object** | Описание решения. Используется и как комментарий к серверу | [optional] 
**model_id** | **object** | ID модели, с которой будет работать решение. Подходят только действующие текстовые модели (&#x60;type: llm&#x60; в &#x60;GET /api/v3/cloud-ai/models&#x60;) | 
**preset_id** | **object** | ID тарифа сервера из &#x60;GET /api/v1/presets/servers&#x60;. Тариф должен быть не ниже требований типа решения (при создании это не проверяется) и из той же локации, что и зона доступности. Баланса аккаунта должно хватать хотя бы на час работы тарифа | 
**project_id** | **object** | ID проекта, в который добавляются сервер и ключ AI Gateway решения | [optional] 
**availability_zone** | **object** | Зона доступности сервера. Если не указана, используется зона по умолчанию для региона аккаунта. Зона должна относиться к локации тарифа, а образ решения должен быть доступен в этой зоне | [optional] 

## Example

```python
from timeweb_cloud_api.models.create_ai_solution import CreateAiSolution

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAiSolution from a JSON string
create_ai_solution_instance = CreateAiSolution.from_json(json)
# print the JSON string representation of the object
print CreateAiSolution.to_json()

# convert the object into a dict
create_ai_solution_dict = create_ai_solution_instance.to_dict()
# create an instance of CreateAiSolution from a dict
create_ai_solution_form_dict = create_ai_solution.from_dict(create_ai_solution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


