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

class DbParametersByType(BaseModel):
    """
    Имена параметров конфигурации, доступных для каждого типа кластера базы данных. Ключ объекта — тип кластера (значение поля `type` при создании кластера), значение — массив имён параметров, которые можно передать в `config_parameters` для кластера этого типа. Наборы параметров различаются между версиями одной СУБД. Значения параметров этот метод не возвращает — рекомендуемые значения можно получить в `GET /api/v1/dbs/default-parameters`.
    """
    mysql5: Optional[Any] = Field(..., description="Параметры, доступные для кластеров типа `mysql5`.")
    mysql: Optional[Any] = Field(..., description="Параметры, доступные для кластеров типа `mysql`.")
    mysql8_4: Optional[Any] = Field(..., description="Параметры, доступные для кластеров типа `mysql8_4`.")
    postgres: Optional[Any] = Field(..., description="Параметры, доступные для кластеров типа `postgres` (PostgreSQL 13).")
    postgres14: Optional[Any] = Field(..., description="Параметры, доступные для кластеров типа `postgres14`.")
    postgres15: Optional[Any] = Field(..., description="Параметры, доступные для кластеров типа `postgres15`.")
    postgres16: Optional[Any] = Field(..., description="Параметры, доступные для кластеров типа `postgres16`.")
    postgres17: Optional[Any] = Field(..., description="Параметры, доступные для кластеров типа `postgres17`.")
    postgres18: Optional[Any] = Field(..., description="Параметры, доступные для кластеров типа `postgres18`. Набор отличается от предыдущих версий PostgreSQL — например, добавлены `io_method` и `io_workers`.")
    redis: Optional[Any] = Field(..., description="Параметры, доступные для кластеров типа `redis`.")
    redis7: Optional[Any] = Field(..., description="Параметры, доступные для кластеров типа `redis7`.")
    redis8_1: Optional[Any] = Field(..., description="Параметры, доступные для кластеров типа `redis8_1`.")
    valkey: Optional[Any] = Field(..., description="Параметры, доступные для кластеров типа `valkey`.")
    valkey7: Optional[Any] = Field(..., description="Параметры, доступные для кластеров типа `valkey7`.")
    valkey8_1: Optional[Any] = Field(..., description="Параметры, доступные для кластеров типа `valkey8_1`.")
    valkey9_1: Optional[Any] = Field(..., description="Параметры, доступные для кластеров типа `valkey9_1`.")
    mongodb4: Optional[Any] = Field(..., description="Для кластеров типа `mongodb4` настраиваемых параметров нет — всегда пустой массив.")
    mongodb: Optional[Any] = Field(..., description="Для кластеров типа `mongodb` настраиваемых параметров нет — всегда пустой массив.")
    mongodb6: Optional[Any] = Field(..., description="Для кластеров типа `mongodb6` настраиваемых параметров нет — всегда пустой массив.")
    mongodb7: Optional[Any] = Field(..., description="Для кластеров типа `mongodb7` настраиваемых параметров нет — всегда пустой массив.")
    mongodb8_0: Optional[Any] = Field(..., description="Для кластеров типа `mongodb8_0` настраиваемых параметров нет — всегда пустой массив.")
    opensearch: Optional[Any] = Field(..., description="Для кластеров типа `opensearch` настраиваемых параметров нет — всегда пустой массив.")
    opensearch2_19: Optional[Any] = Field(..., description="Для кластеров типа `opensearch2_19` настраиваемых параметров нет — всегда пустой массив.")
    clickhouse: Optional[Any] = Field(..., description="Для кластеров типа `clickhouse` настраиваемых параметров нет — всегда пустой массив.")
    clickhouse24: Optional[Any] = Field(..., description="Для кластеров типа `clickhouse24` настраиваемых параметров нет — всегда пустой массив.")
    clickhouse25: Optional[Any] = Field(..., description="Для кластеров типа `clickhouse25` настраиваемых параметров нет — всегда пустой массив.")
    kafka: Optional[Any] = Field(..., description="Для кластеров типа `kafka` настраиваемых параметров нет — всегда пустой массив.")
    rabbitmq: Optional[Any] = Field(..., description="Для кластеров типа `rabbitmq` настраиваемых параметров нет — всегда пустой массив.")
    rabbitmq4_0: Optional[Any] = Field(..., description="Для кластеров типа `rabbitmq4_0` настраиваемых параметров нет — всегда пустой массив.")
    __properties = ["mysql5", "mysql", "mysql8_4", "postgres", "postgres14", "postgres15", "postgres16", "postgres17", "postgres18", "redis", "redis7", "redis8_1", "valkey", "valkey7", "valkey8_1", "valkey9_1", "mongodb4", "mongodb", "mongodb6", "mongodb7", "mongodb8_0", "opensearch", "opensearch2_19", "clickhouse", "clickhouse24", "clickhouse25", "kafka", "rabbitmq", "rabbitmq4_0"]

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
    def from_json(cls, json_str: str) -> DbParametersByType:
        """Create an instance of DbParametersByType from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if mysql5 (nullable) is None
        # and __fields_set__ contains the field
        if self.mysql5 is None and "mysql5" in self.__fields_set__:
            _dict['mysql5'] = None

        # set to None if mysql (nullable) is None
        # and __fields_set__ contains the field
        if self.mysql is None and "mysql" in self.__fields_set__:
            _dict['mysql'] = None

        # set to None if mysql8_4 (nullable) is None
        # and __fields_set__ contains the field
        if self.mysql8_4 is None and "mysql8_4" in self.__fields_set__:
            _dict['mysql8_4'] = None

        # set to None if postgres (nullable) is None
        # and __fields_set__ contains the field
        if self.postgres is None and "postgres" in self.__fields_set__:
            _dict['postgres'] = None

        # set to None if postgres14 (nullable) is None
        # and __fields_set__ contains the field
        if self.postgres14 is None and "postgres14" in self.__fields_set__:
            _dict['postgres14'] = None

        # set to None if postgres15 (nullable) is None
        # and __fields_set__ contains the field
        if self.postgres15 is None and "postgres15" in self.__fields_set__:
            _dict['postgres15'] = None

        # set to None if postgres16 (nullable) is None
        # and __fields_set__ contains the field
        if self.postgres16 is None and "postgres16" in self.__fields_set__:
            _dict['postgres16'] = None

        # set to None if postgres17 (nullable) is None
        # and __fields_set__ contains the field
        if self.postgres17 is None and "postgres17" in self.__fields_set__:
            _dict['postgres17'] = None

        # set to None if postgres18 (nullable) is None
        # and __fields_set__ contains the field
        if self.postgres18 is None and "postgres18" in self.__fields_set__:
            _dict['postgres18'] = None

        # set to None if redis (nullable) is None
        # and __fields_set__ contains the field
        if self.redis is None and "redis" in self.__fields_set__:
            _dict['redis'] = None

        # set to None if redis7 (nullable) is None
        # and __fields_set__ contains the field
        if self.redis7 is None and "redis7" in self.__fields_set__:
            _dict['redis7'] = None

        # set to None if redis8_1 (nullable) is None
        # and __fields_set__ contains the field
        if self.redis8_1 is None and "redis8_1" in self.__fields_set__:
            _dict['redis8_1'] = None

        # set to None if valkey (nullable) is None
        # and __fields_set__ contains the field
        if self.valkey is None and "valkey" in self.__fields_set__:
            _dict['valkey'] = None

        # set to None if valkey7 (nullable) is None
        # and __fields_set__ contains the field
        if self.valkey7 is None and "valkey7" in self.__fields_set__:
            _dict['valkey7'] = None

        # set to None if valkey8_1 (nullable) is None
        # and __fields_set__ contains the field
        if self.valkey8_1 is None and "valkey8_1" in self.__fields_set__:
            _dict['valkey8_1'] = None

        # set to None if valkey9_1 (nullable) is None
        # and __fields_set__ contains the field
        if self.valkey9_1 is None and "valkey9_1" in self.__fields_set__:
            _dict['valkey9_1'] = None

        # set to None if mongodb4 (nullable) is None
        # and __fields_set__ contains the field
        if self.mongodb4 is None and "mongodb4" in self.__fields_set__:
            _dict['mongodb4'] = None

        # set to None if mongodb (nullable) is None
        # and __fields_set__ contains the field
        if self.mongodb is None and "mongodb" in self.__fields_set__:
            _dict['mongodb'] = None

        # set to None if mongodb6 (nullable) is None
        # and __fields_set__ contains the field
        if self.mongodb6 is None and "mongodb6" in self.__fields_set__:
            _dict['mongodb6'] = None

        # set to None if mongodb7 (nullable) is None
        # and __fields_set__ contains the field
        if self.mongodb7 is None and "mongodb7" in self.__fields_set__:
            _dict['mongodb7'] = None

        # set to None if mongodb8_0 (nullable) is None
        # and __fields_set__ contains the field
        if self.mongodb8_0 is None and "mongodb8_0" in self.__fields_set__:
            _dict['mongodb8_0'] = None

        # set to None if opensearch (nullable) is None
        # and __fields_set__ contains the field
        if self.opensearch is None and "opensearch" in self.__fields_set__:
            _dict['opensearch'] = None

        # set to None if opensearch2_19 (nullable) is None
        # and __fields_set__ contains the field
        if self.opensearch2_19 is None and "opensearch2_19" in self.__fields_set__:
            _dict['opensearch2_19'] = None

        # set to None if clickhouse (nullable) is None
        # and __fields_set__ contains the field
        if self.clickhouse is None and "clickhouse" in self.__fields_set__:
            _dict['clickhouse'] = None

        # set to None if clickhouse24 (nullable) is None
        # and __fields_set__ contains the field
        if self.clickhouse24 is None and "clickhouse24" in self.__fields_set__:
            _dict['clickhouse24'] = None

        # set to None if clickhouse25 (nullable) is None
        # and __fields_set__ contains the field
        if self.clickhouse25 is None and "clickhouse25" in self.__fields_set__:
            _dict['clickhouse25'] = None

        # set to None if kafka (nullable) is None
        # and __fields_set__ contains the field
        if self.kafka is None and "kafka" in self.__fields_set__:
            _dict['kafka'] = None

        # set to None if rabbitmq (nullable) is None
        # and __fields_set__ contains the field
        if self.rabbitmq is None and "rabbitmq" in self.__fields_set__:
            _dict['rabbitmq'] = None

        # set to None if rabbitmq4_0 (nullable) is None
        # and __fields_set__ contains the field
        if self.rabbitmq4_0 is None and "rabbitmq4_0" in self.__fields_set__:
            _dict['rabbitmq4_0'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DbParametersByType:
        """Create an instance of DbParametersByType from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DbParametersByType.parse_obj(obj)

        _obj = DbParametersByType.parse_obj({
            "mysql5": obj.get("mysql5"),
            "mysql": obj.get("mysql"),
            "mysql8_4": obj.get("mysql8_4"),
            "postgres": obj.get("postgres"),
            "postgres14": obj.get("postgres14"),
            "postgres15": obj.get("postgres15"),
            "postgres16": obj.get("postgres16"),
            "postgres17": obj.get("postgres17"),
            "postgres18": obj.get("postgres18"),
            "redis": obj.get("redis"),
            "redis7": obj.get("redis7"),
            "redis8_1": obj.get("redis8_1"),
            "valkey": obj.get("valkey"),
            "valkey7": obj.get("valkey7"),
            "valkey8_1": obj.get("valkey8_1"),
            "valkey9_1": obj.get("valkey9_1"),
            "mongodb4": obj.get("mongodb4"),
            "mongodb": obj.get("mongodb"),
            "mongodb6": obj.get("mongodb6"),
            "mongodb7": obj.get("mongodb7"),
            "mongodb8_0": obj.get("mongodb8_0"),
            "opensearch": obj.get("opensearch"),
            "opensearch2_19": obj.get("opensearch2_19"),
            "clickhouse": obj.get("clickhouse"),
            "clickhouse24": obj.get("clickhouse24"),
            "clickhouse25": obj.get("clickhouse25"),
            "kafka": obj.get("kafka"),
            "rabbitmq": obj.get("rabbitmq"),
            "rabbitmq4_0": obj.get("rabbitmq4_0")
        })
        return _obj

