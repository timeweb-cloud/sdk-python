# ConfigParameters

Параметры базы данных

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_increment_increment** | **object** | Интервал между значениями столбцов с атрибутом &#x60;AUTO_INCREMENT&#x60; (&#x60;mysql5&#x60; | &#x60;mysql&#x60;). | [optional] 
**auto_increment_offset** | **object** | Начальное значение для столбцов с атрибутом &#x60;AUTO_INCREMENT&#x60; (&#x60;mysql5&#x60; | &#x60;mysql&#x60;). | [optional] 
**innodb_io_capacity** | **object** | Количество операций ввода-вывода в секунду &#x60;IOPS&#x60; (&#x60;mysql5&#x60; | &#x60;mysql&#x60;). | [optional] 
**innodb_purge_threads** | **object** | Количество потоков ввода-вывода, используемых для операций очистки (&#x60;mysql5&#x60; | &#x60;mysql&#x60;). | [optional] 
**innodb_read_io_threads** | **object** | Количество потоков ввода-вывода, используемых для операций чтения (&#x60;mysql5&#x60; | &#x60;mysql&#x60;). | [optional] 
**innodb_thread_concurrency** | **object** | Максимальное число потоков, которые могут исполняться (&#x60;mysql5&#x60; | &#x60;mysql&#x60;). | [optional] 
**innodb_write_io_threads** | **object** | Количество потоков ввода-вывода, используемых для операций записи (&#x60;mysql5&#x60; | &#x60;mysql&#x60;). | [optional] 
**join_buffer_size** | **object** | Минимальный размер буфера (&#x60;mysql5&#x60; | &#x60;mysql&#x60;). | [optional] 
**max_allowed_packet** | **object** | Максимальный размер одного пакета, строки или параметра, отправляемого функцией &#x60;mysql_stmt_send_long_data()&#x60; (&#x60;mysql5&#x60; | &#x60;mysql&#x60;). | [optional] 
**max_heap_table_size** | **object** | Максимальный размер пользовательских MEMORY-таблиц (&#x60;mysql5&#x60; | &#x60;mysql&#x60;). | [optional] 
**autovacuum_analyze_scale_factor** | **object** | Доля измененных или удаленных записей в таблице, при которой процесс автоочистки выполнит команду &#x60;ANALYZE&#x60; (&#x60;postgres&#x60; | &#x60;postgres14&#x60;| &#x60;postgres15&#x60;). | [optional] 
**bgwriter_delay** | **object** | Задержка между запусками процесса фоновой записи (&#x60;postgres&#x60; | &#x60;postgres14&#x60;| &#x60;postgres15&#x60;). | [optional] 
**bgwriter_lru_maxpages** | **object** | Максимальное число элементов буферного кеша (&#x60;postgres&#x60; | &#x60;postgres14&#x60;| &#x60;postgres15&#x60;). | [optional] 
**deadlock_timeout** | **object** | Время ожидания, по истечении которого будет выполняться проверка состояния перекрестной блокировки (&#x60;postgres&#x60; | &#x60;postgres14&#x60;| &#x60;postgres15&#x60;). | [optional] 
**gin_pending_list_limit** | **object** | Максимальный размер очереди записей индекса &#x60;GIN&#x60; (&#x60;postgres&#x60; | &#x60;postgres14&#x60;| &#x60;postgres15&#x60;). | [optional] 
**idle_in_transaction_session_timeout** | **object** | Время простоя открытой транзакции, при превышении которого будет завершена сессия с этой транзакцией (&#x60;postgres&#x60; | &#x60;postgres14&#x60;| &#x60;postgres15&#x60;). | [optional] 
**idle_session_timeout** | **object** | Время простоя не открытой транзакции, при превышении которого будет завершена сессия с этой транзакцией (&#x60;postgres&#x60; | &#x60;postgres14&#x60;| &#x60;postgres15&#x60;). | [optional] 
**join_collapse_limit** | **object** | Значение количества элементов в списке &#x60;FROM&#x60; при превышении которого, планировщик будет переносить в список явные инструкции &#x60;JOIN&#x60; (&#x60;postgres&#x60; | &#x60;postgres14&#x60;| &#x60;postgres15&#x60;). | [optional] 
**lock_timeout** | **object** | Время ожидания освобождения блокировки (&#x60;postgres&#x60; | &#x60;postgres14&#x60;| &#x60;postgres15&#x60;). | [optional] 
**max_prepared_transactions** | **object** | Максимальное число транзакций, которые могут одновременно находиться в подготовленном состоянии (&#x60;postgres&#x60; | &#x60;postgres14&#x60;| &#x60;postgres15&#x60;). | [optional] 
**max_connections** | **object** | Допустимое количество соединений (&#x60;postgres&#x60; | &#x60;postgres14&#x60;| &#x60;postgres15&#x60; | &#x60;mysql&#x60;). | [optional] 
**shared_buffers** | **object** | Устанавливает количество буферов общей памяти, используемых сервером (&#x60;postgres&#x60; | &#x60;postgres14&#x60;| &#x60;postgres15&#x60;). | [optional] 
**wal_buffers** | **object** | Устанавливает количество буферов дисковых страниц в общей памяти для WAL (&#x60;postgres&#x60; | &#x60;postgres14&#x60;| &#x60;postgres15&#x60;). | [optional] 
**temp_buffers** | **object** | Устанавливает максимальное количество временных буферов, используемых каждой сессией (&#x60;postgres&#x60; | &#x60;postgres14&#x60;| &#x60;postgres15&#x60;). | [optional] 
**work_mem** | **object** | Устанавливает максимальное количество памяти, используемое для рабочих пространств запросов (&#x60;postgres&#x60; | &#x60;postgres14&#x60;| &#x60;postgres15&#x60;). | [optional] 
**sql_mode** | **object** | Устанавливает режим SQL. Можно задать несколько режимов, разделяя их запятой. (&#x60;mysql&#x60;). | [optional] 
**query_cache_type** | **object** | Параметр включает или отключает работу MySQL Query Cache (&#x60;mysql&#x60;). | [optional] 
**query_cache_size** | **object** | Размер в байтах, доступный для кэша запросов (&#x60;mysql&#x60;). | [optional] 

## Example

```python
from timeweb_cloud_api.models.config_parameters import ConfigParameters

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigParameters from a JSON string
config_parameters_instance = ConfigParameters.from_json(json)
# print the JSON string representation of the object
print ConfigParameters.to_json()

# convert the object into a dict
config_parameters_dict = config_parameters_instance.to_dict()
# create an instance of ConfigParameters from a dict
config_parameters_form_dict = config_parameters.from_dict(config_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


