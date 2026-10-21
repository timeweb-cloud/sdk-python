# AiSolutionType

Тип AI-решения

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **object** | Тип решения | 
**name** | **object** | Название решения | 
**description** | **object** | Описание решения в HTML | 
**os_ids** | **object** | ID операционной системы, на которой работает решение (один элемент). Пустой массив, если этой ОС нет в каталоге ОС аккаунта | 
**installations** | **object** | Количество установок. Всегда &#x60;0&#x60;, оставлено для обратной совместимости | 
**requirements** | [**AiSolutionTypeRequirements**](AiSolutionTypeRequirements.md) |  | [optional] 

## Example

```python
from timeweb_cloud_api.models.ai_solution_type import AiSolutionType

# TODO update the JSON string below
json = "{}"
# create an instance of AiSolutionType from a JSON string
ai_solution_type_instance = AiSolutionType.from_json(json)
# print the JSON string representation of the object
print AiSolutionType.to_json()

# convert the object into a dict
ai_solution_type_dict = ai_solution_type_instance.to_dict()
# create an instance of AiSolutionType from a dict
ai_solution_type_form_dict = ai_solution_type.from_dict(ai_solution_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


