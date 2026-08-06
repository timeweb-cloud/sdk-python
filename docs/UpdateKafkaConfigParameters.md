# UpdateKafkaConfigParameters

Настройки топика Kafka. Передаются только для кластеров Kafka: для кластеров других типов запрос вернется с ошибкой `forbidden_change_configuration`. Не переданные параметры получают значения по умолчанию. Числовые значения можно передавать как числом, так и строкой.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partitions** | **object** | Количество партиций топика. Количество партиций нельзя уменьшить: если передать значение меньше текущего, останется текущее. | [optional] 
**cleanup_policy** | **object** | Политика очистки старых сегментов лога: &#x60;delete&#x60; — удалять, &#x60;compact&#x60; — уплотнять. | [optional] 
**compression_type** | **object** | Тип сжатия сообщений в топике. | [optional] 
**delete_retention_ms** | **object** | Время (в мс) хранения меток удаления для уплотняемых топиков. Максимальное значение — 9223372036854775807. | [optional] 
**file_delete_delay_ms** | **object** | Задержка (в мс) перед удалением файла из файловой системы. Максимальное значение — 9223372036854775807. | [optional] 
**flush_messages** | **object** | Количество сообщений, после которого данные принудительно сбрасываются на диск. Максимальное значение — 9223372036854775807. | [optional] 
**flush_ms** | **object** | Интервал (в мс), после которого данные принудительно сбрасываются на диск. Максимальное значение — 9223372036854775807. | [optional] 
**index_interval_bytes** | **object** | Интервал (в байтах), с которым Kafka добавляет запись в индекс смещений. | [optional] 
**min_compaction_lag_ms** | **object** | Минимальное время (в мс), в течение которого сообщение остается неуплотненным. Максимальное значение — 9223372036854775807. | [optional] 
**max_compaction_lag_ms** | **object** | Максимальное время (в мс), в течение которого сообщение может оставаться неуплотненным. Максимальное значение — 9223372036854775807. | [optional] 
**max_message_bytes** | **object** | Максимальный размер (в байтах) пакета сообщений. | [optional] 
**message_format_version** | **object** | Версия формата сообщений, в котором Kafka добавляет сообщения в лог. | [optional] 
**message_timestamp_difference_max_ms** | **object** | Максимально допустимая разница (в мс) между временной меткой сообщения и временем его получения брокером. Максимальное значение — 9223372036854775807. | [optional] 
**message_downconversion_enable** | **object** | Понижение версии формата сообщений для старых клиентов. | [optional] 
**message_timestamp_type** | **object** | Источник временной метки сообщения: &#x60;CreateTime&#x60; — время создания сообщения клиентом, &#x60;LogAppendTime&#x60; — время добавления сообщения в лог брокером. | [optional] 
**min_cleanable_dirty_ratio** | **object** | Доля неуплотненных данных в логе, при которой запускается уплотнение. | [optional] 
**min_insync_replicas** | **object** | Минимальное количество синхронизированных реплик, необходимое для подтверждения записи. | [optional] 
**preallocate** | **object** | Предварительное выделение места на диске при создании нового сегмента лога. | [optional] 
**retention_bytes** | **object** | Максимальный размер (в байтах) партиции топика, после которого старые сегменты удаляются. &#x60;-1&#x60; — без ограничения. Максимальное значение — 9223372036854775807. | [optional] 
**retention_ms** | **object** | Время (в мс) хранения сообщений в топике. &#x60;-1&#x60; — хранить бессрочно. Максимальное значение — 9223372036854775807. | [optional] 
**segment_bytes** | **object** | Максимальный размер (в байтах) одного сегмента лога. | [optional] 
**segment_index_bytes** | **object** | Максимальный размер (в байтах) индексного файла сегмента лога. | [optional] 
**segment_jitter_ms** | **object** | Максимальное случайное отклонение (в мс) от времени ротации сегмента. Максимальное значение — 9223372036854775807. | [optional] 
**segment_ms** | **object** | Период (в мс), после которого Kafka создает новый сегмент лога. Максимальное значение — 9223372036854775807. | [optional] 
**unclean_leader_election_enable** | **object** | Возможность выбрать лидером партиции реплику, которая не входит в число синхронизированных. | [optional] 

## Example

```python
from timeweb_cloud_api.models.update_kafka_config_parameters import UpdateKafkaConfigParameters

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateKafkaConfigParameters from a JSON string
update_kafka_config_parameters_instance = UpdateKafkaConfigParameters.from_json(json)
# print the JSON string representation of the object
print UpdateKafkaConfigParameters.to_json()

# convert the object into a dict
update_kafka_config_parameters_dict = update_kafka_config_parameters_instance.to_dict()
# create an instance of UpdateKafkaConfigParameters from a dict
update_kafka_config_parameters_form_dict = update_kafka_config_parameters.from_dict(update_kafka_config_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


