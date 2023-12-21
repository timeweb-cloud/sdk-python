# coding: utf-8

"""
    Timeweb Cloud API

    # Введение API Timeweb Cloud позволяет вам управлять ресурсами в облаке программным способом с использованием обычных HTTP-запросов.  Множество функций, которые доступны в панели управления Timeweb Cloud, также доступны через API, что позволяет вам автоматизировать ваши собственные сценарии.  В этой документации сперва будет описан общий дизайн и принципы работы API, а после этого конкретные конечные точки. Также будут приведены примеры запросов к ним.   ## Запросы Запросы должны выполняться по протоколу `HTTPS`, чтобы гарантировать шифрование транзакций. Поддерживаются следующие методы запроса: |Метод|Применение| |--- |--- | |GET|Извлекает данные о коллекциях и отдельных ресурсах.| |POST|Для коллекций создает новый ресурс этого типа. Также используется для выполнения действий с конкретным ресурсом.| |PUT|Обновляет существующий ресурс.| |PATCH|Некоторые ресурсы поддерживают частичное обновление, то есть обновление только части атрибутов ресурса, в этом случае вместо метода PUT будет использован PATCH.| |DELETE|Удаляет ресурс.|  Методы `POST`, `PUT` и `PATCH` могут включать объект в тело запроса с типом содержимого `application/json`.  ### Параметры в запросах Некоторые коллекции поддерживают пагинацию, поиск или сортировку в запросах. В параметрах запроса требуется передать: - `limit` — обозначает количество записей, которое необходимо вернуть  - `offset` — указывает на смещение, относительно начала списка  - `search` — позволяет указать набор символов для поиска  - `sort` — можно задать правило сортировки коллекции  ## Ответы Запросы вернут один из следующих кодов состояния ответа HTTP:  |Статус|Описание| |--- |--- | |200 OK|Действие с ресурсом было выполнено успешно.| |201 Created|Ресурс был успешно создан. При этом ресурс может быть как уже готовым к использованию, так и находиться в процессе запуска.| |204 No Content|Действие с ресурсом было выполнено успешно, и ответ не содержит дополнительной информации в теле.| |400 Bad Request|Был отправлен неверный запрос, например, в нем отсутствуют обязательные параметры и т. д. Тело ответа будет содержать дополнительную информацию об ошибке.| |401 Unauthorized|Ошибка аутентификации.| |403 Forbidden|Аутентификация прошла успешно, но недостаточно прав для выполнения действия.| |404 Not Found|Запрашиваемый ресурс не найден.| |409 Conflict|Запрос конфликтует с текущим состоянием.| |423 Locked|Ресурс из запроса заблокирован от применения к нему указанного метода.| |429 Too Many Requests|Был достигнут лимит по количеству запросов в единицу времени.| |500 Internal Server Error|При выполнении запроса произошла какая-то внутренняя ошибка. Чтобы решить эту проблему, лучше всего создать тикет в панели управления.|  ### Структура успешного ответа Все конечные точки будут возвращать данные в формате `JSON`. Ответы на `GET`-запросы будут иметь на верхнем уровне следующую структуру атрибутов:  |Название поля|Тип|Описание| |--- |--- |--- | |[entity_name]|object, object[], string[], number[], boolean|Динамическое поле, которое будет меняться в зависимости от запрашиваемого ресурса и будет содержать все атрибуты, необходимые для описания этого ресурса. Например, при запросе списка баз данных будет возвращаться поле `dbs`, а при запросе конкретного облачного сервера `server`. Для некоторых конечных точек в ответе может возвращаться сразу несколько ресурсов.| |meta|object|Опционально. Объект, который содержит вспомогательную информацию о ресурсе. Чаще всего будет встречаться при запросе коллекций и содержать поле `total`, которое будет указывать на количество элементов в коллекции.| |response_id|string|Опционально. В большинстве случаев в ответе будет содержаться уникальный идентификатор ответа в формате UUIDv4, который однозначно указывает на ваш запрос внутри нашей системы. Если вам потребуется задать вопрос нашей поддержке, приложите к вопросу этот идентификатор — так мы сможем найти ответ на него намного быстрее. Также вы можете использовать этот идентификатор, чтобы убедиться, что это новый ответ на запрос и результат не был получен из кэша.|  Пример запроса на получение списка SSH-ключей: ```     HTTP/2.0 200 OK     {       \"ssh_keys\":[           {             \"body\":\"ssh-rsa AAAAB3NzaC1sdfghjkOAsBwWhs= example@device.local\",             \"created_at\":\"2021-09-15T19:52:27Z\",             \"expired_at\":null,             \"id\":5297,             \"is_default\":false,             \"name\":\"example@device.local\",             \"used_at\":null,             \"used_by\":[]           }       ],       \"meta\":{           \"total\":1       },       \"response_id\":\"94608d15-8672-4eed-8ab6-28bd6fa3cdf7\"     } ```  ### Структура ответа с ошибкой |Название поля|Тип|Описание| |--- |--- |--- | |status_code|number|Короткий числовой идентификатор ошибки.| |error_code|string|Короткий текстовый идентификатор ошибки, который уточняет числовой идентификатор и удобен для программной обработки. Самый простой пример — это код `not_found` для ошибки 404.| |message|string, string[]|Опционально. В большинстве случаев в ответе будет содержаться человекочитаемое подробное описание ошибки или ошибок, которые помогут понять, что нужно исправить.| |response_id|string|Опционально. В большинстве случае в ответе будет содержаться уникальный идентификатор ответа в формате UUIDv4, который однозначно указывает на ваш запрос внутри нашей системы. Если вам потребуется задать вопрос нашей поддержке, приложите к вопросу этот идентификатор — так мы сможем найти ответ на него намного быстрее.|  Пример: ```     HTTP/2.0 403 Forbidden     {       \"status_code\": 403,       \"error_code\":  \"forbidden\",       \"message\":     \"You do not have access for the attempted action\",       \"response_id\": \"94608d15-8672-4eed-8ab6-28bd6fa3cdf7\"     } ```  ## Статусы ресурсов Важно учесть, что при создании большинства ресурсов внутри платформы вам будет сразу возвращен ответ от сервера со статусом `200 OK` или `201 Created` и идентификатором созданного ресурса в теле ответа, но при этом этот ресурс может быть ещё в *состоянии запуска*.  Для того чтобы понять, в каком состоянии сейчас находится ваш ресурс, мы добавили поле `status` в ответ на получение информации о ресурсе.  Список статусов будет отличаться в зависимости от типа ресурса. Увидеть поддерживаемый список статусов вы сможете в описании каждого конкретного ресурса.     ## Ограничение скорости запросов (Rate Limiting) Чтобы обеспечить стабильность для всех пользователей, Timeweb Cloud защищает API от всплесков входящего трафика, анализируя количество запросов c каждого аккаунта к каждой конечной точке.  Если ваше приложение отправляет более 20 запросов в секунду на одну конечную точку, то для этого запроса API может вернуть код состояния HTTP `429 Too Many Requests`.   ## Аутентификация Доступ к API осуществляется с помощью JWT-токена. Токенами можно управлять внутри панели управления Timeweb Cloud в разделе *API и Terraform*.  Токен необходимо передавать в заголовке каждого запроса в формате: ```   Authorization: Bearer $TIMEWEB_CLOUD_TOKEN ```  ## Формат примеров API Примеры в этой документации описаны с помощью `curl`, HTTP-клиента командной строки. На компьютерах `Linux` и `macOS` обычно по умолчанию установлен `curl`, и он доступен для загрузки на всех популярных платформах, включая `Windows`.  Каждый пример разделен на несколько строк символом `\\`, который совместим с `bash`. Типичный пример выглядит так: ```   curl -X PATCH      -H \"Content-Type: application/json\"      -H \"Authorization: Bearer $TIMEWEB_CLOUD_TOKEN\"      -d '{\"name\":\"Cute Corvus\",\"comment\":\"Development Server\"}'      \"https://api.timeweb.cloud/api/v1/dedicated/1051\" ``` - Параметр `-X` задает метод запроса. Для согласованности метод будет указан во всех примерах, даже если он явно не требуется для методов `GET`. - Строки `-H` задают требуемые HTTP-заголовки. - Примеры, для которых требуется объект JSON в теле запроса, передают требуемые данные через параметр `-d`.  Чтобы использовать приведенные примеры, не подставляя каждый раз в них свой токен, вы можете добавить токен один раз в переменные окружения в вашей консоли. Например, на `Linux` это можно сделать с помощью команды:  ``` TIMEWEB_CLOUD_TOKEN=\"token\" ```  После этого токен будет автоматически подставляться в ваши запросы.  Обратите внимание, что все значения в этой документации являются примерами. Не полагайтесь на идентификаторы операционных систем, тарифов и т.д., используемые в примерах. Используйте соответствующую конечную точку для получения значений перед созданием ресурсов.   ## Версионирование API построено согласно принципам [семантического версионирования](https://semver.org/lang/ru). Это значит, что мы гарантируем обратную совместимость всех изменений в пределах одной мажорной версии.  Мажорная версия каждой конечной точки обозначается в пути запроса, например, запрос `/api/v1/servers` указывает, что этот метод имеет версию 1.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: info@timeweb.cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import timeweb_cloud_api
from timeweb_cloud_api.models.create_database201_response import CreateDatabase201Response  # noqa: E501
from timeweb_cloud_api.rest import ApiException

class TestCreateDatabase201Response(unittest.TestCase):
    """CreateDatabase201Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateDatabase201Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateDatabase201Response`
        """
        model = timeweb_cloud_api.models.create_database201_response.CreateDatabase201Response()  # noqa: E501
        if include_optional :
            return CreateDatabase201Response(
                db = timeweb_cloud_api.models.db.db(
                    id = 1, 
                    created_at = 2021-02-25T11:04:15Z, 
                    account_id = cp78562, 
                    login = test_user, 
                    location = ru-1, 
                    password = password, 
                    name = default_db, 
                    host = test.ru, 
                    type = mysql, 
                    hash_type = caching_sha2, 
                    port = 3000, 
                    ip = 127.0.0.1, 
                    local_ip = 127.0.0.1, 
                    status = started, 
                    preset_id = 5, 
                    disk_stats = timeweb_cloud_api.models.db_disk_stats.db_disk_stats(
                        size = 10485760, 
                        used = 486.11328125, ), 
                    config_parameters = timeweb_cloud_api.models.config_parameters.config-parameters(
                        auto_increment_increment = 1, 
                        auto_increment_offset = 1, 
                        innodb_io_capacity = 200, 
                        innodb_purge_threads = 4, 
                        innodb_read_io_threads = 4, 
                        innodb_thread_concurrency = 0, 
                        innodb_write_io_threads = 4, 
                        join_buffer_size = 262144, 
                        max_allowed_packet = 16777216, 
                        max_heap_table_size = 16777216, 
                        autovacuum_analyze_scale_factor = 0.0001, 
                        bgwriter_delay = 200, 
                        bgwriter_lru_maxpages = 100, 
                        deadlock_timeout = 100, 
                        gin_pending_list_limit = 4194304, 
                        idle_in_transaction_session_timeout = 0, 
                        idle_session_timeout = 0, 
                        join_collapse_limit = 8, 
                        lock_timeout = 0, 
                        max_prepared_transactions = 0, 
                        max_connections = 1, 
                        shared_buffers = 128, 
                        wal_buffers = 16, 
                        temp_buffers = 8, 
                        work_mem = 4, 
                        sql_mode = STRICT_TRANS_TABLES, 
                        query_cache_type = 0, 
                        query_cache_size = 0, ), 
                    is_only_local_ip_access = false, 
                    availability_zone = spb-1, )
            )
        else :
            return CreateDatabase201Response(
                db = timeweb_cloud_api.models.db.db(
                    id = 1, 
                    created_at = 2021-02-25T11:04:15Z, 
                    account_id = cp78562, 
                    login = test_user, 
                    location = ru-1, 
                    password = password, 
                    name = default_db, 
                    host = test.ru, 
                    type = mysql, 
                    hash_type = caching_sha2, 
                    port = 3000, 
                    ip = 127.0.0.1, 
                    local_ip = 127.0.0.1, 
                    status = started, 
                    preset_id = 5, 
                    disk_stats = timeweb_cloud_api.models.db_disk_stats.db_disk_stats(
                        size = 10485760, 
                        used = 486.11328125, ), 
                    config_parameters = timeweb_cloud_api.models.config_parameters.config-parameters(
                        auto_increment_increment = 1, 
                        auto_increment_offset = 1, 
                        innodb_io_capacity = 200, 
                        innodb_purge_threads = 4, 
                        innodb_read_io_threads = 4, 
                        innodb_thread_concurrency = 0, 
                        innodb_write_io_threads = 4, 
                        join_buffer_size = 262144, 
                        max_allowed_packet = 16777216, 
                        max_heap_table_size = 16777216, 
                        autovacuum_analyze_scale_factor = 0.0001, 
                        bgwriter_delay = 200, 
                        bgwriter_lru_maxpages = 100, 
                        deadlock_timeout = 100, 
                        gin_pending_list_limit = 4194304, 
                        idle_in_transaction_session_timeout = 0, 
                        idle_session_timeout = 0, 
                        join_collapse_limit = 8, 
                        lock_timeout = 0, 
                        max_prepared_transactions = 0, 
                        max_connections = 1, 
                        shared_buffers = 128, 
                        wal_buffers = 16, 
                        temp_buffers = 8, 
                        work_mem = 4, 
                        sql_mode = STRICT_TRANS_TABLES, 
                        query_cache_type = 0, 
                        query_cache_size = 0, ), 
                    is_only_local_ip_access = false, 
                    availability_zone = spb-1, ),
        )
        """

    def testCreateDatabase201Response(self):
        """Test CreateDatabase201Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
