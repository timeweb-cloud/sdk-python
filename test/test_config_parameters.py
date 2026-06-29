# coding: utf-8

"""
    Timeweb Cloud API

    # Введение API Timeweb Cloud позволяет вам управлять ресурсами в облаке программным способом с использованием обычных HTTP-запросов.  Множество функций, которые доступны в панели управления Timeweb Cloud, также доступны через API, что позволяет вам автоматизировать ваши собственные сценарии.  В этой документации сперва будет описан общий дизайн и принципы работы API, а после этого конкретные конечные точки. Также будут приведены примеры запросов к ним.   ## Запросы Запросы должны выполняться по протоколу `HTTPS`, чтобы гарантировать шифрование транзакций. Поддерживаются следующие методы запроса: |Метод|Применение| |--- |--- | |GET|Извлекает данные о коллекциях и отдельных ресурсах.| |POST|Для коллекций создает новый ресурс этого типа. Также используется для выполнения действий с конкретным ресурсом.| |PUT|Обновляет существующий ресурс.| |PATCH|Некоторые ресурсы поддерживают частичное обновление, то есть обновление только части атрибутов ресурса, в этом случае вместо метода PUT будет использован PATCH.| |DELETE|Удаляет ресурс.|  Методы `POST`, `PUT` и `PATCH` могут включать объект в тело запроса с типом содержимого `application/json`.  ### Параметры в запросах Некоторые коллекции поддерживают пагинацию, поиск или сортировку в запросах. В параметрах запроса требуется передать: - `limit` — обозначает количество записей, которое необходимо вернуть  - `offset` — указывает на смещение, относительно начала списка  - `search` — позволяет указать набор символов для поиска  - `sort` — можно задать правило сортировки коллекции  ## Ответы Запросы вернут один из следующих кодов состояния ответа HTTP:  |Статус|Описание| |--- |--- | |200 OK|Действие с ресурсом было выполнено успешно.| |201 Created|Ресурс был успешно создан. При этом ресурс может быть как уже готовым к использованию, так и находиться в процессе запуска.| |204 No Content|Действие с ресурсом было выполнено успешно, и ответ не содержит дополнительной информации в теле.| |400 Bad Request|Был отправлен неверный запрос, например, в нем отсутствуют обязательные параметры и т. д. Тело ответа будет содержать дополнительную информацию об ошибке.| |401 Unauthorized|Ошибка аутентификации.| |403 Forbidden|Аутентификация прошла успешно, но недостаточно прав для выполнения действия.| |404 Not Found|Запрашиваемый ресурс не найден.| |409 Conflict|Запрос конфликтует с текущим состоянием.| |423 Locked|Ресурс из запроса заблокирован от применения к нему указанного метода.| |429 Too Many Requests|Был достигнут лимит по количеству запросов в единицу времени.| |500 Internal Server Error|При выполнении запроса произошла какая-то внутренняя ошибка. Чтобы решить эту проблему, лучше всего создать тикет в панели управления.|  ### Структура успешного ответа Все конечные точки будут возвращать данные в формате `JSON`. Ответы на `GET`-запросы будут иметь на верхнем уровне следующую структуру атрибутов:  |Название поля|Тип|Описание| |--- |--- |--- | |[entity_name]|object, object[], string[], number[], boolean|Динамическое поле, которое будет меняться в зависимости от запрашиваемого ресурса и будет содержать все атрибуты, необходимые для описания этого ресурса. Например, при запросе списка баз данных будет возвращаться поле `dbs`, а при запросе конкретного облачного сервера `server`. Для некоторых конечных точек в ответе может возвращаться сразу несколько ресурсов.| |meta|object|Опционально. Объект, который содержит вспомогательную информацию о ресурсе. Чаще всего будет встречаться при запросе коллекций и содержать поле `total`, которое будет указывать на количество элементов в коллекции.| |response_id|string|Опционально. В большинстве случаев в ответе будет содержаться ID ответа в формате UUIDv4, который однозначно указывает на ваш запрос внутри нашей системы. Если вам потребуется задать вопрос нашей поддержке, приложите к вопросу этот ID— так мы сможем найти ответ на него намного быстрее. Также вы можете использовать этот ID, чтобы убедиться, что это новый ответ на запрос и результат не был получен из кэша.|  Пример запроса на получение списка SSH-ключей: ```     HTTP/2.0 200 OK     {       \"ssh_keys\":[           {             \"body\":\"ssh-rsa AAAAB3NzaC1sdfghjkOAsBwWhs= example@device.local\",             \"created_at\":\"2021-09-15T19:52:27Z\",             \"expired_at\":null,             \"id\":5297,             \"is_default\":false,             \"name\":\"example@device.local\",             \"used_at\":null,             \"used_by\":[]           }       ],       \"meta\":{           \"total\":1       },       \"response_id\":\"94608d15-8672-4eed-8ab6-28bd6fa3cdf7\"     } ```  ### Структура ответа с ошибкой |Название поля|Тип|Описание| |--- |--- |--- | |status_code|number|Короткий числовой идентификатор ошибки.| |error_code|string|Короткий текстовый идентификатор ошибки, который уточняет числовой идентификатор и удобен для программной обработки. Самый простой пример — это код `not_found` для ошибки 404.| |message|string, string[]|Опционально. В большинстве случаев в ответе будет содержаться человекочитаемое подробное описание ошибки или ошибок, которые помогут понять, что нужно исправить.| |response_id|string|Опционально. В большинстве случае в ответе будет содержаться ID ответа в формате UUIDv4, который однозначно указывает на ваш запрос внутри нашей системы. Если вам потребуется задать вопрос нашей поддержке, приложите к вопросу этот ID — так мы сможем найти ответ на него намного быстрее.|  Пример: ```     HTTP/2.0 403 Forbidden     {       \"status_code\": 403,       \"error_code\":  \"forbidden\",       \"message\":     \"You do not have access for the attempted action\",       \"response_id\": \"94608d15-8672-4eed-8ab6-28bd6fa3cdf7\"     } ```  ## Статусы ресурсов Важно учесть, что при создании большинства ресурсов внутри платформы вам будет сразу возвращен ответ от сервера со статусом `200 OK` или `201 Created` и ID созданного ресурса в теле ответа, но при этом этот ресурс может быть ещё в *состоянии запуска*.  Для того чтобы понять, в каком состоянии сейчас находится ваш ресурс, мы добавили поле `status` в ответ на получение информации о ресурсе.  Список статусов будет отличаться в зависимости от типа ресурса. Увидеть поддерживаемый список статусов вы сможете в описании каждого конкретного ресурса.     ## Ограничение скорости запросов (Rate Limiting) Чтобы обеспечить стабильность для всех пользователей, Timeweb Cloud защищает API от всплесков входящего трафика, анализируя количество запросов c каждого аккаунта к каждой конечной точке.  Если ваше приложение отправляет более 20 запросов в секунду на одну конечную точку, то для этого запроса API может вернуть код состояния HTTP `429 Too Many Requests`.   ## Аутентификация Доступ к API осуществляется с помощью JWT-токена. Токенами можно управлять внутри панели управления Timeweb Cloud в разделе *API и Terraform*.  Токен необходимо передавать в заголовке каждого запроса в формате: ```   Authorization: Bearer $TIMEWEB_CLOUD_TOKEN ```  ## Формат примеров API Примеры в этой документации описаны с помощью `curl`, HTTP-клиента командной строки. На компьютерах `Linux` и `macOS` обычно по умолчанию установлен `curl`, и он доступен для загрузки на всех популярных платформах, включая `Windows`.  Каждый пример разделен на несколько строк символом `\\`, который совместим с `bash`. Типичный пример выглядит так: ```   curl -X PATCH      -H \"Content-Type: application/json\"      -H \"Authorization: Bearer $TIMEWEB_CLOUD_TOKEN\"      -d '{\"name\":\"Cute Corvus\",\"comment\":\"Development Server\"}'      \"https://api.timeweb.cloud/api/v1/dedicated/1051\" ``` - Параметр `-X` задает метод запроса. Для согласованности метод будет указан во всех примерах, даже если он явно не требуется для методов `GET`. - Строки `-H` задают требуемые HTTP-заголовки. - Примеры, для которых требуется объект JSON в теле запроса, передают требуемые данные через параметр `-d`.  Чтобы использовать приведенные примеры, не подставляя каждый раз в них свой токен, вы можете добавить токен один раз в переменные окружения в вашей консоли. Например, на `Linux` это можно сделать с помощью команды:  ``` TIMEWEB_CLOUD_TOKEN=\"token\" ```  После этого токен будет автоматически подставляться в ваши запросы.  Обратите внимание, что все значения в этой документации являются примерами. Не полагайтесь на IDы операционных систем, тарифов и т.д., используемые в примерах. Используйте соответствующую конечную точку для получения значений перед созданием ресурсов.   ## Версионирование API построено согласно принципам [семантического версионирования](https://semver.org/lang/ru). Это значит, что мы гарантируем обратную совместимость всех изменений в пределах одной мажорной версии.  Мажорная версия каждой конечной точки обозначается в пути запроса, например, запрос `/api/v1/servers` указывает, что этот метод имеет версию 1.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: info@timeweb.cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import timeweb_cloud_api
from timeweb_cloud_api.models.config_parameters import ConfigParameters  # noqa: E501
from timeweb_cloud_api.rest import ApiException

class TestConfigParameters(unittest.TestCase):
    """ConfigParameters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ConfigParameters
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConfigParameters`
        """
        model = timeweb_cloud_api.models.config_parameters.ConfigParameters()  # noqa: E501
        if include_optional :
            return ConfigParameters(
                mysql = timeweb_cloud_api.models.config_parameters_mysql.config_parameters_mysql(
                    join_buffer_size = 4194304, 
                    max_connections = 200, 
                    sort_buffer_size = 2097152, 
                    thread_cache_size = 8, 
                    innodb_buffer_pool_size = 864026624, 
                    auto_increment_increment = 3, 
                    auto_increment_offset = 3, 
                    innodb_io_capacity = 1500, 
                    innodb_purge_threads = 4, 
                    innodb_read_io_threads = 4, 
                    innodb_thread_concurrency = 0, 
                    innodb_write_io_threads = 4, 
                    innodb_log_file_size = 432013312, 
                    max_allowed_packet = 16777216, 
                    max_heap_table_size = 16777216, 
                    sql_mode = , 
                    query_cache_type = 2, 
                    query_cache_size = 1, 
                    innodb_flush_log_at_trx_commit = 1, 
                    transaction_isolation = read-uncommitted, 
                    long_query_time = 10, 
                    tmp_table_size = 16777216, 
                    table_open_cache = 4970, 
                    table_open_cache_instances = 16, 
                    innodb_flush_method = O_DSYNC, 
                    innodb_strict_mode = ON, 
                    slow_query_log = ON, 
                    binlog_cache_size = 32768, 
                    binlog_group_commit_sync_delay = 1, 
                    binlog_row_image = full, 
                    binlog_rows_query_log_events = OFF, 
                    character_set_server = utf8, 
                    explicit_defaults_for_timestamp = ON, 
                    group_concat_max_len = 1024, 
                    innodb_adaptive_hash_index = ON, 
                    innodb_lock_wait_timeout = 50, 
                    innodb_numa_interleave = OFF, 
                    net_read_timeout = 30, 
                    net_write_timeout = 1, 
                    regexp_time_limit = 32, 
                    sync_binlog = 1, 
                    table_definition_cache = 2000, 
                    log_bin_trust_function_creators = ON, 
                    skip_name_resolve = OFF, 
                    innodb_redo_log_capacity = 104857600, 
                    wait_timeout = 28800, 
                    interactive_timeout = 28800, 
                    default_time_zone = +00:00, 
                    pxc_strict_mode = ENFORCING, ), 
                postgres = timeweb_cloud_api.models.config_parameters_postgres.config_parameters_postgres(
                    max_connections = 200, 
                    autovacuum_analyze_scale_factor = 0.1, 
                    autovacuum_max_workers = 3, 
                    autovacuum_naptime = 120, 
                    autovacuum_vacuum_insert_scale_factor = 0.2, 
                    autovacuum_vacuum_scale_factor = 0.2, 
                    autovacuum_work_mem = -1, 
                    bgwriter_delay = 200, 
                    bgwriter_lru_maxpages = 100, 
                    deadlock_timeout = 1000, 
                    gin_pending_list_limit = 4096, 
                    idle_in_transaction_session_timeout = 0, 
                    join_collapse_limit = 8, 
                    lock_timeout = 0, 
                    max_prepared_transactions = 0, 
                    shared_buffers = 65536, 
                    log_min_duration_statement = -1, 
                    wal_buffers = 2048, 
                    temp_buffers = 1024, 
                    work_mem = 4096, 
                    default_transaction_isolation = read committed, 
                    effective_cache_size = 131072, 
                    max_wal_size = 1024, 
                    min_wal_size = 80, 
                    wal_level = replica, 
                    max_replication_slots = 10, 
                    max_wal_senders = 10, 
                    max_worker_processes = 8, 
                    max_logical_replication_workers = 4, 
                    max_parallel_maintenance_workers = 2, 
                    max_parallel_workers = 8, 
                    max_parallel_workers_per_gather = 2, 
                    array_nulls = ON, 
                    backend_flush_after = 0, 
                    backslash_quote = safe_encoding, 
                    bgwriter_flush_after = 64, 
                    bgwriter_lru_multiplier = 2, 
                    default_transaction_read_only = OFF, 
                    enable_hashagg = ON, 
                    enable_hashjoin = ON, 
                    enable_incremental_sort = ON, 
                    enable_indexscan = ON, 
                    enable_indexonlyscan = ON, 
                    enable_material = ON, 
                    enable_memoize = ON, 
                    enable_mergejoin = ON, 
                    enable_parallel_append = ON, 
                    enable_parallel_hash = ON, 
                    enable_partition_pruning = ON, 
                    enable_partitionwise_join = OFF, 
                    enable_partitionwise_aggregate = OFF, 
                    enable_seqscan = ON, 
                    enable_sort = ON, 
                    enable_tidscan = ON, 
                    exit_on_error = OFF, 
                    from_collapse_limit = 8, 
                    jit = ON, 
                    plan_cache_mode = auto, 
                    quote_all_identifiers = OFF, 
                    standard_conforming_strings = ON, 
                    statement_timeout = 0, 
                    timezone = +00:00, 
                    transform_null_equals = OFF, 
                    max_locks_per_transaction = 64, 
                    autovacuum_vacuum_cost_limit = 200, 
                    checkpoint_timeout = 300, 
                    checkpoint_completion_target = 0.5, 
                    wal_compression = off, 
                    random_page_cost = 4, 
                    effective_io_concurrency = 1, 
                    log_lock_waits = OFF, 
                    log_temp_files = -1, 
                    track_io_timing = OFF, 
                    maintenance_work_mem = 262144, 
                    idle_session_timeout = 900000, 
                    io_method = worker, 
                    io_workers = 3, )
            )
        else :
            return ConfigParameters(
        )
        """

    def testConfigParameters(self):
        """Test ConfigParameters"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
