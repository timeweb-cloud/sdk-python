# ModelParameter

Характеристика модели из справочника

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **object** | Код характеристики — ключ в &#x60;parameter_values&#x60; модели | 
**name** | **object** | Название характеристики | [optional] 
**description** | **object** | Описание характеристики | [optional] 
**type** | **object** | Тип значения | 
**unit** | **object** | Единица измерения (&#x60;tokens&#x60;, &#x60;tokens_per_second&#x60;, &#x60;currency_per_million&#x60;, ...). &#x60;null&#x60;, если нет | 
**group** | **object** | Группа характеристик: &#x60;pricing&#x60;, &#x60;quality&#x60;, &#x60;performance&#x60;, &#x60;capabilities&#x60;, &#x60;limits&#x60;, &#x60;meta&#x60; | 
**sort_order** | **object** | Порядок отображения | 
**comparison_direction** | **object** | Какое значение лучше при сравнении моделей | 
**format** | **object** | Подсказка для отображения значения. &#x60;currency_per_million_tokens&#x60; — значение в &#x60;parameter_values&#x60; указано за 1 токен, показывать его удобно за 1 млн токенов | 

## Example

```python
from timeweb_cloud_api.models.model_parameter import ModelParameter

# TODO update the JSON string below
json = "{}"
# create an instance of ModelParameter from a JSON string
model_parameter_instance = ModelParameter.from_json(json)
# print the JSON string representation of the object
print ModelParameter.to_json()

# convert the object into a dict
model_parameter_dict = model_parameter_instance.to_dict()
# create an instance of ModelParameter from a dict
model_parameter_form_dict = model_parameter.from_dict(model_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


