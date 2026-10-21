# UpdateAiSolution

Изменяемые параметры AI-решения. Все поля необязательны, пустое тело ничего не меняет

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Название решения | [optional] 
**description** | **object** | Описание решения. &#x60;null&#x60; очищает описание | [optional] 
**model_id** | **object** | ID новой модели. Изменение записывается в конфигурацию агента на сервере решения, поэтому сервер должен быть включён и полностью развёрнут | [optional] 

## Example

```python
from timeweb_cloud_api.models.update_ai_solution import UpdateAiSolution

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAiSolution from a JSON string
update_ai_solution_instance = UpdateAiSolution.from_json(json)
# print the JSON string representation of the object
print UpdateAiSolution.to_json()

# convert the object into a dict
update_ai_solution_dict = update_ai_solution_instance.to_dict()
# create an instance of UpdateAiSolution from a dict
update_ai_solution_form_dict = update_ai_solution.from_dict(update_ai_solution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


