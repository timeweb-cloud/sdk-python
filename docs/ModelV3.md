# ModelV3

AI модель с характеристиками для сравнения (v3). Цены и характеристики — в `parameter_values`

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
**created_at** | **object** | Дата и время добавления модели | 
**updated_at** | **object** | Дата и время последнего изменения модели | 
**params_info** | [**Dict[str, ModelParamInfo]**](ModelParamInfo.md) | Параметры генерации, которые можно настроить у агента с этой моделью. Ключ — имя параметра (&#x60;temperature&#x60;, &#x60;top_p&#x60;, &#x60;max_tokens&#x60;, &#x60;reasoning_effort&#x60; и т.д.). &#x60;null&#x60;, если параметры не заданы | 
**parameter_values** | **Dict[str, object]** | Характеристики модели. Ключ — &#x60;code&#x60; из справочника &#x60;GET /api/v3/cloud-ai/model-parameters&#x60;, значение — число, строка, булево значение или массив строк. Если значение неизвестно, ключа нет.  Основные коды: - &#x60;cost_in&#x60;, &#x60;cost_out&#x60; — цена 1 входного / выходного токена в рублях - &#x60;cost_cache_read&#x60;, &#x60;cost_cache_write&#x60; — цена 1 токена чтения / записи кэша промпта в рублях; ключа нет, если отдельной цены нет (тарифицируется по &#x60;cost_in&#x60;) - &#x60;pricing_unit&#x60; — единица тарификации: &#x60;token&#x60; (по умолчанию), &#x60;megapixel&#x60;, &#x60;credit&#x60; - &#x60;cost_per_image&#x60; — цена изображения базового размера (1 МП) в рублях - &#x60;credits_from&#x60;, &#x60;cost_per_second_from&#x60; — минимальная ставка в кредитах провайдера и цена от, в рублях, за секунду видео - &#x60;context_window&#x60;, &#x60;max_output_tokens&#x60; — размер контекста и максимум токенов в ответе - &#x60;is_reasoning&#x60;, &#x60;supports_function_calling&#x60; — поддержка рассуждений и вызова инструментов - &#x60;supported_input_modalities&#x60;, &#x60;supported_output_modalities&#x60; — входные и выходные модальности (&#x60;text&#x60;, &#x60;image&#x60;, ...) - &#x60;avg_speed&#x60; — средняя скорость генерации, токенов в секунду - &#x60;aa_intelligence_index&#x60;, &#x60;aa_coding_index&#x60;, &#x60;aa_agentic_index&#x60; — индексы Artificial Analysis - &#x60;release_date&#x60; — дата релиза (&#x60;YYYY-MM-DD&#x60;) | 
**price_tiers** | **object** | Ступени цены по размеру входного контекста, по возрастанию порога. Пустой массив — у модели одна цена при любом контексте | 
**batch** | [**ModelBatch**](ModelBatch.md) |  | 

## Example

```python
from timeweb_cloud_api.models.model_v3 import ModelV3

# TODO update the JSON string below
json = "{}"
# create an instance of ModelV3 from a JSON string
model_v3_instance = ModelV3.from_json(json)
# print the JSON string representation of the object
print ModelV3.to_json()

# convert the object into a dict
model_v3_dict = model_v3_instance.to_dict()
# create an instance of ModelV3 from a dict
model_v3_form_dict = model_v3.from_dict(model_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


