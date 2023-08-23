# coding: utf-8

"""
    Timeweb Cloud API

    # Введение API Timeweb Cloud позволяет вам управлять ресурсами в облаке программным способом с использованием обычных HTTP-запросов.  Множество функций, которые доступны в панели управления Timeweb Cloud, также доступны через API, что позволяет вам автоматизировать ваши собственные сценарии.  В этой документации сперва будет описан общий дизайн и принципы работы API, а после этого конкретные конечные точки. Также будут приведены примеры запросов к ним.   ## Запросы Запросы должны выполняться по протоколу `HTTPS`, чтобы гарантировать шифрование транзакций. Поддерживаются следующие методы запроса: |Метод|Применение| |--- |--- | |GET|Извлекает данные о коллекциях и отдельных ресурсах.| |POST|Для коллекций создает новый ресурс этого типа. Также используется для выполнения действий с конкретным ресурсом.| |PUT|Обновляет существующий ресурс.| |PATCH|Некоторые ресурсы поддерживают частичное обновление, то есть обновление только части атрибутов ресурса, в этом случае вместо метода PUT будет использован PATCH.| |DELETE|Удаляет ресурс.|  Методы `POST`, `PUT` и `PATCH` могут включать объект в тело запроса с типом содержимого `application/json`.  ### Параметры в запросах Некоторые коллекции поддерживают пагинацию, поиск или сортировку в запросах. В параметрах запроса требуется передать: - `limit` — обозначает количество записей, которое необходимо вернуть  - `offset` — указывает на смещение, относительно начала списка  - `search` — позволяет указать набор символов для поиска  - `sort` — можно задать правило сортировки коллекции  ## Ответы Запросы вернут один из следующих кодов состояния ответа HTTP:  |Статус|Описание| |--- |--- | |200 OK|Действие с ресурсом было выполнено успешно.| |201 Created|Ресурс был успешно создан. При этом ресурс может быть как уже готовым к использованию, так и находиться в процессе запуска.| |204 No Content|Действие с ресурсом было выполнено успешно, и ответ не содержит дополнительной информации в теле.| |400 Bad Request|Был отправлен неверный запрос, например, в нем отсутствуют обязательные параметры и т. д. Тело ответа будет содержать дополнительную информацию об ошибке.| |401 Unauthorized|Ошибка аутентификации.| |403 Forbidden|Аутентификация прошла успешно, но недостаточно прав для выполнения действия.| |404 Not Found|Запрашиваемый ресурс не найден.| |409 Conflict|Запрос конфликтует с текущим состоянием.| |423 Locked|Ресурс из запроса заблокирован от применения к нему указанного метода.| |429 Too Many Requests|Был достигнут лимит по количеству запросов в единицу времени.| |500 Internal Server Error|При выполнении запроса произошла какая-то внутренняя ошибка. Чтобы решить эту проблему, лучше всего создать тикет в панели управления.|  ### Структура успешного ответа Все конечные точки будут возвращать данные в формате `JSON`. Ответы на `GET`-запросы будут иметь на верхнем уровне следующую структуру атрибутов:  |Название поля|Тип|Описание| |--- |--- |--- | |[entity_name]|object, object[], string[], number[], boolean|Динамическое поле, которое будет меняться в зависимости от запрашиваемого ресурса и будет содержать все атрибуты, необходимые для описания этого ресурса. Например, при запросе списка баз данных будет возвращаться поле `dbs`, а при запросе конкретного облачного сервера `server`. Для некоторых конечных точек в ответе может возвращаться сразу несколько ресурсов.| |meta|object|Опционально. Объект, который содержит вспомогательную информацию о ресурсе. Чаще всего будет встречаться при запросе коллекций и содержать поле `total`, которое будет указывать на количество элементов в коллекции.| |response_id|string|Опционально. В большинстве случаев в ответе будет содержаться уникальный идентификатор ответа в формате UUIDv4, который однозначно указывает на ваш запрос внутри нашей системы. Если вам потребуется задать вопрос нашей поддержке, приложите к вопросу этот идентификатор — так мы сможем найти ответ на него намного быстрее. Также вы можете использовать этот идентификатор, чтобы убедиться, что это новый ответ на запрос и результат не был получен из кэша.|  Пример запроса на получение списка SSH-ключей: ```     HTTP/2.0 200 OK     {       \"ssh_keys\":[           {             \"body\":\"ssh-rsa AAAAB3NzaC1sdfghjkOAsBwWhs= example@device.local\",             \"created_at\":\"2021-09-15T19:52:27Z\",             \"expired_at\":null,             \"id\":5297,             \"is_default\":false,             \"name\":\"example@device.local\",             \"used_at\":null,             \"used_by\":[]           }       ],       \"meta\":{           \"total\":1       },       \"response_id\":\"94608d15-8672-4eed-8ab6-28bd6fa3cdf7\"     } ```  ### Структура ответа с ошибкой |Название поля|Тип|Описание| |--- |--- |--- | |status_code|number|Короткий числовой идентификатор ошибки.| |error_code|string|Короткий текстовый идентификатор ошибки, который уточняет числовой идентификатор и удобен для программной обработки. Самый простой пример — это код `not_found` для ошибки 404.| |message|string, string[]|Опционально. В большинстве случаев в ответе будет содержаться человекочитаемое подробное описание ошибки или ошибок, которые помогут понять, что нужно исправить.| |response_id|string|Опционально. В большинстве случае в ответе будет содержаться уникальный идентификатор ответа в формате UUIDv4, который однозначно указывает на ваш запрос внутри нашей системы. Если вам потребуется задать вопрос нашей поддержке, приложите к вопросу этот идентификатор — так мы сможем найти ответ на него намного быстрее.|  Пример: ```     HTTP/2.0 403 Forbidden     {       \"status_code\": 403,       \"error_code\":  \"forbidden\",       \"message\":     \"You do not have access for the attempted action\",       \"response_id\": \"94608d15-8672-4eed-8ab6-28bd6fa3cdf7\"     } ```  ## Статусы ресурсов Важно учесть, что при создании большинства ресурсов внутри платформы вам будет сразу возвращен ответ от сервера со статусом `200 OK` или `201 Created` и идентификатором созданного ресурса в теле ответа, но при этом этот ресурс может быть ещё в *состоянии запуска*.  Для того чтобы понять, в каком состоянии сейчас находится ваш ресурс, мы добавили поле `status` в ответ на получение информации о ресурсе.  Список статусов будет отличаться в зависимости от типа ресурса. Увидеть поддерживаемый список статусов вы сможете в описании каждого конкретного ресурса.     ## Ограничение скорости запросов (Rate Limiting) Чтобы обеспечить стабильность для всех пользователей, Timeweb Cloud защищает API от всплесков входящего трафика, анализируя количество запросов c каждого аккаунта к каждой конечной точке.  Если ваше приложение отправляет более 20 запросов в секунду на одну конечную точку, то для этого запроса API может вернуть код состояния HTTP `429 Too Many Requests`.   ## Аутентификация Доступ к API осуществляется с помощью JWT-токена. Токенами можно управлять внутри панели управления Timeweb Cloud в разделе *API и Terraform*.  Токен необходимо передавать в заголовке каждого запроса в формате: ```   Authorization: Bearer $TIMEWEB_CLOUD_TOKEN ```  ## Формат примеров API Примеры в этой документации описаны с помощью `curl`, HTTP-клиента командной строки. На компьютерах `Linux` и `macOS` обычно по умолчанию установлен `curl`, и он доступен для загрузки на всех популярных платформах, включая `Windows`.  Каждый пример разделен на несколько строк символом `\\`, который совместим с `bash`. Типичный пример выглядит так: ```   curl -X PATCH      -H \"Content-Type: application/json\"      -H \"Authorization: Bearer $TIMEWEB_CLOUD_TOKEN\"      -d '{\"name\":\"Cute Corvus\",\"comment\":\"Development Server\"}'      \"https://api.timeweb.cloud/api/v1/dedicated/1051\" ``` - Параметр `-X` задает метод запроса. Для согласованности метод будет указан во всех примерах, даже если он явно не требуется для методов `GET`. - Строки `-H` задают требуемые HTTP-заголовки. - Примеры, для которых требуется объект JSON в теле запроса, передают требуемые данные через параметр `-d`.  Чтобы использовать приведенные примеры, не подставляя каждый раз в них свой токен, вы можете добавить токен один раз в переменные окружения в вашей консоли. Например, на `Linux` это можно сделать с помощью команды:  ``` TIMEWEB_CLOUD_TOKEN=\"token\" ```  После этого токен будет автоматически подставляться в ваши запросы.  Обратите внимание, что все значения в этой документации являются примерами. Не полагайтесь на идентификаторы операционных систем, тарифов и т.д., используемые в примерах. Используйте соответствующую конечную точку для получения значений перед созданием ресурсов.   ## Версионирование API построено согласно принципам [семантического версионирования](https://semver.org/lang/ru). Это значит, что мы гарантируем обратную совместимость всех изменений в пределах одной мажорной версии.  Мажорная версия каждой конечной точки обозначается в пути запроса, например, запрос `/api/v1/servers` указывает, что этот метод имеет версию 1.  # noqa: E501

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

class ConfigParameters(BaseModel):
    """
    ConfigParameters
    """
    auto_increment_increment: Optional[Any] = Field(None, description="Интервал между значениями столбцов с атрибутом `AUTO_INCREMENT` (`mysql5` | `mysql`).")
    auto_increment_offset: Optional[Any] = Field(None, description="Начальное значение для столбцов с атрибутом `AUTO_INCREMENT` (`mysql5` | `mysql`).")
    innodb_io_capacity: Optional[Any] = Field(None, description="Количество операций ввода-вывода в секунду `IOPS` (`mysql5` | `mysql`).")
    innodb_purge_threads: Optional[Any] = Field(None, description="Количество потоков ввода-вывода, используемых для операций очистки (`mysql5` | `mysql`).")
    innodb_read_io_threads: Optional[Any] = Field(None, description="Количество потоков ввода-вывода, используемых для операций чтения (`mysql5` | `mysql`).")
    innodb_thread_concurrency: Optional[Any] = Field(None, description="Максимальное число потоков, которые могут исполняться (`mysql5` | `mysql`).")
    innodb_write_io_threads: Optional[Any] = Field(None, description="Количество потоков ввода-вывода, используемых для операций записи (`mysql5` | `mysql`).")
    join_buffer_size: Optional[Any] = Field(None, description="Минимальный размер буфера (`mysql5` | `mysql`).")
    max_allowed_packet: Optional[Any] = Field(None, description="Максимальный размер одного пакета, строки или параметра, отправляемого функцией `mysql_stmt_send_long_data()` (`mysql5` | `mysql`).")
    max_heap_table_size: Optional[Any] = Field(None, description="Максимальный размер пользовательских MEMORY-таблиц (`mysql5` | `mysql`).")
    autovacuum_analyze_scale_factor: Optional[Any] = Field(None, description="Доля измененных или удаленных записей в таблице, при которой процесс автоочистки выполнит команду `ANALYZE` (`postgres`).")
    bgwriter_delay: Optional[Any] = Field(None, description="Задержка между запусками процесса фоновой записи (`postgres`).")
    bgwriter_lru_maxpages: Optional[Any] = Field(None, description="Максимальное число элементов буферного кеша (`postgres`).")
    deadlock_timeout: Optional[Any] = Field(None, description="Время ожидания, по истечении которого будет выполняться проверка состояния перекрестной блокировки (`postgres`).")
    gin_pending_list_limit: Optional[Any] = Field(None, description="Максимальный размер очереди записей индекса `GIN` (`postgres`).")
    idle_in_transaction_session_timeout: Optional[Any] = Field(None, description="Время простоя открытой транзакции, при превышении которого будет завершена сессия с этой транзакцией (`postgres`).")
    idle_session_timeout: Optional[Any] = Field(None, description="Время простоя не открытой транзакции, при превышении которого будет завершена сессия с этой транзакцией (`postgres`).")
    join_collapse_limit: Optional[Any] = Field(None, description="Значение количества элементов в списке `FROM` при превышении которого, планировщик будет переносить в список явные инструкции `JOIN` (`postgres`).")
    lock_timeout: Optional[Any] = Field(None, description="Время ожидания освобождения блокировки (`postgres`).")
    max_prepared_transactions: Optional[Any] = Field(None, description="Максимальное число транзакций, которые могут одновременно находиться в подготовленном состоянии (`postgres`).")
    max_connections: Optional[Any] = Field(None, description="Допустимое количество соединений (`postgres` | `mysql`).")
    shared_buffers: Optional[Any] = Field(None, description="Устанавливает количество буферов общей памяти, используемых сервером (`postgres`).")
    wal_buffers: Optional[Any] = Field(None, description="Устанавливает количество буферов дисковых страниц в общей памяти для WAL (`postgres`).")
    temp_buffers: Optional[Any] = Field(None, description="Устанавливает максимальное количество временных буферов, используемых каждой сессией (`postgres`).")
    work_mem: Optional[Any] = Field(None, description="Устанавливает максимальное количество памяти, используемое для рабочих пространств запросов (`postgres`).")
    sql_mode: Optional[Any] = Field(None, description="Устанавливает режим SQL. Можно задать несколько режимов, разделяя их запятой. (`mysql`).")
    query_cache_type: Optional[Any] = Field(None, description="Параметр включает или отключает работу MySQL Query Cache (`mysql`).")
    query_cache_size: Optional[Any] = Field(None, description="Размер в байтах, доступный для кэша запросов (`mysql`).")
    __properties = ["auto_increment_increment", "auto_increment_offset", "innodb_io_capacity", "innodb_purge_threads", "innodb_read_io_threads", "innodb_thread_concurrency", "innodb_write_io_threads", "join_buffer_size", "max_allowed_packet", "max_heap_table_size", "autovacuum_analyze_scale_factor", "bgwriter_delay", "bgwriter_lru_maxpages", "deadlock_timeout", "gin_pending_list_limit", "idle_in_transaction_session_timeout", "idle_session_timeout", "join_collapse_limit", "lock_timeout", "max_prepared_transactions", "max_connections", "shared_buffers", "wal_buffers", "temp_buffers", "work_mem", "sql_mode", "query_cache_type", "query_cache_size"]

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
    def from_json(cls, json_str: str) -> ConfigParameters:
        """Create an instance of ConfigParameters from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
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

        # set to None if join_buffer_size (nullable) is None
        # and __fields_set__ contains the field
        if self.join_buffer_size is None and "join_buffer_size" in self.__fields_set__:
            _dict['join_buffer_size'] = None

        # set to None if max_allowed_packet (nullable) is None
        # and __fields_set__ contains the field
        if self.max_allowed_packet is None and "max_allowed_packet" in self.__fields_set__:
            _dict['max_allowed_packet'] = None

        # set to None if max_heap_table_size (nullable) is None
        # and __fields_set__ contains the field
        if self.max_heap_table_size is None and "max_heap_table_size" in self.__fields_set__:
            _dict['max_heap_table_size'] = None

        # set to None if autovacuum_analyze_scale_factor (nullable) is None
        # and __fields_set__ contains the field
        if self.autovacuum_analyze_scale_factor is None and "autovacuum_analyze_scale_factor" in self.__fields_set__:
            _dict['autovacuum_analyze_scale_factor'] = None

        # set to None if bgwriter_delay (nullable) is None
        # and __fields_set__ contains the field
        if self.bgwriter_delay is None and "bgwriter_delay" in self.__fields_set__:
            _dict['bgwriter_delay'] = None

        # set to None if bgwriter_lru_maxpages (nullable) is None
        # and __fields_set__ contains the field
        if self.bgwriter_lru_maxpages is None and "bgwriter_lru_maxpages" in self.__fields_set__:
            _dict['bgwriter_lru_maxpages'] = None

        # set to None if deadlock_timeout (nullable) is None
        # and __fields_set__ contains the field
        if self.deadlock_timeout is None and "deadlock_timeout" in self.__fields_set__:
            _dict['deadlock_timeout'] = None

        # set to None if gin_pending_list_limit (nullable) is None
        # and __fields_set__ contains the field
        if self.gin_pending_list_limit is None and "gin_pending_list_limit" in self.__fields_set__:
            _dict['gin_pending_list_limit'] = None

        # set to None if idle_in_transaction_session_timeout (nullable) is None
        # and __fields_set__ contains the field
        if self.idle_in_transaction_session_timeout is None and "idle_in_transaction_session_timeout" in self.__fields_set__:
            _dict['idle_in_transaction_session_timeout'] = None

        # set to None if idle_session_timeout (nullable) is None
        # and __fields_set__ contains the field
        if self.idle_session_timeout is None and "idle_session_timeout" in self.__fields_set__:
            _dict['idle_session_timeout'] = None

        # set to None if join_collapse_limit (nullable) is None
        # and __fields_set__ contains the field
        if self.join_collapse_limit is None and "join_collapse_limit" in self.__fields_set__:
            _dict['join_collapse_limit'] = None

        # set to None if lock_timeout (nullable) is None
        # and __fields_set__ contains the field
        if self.lock_timeout is None and "lock_timeout" in self.__fields_set__:
            _dict['lock_timeout'] = None

        # set to None if max_prepared_transactions (nullable) is None
        # and __fields_set__ contains the field
        if self.max_prepared_transactions is None and "max_prepared_transactions" in self.__fields_set__:
            _dict['max_prepared_transactions'] = None

        # set to None if max_connections (nullable) is None
        # and __fields_set__ contains the field
        if self.max_connections is None and "max_connections" in self.__fields_set__:
            _dict['max_connections'] = None

        # set to None if shared_buffers (nullable) is None
        # and __fields_set__ contains the field
        if self.shared_buffers is None and "shared_buffers" in self.__fields_set__:
            _dict['shared_buffers'] = None

        # set to None if wal_buffers (nullable) is None
        # and __fields_set__ contains the field
        if self.wal_buffers is None and "wal_buffers" in self.__fields_set__:
            _dict['wal_buffers'] = None

        # set to None if temp_buffers (nullable) is None
        # and __fields_set__ contains the field
        if self.temp_buffers is None and "temp_buffers" in self.__fields_set__:
            _dict['temp_buffers'] = None

        # set to None if work_mem (nullable) is None
        # and __fields_set__ contains the field
        if self.work_mem is None and "work_mem" in self.__fields_set__:
            _dict['work_mem'] = None

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

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ConfigParameters:
        """Create an instance of ConfigParameters from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ConfigParameters.parse_obj(obj)

        _obj = ConfigParameters.parse_obj({
            "auto_increment_increment": obj.get("auto_increment_increment"),
            "auto_increment_offset": obj.get("auto_increment_offset"),
            "innodb_io_capacity": obj.get("innodb_io_capacity"),
            "innodb_purge_threads": obj.get("innodb_purge_threads"),
            "innodb_read_io_threads": obj.get("innodb_read_io_threads"),
            "innodb_thread_concurrency": obj.get("innodb_thread_concurrency"),
            "innodb_write_io_threads": obj.get("innodb_write_io_threads"),
            "join_buffer_size": obj.get("join_buffer_size"),
            "max_allowed_packet": obj.get("max_allowed_packet"),
            "max_heap_table_size": obj.get("max_heap_table_size"),
            "autovacuum_analyze_scale_factor": obj.get("autovacuum_analyze_scale_factor"),
            "bgwriter_delay": obj.get("bgwriter_delay"),
            "bgwriter_lru_maxpages": obj.get("bgwriter_lru_maxpages"),
            "deadlock_timeout": obj.get("deadlock_timeout"),
            "gin_pending_list_limit": obj.get("gin_pending_list_limit"),
            "idle_in_transaction_session_timeout": obj.get("idle_in_transaction_session_timeout"),
            "idle_session_timeout": obj.get("idle_session_timeout"),
            "join_collapse_limit": obj.get("join_collapse_limit"),
            "lock_timeout": obj.get("lock_timeout"),
            "max_prepared_transactions": obj.get("max_prepared_transactions"),
            "max_connections": obj.get("max_connections"),
            "shared_buffers": obj.get("shared_buffers"),
            "wal_buffers": obj.get("wal_buffers"),
            "temp_buffers": obj.get("temp_buffers"),
            "work_mem": obj.get("work_mem"),
            "sql_mode": obj.get("sql_mode"),
            "query_cache_type": obj.get("query_cache_type"),
            "query_cache_size": obj.get("query_cache_size")
        })
        return _obj

