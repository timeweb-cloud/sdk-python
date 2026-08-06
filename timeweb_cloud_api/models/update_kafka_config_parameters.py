# coding: utf-8

"""
    Timeweb Cloud API

    # Введение API Timeweb Cloud позволяет вам управлять ресурсами в облаке программным способом с использованием обычных HTTP-запросов.  Множество функций, которые доступны в панели управления Timeweb Cloud, также доступны через API, что позволяет вам автоматизировать ваши собственные сценарии.  В этой документации сперва будет описан общий дизайн и принципы работы API, а после этого конкретные конечные точки. Также будут приведены примеры запросов к ним.   ## Запросы Запросы должны выполняться по протоколу `HTTPS`, чтобы гарантировать шифрование транзакций. Поддерживаются следующие методы запроса: |Метод|Применение| |--- |--- | |GET|Извлекает данные о коллекциях и отдельных ресурсах.| |POST|Для коллекций создает новый ресурс этого типа. Также используется для выполнения действий с конкретным ресурсом.| |PUT|Обновляет существующий ресурс.| |PATCH|Некоторые ресурсы поддерживают частичное обновление, то есть обновление только части атрибутов ресурса, в этом случае вместо метода PUT будет использован PATCH.| |DELETE|Удаляет ресурс.|  Методы `POST`, `PUT` и `PATCH` могут включать объект в тело запроса с типом содержимого `application/json`.  ### Параметры в запросах Некоторые коллекции поддерживают пагинацию, поиск или сортировку в запросах. В параметрах запроса требуется передать: - `limit` — обозначает количество записей, которое необходимо вернуть  - `offset` — указывает на смещение, относительно начала списка  - `search` — позволяет указать набор символов для поиска  - `sort` — можно задать правило сортировки коллекции  ## Ответы Запросы вернут один из следующих кодов состояния ответа HTTP:  |Статус|Описание| |--- |--- | |200 OK|Действие с ресурсом было выполнено успешно.| |201 Created|Ресурс был успешно создан. При этом ресурс может быть как уже готовым к использованию, так и находиться в процессе запуска.| |204 No Content|Действие с ресурсом было выполнено успешно, и ответ не содержит дополнительной информации в теле.| |400 Bad Request|Был отправлен неверный запрос, например, в нем отсутствуют обязательные параметры и т. д. Тело ответа будет содержать дополнительную информацию об ошибке.| |401 Unauthorized|Ошибка аутентификации.| |403 Forbidden|Аутентификация прошла успешно, но недостаточно прав для выполнения действия.| |404 Not Found|Запрашиваемый ресурс не найден.| |409 Conflict|Запрос конфликтует с текущим состоянием.| |423 Locked|Ресурс из запроса заблокирован от применения к нему указанного метода.| |429 Too Many Requests|Был достигнут лимит по количеству запросов в единицу времени.| |500 Internal Server Error|При выполнении запроса произошла какая-то внутренняя ошибка. Чтобы решить эту проблему, лучше всего создать тикет в панели управления.|  ### Структура успешного ответа Все конечные точки будут возвращать данные в формате `JSON`. Ответы на `GET`-запросы будут иметь на верхнем уровне следующую структуру атрибутов:  |Название поля|Тип|Описание| |--- |--- |--- | |[entity_name]|object, object[], string[], number[], boolean|Динамическое поле, которое будет меняться в зависимости от запрашиваемого ресурса и будет содержать все атрибуты, необходимые для описания этого ресурса. Например, при запросе списка баз данных будет возвращаться поле `dbs`, а при запросе конкретного облачного сервера `server`. Для некоторых конечных точек в ответе может возвращаться сразу несколько ресурсов.| |meta|object|Опционально. Объект, который содержит вспомогательную информацию о ресурсе. Чаще всего будет встречаться при запросе коллекций и содержать поле `total`, которое будет указывать на количество элементов в коллекции.| |response_id|string|Опционально. В большинстве случаев в ответе будет содержаться ID ответа в формате UUIDv4, который однозначно указывает на ваш запрос внутри нашей системы. Если вам потребуется задать вопрос нашей поддержке, приложите к вопросу этот ID— так мы сможем найти ответ на него намного быстрее. Также вы можете использовать этот ID, чтобы убедиться, что это новый ответ на запрос и результат не был получен из кэша.|  Пример запроса на получение списка SSH-ключей: ```     HTTP/2.0 200 OK     {       \"ssh_keys\":[           {             \"body\":\"ssh-rsa AAAAB3NzaC1sdfghjkOAsBwWhs= example@device.local\",             \"created_at\":\"2021-09-15T19:52:27Z\",             \"expired_at\":null,             \"id\":5297,             \"is_default\":false,             \"name\":\"example@device.local\",             \"used_at\":null,             \"used_by\":[]           }       ],       \"meta\":{           \"total\":1       },       \"response_id\":\"94608d15-8672-4eed-8ab6-28bd6fa3cdf7\"     } ```  ### Структура ответа с ошибкой |Название поля|Тип|Описание| |--- |--- |--- | |status_code|number|Короткий числовой идентификатор ошибки.| |error_code|string|Короткий текстовый идентификатор ошибки, который уточняет числовой идентификатор и удобен для программной обработки. Самый простой пример — это код `not_found` для ошибки 404.| |message|string, string[]|Опционально. В большинстве случаев в ответе будет содержаться человекочитаемое подробное описание ошибки или ошибок, которые помогут понять, что нужно исправить.| |response_id|string|Опционально. В большинстве случае в ответе будет содержаться ID ответа в формате UUIDv4, который однозначно указывает на ваш запрос внутри нашей системы. Если вам потребуется задать вопрос нашей поддержке, приложите к вопросу этот ID — так мы сможем найти ответ на него намного быстрее.|  Пример: ```     HTTP/2.0 403 Forbidden     {       \"status_code\": 403,       \"error_code\":  \"forbidden\",       \"message\":     \"You do not have access for the attempted action\",       \"response_id\": \"94608d15-8672-4eed-8ab6-28bd6fa3cdf7\"     } ```  ## Статусы ресурсов Важно учесть, что при создании большинства ресурсов внутри платформы вам будет сразу возвращен ответ от сервера со статусом `200 OK` или `201 Created` и ID созданного ресурса в теле ответа, но при этом этот ресурс может быть ещё в *состоянии запуска*.  Для того чтобы понять, в каком состоянии сейчас находится ваш ресурс, мы добавили поле `status` в ответ на получение информации о ресурсе.  Список статусов будет отличаться в зависимости от типа ресурса. Увидеть поддерживаемый список статусов вы сможете в описании каждого конкретного ресурса.     ## Ограничение скорости запросов (Rate Limiting) Чтобы обеспечить стабильность для всех пользователей, Timeweb Cloud защищает API от всплесков входящего трафика, анализируя количество запросов c каждого аккаунта к каждой конечной точке.  Если ваше приложение отправляет более 20 запросов в секунду на одну конечную точку, то для этого запроса API может вернуть код состояния HTTP `429 Too Many Requests`.   ## Аутентификация Доступ к API осуществляется с помощью JWT-токена. Токенами можно управлять внутри панели управления Timeweb Cloud в разделе *API и Terraform*.  Токен необходимо передавать в заголовке каждого запроса в формате: ```   Authorization: Bearer $TIMEWEB_CLOUD_TOKEN ```  ## Формат примеров API Примеры в этой документации описаны с помощью `curl`, HTTP-клиента командной строки. На компьютерах `Linux` и `macOS` обычно по умолчанию установлен `curl`, и он доступен для загрузки на всех популярных платформах, включая `Windows`.  Каждый пример разделен на несколько строк символом `\\`, который совместим с `bash`. Типичный пример выглядит так: ```   curl -X PATCH      -H \"Content-Type: application/json\"      -H \"Authorization: Bearer $TIMEWEB_CLOUD_TOKEN\"      -d '{\"name\":\"Cute Corvus\",\"comment\":\"Development Server\"}'      \"https://api.timeweb.cloud/api/v1/dedicated/1051\" ``` - Параметр `-X` задает метод запроса. Для согласованности метод будет указан во всех примерах, даже если он явно не требуется для методов `GET`. - Строки `-H` задают требуемые HTTP-заголовки. - Примеры, для которых требуется объект JSON в теле запроса, передают требуемые данные через параметр `-d`.  Чтобы использовать приведенные примеры, не подставляя каждый раз в них свой токен, вы можете добавить токен один раз в переменные окружения в вашей консоли. Например, на `Linux` это можно сделать с помощью команды:  ``` TIMEWEB_CLOUD_TOKEN=\"token\" ```  После этого токен будет автоматически подставляться в ваши запросы.  Обратите внимание, что все значения в этой документации являются примерами. Не полагайтесь на IDы операционных систем, тарифов и т.д., используемые в примерах. Используйте соответствующую конечную точку для получения значений перед созданием ресурсов.   ## Версионирование API построено согласно принципам [семантического версионирования](https://semver.org/lang/ru). Это значит, что мы гарантируем обратную совместимость всех изменений в пределах одной мажорной версии.  Мажорная версия каждой конечной точки обозначается в пути запроса, например, запрос `/api/v1/servers` указывает, что этот метод имеет версию 1.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: info@timeweb.cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Optional
from pydantic import BaseModel, Field, validator

class UpdateKafkaConfigParameters(BaseModel):
    """
    Настройки топика Kafka. Передаются только для кластеров Kafka: для кластеров других типов запрос вернется с ошибкой `forbidden_change_configuration`. Не переданные параметры получают значения по умолчанию. Числовые значения можно передавать как числом, так и строкой.
    """
    partitions: Optional[Any] = Field(None, description="Количество партиций топика. Количество партиций нельзя уменьшить: если передать значение меньше текущего, останется текущее.")
    cleanup_policy: Optional[Any] = Field(None, description="Политика очистки старых сегментов лога: `delete` — удалять, `compact` — уплотнять.")
    compression_type: Optional[Any] = Field(None, description="Тип сжатия сообщений в топике.")
    delete_retention_ms: Optional[Any] = Field(None, description="Время (в мс) хранения меток удаления для уплотняемых топиков. Максимальное значение — 9223372036854775807.")
    file_delete_delay_ms: Optional[Any] = Field(None, description="Задержка (в мс) перед удалением файла из файловой системы. Максимальное значение — 9223372036854775807.")
    flush_messages: Optional[Any] = Field(None, description="Количество сообщений, после которого данные принудительно сбрасываются на диск. Максимальное значение — 9223372036854775807.")
    flush_ms: Optional[Any] = Field(None, description="Интервал (в мс), после которого данные принудительно сбрасываются на диск. Максимальное значение — 9223372036854775807.")
    index_interval_bytes: Optional[Any] = Field(None, description="Интервал (в байтах), с которым Kafka добавляет запись в индекс смещений.")
    min_compaction_lag_ms: Optional[Any] = Field(None, description="Минимальное время (в мс), в течение которого сообщение остается неуплотненным. Максимальное значение — 9223372036854775807.")
    max_compaction_lag_ms: Optional[Any] = Field(None, description="Максимальное время (в мс), в течение которого сообщение может оставаться неуплотненным. Максимальное значение — 9223372036854775807.")
    max_message_bytes: Optional[Any] = Field(None, description="Максимальный размер (в байтах) пакета сообщений.")
    message_format_version: Optional[Any] = Field(None, description="Версия формата сообщений, в котором Kafka добавляет сообщения в лог.")
    message_timestamp_difference_max_ms: Optional[Any] = Field(None, description="Максимально допустимая разница (в мс) между временной меткой сообщения и временем его получения брокером. Максимальное значение — 9223372036854775807.")
    message_downconversion_enable: Optional[Any] = Field(None, description="Понижение версии формата сообщений для старых клиентов.")
    message_timestamp_type: Optional[Any] = Field(None, description="Источник временной метки сообщения: `CreateTime` — время создания сообщения клиентом, `LogAppendTime` — время добавления сообщения в лог брокером.")
    min_cleanable_dirty_ratio: Optional[Any] = Field(None, description="Доля неуплотненных данных в логе, при которой запускается уплотнение.")
    min_insync_replicas: Optional[Any] = Field(None, description="Минимальное количество синхронизированных реплик, необходимое для подтверждения записи.")
    preallocate: Optional[Any] = Field(None, description="Предварительное выделение места на диске при создании нового сегмента лога.")
    retention_bytes: Optional[Any] = Field(None, description="Максимальный размер (в байтах) партиции топика, после которого старые сегменты удаляются. `-1` — без ограничения. Максимальное значение — 9223372036854775807.")
    retention_ms: Optional[Any] = Field(None, description="Время (в мс) хранения сообщений в топике. `-1` — хранить бессрочно. Максимальное значение — 9223372036854775807.")
    segment_bytes: Optional[Any] = Field(None, description="Максимальный размер (в байтах) одного сегмента лога.")
    segment_index_bytes: Optional[Any] = Field(None, description="Максимальный размер (в байтах) индексного файла сегмента лога.")
    segment_jitter_ms: Optional[Any] = Field(None, description="Максимальное случайное отклонение (в мс) от времени ротации сегмента. Максимальное значение — 9223372036854775807.")
    segment_ms: Optional[Any] = Field(None, description="Период (в мс), после которого Kafka создает новый сегмент лога. Максимальное значение — 9223372036854775807.")
    unclean_leader_election_enable: Optional[Any] = Field(None, description="Возможность выбрать лидером партиции реплику, которая не входит в число синхронизированных.")
    __properties = ["partitions", "cleanup_policy", "compression_type", "delete_retention_ms", "file_delete_delay_ms", "flush_messages", "flush_ms", "index_interval_bytes", "min_compaction_lag_ms", "max_compaction_lag_ms", "max_message_bytes", "message_format_version", "message_timestamp_difference_max_ms", "message_downconversion_enable", "message_timestamp_type", "min_cleanable_dirty_ratio", "min_insync_replicas", "preallocate", "retention_bytes", "retention_ms", "segment_bytes", "segment_index_bytes", "segment_jitter_ms", "segment_ms", "unclean_leader_election_enable"]

    @validator('cleanup_policy')
    def cleanup_policy_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('delete', 'compact'):
            raise ValueError("must be one of enum values ('delete', 'compact')")
        return value

    @validator('compression_type')
    def compression_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('uncompressed', 'zstd', 'lz4', 'snappy', 'gzip', 'producer'):
            raise ValueError("must be one of enum values ('uncompressed', 'zstd', 'lz4', 'snappy', 'gzip', 'producer')")
        return value

    @validator('message_format_version')
    def message_format_version_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('0.8.0', '0.8.1', '0.8.2', '0.9.0', '0.10.0-IV0', '0.10.0-IV1', '0.10.1-IV0', '0.10.1-IV1', '0.10.1-IV2', '0.10.2-IV0', '0.11.0-IV0', '0.11.0-IV1', '0.11.0-IV2', '1.0-IV0', '1.1-IV0', '2.0-IV0', '2.0-IV1', '2.1-IV0', '2.1-IV1', '2.1-IV2', '2.2-IV0', '2.2-IV1', '2.3-IV0', '2.3-IV1', '2.4-IV0', '2.4-IV1', '2.5-IV0', '2.6-IV0', '2.7-IV0', '2.7-IV1', '2.7-IV2', '2.8-IV0', '2.8-IV1', '3.0-IV0', '3.0-IV1', '3.1-IV0', '3.2-IV0', '3.3-IV0', '3.3-IV1', '3.3-IV2', '3.3-IV3', '3.4-IV0', '3.5-IV0', '3.5-IV1', '3.5-IV2'):
            raise ValueError("must be one of enum values ('0.8.0', '0.8.1', '0.8.2', '0.9.0', '0.10.0-IV0', '0.10.0-IV1', '0.10.1-IV0', '0.10.1-IV1', '0.10.1-IV2', '0.10.2-IV0', '0.11.0-IV0', '0.11.0-IV1', '0.11.0-IV2', '1.0-IV0', '1.1-IV0', '2.0-IV0', '2.0-IV1', '2.1-IV0', '2.1-IV1', '2.1-IV2', '2.2-IV0', '2.2-IV1', '2.3-IV0', '2.3-IV1', '2.4-IV0', '2.4-IV1', '2.5-IV0', '2.6-IV0', '2.7-IV0', '2.7-IV1', '2.7-IV2', '2.8-IV0', '2.8-IV1', '3.0-IV0', '3.0-IV1', '3.1-IV0', '3.2-IV0', '3.3-IV0', '3.3-IV1', '3.3-IV2', '3.3-IV3', '3.4-IV0', '3.5-IV0', '3.5-IV1', '3.5-IV2')")
        return value

    @validator('message_downconversion_enable')
    def message_downconversion_enable_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('ON', 'OFF'):
            raise ValueError("must be one of enum values ('ON', 'OFF')")
        return value

    @validator('message_timestamp_type')
    def message_timestamp_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('CreateTime', 'LogAppendTime'):
            raise ValueError("must be one of enum values ('CreateTime', 'LogAppendTime')")
        return value

    @validator('preallocate')
    def preallocate_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('ON', 'OFF'):
            raise ValueError("must be one of enum values ('ON', 'OFF')")
        return value

    @validator('unclean_leader_election_enable')
    def unclean_leader_election_enable_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('ON', 'OFF'):
            raise ValueError("must be one of enum values ('ON', 'OFF')")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> UpdateKafkaConfigParameters:
        """Create an instance of UpdateKafkaConfigParameters from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if partitions (nullable) is None
        # and __fields_set__ contains the field
        if self.partitions is None and "partitions" in self.__fields_set__:
            _dict['partitions'] = None

        # set to None if cleanup_policy (nullable) is None
        # and __fields_set__ contains the field
        if self.cleanup_policy is None and "cleanup_policy" in self.__fields_set__:
            _dict['cleanup_policy'] = None

        # set to None if compression_type (nullable) is None
        # and __fields_set__ contains the field
        if self.compression_type is None and "compression_type" in self.__fields_set__:
            _dict['compression_type'] = None

        # set to None if delete_retention_ms (nullable) is None
        # and __fields_set__ contains the field
        if self.delete_retention_ms is None and "delete_retention_ms" in self.__fields_set__:
            _dict['delete_retention_ms'] = None

        # set to None if file_delete_delay_ms (nullable) is None
        # and __fields_set__ contains the field
        if self.file_delete_delay_ms is None and "file_delete_delay_ms" in self.__fields_set__:
            _dict['file_delete_delay_ms'] = None

        # set to None if flush_messages (nullable) is None
        # and __fields_set__ contains the field
        if self.flush_messages is None and "flush_messages" in self.__fields_set__:
            _dict['flush_messages'] = None

        # set to None if flush_ms (nullable) is None
        # and __fields_set__ contains the field
        if self.flush_ms is None and "flush_ms" in self.__fields_set__:
            _dict['flush_ms'] = None

        # set to None if index_interval_bytes (nullable) is None
        # and __fields_set__ contains the field
        if self.index_interval_bytes is None and "index_interval_bytes" in self.__fields_set__:
            _dict['index_interval_bytes'] = None

        # set to None if min_compaction_lag_ms (nullable) is None
        # and __fields_set__ contains the field
        if self.min_compaction_lag_ms is None and "min_compaction_lag_ms" in self.__fields_set__:
            _dict['min_compaction_lag_ms'] = None

        # set to None if max_compaction_lag_ms (nullable) is None
        # and __fields_set__ contains the field
        if self.max_compaction_lag_ms is None and "max_compaction_lag_ms" in self.__fields_set__:
            _dict['max_compaction_lag_ms'] = None

        # set to None if max_message_bytes (nullable) is None
        # and __fields_set__ contains the field
        if self.max_message_bytes is None and "max_message_bytes" in self.__fields_set__:
            _dict['max_message_bytes'] = None

        # set to None if message_format_version (nullable) is None
        # and __fields_set__ contains the field
        if self.message_format_version is None and "message_format_version" in self.__fields_set__:
            _dict['message_format_version'] = None

        # set to None if message_timestamp_difference_max_ms (nullable) is None
        # and __fields_set__ contains the field
        if self.message_timestamp_difference_max_ms is None and "message_timestamp_difference_max_ms" in self.__fields_set__:
            _dict['message_timestamp_difference_max_ms'] = None

        # set to None if message_downconversion_enable (nullable) is None
        # and __fields_set__ contains the field
        if self.message_downconversion_enable is None and "message_downconversion_enable" in self.__fields_set__:
            _dict['message_downconversion_enable'] = None

        # set to None if message_timestamp_type (nullable) is None
        # and __fields_set__ contains the field
        if self.message_timestamp_type is None and "message_timestamp_type" in self.__fields_set__:
            _dict['message_timestamp_type'] = None

        # set to None if min_cleanable_dirty_ratio (nullable) is None
        # and __fields_set__ contains the field
        if self.min_cleanable_dirty_ratio is None and "min_cleanable_dirty_ratio" in self.__fields_set__:
            _dict['min_cleanable_dirty_ratio'] = None

        # set to None if min_insync_replicas (nullable) is None
        # and __fields_set__ contains the field
        if self.min_insync_replicas is None and "min_insync_replicas" in self.__fields_set__:
            _dict['min_insync_replicas'] = None

        # set to None if preallocate (nullable) is None
        # and __fields_set__ contains the field
        if self.preallocate is None and "preallocate" in self.__fields_set__:
            _dict['preallocate'] = None

        # set to None if retention_bytes (nullable) is None
        # and __fields_set__ contains the field
        if self.retention_bytes is None and "retention_bytes" in self.__fields_set__:
            _dict['retention_bytes'] = None

        # set to None if retention_ms (nullable) is None
        # and __fields_set__ contains the field
        if self.retention_ms is None and "retention_ms" in self.__fields_set__:
            _dict['retention_ms'] = None

        # set to None if segment_bytes (nullable) is None
        # and __fields_set__ contains the field
        if self.segment_bytes is None and "segment_bytes" in self.__fields_set__:
            _dict['segment_bytes'] = None

        # set to None if segment_index_bytes (nullable) is None
        # and __fields_set__ contains the field
        if self.segment_index_bytes is None and "segment_index_bytes" in self.__fields_set__:
            _dict['segment_index_bytes'] = None

        # set to None if segment_jitter_ms (nullable) is None
        # and __fields_set__ contains the field
        if self.segment_jitter_ms is None and "segment_jitter_ms" in self.__fields_set__:
            _dict['segment_jitter_ms'] = None

        # set to None if segment_ms (nullable) is None
        # and __fields_set__ contains the field
        if self.segment_ms is None and "segment_ms" in self.__fields_set__:
            _dict['segment_ms'] = None

        # set to None if unclean_leader_election_enable (nullable) is None
        # and __fields_set__ contains the field
        if self.unclean_leader_election_enable is None and "unclean_leader_election_enable" in self.__fields_set__:
            _dict['unclean_leader_election_enable'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UpdateKafkaConfigParameters:
        """Create an instance of UpdateKafkaConfigParameters from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UpdateKafkaConfigParameters.parse_obj(obj)

        _obj = UpdateKafkaConfigParameters.parse_obj({
            "partitions": obj.get("partitions"),
            "cleanup_policy": obj.get("cleanup_policy"),
            "compression_type": obj.get("compression_type"),
            "delete_retention_ms": obj.get("delete_retention_ms"),
            "file_delete_delay_ms": obj.get("file_delete_delay_ms"),
            "flush_messages": obj.get("flush_messages"),
            "flush_ms": obj.get("flush_ms"),
            "index_interval_bytes": obj.get("index_interval_bytes"),
            "min_compaction_lag_ms": obj.get("min_compaction_lag_ms"),
            "max_compaction_lag_ms": obj.get("max_compaction_lag_ms"),
            "max_message_bytes": obj.get("max_message_bytes"),
            "message_format_version": obj.get("message_format_version"),
            "message_timestamp_difference_max_ms": obj.get("message_timestamp_difference_max_ms"),
            "message_downconversion_enable": obj.get("message_downconversion_enable"),
            "message_timestamp_type": obj.get("message_timestamp_type"),
            "min_cleanable_dirty_ratio": obj.get("min_cleanable_dirty_ratio"),
            "min_insync_replicas": obj.get("min_insync_replicas"),
            "preallocate": obj.get("preallocate"),
            "retention_bytes": obj.get("retention_bytes"),
            "retention_ms": obj.get("retention_ms"),
            "segment_bytes": obj.get("segment_bytes"),
            "segment_index_bytes": obj.get("segment_index_bytes"),
            "segment_jitter_ms": obj.get("segment_jitter_ms"),
            "segment_ms": obj.get("segment_ms"),
            "unclean_leader_election_enable": obj.get("unclean_leader_election_enable")
        })
        return _obj

