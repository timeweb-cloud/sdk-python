# WorkerPresetOutApi


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | Уникальный идентификатор тарифа | 
**description** | **object** | Описание тарифа | 
**description_short** | **object** | Краткое описание тарифа | 
**price** | **object** | Стоимость | 
**cpu** | **object** | Количество ядер ноды | 
**ram** | **object** | Количество памяти ноды | 
**disk** | **object** | Количество пространства на ноде | 
**network** | **object** | Пропускная способность ноды | 
**type** | **object** | Тип тарифа | [optional] 

## Example

```python
from openapi_client.models.worker_preset_out_api import WorkerPresetOutApi

# TODO update the JSON string below
json = "{}"
# create an instance of WorkerPresetOutApi from a JSON string
worker_preset_out_api_instance = WorkerPresetOutApi.from_json(json)
# print the JSON string representation of the object
print WorkerPresetOutApi.to_json()

# convert the object into a dict
worker_preset_out_api_dict = worker_preset_out_api_instance.to_dict()
# create an instance of WorkerPresetOutApi from a dict
worker_preset_out_api_form_dict = worker_preset_out_api.from_dict(worker_preset_out_api_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


