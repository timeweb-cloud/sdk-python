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
from timeweb_cloud_api.models.config_parameters import ConfigParameters
from timeweb_cloud_api.models.database_cluster_disk_stats import DatabaseClusterDiskStats
from timeweb_cloud_api.models.db_type import DbType

class DatabaseCluster(BaseModel):
    """
    Кластер базы данных
    """
    id: Optional[Any] = Field(..., description="ID для каждого экземпляра базы данных. Автоматически генерируется при создании.")
    created_at: Optional[Any] = Field(..., description="Значение времени, указанное в комбинированном формате даты и времени ISO8601, которое представляет, когда была создана база данных.")
    location: Optional[Any] = Field(..., description="Локация сервера.")
    name: Optional[Any] = Field(..., description="Название кластера базы данных.")
    networks: Optional[Any] = Field(..., description="Список сетей кластера базы данных.")
    type: DbType = Field(...)
    hash_type: Optional[Any] = Field(..., description="Тип хеширования кластера базы данных (mysql5 | mysql | postgres).")
    avatar_link: Optional[Any] = Field(..., description="Ссылка на аватар для базы данных.")
    port: Optional[Any] = Field(..., description="Порт")
    status: Optional[Any] = Field(..., description="Текущий статус кластера базы данных.")
    preset_id: Optional[Any] = Field(..., description="ID тарифа.")
    disk_stats: DatabaseClusterDiskStats = Field(...)
    config_parameters: ConfigParameters = Field(...)
    is_enabled_public_network: Optional[Any] = Field(..., description="Доступность публичного IP-адреса")
    __properties = ["id", "created_at", "location", "name", "networks", "type", "hash_type", "avatar_link", "port", "status", "preset_id", "disk_stats", "config_parameters", "is_enabled_public_network"]

    @validator('location')
    def location_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('ru-1', 'ru-2', 'pl-1', 'kz-1'):
            raise ValueError("must be one of enum values ('ru-1', 'ru-2', 'pl-1', 'kz-1')")
        return value

    @validator('hash_type')
    def hash_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('caching_sha2', 'mysql_native', 'null'):
            raise ValueError("must be one of enum values ('caching_sha2', 'mysql_native', 'null')")
        return value

    @validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('started', 'starting', 'stopped', 'no_paid', 'lan_transfer', 'error', 'blocked', 'backup_recovery', 'rebooting', 'turning_off', 'turning_on'):
            raise ValueError("must be one of enum values ('started', 'starting', 'stopped', 'no_paid', 'lan_transfer', 'error', 'blocked', 'backup_recovery', 'rebooting', 'turning_off', 'turning_on')")
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
    def from_json(cls, json_str: str) -> DatabaseCluster:
        """Create an instance of DatabaseCluster from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of disk_stats
        if self.disk_stats:
            _dict['disk_stats'] = self.disk_stats.to_dict()
        # override the default output from pydantic by calling `to_dict()` of config_parameters
        if self.config_parameters:
            _dict['config_parameters'] = self.config_parameters.to_dict()
        # set to None if id (nullable) is None
        # and __fields_set__ contains the field
        if self.id is None and "id" in self.__fields_set__:
            _dict['id'] = None

        # set to None if created_at (nullable) is None
        # and __fields_set__ contains the field
        if self.created_at is None and "created_at" in self.__fields_set__:
            _dict['created_at'] = None

        # set to None if location (nullable) is None
        # and __fields_set__ contains the field
        if self.location is None and "location" in self.__fields_set__:
            _dict['location'] = None

        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict['name'] = None

        # set to None if networks (nullable) is None
        # and __fields_set__ contains the field
        if self.networks is None and "networks" in self.__fields_set__:
            _dict['networks'] = None

        # set to None if hash_type (nullable) is None
        # and __fields_set__ contains the field
        if self.hash_type is None and "hash_type" in self.__fields_set__:
            _dict['hash_type'] = None

        # set to None if avatar_link (nullable) is None
        # and __fields_set__ contains the field
        if self.avatar_link is None and "avatar_link" in self.__fields_set__:
            _dict['avatar_link'] = None

        # set to None if port (nullable) is None
        # and __fields_set__ contains the field
        if self.port is None and "port" in self.__fields_set__:
            _dict['port'] = None

        # set to None if status (nullable) is None
        # and __fields_set__ contains the field
        if self.status is None and "status" in self.__fields_set__:
            _dict['status'] = None

        # set to None if preset_id (nullable) is None
        # and __fields_set__ contains the field
        if self.preset_id is None and "preset_id" in self.__fields_set__:
            _dict['preset_id'] = None

        # set to None if is_enabled_public_network (nullable) is None
        # and __fields_set__ contains the field
        if self.is_enabled_public_network is None and "is_enabled_public_network" in self.__fields_set__:
            _dict['is_enabled_public_network'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DatabaseCluster:
        """Create an instance of DatabaseCluster from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DatabaseCluster.parse_obj(obj)

        _obj = DatabaseCluster.parse_obj({
            "id": obj.get("id"),
            "created_at": obj.get("created_at"),
            "location": obj.get("location"),
            "name": obj.get("name"),
            "networks": obj.get("networks"),
            "type": obj.get("type"),
            "hash_type": obj.get("hash_type"),
            "avatar_link": obj.get("avatar_link"),
            "port": obj.get("port"),
            "status": obj.get("status"),
            "preset_id": obj.get("preset_id"),
            "disk_stats": DatabaseClusterDiskStats.from_dict(obj.get("disk_stats")) if obj.get("disk_stats") is not None else None,
            "config_parameters": ConfigParameters.from_dict(obj.get("config_parameters")) if obj.get("config_parameters") is not None else None,
            "is_enabled_public_network": obj.get("is_enabled_public_network")
        })
        return _obj

