# Valkey

Параметры Valkey (`valkey` | `valkey7` | `valkey8_1` | `valkey9_1`)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_output_buffer_limit_normal** | **object** | Ограничение буфера вывода для обычных клиентских подключений. Формат: &#x60;hard-limit soft-limit soft-seconds&#x60; (&#x60;valkey&#x60; | &#x60;valkey7&#x60; | &#x60;valkey8_1&#x60; | &#x60;valkey9_1&#x60;). | [optional] 
**client_output_buffer_limit_pubsub** | **object** | Ограничение буфера вывода для клиентов pub/sub. Формат: &#x60;hard-limit soft-limit soft-seconds&#x60; (&#x60;valkey&#x60; | &#x60;valkey7&#x60; | &#x60;valkey8_1&#x60; | &#x60;valkey9_1&#x60;). | [optional] 
**databases** | **object** | Количество логических баз данных на сервере (&#x60;valkey&#x60; | &#x60;valkey7&#x60; | &#x60;valkey8_1&#x60; | &#x60;valkey9_1&#x60;). | [optional] 
**timeout** | **object** | Время ожидания в секундах перед закрытием неактивного клиентского соединения. &#x60;0&#x60; — отключено (&#x60;valkey&#x60; | &#x60;valkey7&#x60; | &#x60;valkey8_1&#x60; | &#x60;valkey9_1&#x60;). | [optional] 
**maxmemory_policy** | **object** | Политика вытеснения ключей при достижении лимита памяти (&#x60;valkey&#x60; | &#x60;valkey7&#x60; | &#x60;valkey8_1&#x60; | &#x60;valkey9_1&#x60;). | [optional] 
**slowlog_log_slower_than** | **object** | Минимальное время выполнения команды в микросекундах для записи в журнал медленных команд (&#x60;valkey&#x60; | &#x60;valkey7&#x60; | &#x60;valkey8_1&#x60; | &#x60;valkey9_1&#x60;). | [optional] 
**slowlog_max_len** | **object** | Максимальное количество записей, хранящихся в журнале медленных команд (&#x60;valkey&#x60; | &#x60;valkey7&#x60; | &#x60;valkey8_1&#x60; | &#x60;valkey9_1&#x60;). | [optional] 
**save** | **object** | Условие создания снимка RDB на диск. Формат: &#x60;seconds changes&#x60; — сохранение выполняется, если за указанное время было сделано не менее указанного количества изменений (&#x60;valkey&#x60; | &#x60;valkey7&#x60; | &#x60;valkey8_1&#x60; | &#x60;valkey9_1&#x60;). | [optional] 
**appendonly** | **object** | Включение режима AOF (Append Only File) для персистентного хранения данных (&#x60;valkey&#x60; | &#x60;valkey7&#x60; | &#x60;valkey8_1&#x60; | &#x60;valkey9_1&#x60;). | [optional] 
**appendfsync** | **object** | Режим синхронизации AOF-файла с диском: &#x60;always&#x60; — при каждой записи, &#x60;everysec&#x60; — раз в секунду, &#x60;no&#x60; — управление передаётся ОС (&#x60;valkey&#x60; | &#x60;valkey7&#x60; | &#x60;valkey8_1&#x60; | &#x60;valkey9_1&#x60;). | [optional] 
**tcp_keepalive** | **object** | Интервал проверки активности TCP-соединения в секундах. &#x60;0&#x60; — отключено (&#x60;valkey&#x60; | &#x60;valkey7&#x60; | &#x60;valkey8_1&#x60; | &#x60;valkey9_1&#x60;). | [optional] 

## Example

```python
from timeweb_cloud_api.models.valkey import Valkey

# TODO update the JSON string below
json = "{}"
# create an instance of Valkey from a JSON string
valkey_instance = Valkey.from_json(json)
# print the JSON string representation of the object
print Valkey.to_json()

# convert the object into a dict
valkey_dict = valkey_instance.to_dict()
# create an instance of Valkey from a dict
valkey_form_dict = valkey.from_dict(valkey_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


