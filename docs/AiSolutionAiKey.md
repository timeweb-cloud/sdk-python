# AiSolutionAiKey

Перевыпущенный ключ AI Gateway решения

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ai_key_id** | **object** | ID ключа AI Gateway решения. При перевыпуске не меняется | 
**key** | **object** | Новое значение ключа. Возвращается один раз: ключ уже записан в конфигурацию агента на сервере решения, повторно получить его нельзя | 

## Example

```python
from timeweb_cloud_api.models.ai_solution_ai_key import AiSolutionAiKey

# TODO update the JSON string below
json = "{}"
# create an instance of AiSolutionAiKey from a JSON string
ai_solution_ai_key_instance = AiSolutionAiKey.from_json(json)
# print the JSON string representation of the object
print AiSolutionAiKey.to_json()

# convert the object into a dict
ai_solution_ai_key_dict = ai_solution_ai_key_instance.to_dict()
# create an instance of AiSolutionAiKey from a dict
ai_solution_ai_key_form_dict = ai_solution_ai_key.from_dict(ai_solution_ai_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


