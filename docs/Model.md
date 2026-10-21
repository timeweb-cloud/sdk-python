# Model

AI модель

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID модели | 
**provider_id** | **object** | ID провайдера модели | 
**name** | **object** | Семейство модели | 
**public_name** | **object** | Отображаемое название модели | 
**model_name** | **object** | Идентификатор модели с префиксом провайдера — передаётся в поле &#x60;model&#x60; запросов к AI Gateway | 
**type** | **object** | Тип модели: - &#x60;llm&#x60; — языковая модель - &#x60;hosted-llm&#x60; — языковая модель, размещённая в Timeweb Cloud - &#x60;embedding&#x60; — модель эмбеддингов - &#x60;image&#x60; — генерация изображений - &#x60;audio&#x60; — работа с аудио - &#x60;video&#x60; — генерация видео - &#x60;moderation&#x60; — модерация контента - &#x60;system-one&#x60; — служебная модель с собственным API | 
**version** | **object** | Версия модели | 
**is_deprecated** | **object** | Модель устарела и недоступна для выбора в новых агентах | 
**is_stopped** | **object** | Поддержка модели остановлена: запросы к ней не выполняются | 
**deprecation_date** | **object** | Дата отключения модели у провайдера. &#x60;null&#x60;, если отключение не запланировано | 
**is_reasoning** | **object** | Модель поддерживает режим рассуждений | 
**params_info** | [**Dict[str, ModelParamInfo]**](ModelParamInfo.md) | Параметры генерации, которые можно настроить у агента с этой моделью. Ключ — имя параметра (&#x60;temperature&#x60;, &#x60;top_p&#x60;, &#x60;max_tokens&#x60;, &#x60;reasoning_effort&#x60; и т.д.). &#x60;null&#x60;, если параметры не заданы | 

## Example

```python
from timeweb_cloud_api.models.model import Model

# TODO update the JSON string below
json = "{}"
# create an instance of Model from a JSON string
model_instance = Model.from_json(json)
# print the JSON string representation of the object
print Model.to_json()

# convert the object into a dict
model_dict = model_instance.to_dict()
# create an instance of Model from a dict
model_form_dict = model.from_dict(model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


