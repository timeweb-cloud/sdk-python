# ModelBatch

Условия Batch API для модели. Цена в batch = обычная цена × множитель

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**multiplier_in** | **object** | Множитель цены входных токенов | 
**multiplier_out** | **object** | Множитель цены выходных токенов | 
**multiplier_cache_read** | **object** | Множитель цены токенов, прочитанных из кэша | 
**multiplier_cache_write** | **object** | Множитель цены токенов, записанных в кэш | 
**endpoints** | **object** | Эндпоинты, допустимые в строках batch-файла | 
**supports_images** | **object** | Принимает ли модель изображения в batch-запросах | 

## Example

```python
from timeweb_cloud_api.models.model_batch import ModelBatch

# TODO update the JSON string below
json = "{}"
# create an instance of ModelBatch from a JSON string
model_batch_instance = ModelBatch.from_json(json)
# print the JSON string representation of the object
print ModelBatch.to_json()

# convert the object into a dict
model_batch_dict = model_batch_instance.to_dict()
# create an instance of ModelBatch from a dict
model_batch_form_dict = model_batch.from_dict(model_batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


