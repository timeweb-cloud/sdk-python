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

class Postgres(BaseModel):
    """
    Параметры PostgreSQL (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`)
    """
    max_connections: Optional[Any] = Field(None, description="Максимальное количество одновременных подключений к серверу (`mysql5` | `mysql` | `mysql8_4` | `postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    autovacuum_analyze_scale_factor: Optional[Any] = Field(None, description="Доля изменения строк таблицы перед запуском автоматического анализа (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    autovacuum_max_workers: Optional[Any] = Field(None, description="Максимальное количество процессов autovacuum, которые могут работать одновременно (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    autovacuum_naptime: Optional[Any] = Field(None, description="Интервал между запусками процессов autovacuum (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    autovacuum_vacuum_insert_scale_factor: Optional[Any] = Field(None, description="Доля вставленных строк перед запуском vacuum для таблиц с большим количеством вставок (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    autovacuum_vacuum_scale_factor: Optional[Any] = Field(None, description="Доля измененных или удаленных строк перед запуском autovacuum (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    autovacuum_work_mem: Optional[Any] = Field(None, description="Объем памяти, используемый одним процессом autovacuum (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    bgwriter_delay: Optional[Any] = Field(None, description="Интервал между циклами фонового процесса записи страниц (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    bgwriter_lru_maxpages: Optional[Any] = Field(None, description="Максимальное количество страниц, записываемых background writer за один цикл (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    deadlock_timeout: Optional[Any] = Field(None, description="Время ожидания блокировки перед проверкой взаимной блокировки (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    gin_pending_list_limit: Optional[Any] = Field(None, description="Максимальный размер списка ожидающих вставок индекса GIN (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    idle_in_transaction_session_timeout: Optional[Any] = Field(None, description="Время ожидания неактивной транзакционной сессии перед завершением соединения (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    join_collapse_limit: Optional[Any] = Field(None, description="Максимальное количество таблиц в JOIN, которые планировщик может переупорядочить (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    lock_timeout: Optional[Any] = Field(None, description="Максимальное время ожидания блокировки перед отменой запроса (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    max_prepared_transactions: Optional[Any] = Field(None, description="Максимальное количество подготовленных транзакций, которые могут существовать одновременно (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    shared_buffers: Optional[Any] = Field(None, description="Размер общей памяти, используемой PostgreSQL для буферного кэша (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    log_min_duration_statement: Optional[Any] = Field(None, description="Минимальное время выполнения запроса, после которого он записывается в журнал (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    wal_buffers: Optional[Any] = Field(None, description="Размер памяти, используемой для буферизации WAL-записей (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    temp_buffers: Optional[Any] = Field(None, description="Максимальный объем памяти для временных таблиц каждой сессии (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    work_mem: Optional[Any] = Field(None, description="Объем памяти, используемый одной операцией сортировки или хеширования (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    default_transaction_isolation: Optional[Any] = Field(None, description="Уровень изоляции транзакций по умолчанию (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    effective_cache_size: Optional[Any] = Field(None, description="Оценка объема дискового кэша, доступного планировщику запросов (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    max_wal_size: Optional[Any] = Field(None, description="Максимальный размер WAL перед запуском контрольной точки (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    min_wal_size: Optional[Any] = Field(None, description="Минимальный размер WAL, который сохраняется между контрольными точками (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    wal_level: Optional[Any] = Field(None, description="Уровень детализации записи WAL для восстановления и репликации (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    max_replication_slots: Optional[Any] = Field(None, description="Максимальное количество слотов репликации, которые могут быть созданы (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    max_wal_senders: Optional[Any] = Field(None, description="Максимальное количество процессов отправки WAL для репликации (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    max_worker_processes: Optional[Any] = Field(None, description="Максимальное количество фоновых процессов PostgreSQL (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    max_logical_replication_workers: Optional[Any] = Field(None, description="Максимальное количество процессов логической репликации (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    max_parallel_maintenance_workers: Optional[Any] = Field(None, description="Максимальное количество параллельных процессов для операций обслуживания (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    max_parallel_workers: Optional[Any] = Field(None, description="Максимальное количество параллельных рабочих процессов для запросов (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    max_parallel_workers_per_gather: Optional[Any] = Field(None, description="Максимальное количество параллельных рабочих процессов на один Gather-узел (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    array_nulls: Optional[Any] = Field(None, description="Разрешение использования NULL в массивах PostgreSQL (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    backend_flush_after: Optional[Any] = Field(None, description="Количество страниц, после записи которых выполняется принудительная очистка данных на диск серверным процессом (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    backslash_quote: Optional[Any] = Field(None, description="Управление использованием обратного слеша в строковых литералах (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    bgwriter_flush_after: Optional[Any] = Field(None, description="Количество страниц, после которого background writer выполняет очистку данных на диск (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    bgwriter_lru_multiplier: Optional[Any] = Field(None, description="Множитель количества страниц, которые background writer пытается очистить (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    default_transaction_read_only: Optional[Any] = Field(None, description="Определяет режим транзакций только для чтения по умолчанию (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    enable_hashagg: Optional[Any] = Field(None, description="Разрешение использования Hash Aggregate планировщиком запросов (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    enable_hashjoin: Optional[Any] = Field(None, description="Разрешение использования Hash Join планировщиком запросов (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    enable_incremental_sort: Optional[Any] = Field(None, description="Разрешение использования инкрементальной сортировки планировщиком (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    enable_indexscan: Optional[Any] = Field(None, description="Разрешение использования обычного индексного сканирования (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    enable_indexonlyscan: Optional[Any] = Field(None, description="Разрешение использования index-only scan (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    enable_material: Optional[Any] = Field(None, description="Разрешение использования материализации промежуточных результатов запросов (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    enable_memoize: Optional[Any] = Field(None, description="Разрешение использования Memoize узлов планировщиком запросов (`postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    enable_mergejoin: Optional[Any] = Field(None, description="Разрешение использования Merge Join планировщиком запросов (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    enable_parallel_append: Optional[Any] = Field(None, description="Разрешение использования параллельного Append для запросов (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    enable_parallel_hash: Optional[Any] = Field(None, description="Разрешение использования параллельных Hash операций (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    enable_partition_pruning: Optional[Any] = Field(None, description="Разрешение удаления ненужных разделов таблицы при планировании запроса (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    enable_partitionwise_join: Optional[Any] = Field(None, description="Разрешение выполнения соединений между секционированными таблицами с учетом секций (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    enable_partitionwise_aggregate: Optional[Any] = Field(None, description="Разрешение выполнения агрегатных операций отдельно для секций таблиц (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    enable_seqscan: Optional[Any] = Field(None, description="Разрешение использования последовательного сканирования таблиц планировщиком запросов (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    enable_sort: Optional[Any] = Field(None, description="Разрешение использования операций сортировки планировщиком запросов (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    enable_tidscan: Optional[Any] = Field(None, description="Разрешение использования TID Scan для поиска строк по физическим идентификаторам (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    exit_on_error: Optional[Any] = Field(None, description="Завершение сессии при возникновении ошибки SQL (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    from_collapse_limit: Optional[Any] = Field(None, description="Максимальное количество элементов FROM, которые планировщик может объединять при оптимизации запросов (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    jit: Optional[Any] = Field(None, description="Включение JIT-компиляции для ускорения выполнения запросов (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    plan_cache_mode: Optional[Any] = Field(None, description="Режим использования кэша планов подготовленных запросов (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    quote_all_identifiers: Optional[Any] = Field(None, description="Всегда заключать идентификаторы в кавычки при генерации SQL (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    standard_conforming_strings: Optional[Any] = Field(None, description="Использование стандартного поведения строковых литералов SQL (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    statement_timeout: Optional[Any] = Field(None, description="Максимальное время выполнения SQL-запроса перед автоматической отменой (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    timezone: Optional[Any] = Field(None, description="Часовой пояс сервера PostgreSQL по умолчанию (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    transform_null_equals: Optional[Any] = Field(None, description="Преобразование выражений вида `NULL = NULL` в проверку IS NULL (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    max_locks_per_transaction: Optional[Any] = Field(None, description="Количество объектов, которые может блокировать одна транзакция (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    autovacuum_vacuum_cost_limit: Optional[Any] = Field(None, description="Лимит стоимости операций autovacuum перед приостановкой работы (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    checkpoint_timeout: Optional[Any] = Field(None, description="Максимальный интервал времени между автоматическими контрольными точками (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    checkpoint_completion_target: Optional[Any] = Field(None, description="Доля интервала checkpoint, за которую PostgreSQL распределяет запись данных (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    wal_compression: Optional[Any] = Field(None, description="Включение сжатия WAL-записей для уменьшения объема журнала (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    random_page_cost: Optional[Any] = Field(None, description="Оценочная стоимость случайного чтения страницы для планировщика запросов (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    effective_io_concurrency: Optional[Any] = Field(None, description="Количество параллельных операций ввода-вывода, которые планировщик может учитывать (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    log_lock_waits: Optional[Any] = Field(None, description="Включение записи в журнал информации об ожидании блокировок дольше deadlock_timeout (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    log_temp_files: Optional[Any] = Field(None, description="Минимальный размер временных файлов, при котором они записываются в журнал (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    track_io_timing: Optional[Any] = Field(None, description="Включение сбора статистики времени операций ввода-вывода (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    maintenance_work_mem: Optional[Any] = Field(None, description="Максимальный объем памяти для операций обслуживания, таких как VACUUM и CREATE INDEX (`postgres` | `postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    idle_session_timeout: Optional[Any] = Field(None, description="Время ожидания неактивной сессии перед автоматическим завершением соединения (`postgres14` | `postgres15` | `postgres16` | `postgres17` | `postgres18`).")
    io_method: Optional[Any] = Field(None, description="Метод выполнения операций ввода-вывода PostgreSQL (`postgres18`).")
    io_workers: Optional[Any] = Field(None, description="Количество фоновых процессов для выполнения операций ввода-вывода (`postgres18`).")
    __properties = ["max_connections", "autovacuum_analyze_scale_factor", "autovacuum_max_workers", "autovacuum_naptime", "autovacuum_vacuum_insert_scale_factor", "autovacuum_vacuum_scale_factor", "autovacuum_work_mem", "bgwriter_delay", "bgwriter_lru_maxpages", "deadlock_timeout", "gin_pending_list_limit", "idle_in_transaction_session_timeout", "join_collapse_limit", "lock_timeout", "max_prepared_transactions", "shared_buffers", "log_min_duration_statement", "wal_buffers", "temp_buffers", "work_mem", "default_transaction_isolation", "effective_cache_size", "max_wal_size", "min_wal_size", "wal_level", "max_replication_slots", "max_wal_senders", "max_worker_processes", "max_logical_replication_workers", "max_parallel_maintenance_workers", "max_parallel_workers", "max_parallel_workers_per_gather", "array_nulls", "backend_flush_after", "backslash_quote", "bgwriter_flush_after", "bgwriter_lru_multiplier", "default_transaction_read_only", "enable_hashagg", "enable_hashjoin", "enable_incremental_sort", "enable_indexscan", "enable_indexonlyscan", "enable_material", "enable_memoize", "enable_mergejoin", "enable_parallel_append", "enable_parallel_hash", "enable_partition_pruning", "enable_partitionwise_join", "enable_partitionwise_aggregate", "enable_seqscan", "enable_sort", "enable_tidscan", "exit_on_error", "from_collapse_limit", "jit", "plan_cache_mode", "quote_all_identifiers", "standard_conforming_strings", "statement_timeout", "timezone", "transform_null_equals", "max_locks_per_transaction", "autovacuum_vacuum_cost_limit", "checkpoint_timeout", "checkpoint_completion_target", "wal_compression", "random_page_cost", "effective_io_concurrency", "log_lock_waits", "log_temp_files", "track_io_timing", "maintenance_work_mem", "idle_session_timeout", "io_method", "io_workers"]

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
    def from_json(cls, json_str: str) -> Postgres:
        """Create an instance of Postgres from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if max_connections (nullable) is None
        # and __fields_set__ contains the field
        if self.max_connections is None and "max_connections" in self.__fields_set__:
            _dict['max_connections'] = None

        # set to None if autovacuum_analyze_scale_factor (nullable) is None
        # and __fields_set__ contains the field
        if self.autovacuum_analyze_scale_factor is None and "autovacuum_analyze_scale_factor" in self.__fields_set__:
            _dict['autovacuum_analyze_scale_factor'] = None

        # set to None if autovacuum_max_workers (nullable) is None
        # and __fields_set__ contains the field
        if self.autovacuum_max_workers is None and "autovacuum_max_workers" in self.__fields_set__:
            _dict['autovacuum_max_workers'] = None

        # set to None if autovacuum_naptime (nullable) is None
        # and __fields_set__ contains the field
        if self.autovacuum_naptime is None and "autovacuum_naptime" in self.__fields_set__:
            _dict['autovacuum_naptime'] = None

        # set to None if autovacuum_vacuum_insert_scale_factor (nullable) is None
        # and __fields_set__ contains the field
        if self.autovacuum_vacuum_insert_scale_factor is None and "autovacuum_vacuum_insert_scale_factor" in self.__fields_set__:
            _dict['autovacuum_vacuum_insert_scale_factor'] = None

        # set to None if autovacuum_vacuum_scale_factor (nullable) is None
        # and __fields_set__ contains the field
        if self.autovacuum_vacuum_scale_factor is None and "autovacuum_vacuum_scale_factor" in self.__fields_set__:
            _dict['autovacuum_vacuum_scale_factor'] = None

        # set to None if autovacuum_work_mem (nullable) is None
        # and __fields_set__ contains the field
        if self.autovacuum_work_mem is None and "autovacuum_work_mem" in self.__fields_set__:
            _dict['autovacuum_work_mem'] = None

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

        # set to None if shared_buffers (nullable) is None
        # and __fields_set__ contains the field
        if self.shared_buffers is None and "shared_buffers" in self.__fields_set__:
            _dict['shared_buffers'] = None

        # set to None if log_min_duration_statement (nullable) is None
        # and __fields_set__ contains the field
        if self.log_min_duration_statement is None and "log_min_duration_statement" in self.__fields_set__:
            _dict['log_min_duration_statement'] = None

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

        # set to None if default_transaction_isolation (nullable) is None
        # and __fields_set__ contains the field
        if self.default_transaction_isolation is None and "default_transaction_isolation" in self.__fields_set__:
            _dict['default_transaction_isolation'] = None

        # set to None if effective_cache_size (nullable) is None
        # and __fields_set__ contains the field
        if self.effective_cache_size is None and "effective_cache_size" in self.__fields_set__:
            _dict['effective_cache_size'] = None

        # set to None if max_wal_size (nullable) is None
        # and __fields_set__ contains the field
        if self.max_wal_size is None and "max_wal_size" in self.__fields_set__:
            _dict['max_wal_size'] = None

        # set to None if min_wal_size (nullable) is None
        # and __fields_set__ contains the field
        if self.min_wal_size is None and "min_wal_size" in self.__fields_set__:
            _dict['min_wal_size'] = None

        # set to None if wal_level (nullable) is None
        # and __fields_set__ contains the field
        if self.wal_level is None and "wal_level" in self.__fields_set__:
            _dict['wal_level'] = None

        # set to None if max_replication_slots (nullable) is None
        # and __fields_set__ contains the field
        if self.max_replication_slots is None and "max_replication_slots" in self.__fields_set__:
            _dict['max_replication_slots'] = None

        # set to None if max_wal_senders (nullable) is None
        # and __fields_set__ contains the field
        if self.max_wal_senders is None and "max_wal_senders" in self.__fields_set__:
            _dict['max_wal_senders'] = None

        # set to None if max_worker_processes (nullable) is None
        # and __fields_set__ contains the field
        if self.max_worker_processes is None and "max_worker_processes" in self.__fields_set__:
            _dict['max_worker_processes'] = None

        # set to None if max_logical_replication_workers (nullable) is None
        # and __fields_set__ contains the field
        if self.max_logical_replication_workers is None and "max_logical_replication_workers" in self.__fields_set__:
            _dict['max_logical_replication_workers'] = None

        # set to None if max_parallel_maintenance_workers (nullable) is None
        # and __fields_set__ contains the field
        if self.max_parallel_maintenance_workers is None and "max_parallel_maintenance_workers" in self.__fields_set__:
            _dict['max_parallel_maintenance_workers'] = None

        # set to None if max_parallel_workers (nullable) is None
        # and __fields_set__ contains the field
        if self.max_parallel_workers is None and "max_parallel_workers" in self.__fields_set__:
            _dict['max_parallel_workers'] = None

        # set to None if max_parallel_workers_per_gather (nullable) is None
        # and __fields_set__ contains the field
        if self.max_parallel_workers_per_gather is None and "max_parallel_workers_per_gather" in self.__fields_set__:
            _dict['max_parallel_workers_per_gather'] = None

        # set to None if array_nulls (nullable) is None
        # and __fields_set__ contains the field
        if self.array_nulls is None and "array_nulls" in self.__fields_set__:
            _dict['array_nulls'] = None

        # set to None if backend_flush_after (nullable) is None
        # and __fields_set__ contains the field
        if self.backend_flush_after is None and "backend_flush_after" in self.__fields_set__:
            _dict['backend_flush_after'] = None

        # set to None if backslash_quote (nullable) is None
        # and __fields_set__ contains the field
        if self.backslash_quote is None and "backslash_quote" in self.__fields_set__:
            _dict['backslash_quote'] = None

        # set to None if bgwriter_flush_after (nullable) is None
        # and __fields_set__ contains the field
        if self.bgwriter_flush_after is None and "bgwriter_flush_after" in self.__fields_set__:
            _dict['bgwriter_flush_after'] = None

        # set to None if bgwriter_lru_multiplier (nullable) is None
        # and __fields_set__ contains the field
        if self.bgwriter_lru_multiplier is None and "bgwriter_lru_multiplier" in self.__fields_set__:
            _dict['bgwriter_lru_multiplier'] = None

        # set to None if default_transaction_read_only (nullable) is None
        # and __fields_set__ contains the field
        if self.default_transaction_read_only is None and "default_transaction_read_only" in self.__fields_set__:
            _dict['default_transaction_read_only'] = None

        # set to None if enable_hashagg (nullable) is None
        # and __fields_set__ contains the field
        if self.enable_hashagg is None and "enable_hashagg" in self.__fields_set__:
            _dict['enable_hashagg'] = None

        # set to None if enable_hashjoin (nullable) is None
        # and __fields_set__ contains the field
        if self.enable_hashjoin is None and "enable_hashjoin" in self.__fields_set__:
            _dict['enable_hashjoin'] = None

        # set to None if enable_incremental_sort (nullable) is None
        # and __fields_set__ contains the field
        if self.enable_incremental_sort is None and "enable_incremental_sort" in self.__fields_set__:
            _dict['enable_incremental_sort'] = None

        # set to None if enable_indexscan (nullable) is None
        # and __fields_set__ contains the field
        if self.enable_indexscan is None and "enable_indexscan" in self.__fields_set__:
            _dict['enable_indexscan'] = None

        # set to None if enable_indexonlyscan (nullable) is None
        # and __fields_set__ contains the field
        if self.enable_indexonlyscan is None and "enable_indexonlyscan" in self.__fields_set__:
            _dict['enable_indexonlyscan'] = None

        # set to None if enable_material (nullable) is None
        # and __fields_set__ contains the field
        if self.enable_material is None and "enable_material" in self.__fields_set__:
            _dict['enable_material'] = None

        # set to None if enable_memoize (nullable) is None
        # and __fields_set__ contains the field
        if self.enable_memoize is None and "enable_memoize" in self.__fields_set__:
            _dict['enable_memoize'] = None

        # set to None if enable_mergejoin (nullable) is None
        # and __fields_set__ contains the field
        if self.enable_mergejoin is None and "enable_mergejoin" in self.__fields_set__:
            _dict['enable_mergejoin'] = None

        # set to None if enable_parallel_append (nullable) is None
        # and __fields_set__ contains the field
        if self.enable_parallel_append is None and "enable_parallel_append" in self.__fields_set__:
            _dict['enable_parallel_append'] = None

        # set to None if enable_parallel_hash (nullable) is None
        # and __fields_set__ contains the field
        if self.enable_parallel_hash is None and "enable_parallel_hash" in self.__fields_set__:
            _dict['enable_parallel_hash'] = None

        # set to None if enable_partition_pruning (nullable) is None
        # and __fields_set__ contains the field
        if self.enable_partition_pruning is None and "enable_partition_pruning" in self.__fields_set__:
            _dict['enable_partition_pruning'] = None

        # set to None if enable_partitionwise_join (nullable) is None
        # and __fields_set__ contains the field
        if self.enable_partitionwise_join is None and "enable_partitionwise_join" in self.__fields_set__:
            _dict['enable_partitionwise_join'] = None

        # set to None if enable_partitionwise_aggregate (nullable) is None
        # and __fields_set__ contains the field
        if self.enable_partitionwise_aggregate is None and "enable_partitionwise_aggregate" in self.__fields_set__:
            _dict['enable_partitionwise_aggregate'] = None

        # set to None if enable_seqscan (nullable) is None
        # and __fields_set__ contains the field
        if self.enable_seqscan is None and "enable_seqscan" in self.__fields_set__:
            _dict['enable_seqscan'] = None

        # set to None if enable_sort (nullable) is None
        # and __fields_set__ contains the field
        if self.enable_sort is None and "enable_sort" in self.__fields_set__:
            _dict['enable_sort'] = None

        # set to None if enable_tidscan (nullable) is None
        # and __fields_set__ contains the field
        if self.enable_tidscan is None and "enable_tidscan" in self.__fields_set__:
            _dict['enable_tidscan'] = None

        # set to None if exit_on_error (nullable) is None
        # and __fields_set__ contains the field
        if self.exit_on_error is None and "exit_on_error" in self.__fields_set__:
            _dict['exit_on_error'] = None

        # set to None if from_collapse_limit (nullable) is None
        # and __fields_set__ contains the field
        if self.from_collapse_limit is None and "from_collapse_limit" in self.__fields_set__:
            _dict['from_collapse_limit'] = None

        # set to None if jit (nullable) is None
        # and __fields_set__ contains the field
        if self.jit is None and "jit" in self.__fields_set__:
            _dict['jit'] = None

        # set to None if plan_cache_mode (nullable) is None
        # and __fields_set__ contains the field
        if self.plan_cache_mode is None and "plan_cache_mode" in self.__fields_set__:
            _dict['plan_cache_mode'] = None

        # set to None if quote_all_identifiers (nullable) is None
        # and __fields_set__ contains the field
        if self.quote_all_identifiers is None and "quote_all_identifiers" in self.__fields_set__:
            _dict['quote_all_identifiers'] = None

        # set to None if standard_conforming_strings (nullable) is None
        # and __fields_set__ contains the field
        if self.standard_conforming_strings is None and "standard_conforming_strings" in self.__fields_set__:
            _dict['standard_conforming_strings'] = None

        # set to None if statement_timeout (nullable) is None
        # and __fields_set__ contains the field
        if self.statement_timeout is None and "statement_timeout" in self.__fields_set__:
            _dict['statement_timeout'] = None

        # set to None if timezone (nullable) is None
        # and __fields_set__ contains the field
        if self.timezone is None and "timezone" in self.__fields_set__:
            _dict['timezone'] = None

        # set to None if transform_null_equals (nullable) is None
        # and __fields_set__ contains the field
        if self.transform_null_equals is None and "transform_null_equals" in self.__fields_set__:
            _dict['transform_null_equals'] = None

        # set to None if max_locks_per_transaction (nullable) is None
        # and __fields_set__ contains the field
        if self.max_locks_per_transaction is None and "max_locks_per_transaction" in self.__fields_set__:
            _dict['max_locks_per_transaction'] = None

        # set to None if autovacuum_vacuum_cost_limit (nullable) is None
        # and __fields_set__ contains the field
        if self.autovacuum_vacuum_cost_limit is None and "autovacuum_vacuum_cost_limit" in self.__fields_set__:
            _dict['autovacuum_vacuum_cost_limit'] = None

        # set to None if checkpoint_timeout (nullable) is None
        # and __fields_set__ contains the field
        if self.checkpoint_timeout is None and "checkpoint_timeout" in self.__fields_set__:
            _dict['checkpoint_timeout'] = None

        # set to None if checkpoint_completion_target (nullable) is None
        # and __fields_set__ contains the field
        if self.checkpoint_completion_target is None and "checkpoint_completion_target" in self.__fields_set__:
            _dict['checkpoint_completion_target'] = None

        # set to None if wal_compression (nullable) is None
        # and __fields_set__ contains the field
        if self.wal_compression is None and "wal_compression" in self.__fields_set__:
            _dict['wal_compression'] = None

        # set to None if random_page_cost (nullable) is None
        # and __fields_set__ contains the field
        if self.random_page_cost is None and "random_page_cost" in self.__fields_set__:
            _dict['random_page_cost'] = None

        # set to None if effective_io_concurrency (nullable) is None
        # and __fields_set__ contains the field
        if self.effective_io_concurrency is None and "effective_io_concurrency" in self.__fields_set__:
            _dict['effective_io_concurrency'] = None

        # set to None if log_lock_waits (nullable) is None
        # and __fields_set__ contains the field
        if self.log_lock_waits is None and "log_lock_waits" in self.__fields_set__:
            _dict['log_lock_waits'] = None

        # set to None if log_temp_files (nullable) is None
        # and __fields_set__ contains the field
        if self.log_temp_files is None and "log_temp_files" in self.__fields_set__:
            _dict['log_temp_files'] = None

        # set to None if track_io_timing (nullable) is None
        # and __fields_set__ contains the field
        if self.track_io_timing is None and "track_io_timing" in self.__fields_set__:
            _dict['track_io_timing'] = None

        # set to None if maintenance_work_mem (nullable) is None
        # and __fields_set__ contains the field
        if self.maintenance_work_mem is None and "maintenance_work_mem" in self.__fields_set__:
            _dict['maintenance_work_mem'] = None

        # set to None if idle_session_timeout (nullable) is None
        # and __fields_set__ contains the field
        if self.idle_session_timeout is None and "idle_session_timeout" in self.__fields_set__:
            _dict['idle_session_timeout'] = None

        # set to None if io_method (nullable) is None
        # and __fields_set__ contains the field
        if self.io_method is None and "io_method" in self.__fields_set__:
            _dict['io_method'] = None

        # set to None if io_workers (nullable) is None
        # and __fields_set__ contains the field
        if self.io_workers is None and "io_workers" in self.__fields_set__:
            _dict['io_workers'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Postgres:
        """Create an instance of Postgres from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Postgres.parse_obj(obj)

        _obj = Postgres.parse_obj({
            "max_connections": obj.get("max_connections"),
            "autovacuum_analyze_scale_factor": obj.get("autovacuum_analyze_scale_factor"),
            "autovacuum_max_workers": obj.get("autovacuum_max_workers"),
            "autovacuum_naptime": obj.get("autovacuum_naptime"),
            "autovacuum_vacuum_insert_scale_factor": obj.get("autovacuum_vacuum_insert_scale_factor"),
            "autovacuum_vacuum_scale_factor": obj.get("autovacuum_vacuum_scale_factor"),
            "autovacuum_work_mem": obj.get("autovacuum_work_mem"),
            "bgwriter_delay": obj.get("bgwriter_delay"),
            "bgwriter_lru_maxpages": obj.get("bgwriter_lru_maxpages"),
            "deadlock_timeout": obj.get("deadlock_timeout"),
            "gin_pending_list_limit": obj.get("gin_pending_list_limit"),
            "idle_in_transaction_session_timeout": obj.get("idle_in_transaction_session_timeout"),
            "join_collapse_limit": obj.get("join_collapse_limit"),
            "lock_timeout": obj.get("lock_timeout"),
            "max_prepared_transactions": obj.get("max_prepared_transactions"),
            "shared_buffers": obj.get("shared_buffers"),
            "log_min_duration_statement": obj.get("log_min_duration_statement"),
            "wal_buffers": obj.get("wal_buffers"),
            "temp_buffers": obj.get("temp_buffers"),
            "work_mem": obj.get("work_mem"),
            "default_transaction_isolation": obj.get("default_transaction_isolation"),
            "effective_cache_size": obj.get("effective_cache_size"),
            "max_wal_size": obj.get("max_wal_size"),
            "min_wal_size": obj.get("min_wal_size"),
            "wal_level": obj.get("wal_level"),
            "max_replication_slots": obj.get("max_replication_slots"),
            "max_wal_senders": obj.get("max_wal_senders"),
            "max_worker_processes": obj.get("max_worker_processes"),
            "max_logical_replication_workers": obj.get("max_logical_replication_workers"),
            "max_parallel_maintenance_workers": obj.get("max_parallel_maintenance_workers"),
            "max_parallel_workers": obj.get("max_parallel_workers"),
            "max_parallel_workers_per_gather": obj.get("max_parallel_workers_per_gather"),
            "array_nulls": obj.get("array_nulls"),
            "backend_flush_after": obj.get("backend_flush_after"),
            "backslash_quote": obj.get("backslash_quote"),
            "bgwriter_flush_after": obj.get("bgwriter_flush_after"),
            "bgwriter_lru_multiplier": obj.get("bgwriter_lru_multiplier"),
            "default_transaction_read_only": obj.get("default_transaction_read_only"),
            "enable_hashagg": obj.get("enable_hashagg"),
            "enable_hashjoin": obj.get("enable_hashjoin"),
            "enable_incremental_sort": obj.get("enable_incremental_sort"),
            "enable_indexscan": obj.get("enable_indexscan"),
            "enable_indexonlyscan": obj.get("enable_indexonlyscan"),
            "enable_material": obj.get("enable_material"),
            "enable_memoize": obj.get("enable_memoize"),
            "enable_mergejoin": obj.get("enable_mergejoin"),
            "enable_parallel_append": obj.get("enable_parallel_append"),
            "enable_parallel_hash": obj.get("enable_parallel_hash"),
            "enable_partition_pruning": obj.get("enable_partition_pruning"),
            "enable_partitionwise_join": obj.get("enable_partitionwise_join"),
            "enable_partitionwise_aggregate": obj.get("enable_partitionwise_aggregate"),
            "enable_seqscan": obj.get("enable_seqscan"),
            "enable_sort": obj.get("enable_sort"),
            "enable_tidscan": obj.get("enable_tidscan"),
            "exit_on_error": obj.get("exit_on_error"),
            "from_collapse_limit": obj.get("from_collapse_limit"),
            "jit": obj.get("jit"),
            "plan_cache_mode": obj.get("plan_cache_mode"),
            "quote_all_identifiers": obj.get("quote_all_identifiers"),
            "standard_conforming_strings": obj.get("standard_conforming_strings"),
            "statement_timeout": obj.get("statement_timeout"),
            "timezone": obj.get("timezone"),
            "transform_null_equals": obj.get("transform_null_equals"),
            "max_locks_per_transaction": obj.get("max_locks_per_transaction"),
            "autovacuum_vacuum_cost_limit": obj.get("autovacuum_vacuum_cost_limit"),
            "checkpoint_timeout": obj.get("checkpoint_timeout"),
            "checkpoint_completion_target": obj.get("checkpoint_completion_target"),
            "wal_compression": obj.get("wal_compression"),
            "random_page_cost": obj.get("random_page_cost"),
            "effective_io_concurrency": obj.get("effective_io_concurrency"),
            "log_lock_waits": obj.get("log_lock_waits"),
            "log_temp_files": obj.get("log_temp_files"),
            "track_io_timing": obj.get("track_io_timing"),
            "maintenance_work_mem": obj.get("maintenance_work_mem"),
            "idle_session_timeout": obj.get("idle_session_timeout"),
            "io_method": obj.get("io_method"),
            "io_workers": obj.get("io_workers")
        })
        return _obj

