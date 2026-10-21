# AiSolutionTypeRequirements

Минимальные требования к конфигурации сервера

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu_min** | **object** | Минимальное количество ядер CPU | [optional] 
**ram_min** | **object** | Минимальный объём RAM, МБ | [optional] 
**disk_min** | **object** | Минимальный размер диска, МБ | [optional] 
**bandwidth_min** | **object** | Минимальная пропускная способность, Мбит/с | [optional] 

## Example

```python
from timeweb_cloud_api.models.ai_solution_type_requirements import AiSolutionTypeRequirements

# TODO update the JSON string below
json = "{}"
# create an instance of AiSolutionTypeRequirements from a JSON string
ai_solution_type_requirements_instance = AiSolutionTypeRequirements.from_json(json)
# print the JSON string representation of the object
print AiSolutionTypeRequirements.to_json()

# convert the object into a dict
ai_solution_type_requirements_dict = ai_solution_type_requirements_instance.to_dict()
# create an instance of AiSolutionTypeRequirements from a dict
ai_solution_type_requirements_form_dict = ai_solution_type_requirements.from_dict(ai_solution_type_requirements_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


