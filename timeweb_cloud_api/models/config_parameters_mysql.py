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
from pydantic import BaseModel, Field

class ConfigParametersMysql(BaseModel):
    """
    Параметры MySQL (`mysql5` | `mysql` | `mysql8_4`)
    """
    join_buffer_size: Optional[Any] = Field(None, description="Размер буфера, используемого при соединениях таблиц без индексов (`mysql5` | `mysql` | `mysql8_4`).")
    max_connections: Optional[Any] = Field(None, description="Максимальное количество одновременных подключений к серверу (`mysql5` | `mysql` | `mysql8_4` | `postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    sort_buffer_size: Optional[Any] = Field(None, description="Размер буфера сортировки для операций ORDER BY и GROUP BY (`mysql5` | `mysql` | `mysql8_4`).")
    thread_cache_size: Optional[Any] = Field(None, description="Количество потоков, которые сервер сохраняет для повторного использования (`mysql5` | `mysql` | `mysql8_4`).")
    innodb_buffer_pool_size: Optional[Any] = Field(None, description="Размер буферного пула InnoDB для хранения данных и индексов в памяти (`mysql5` | `mysql` | `mysql8_4`).")
    auto_increment_increment: Optional[Any] = Field(None, description="Интервал между значениями столбцов с атрибутом `AUTO_INCREMENT` (`mysql5` | `mysql` | `mysql8_4`).")
    auto_increment_offset: Optional[Any] = Field(None, description="Начальное значение для столбцов с атрибутом `AUTO_INCREMENT` (`mysql5` | `mysql` | `mysql8_4`).")
    innodb_io_capacity: Optional[Any] = Field(None, description="Количество операций ввода-вывода в секунду `IOPS`, используемых InnoDB (`mysql5` | `mysql` | `mysql8_4`).")
    innodb_purge_threads: Optional[Any] = Field(None, description="Количество потоков, используемых для фоновой очистки undo-записей InnoDB (`mysql5` | `mysql` | `mysql8_4`).")
    innodb_read_io_threads: Optional[Any] = Field(None, description="Количество потоков ввода-вывода для операций чтения InnoDB (`mysql5` | `mysql` | `mysql8_4`).")
    innodb_thread_concurrency: Optional[Any] = Field(None, description="Ограничение количества одновременно выполняющихся потоков InnoDB (`mysql5` | `mysql` | `mysql8_4`).")
    innodb_write_io_threads: Optional[Any] = Field(None, description="Количество потоков ввода-вывода для операций записи InnoDB (`mysql5` | `mysql` | `mysql8_4`).")
    innodb_log_file_size: Optional[Any] = Field(None, description="Размер файла журнала транзакций InnoDB redo log (`mysql5` | `mysql` | `mysql8_4`).")
    max_allowed_packet: Optional[Any] = Field(None, description="Максимальный размер пакета данных, который может передаваться между клиентом и сервером (`mysql5` | `mysql` | `mysql8_4`).")
    max_heap_table_size: Optional[Any] = Field(None, description="Максимальный размер таблиц типа MEMORY (`mysql5` | `mysql` | `mysql8_4`).")
    sql_mode: Optional[Any] = Field(None, description="Режим работы SQL сервера, определяющий поведение обработки запросов (`mysql5` | `mysql` | `mysql8_4`).")
    query_cache_type: Optional[Any] = Field(None, description="Тип кэша запросов (`mysql5` | `mysql` | `mysql8_4`).")
    query_cache_size: Optional[Any] = Field(None, description="Объем памяти, выделяемый для кэширования результатов запросов (`mysql5` | `mysql` | `mysql8_4`).")
    innodb_flush_log_at_trx_commit: Optional[Any] = Field(None, description="Режим записи журнала InnoDB при фиксации транзакций (`mysql5` | `mysql` | `mysql8_4`).")
    transaction_isolation: Optional[Any] = Field(None, description="Уровень изоляции транзакций по умолчанию (`mysql5` | `mysql` | `mysql8_4`).")
    long_query_time: Optional[Any] = Field(None, description="Время выполнения запроса, после которого он считается долгим и может попасть в slow query log (`mysql5` | `mysql` | `mysql8_4`).")
    tmp_table_size: Optional[Any] = Field(None, description="Максимальный размер временных таблиц в памяти (`mysql5` | `mysql` | `mysql8_4`).")
    table_open_cache: Optional[Any] = Field(None, description="Количество открытых таблиц, которые сервер может хранить в кэше (`mysql5` | `mysql` | `mysql8_4`).")
    table_open_cache_instances: Optional[Any] = Field(None, description="Количество экземпляров кэша открытых таблиц для снижения конкуренции между потоками (`mysql5` | `mysql` | `mysql8_4`).")
    innodb_flush_method: Optional[Any] = Field(None, description="Метод выполнения операций записи и синхронизации файлов InnoDB (`mysql5` | `mysql` | `mysql8_4`).")
    innodb_strict_mode: Optional[Any] = Field(None, description="Включение строгой проверки операций InnoDB (`mysql5` | `mysql` | `mysql8_4`).")
    slow_query_log: Optional[Any] = Field(None, description="Включение журнала медленных запросов (`mysql5` | `mysql` | `mysql8_4`).")
    binlog_cache_size: Optional[Any] = Field(None, description="Размер кэша бинарного журнала для транзакций (`mysql5` | `mysql` | `mysql8_4`).")
    binlog_group_commit_sync_delay: Optional[Any] = Field(None, description="Задержка синхронизации групповой фиксации бинарного журнала в микросекундах (`mysql5` | `mysql` | `mysql8_4`).")
    binlog_row_image: Optional[Any] = Field(None, description="Количество информации, записываемой в бинарный журнал при row-based репликации (`mysql5` | `mysql` | `mysql8_4`).")
    binlog_rows_query_log_events: Optional[Any] = Field(None, description="Включение записи SQL-запросов в бинарный журнал при row-based репликации (`mysql5` | `mysql` | `mysql8_4`).")
    character_set_server: Optional[Any] = Field(None, description="Кодировка по умолчанию для сервера MySQL (`mysql5` | `mysql` | `mysql8_4`).")
    explicit_defaults_for_timestamp: Optional[Any] = Field(None, description="Определяет автоматическое поведение TIMESTAMP без явных значений по умолчанию (`mysql5` | `mysql` | `mysql8_4`).")
    group_concat_max_len: Optional[Any] = Field(None, description="Максимальная длина результата функции GROUP_CONCAT (`mysql5` | `mysql` | `mysql8_4`).")
    innodb_adaptive_hash_index: Optional[Any] = Field(None, description="Включение или отключение адаптивного хэш-индекса InnoDB для ускорения поиска по индексам (`mysql5` | `mysql` | `mysql8_4`).")
    innodb_lock_wait_timeout: Optional[Any] = Field(None, description="Время ожидания блокировки InnoDB перед завершением транзакции с ошибкой (`mysql5` | `mysql` | `mysql8_4`).")
    innodb_numa_interleave: Optional[Any] = Field(None, description="Включение распределения памяти InnoDB между NUMA-узлами (`mysql5` | `mysql` | `mysql8_4`).")
    net_read_timeout: Optional[Any] = Field(None, description="Время ожидания данных от клиента при чтении сетевого соединения (`mysql5` | `mysql` | `mysql8_4`).")
    net_write_timeout: Optional[Any] = Field(None, description="Время ожидания записи данных клиенту через сетевое соединение (`mysql5` | `mysql` | `mysql8_4`).")
    regexp_time_limit: Optional[Any] = Field(None, description="Максимальное время выполнения регулярных выражений (`mysql` | `mysql8_4`).")
    sync_binlog: Optional[Any] = Field(None, description="Количество операций записи бинарного журнала перед принудительной синхронизацией на диск (`mysql5` | `mysql` | `mysql8_4`).")
    table_definition_cache: Optional[Any] = Field(None, description="Количество определений таблиц, хранящихся в кэше (`mysql5` | `mysql` | `mysql8_4`).")
    log_bin_trust_function_creators: Optional[Any] = Field(None, description="Разрешение создания хранимых функций без проверки бинарной регистрации (`mysql5` | `mysql` | `mysql8_4`).")
    skip_name_resolve: Optional[Any] = Field(None, description="Отключение DNS-разрешения имен клиентов при подключении к серверу (`mysql5` | `mysql` | `mysql8_4`).")
    innodb_redo_log_capacity: Optional[Any] = Field(None, description="Общий размер redo log InnoDB для хранения журнала восстановления (`mysql8_4`).")
    wait_timeout: Optional[Any] = Field(None, description="Время ожидания неактивного клиентского соединения перед закрытием (`mysql5` | `mysql` | `mysql8_4`).")
    interactive_timeout: Optional[Any] = Field(None, description="Время ожидания неактивного интерактивного соединения перед закрытием (`mysql5` | `mysql` | `mysql8_4`).")
    default_time_zone: Optional[Any] = Field(None, alias="default-time-zone", description="Часовой пояс сервера MySQL по умолчанию (`mysql5` | `mysql` | `mysql8_4`).")
    pxc_strict_mode: Optional[Any] = Field(None, description="Режим строгой проверки операций в Percona XtraDB Cluster (`mysql5` | `mysql` | `mysql8_4`).")
    __properties = ["join_buffer_size", "max_connections", "sort_buffer_size", "thread_cache_size", "innodb_buffer_pool_size", "auto_increment_increment", "auto_increment_offset", "innodb_io_capacity", "innodb_purge_threads", "innodb_read_io_threads", "innodb_thread_concurrency", "innodb_write_io_threads", "innodb_log_file_size", "max_allowed_packet", "max_heap_table_size", "sql_mode", "query_cache_type", "query_cache_size", "innodb_flush_log_at_trx_commit", "transaction_isolation", "long_query_time", "tmp_table_size", "table_open_cache", "table_open_cache_instances", "innodb_flush_method", "innodb_strict_mode", "slow_query_log", "binlog_cache_size", "binlog_group_commit_sync_delay", "binlog_row_image", "binlog_rows_query_log_events", "character_set_server", "explicit_defaults_for_timestamp", "group_concat_max_len", "innodb_adaptive_hash_index", "innodb_lock_wait_timeout", "innodb_numa_interleave", "net_read_timeout", "net_write_timeout", "regexp_time_limit", "sync_binlog", "table_definition_cache", "log_bin_trust_function_creators", "skip_name_resolve", "innodb_redo_log_capacity", "wait_timeout", "interactive_timeout", "default-time-zone", "pxc_strict_mode"]

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
    def from_json(cls, json_str: str) -> ConfigParametersMysql:
        """Create an instance of ConfigParametersMysql from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if join_buffer_size (nullable) is None
        # and __fields_set__ contains the field
        if self.join_buffer_size is None and "join_buffer_size" in self.__fields_set__:
            _dict['join_buffer_size'] = None

        # set to None if max_connections (nullable) is None
        # and __fields_set__ contains the field
        if self.max_connections is None and "max_connections" in self.__fields_set__:
            _dict['max_connections'] = None

        # set to None if sort_buffer_size (nullable) is None
        # and __fields_set__ contains the field
        if self.sort_buffer_size is None and "sort_buffer_size" in self.__fields_set__:
            _dict['sort_buffer_size'] = None

        # set to None if thread_cache_size (nullable) is None
        # and __fields_set__ contains the field
        if self.thread_cache_size is None and "thread_cache_size" in self.__fields_set__:
            _dict['thread_cache_size'] = None

        # set to None if innodb_buffer_pool_size (nullable) is None
        # and __fields_set__ contains the field
        if self.innodb_buffer_pool_size is None and "innodb_buffer_pool_size" in self.__fields_set__:
            _dict['innodb_buffer_pool_size'] = None

        # set to None if auto_increment_increment (nullable) is None
        # and __fields_set__ contains the field
        if self.auto_increment_increment is None and "auto_increment_increment" in self.__fields_set__:
            _dict['auto_increment_increment'] = None

        # set to None if auto_increment_offset (nullable) is None
        # and __fields_set__ contains the field
        if self.auto_increment_offset is None and "auto_increment_offset" in self.__fields_set__:
            _dict['auto_increment_offset'] = None

        # set to None if innodb_io_capacity (nullable) is None
        # and __fields_set__ contains the field
        if self.innodb_io_capacity is None and "innodb_io_capacity" in self.__fields_set__:
            _dict['innodb_io_capacity'] = None

        # set to None if innodb_purge_threads (nullable) is None
        # and __fields_set__ contains the field
        if self.innodb_purge_threads is None and "innodb_purge_threads" in self.__fields_set__:
            _dict['innodb_purge_threads'] = None

        # set to None if innodb_read_io_threads (nullable) is None
        # and __fields_set__ contains the field
        if self.innodb_read_io_threads is None and "innodb_read_io_threads" in self.__fields_set__:
            _dict['innodb_read_io_threads'] = None

        # set to None if innodb_thread_concurrency (nullable) is None
        # and __fields_set__ contains the field
        if self.innodb_thread_concurrency is None and "innodb_thread_concurrency" in self.__fields_set__:
            _dict['innodb_thread_concurrency'] = None

        # set to None if innodb_write_io_threads (nullable) is None
        # and __fields_set__ contains the field
        if self.innodb_write_io_threads is None and "innodb_write_io_threads" in self.__fields_set__:
            _dict['innodb_write_io_threads'] = None

        # set to None if innodb_log_file_size (nullable) is None
        # and __fields_set__ contains the field
        if self.innodb_log_file_size is None and "innodb_log_file_size" in self.__fields_set__:
            _dict['innodb_log_file_size'] = None

        # set to None if max_allowed_packet (nullable) is None
        # and __fields_set__ contains the field
        if self.max_allowed_packet is None and "max_allowed_packet" in self.__fields_set__:
            _dict['max_allowed_packet'] = None

        # set to None if max_heap_table_size (nullable) is None
        # and __fields_set__ contains the field
        if self.max_heap_table_size is None and "max_heap_table_size" in self.__fields_set__:
            _dict['max_heap_table_size'] = None

        # set to None if sql_mode (nullable) is None
        # and __fields_set__ contains the field
        if self.sql_mode is None and "sql_mode" in self.__fields_set__:
            _dict['sql_mode'] = None

        # set to None if query_cache_type (nullable) is None
        # and __fields_set__ contains the field
        if self.query_cache_type is None and "query_cache_type" in self.__fields_set__:
            _dict['query_cache_type'] = None

        # set to None if query_cache_size (nullable) is None
        # and __fields_set__ contains the field
        if self.query_cache_size is None and "query_cache_size" in self.__fields_set__:
            _dict['query_cache_size'] = None

        # set to None if innodb_flush_log_at_trx_commit (nullable) is None
        # and __fields_set__ contains the field
        if self.innodb_flush_log_at_trx_commit is None and "innodb_flush_log_at_trx_commit" in self.__fields_set__:
            _dict['innodb_flush_log_at_trx_commit'] = None

        # set to None if transaction_isolation (nullable) is None
        # and __fields_set__ contains the field
        if self.transaction_isolation is None and "transaction_isolation" in self.__fields_set__:
            _dict['transaction_isolation'] = None

        # set to None if long_query_time (nullable) is None
        # and __fields_set__ contains the field
        if self.long_query_time is None and "long_query_time" in self.__fields_set__:
            _dict['long_query_time'] = None

        # set to None if tmp_table_size (nullable) is None
        # and __fields_set__ contains the field
        if self.tmp_table_size is None and "tmp_table_size" in self.__fields_set__:
            _dict['tmp_table_size'] = None

        # set to None if table_open_cache (nullable) is None
        # and __fields_set__ contains the field
        if self.table_open_cache is None and "table_open_cache" in self.__fields_set__:
            _dict['table_open_cache'] = None

        # set to None if table_open_cache_instances (nullable) is None
        # and __fields_set__ contains the field
        if self.table_open_cache_instances is None and "table_open_cache_instances" in self.__fields_set__:
            _dict['table_open_cache_instances'] = None

        # set to None if innodb_flush_method (nullable) is None
        # and __fields_set__ contains the field
        if self.innodb_flush_method is None and "innodb_flush_method" in self.__fields_set__:
            _dict['innodb_flush_method'] = None

        # set to None if innodb_strict_mode (nullable) is None
        # and __fields_set__ contains the field
        if self.innodb_strict_mode is None and "innodb_strict_mode" in self.__fields_set__:
            _dict['innodb_strict_mode'] = None

        # set to None if slow_query_log (nullable) is None
        # and __fields_set__ contains the field
        if self.slow_query_log is None and "slow_query_log" in self.__fields_set__:
            _dict['slow_query_log'] = None

        # set to None if binlog_cache_size (nullable) is None
        # and __fields_set__ contains the field
        if self.binlog_cache_size is None and "binlog_cache_size" in self.__fields_set__:
            _dict['binlog_cache_size'] = None

        # set to None if binlog_group_commit_sync_delay (nullable) is None
        # and __fields_set__ contains the field
        if self.binlog_group_commit_sync_delay is None and "binlog_group_commit_sync_delay" in self.__fields_set__:
            _dict['binlog_group_commit_sync_delay'] = None

        # set to None if binlog_row_image (nullable) is None
        # and __fields_set__ contains the field
        if self.binlog_row_image is None and "binlog_row_image" in self.__fields_set__:
            _dict['binlog_row_image'] = None

        # set to None if binlog_rows_query_log_events (nullable) is None
        # and __fields_set__ contains the field
        if self.binlog_rows_query_log_events is None and "binlog_rows_query_log_events" in self.__fields_set__:
            _dict['binlog_rows_query_log_events'] = None

        # set to None if character_set_server (nullable) is None
        # and __fields_set__ contains the field
        if self.character_set_server is None and "character_set_server" in self.__fields_set__:
            _dict['character_set_server'] = None

        # set to None if explicit_defaults_for_timestamp (nullable) is None
        # and __fields_set__ contains the field
        if self.explicit_defaults_for_timestamp is None and "explicit_defaults_for_timestamp" in self.__fields_set__:
            _dict['explicit_defaults_for_timestamp'] = None

        # set to None if group_concat_max_len (nullable) is None
        # and __fields_set__ contains the field
        if self.group_concat_max_len is None and "group_concat_max_len" in self.__fields_set__:
            _dict['group_concat_max_len'] = None

        # set to None if innodb_adaptive_hash_index (nullable) is None
        # and __fields_set__ contains the field
        if self.innodb_adaptive_hash_index is None and "innodb_adaptive_hash_index" in self.__fields_set__:
            _dict['innodb_adaptive_hash_index'] = None

        # set to None if innodb_lock_wait_timeout (nullable) is None
        # and __fields_set__ contains the field
        if self.innodb_lock_wait_timeout is None and "innodb_lock_wait_timeout" in self.__fields_set__:
            _dict['innodb_lock_wait_timeout'] = None

        # set to None if innodb_numa_interleave (nullable) is None
        # and __fields_set__ contains the field
        if self.innodb_numa_interleave is None and "innodb_numa_interleave" in self.__fields_set__:
            _dict['innodb_numa_interleave'] = None

        # set to None if net_read_timeout (nullable) is None
        # and __fields_set__ contains the field
        if self.net_read_timeout is None and "net_read_timeout" in self.__fields_set__:
            _dict['net_read_timeout'] = None

        # set to None if net_write_timeout (nullable) is None
        # and __fields_set__ contains the field
        if self.net_write_timeout is None and "net_write_timeout" in self.__fields_set__:
            _dict['net_write_timeout'] = None

        # set to None if regexp_time_limit (nullable) is None
        # and __fields_set__ contains the field
        if self.regexp_time_limit is None and "regexp_time_limit" in self.__fields_set__:
            _dict['regexp_time_limit'] = None

        # set to None if sync_binlog (nullable) is None
        # and __fields_set__ contains the field
        if self.sync_binlog is None and "sync_binlog" in self.__fields_set__:
            _dict['sync_binlog'] = None

        # set to None if table_definition_cache (nullable) is None
        # and __fields_set__ contains the field
        if self.table_definition_cache is None and "table_definition_cache" in self.__fields_set__:
            _dict['table_definition_cache'] = None

        # set to None if log_bin_trust_function_creators (nullable) is None
        # and __fields_set__ contains the field
        if self.log_bin_trust_function_creators is None and "log_bin_trust_function_creators" in self.__fields_set__:
            _dict['log_bin_trust_function_creators'] = None

        # set to None if skip_name_resolve (nullable) is None
        # and __fields_set__ contains the field
        if self.skip_name_resolve is None and "skip_name_resolve" in self.__fields_set__:
            _dict['skip_name_resolve'] = None

        # set to None if innodb_redo_log_capacity (nullable) is None
        # and __fields_set__ contains the field
        if self.innodb_redo_log_capacity is None and "innodb_redo_log_capacity" in self.__fields_set__:
            _dict['innodb_redo_log_capacity'] = None

        # set to None if wait_timeout (nullable) is None
        # and __fields_set__ contains the field
        if self.wait_timeout is None and "wait_timeout" in self.__fields_set__:
            _dict['wait_timeout'] = None

        # set to None if interactive_timeout (nullable) is None
        # and __fields_set__ contains the field
        if self.interactive_timeout is None and "interactive_timeout" in self.__fields_set__:
            _dict['interactive_timeout'] = None

        # set to None if default_time_zone (nullable) is None
        # and __fields_set__ contains the field
        if self.default_time_zone is None and "default_time_zone" in self.__fields_set__:
            _dict['default-time-zone'] = None

        # set to None if pxc_strict_mode (nullable) is None
        # and __fields_set__ contains the field
        if self.pxc_strict_mode is None and "pxc_strict_mode" in self.__fields_set__:
            _dict['pxc_strict_mode'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ConfigParametersMysql:
        """Create an instance of ConfigParametersMysql from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ConfigParametersMysql.parse_obj(obj)

        _obj = ConfigParametersMysql.parse_obj({
            "join_buffer_size": obj.get("join_buffer_size"),
            "max_connections": obj.get("max_connections"),
            "sort_buffer_size": obj.get("sort_buffer_size"),
            "thread_cache_size": obj.get("thread_cache_size"),
            "innodb_buffer_pool_size": obj.get("innodb_buffer_pool_size"),
            "auto_increment_increment": obj.get("auto_increment_increment"),
            "auto_increment_offset": obj.get("auto_increment_offset"),
            "innodb_io_capacity": obj.get("innodb_io_capacity"),
            "innodb_purge_threads": obj.get("innodb_purge_threads"),
            "innodb_read_io_threads": obj.get("innodb_read_io_threads"),
            "innodb_thread_concurrency": obj.get("innodb_thread_concurrency"),
            "innodb_write_io_threads": obj.get("innodb_write_io_threads"),
            "innodb_log_file_size": obj.get("innodb_log_file_size"),
            "max_allowed_packet": obj.get("max_allowed_packet"),
            "max_heap_table_size": obj.get("max_heap_table_size"),
            "sql_mode": obj.get("sql_mode"),
            "query_cache_type": obj.get("query_cache_type"),
            "query_cache_size": obj.get("query_cache_size"),
            "innodb_flush_log_at_trx_commit": obj.get("innodb_flush_log_at_trx_commit"),
            "transaction_isolation": obj.get("transaction_isolation"),
            "long_query_time": obj.get("long_query_time"),
            "tmp_table_size": obj.get("tmp_table_size"),
            "table_open_cache": obj.get("table_open_cache"),
            "table_open_cache_instances": obj.get("table_open_cache_instances"),
            "innodb_flush_method": obj.get("innodb_flush_method"),
            "innodb_strict_mode": obj.get("innodb_strict_mode"),
            "slow_query_log": obj.get("slow_query_log"),
            "binlog_cache_size": obj.get("binlog_cache_size"),
            "binlog_group_commit_sync_delay": obj.get("binlog_group_commit_sync_delay"),
            "binlog_row_image": obj.get("binlog_row_image"),
            "binlog_rows_query_log_events": obj.get("binlog_rows_query_log_events"),
            "character_set_server": obj.get("character_set_server"),
            "explicit_defaults_for_timestamp": obj.get("explicit_defaults_for_timestamp"),
            "group_concat_max_len": obj.get("group_concat_max_len"),
            "innodb_adaptive_hash_index": obj.get("innodb_adaptive_hash_index"),
            "innodb_lock_wait_timeout": obj.get("innodb_lock_wait_timeout"),
            "innodb_numa_interleave": obj.get("innodb_numa_interleave"),
            "net_read_timeout": obj.get("net_read_timeout"),
            "net_write_timeout": obj.get("net_write_timeout"),
            "regexp_time_limit": obj.get("regexp_time_limit"),
            "sync_binlog": obj.get("sync_binlog"),
            "table_definition_cache": obj.get("table_definition_cache"),
            "log_bin_trust_function_creators": obj.get("log_bin_trust_function_creators"),
            "skip_name_resolve": obj.get("skip_name_resolve"),
            "innodb_redo_log_capacity": obj.get("innodb_redo_log_capacity"),
            "wait_timeout": obj.get("wait_timeout"),
            "interactive_timeout": obj.get("interactive_timeout"),
            "default_time_zone": obj.get("default-time-zone"),
            "pxc_strict_mode": obj.get("pxc_strict_mode")
        })
        return _obj

