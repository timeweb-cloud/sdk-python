# ConfigParametersMysql

Параметры MySQL (`mysql5` | `mysql` | `mysql8_4`)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**join_buffer_size** | **object** | Размер буфера, используемого при соединениях таблиц без индексов (&#x60;mysql5&#x60; | &#x60;mysql&#x60; | &#x60;mysql8_4&#x60;). | [optional] 
**max_connections** | **object** | Максимальное количество одновременных подключений к серверу (&#x60;mysql5&#x60; | &#x60;mysql&#x60; | &#x60;mysql8_4&#x60; | &#x60;postgres&#x60; | &#x60;postgres14&#x60; | &#x60;postgres15&#x60; | &#x60;postgres16&#x60; | &#x60;postgres17&#x60; | &#x60;postgres18&#x60;). | [optional] 
**sort_buffer_size** | **object** | Размер буфера сортировки для операций ORDER BY и GROUP BY (&#x60;mysql5&#x60; | &#x60;mysql&#x60; | &#x60;mysql8_4&#x60;). | [optional] 
**thread_cache_size** | **object** | Количество потоков, которые сервер сохраняет для повторного использования (&#x60;mysql5&#x60; | &#x60;mysql&#x60; | &#x60;mysql8_4&#x60;). | [optional] 
**innodb_buffer_pool_size** | **object** | Размер буферного пула InnoDB для хранения данных и индексов в памяти (&#x60;mysql5&#x60; | &#x60;mysql&#x60; | &#x60;mysql8_4&#x60;). | [optional] 
**auto_increment_increment** | **object** | Интервал между значениями столбцов с атрибутом &#x60;AUTO_INCREMENT&#x60; (&#x60;mysql5&#x60; | &#x60;mysql&#x60; | &#x60;mysql8_4&#x60;). | [optional] 
**auto_increment_offset** | **object** | Начальное значение для столбцов с атрибутом &#x60;AUTO_INCREMENT&#x60; (&#x60;mysql5&#x60; | &#x60;mysql&#x60; | &#x60;mysql8_4&#x60;). | [optional] 
**innodb_io_capacity** | **object** | Количество операций ввода-вывода в секунду &#x60;IOPS&#x60;, используемых InnoDB (&#x60;mysql5&#x60; | &#x60;mysql&#x60; | &#x60;mysql8_4&#x60;). | [optional] 
**innodb_purge_threads** | **object** | Количество потоков, используемых для фоновой очистки undo-записей InnoDB (&#x60;mysql5&#x60; | &#x60;mysql&#x60; | &#x60;mysql8_4&#x60;). | [optional] 
**innodb_read_io_threads** | **object** | Количество потоков ввода-вывода для операций чтения InnoDB (&#x60;mysql5&#x60; | &#x60;mysql&#x60; | &#x60;mysql8_4&#x60;). | [optional] 
**innodb_thread_concurrency** | **object** | Ограничение количества одновременно выполняющихся потоков InnoDB (&#x60;mysql5&#x60; | &#x60;mysql&#x60; | &#x60;mysql8_4&#x60;). | [optional] 
**innodb_write_io_threads** | **object** | Количество потоков ввода-вывода для операций записи InnoDB (&#x60;mysql5&#x60; | &#x60;mysql&#x60; | &#x60;mysql8_4&#x60;). | [optional] 
**innodb_log_file_size** | **object** | Размер файла журнала транзакций InnoDB redo log (&#x60;mysql5&#x60; | &#x60;mysql&#x60; | &#x60;mysql8_4&#x60;). | [optional] 
**max_allowed_packet** | **object** | Максимальный размер пакета данных, который может передаваться между клиентом и сервером (&#x60;mysql5&#x60; | &#x60;mysql&#x60; | &#x60;mysql8_4&#x60;). | [optional] 
**max_heap_table_size** | **object** | Максимальный размер таблиц типа MEMORY (&#x60;mysql5&#x60; | &#x60;mysql&#x60; | &#x60;mysql8_4&#x60;). | [optional] 
**sql_mode** | **object** | Режим работы SQL сервера, определяющий поведение обработки запросов (&#x60;mysql5&#x60; | &#x60;mysql&#x60; | &#x60;mysql8_4&#x60;). | [optional] 
**query_cache_type** | **object** | Тип кэша запросов (&#x60;mysql5&#x60; | &#x60;mysql&#x60; | &#x60;mysql8_4&#x60;). | [optional] 
**query_cache_size** | **object** | Объем памяти, выделяемый для кэширования результатов запросов (&#x60;mysql5&#x60; | &#x60;mysql&#x60; | &#x60;mysql8_4&#x60;). | [optional] 
**innodb_flush_log_at_trx_commit** | **object** | Режим записи журнала InnoDB при фиксации транзакций (&#x60;mysql5&#x60; | &#x60;mysql&#x60; | &#x60;mysql8_4&#x60;). | [optional] 
**transaction_isolation** | **object** | Уровень изоляции транзакций по умолчанию (&#x60;mysql5&#x60; | &#x60;mysql&#x60; | &#x60;mysql8_4&#x60;). | [optional] 
**long_query_time** | **object** | Время выполнения запроса, после которого он считается долгим и может попасть в slow query log (&#x60;mysql5&#x60; | &#x60;mysql&#x60; | &#x60;mysql8_4&#x60;). | [optional] 
**tmp_table_size** | **object** | Максимальный размер временных таблиц в памяти (&#x60;mysql5&#x60; | &#x60;mysql&#x60; | &#x60;mysql8_4&#x60;). | [optional] 
**table_open_cache** | **object** | Количество открытых таблиц, которые сервер может хранить в кэше (&#x60;mysql5&#x60; | &#x60;mysql&#x60; | &#x60;mysql8_4&#x60;). | [optional] 
**table_open_cache_instances** | **object** | Количество экземпляров кэша открытых таблиц для снижения конкуренции между потоками (&#x60;mysql5&#x60; | &#x60;mysql&#x60; | &#x60;mysql8_4&#x60;). | [optional] 
**innodb_flush_method** | **object** | Метод выполнения операций записи и синхронизации файлов InnoDB (&#x60;mysql5&#x60; | &#x60;mysql&#x60; | &#x60;mysql8_4&#x60;). | [optional] 
**innodb_strict_mode** | **object** | Включение строгой проверки операций InnoDB (&#x60;mysql5&#x60; | &#x60;mysql&#x60; | &#x60;mysql8_4&#x60;). | [optional] 
**slow_query_log** | **object** | Включение журнала медленных запросов (&#x60;mysql5&#x60; | &#x60;mysql&#x60; | &#x60;mysql8_4&#x60;). | [optional] 
**binlog_cache_size** | **object** | Размер кэша бинарного журнала для транзакций (&#x60;mysql5&#x60; | &#x60;mysql&#x60; | &#x60;mysql8_4&#x60;). | [optional] 
**binlog_group_commit_sync_delay** | **object** | Задержка синхронизации групповой фиксации бинарного журнала в микросекундах (&#x60;mysql5&#x60; | &#x60;mysql&#x60; | &#x60;mysql8_4&#x60;). | [optional] 
**binlog_row_image** | **object** | Количество информации, записываемой в бинарный журнал при row-based репликации (&#x60;mysql5&#x60; | &#x60;mysql&#x60; | &#x60;mysql8_4&#x60;). | [optional] 
**binlog_rows_query_log_events** | **object** | Включение записи SQL-запросов в бинарный журнал при row-based репликации (&#x60;mysql5&#x60; | &#x60;mysql&#x60; | &#x60;mysql8_4&#x60;). | [optional] 
**character_set_server** | **object** | Кодировка по умолчанию для сервера MySQL (&#x60;mysql5&#x60; | &#x60;mysql&#x60; | &#x60;mysql8_4&#x60;). | [optional] 
**explicit_defaults_for_timestamp** | **object** | Определяет автоматическое поведение TIMESTAMP без явных значений по умолчанию (&#x60;mysql5&#x60; | &#x60;mysql&#x60; | &#x60;mysql8_4&#x60;). | [optional] 
**group_concat_max_len** | **object** | Максимальная длина результата функции GROUP_CONCAT (&#x60;mysql5&#x60; | &#x60;mysql&#x60; | &#x60;mysql8_4&#x60;). | [optional] 
**innodb_adaptive_hash_index** | **object** | Включение или отключение адаптивного хэш-индекса InnoDB для ускорения поиска по индексам (&#x60;mysql5&#x60; | &#x60;mysql&#x60; | &#x60;mysql8_4&#x60;). | [optional] 
**innodb_lock_wait_timeout** | **object** | Время ожидания блокировки InnoDB перед завершением транзакции с ошибкой (&#x60;mysql5&#x60; | &#x60;mysql&#x60; | &#x60;mysql8_4&#x60;). | [optional] 
**innodb_numa_interleave** | **object** | Включение распределения памяти InnoDB между NUMA-узлами (&#x60;mysql5&#x60; | &#x60;mysql&#x60; | &#x60;mysql8_4&#x60;). | [optional] 
**net_read_timeout** | **object** | Время ожидания данных от клиента при чтении сетевого соединения (&#x60;mysql5&#x60; | &#x60;mysql&#x60; | &#x60;mysql8_4&#x60;). | [optional] 
**net_write_timeout** | **object** | Время ожидания записи данных клиенту через сетевое соединение (&#x60;mysql5&#x60; | &#x60;mysql&#x60; | &#x60;mysql8_4&#x60;). | [optional] 
**regexp_time_limit** | **object** | Максимальное время выполнения регулярных выражений (&#x60;mysql&#x60; | &#x60;mysql8_4&#x60;). | [optional] 
**sync_binlog** | **object** | Количество операций записи бинарного журнала перед принудительной синхронизацией на диск (&#x60;mysql5&#x60; | &#x60;mysql&#x60; | &#x60;mysql8_4&#x60;). | [optional] 
**table_definition_cache** | **object** | Количество определений таблиц, хранящихся в кэше (&#x60;mysql5&#x60; | &#x60;mysql&#x60; | &#x60;mysql8_4&#x60;). | [optional] 
**log_bin_trust_function_creators** | **object** | Разрешение создания хранимых функций без проверки бинарной регистрации (&#x60;mysql5&#x60; | &#x60;mysql&#x60; | &#x60;mysql8_4&#x60;). | [optional] 
**skip_name_resolve** | **object** | Отключение DNS-разрешения имен клиентов при подключении к серверу (&#x60;mysql5&#x60; | &#x60;mysql&#x60; | &#x60;mysql8_4&#x60;). | [optional] 
**innodb_redo_log_capacity** | **object** | Общий размер redo log InnoDB для хранения журнала восстановления (&#x60;mysql8_4&#x60;). | [optional] 
**wait_timeout** | **object** | Время ожидания неактивного клиентского соединения перед закрытием (&#x60;mysql5&#x60; | &#x60;mysql&#x60; | &#x60;mysql8_4&#x60;). | [optional] 
**interactive_timeout** | **object** | Время ожидания неактивного интерактивного соединения перед закрытием (&#x60;mysql5&#x60; | &#x60;mysql&#x60; | &#x60;mysql8_4&#x60;). | [optional] 
**default_time_zone** | **object** | Часовой пояс сервера MySQL по умолчанию (&#x60;mysql5&#x60; | &#x60;mysql&#x60; | &#x60;mysql8_4&#x60;). | [optional] 
**pxc_strict_mode** | **object** | Режим строгой проверки операций в Percona XtraDB Cluster (&#x60;mysql5&#x60; | &#x60;mysql&#x60; | &#x60;mysql8_4&#x60;). | [optional] 

## Example

```python
from timeweb_cloud_api.models.config_parameters_mysql import ConfigParametersMysql

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigParametersMysql from a JSON string
config_parameters_mysql_instance = ConfigParametersMysql.from_json(json)
# print the JSON string representation of the object
print ConfigParametersMysql.to_json()

# convert the object into a dict
config_parameters_mysql_dict = config_parameters_mysql_instance.to_dict()
# create an instance of ConfigParametersMysql from a dict
config_parameters_mysql_form_dict = config_parameters_mysql.from_dict(config_parameters_mysql_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


