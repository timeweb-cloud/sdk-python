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
from timeweb_cloud_api.models.availability_zone import AvailabilityZone

class Balancer(BaseModel):
    """
    Балансировщик
    """
    id: Optional[Any] = Field(..., description="ID для каждого экземпляра балансировщика. Автоматически генерируется при создании.")
    algo: Optional[Any] = Field(..., description="Алгоритм переключений балансировщика.")
    created_at: Optional[Any] = Field(..., description="Значение времени, указанное в комбинированном формате даты и времени ISO8601, которое представляет, когда был создан балансировщик.")
    fall: Optional[Any] = Field(..., description="Порог количества ошибок.")
    inter: Optional[Any] = Field(..., description="Интервал проверки.")
    ip: Optional[Any] = Field(..., description="IP-адрес сетевого интерфейса IPv4.")
    local_ip: Optional[Any] = Field(..., description="Локальный IP-адрес сетевого интерфейса IPv4.")
    is_keepalive: Optional[Any] = Field(..., description="Это логическое значение, которое показывает, выдает ли балансировщик сигнал о проверке жизнеспособности.")
    name: Optional[Any] = Field(..., description="Удобочитаемое имя, установленное для балансировщика.")
    path: Optional[Any] = Field(..., description="Адрес балансировщика.")
    port: Optional[Any] = Field(..., description="Порт балансировщика.")
    proto: Optional[Any] = Field(..., description="Протокол.")
    rise: Optional[Any] = Field(..., description="Порог количества успешных ответов.")
    maxconn: Optional[Any] = Field(..., description="Максимальное количество соединений.")
    connect_timeout: Optional[Any] = Field(..., description="Таймаут подключения.")
    client_timeout: Optional[Any] = Field(..., description="Таймаут клиента.")
    server_timeout: Optional[Any] = Field(..., description="Таймаут сервера.")
    httprequest_timeout: Optional[Any] = Field(..., description="Таймаут HTTP запроса.")
    preset_id: Optional[Any] = Field(..., description="ID тарифа.")
    is_ssl: Optional[Any] = Field(..., description="Это логическое значение, которое показывает, требуется ли перенаправление на SSL.")
    status: Optional[Any] = Field(..., description="Статус балансировщика.")
    is_sticky: Optional[Any] = Field(..., description="Это логическое значение, которое показывает, сохраняется ли сессия.")
    timeout: Optional[Any] = Field(..., description="Таймаут ответа балансировщика.")
    avatar_link: Optional[Any] = Field(..., description="Ссылка на аватар балансировщика.")
    is_use_proxy: Optional[Any] = Field(..., description="Это логическое значение, которое показывает, выступает ли балансировщик в качестве прокси.")
    rules: Optional[Any] = Field(...)
    ips: Optional[Any] = Field(..., description="Список IP-адресов, привязанных к балансировщику")
    location: Optional[Any] = Field(..., description="Географическое расположение балансировщика")
    availability_zone: AvailabilityZone = Field(...)
    __properties = ["id", "algo", "created_at", "fall", "inter", "ip", "local_ip", "is_keepalive", "name", "path", "port", "proto", "rise", "maxconn", "connect_timeout", "client_timeout", "server_timeout", "httprequest_timeout", "preset_id", "is_ssl", "status", "is_sticky", "timeout", "avatar_link", "is_use_proxy", "rules", "ips", "location", "availability_zone"]

    @validator('algo')
    def algo_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('roundrobin', 'leastconn'):
            raise ValueError("must be one of enum values ('roundrobin', 'leastconn')")
        return value

    @validator('proto')
    def proto_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('http', 'http2', 'https', 'tcp'):
            raise ValueError("must be one of enum values ('http', 'http2', 'https', 'tcp')")
        return value

    @validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('started', 'stoped', 'starting', 'no_paid'):
            raise ValueError("must be one of enum values ('started', 'stoped', 'starting', 'no_paid')")
        return value

    @validator('location')
    def location_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('ru-1', 'pl-1'):
            raise ValueError("must be one of enum values ('ru-1', 'pl-1')")
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
    def from_json(cls, json_str: str) -> Balancer:
        """Create an instance of Balancer from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if id (nullable) is None
        # and __fields_set__ contains the field
        if self.id is None and "id" in self.__fields_set__:
            _dict['id'] = None

        # set to None if algo (nullable) is None
        # and __fields_set__ contains the field
        if self.algo is None and "algo" in self.__fields_set__:
            _dict['algo'] = None

        # set to None if created_at (nullable) is None
        # and __fields_set__ contains the field
        if self.created_at is None and "created_at" in self.__fields_set__:
            _dict['created_at'] = None

        # set to None if fall (nullable) is None
        # and __fields_set__ contains the field
        if self.fall is None and "fall" in self.__fields_set__:
            _dict['fall'] = None

        # set to None if inter (nullable) is None
        # and __fields_set__ contains the field
        if self.inter is None and "inter" in self.__fields_set__:
            _dict['inter'] = None

        # set to None if ip (nullable) is None
        # and __fields_set__ contains the field
        if self.ip is None and "ip" in self.__fields_set__:
            _dict['ip'] = None

        # set to None if local_ip (nullable) is None
        # and __fields_set__ contains the field
        if self.local_ip is None and "local_ip" in self.__fields_set__:
            _dict['local_ip'] = None

        # set to None if is_keepalive (nullable) is None
        # and __fields_set__ contains the field
        if self.is_keepalive is None and "is_keepalive" in self.__fields_set__:
            _dict['is_keepalive'] = None

        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict['name'] = None

        # set to None if path (nullable) is None
        # and __fields_set__ contains the field
        if self.path is None and "path" in self.__fields_set__:
            _dict['path'] = None

        # set to None if port (nullable) is None
        # and __fields_set__ contains the field
        if self.port is None and "port" in self.__fields_set__:
            _dict['port'] = None

        # set to None if proto (nullable) is None
        # and __fields_set__ contains the field
        if self.proto is None and "proto" in self.__fields_set__:
            _dict['proto'] = None

        # set to None if rise (nullable) is None
        # and __fields_set__ contains the field
        if self.rise is None and "rise" in self.__fields_set__:
            _dict['rise'] = None

        # set to None if maxconn (nullable) is None
        # and __fields_set__ contains the field
        if self.maxconn is None and "maxconn" in self.__fields_set__:
            _dict['maxconn'] = None

        # set to None if connect_timeout (nullable) is None
        # and __fields_set__ contains the field
        if self.connect_timeout is None and "connect_timeout" in self.__fields_set__:
            _dict['connect_timeout'] = None

        # set to None if client_timeout (nullable) is None
        # and __fields_set__ contains the field
        if self.client_timeout is None and "client_timeout" in self.__fields_set__:
            _dict['client_timeout'] = None

        # set to None if server_timeout (nullable) is None
        # and __fields_set__ contains the field
        if self.server_timeout is None and "server_timeout" in self.__fields_set__:
            _dict['server_timeout'] = None

        # set to None if httprequest_timeout (nullable) is None
        # and __fields_set__ contains the field
        if self.httprequest_timeout is None and "httprequest_timeout" in self.__fields_set__:
            _dict['httprequest_timeout'] = None

        # set to None if preset_id (nullable) is None
        # and __fields_set__ contains the field
        if self.preset_id is None and "preset_id" in self.__fields_set__:
            _dict['preset_id'] = None

        # set to None if is_ssl (nullable) is None
        # and __fields_set__ contains the field
        if self.is_ssl is None and "is_ssl" in self.__fields_set__:
            _dict['is_ssl'] = None

        # set to None if status (nullable) is None
        # and __fields_set__ contains the field
        if self.status is None and "status" in self.__fields_set__:
            _dict['status'] = None

        # set to None if is_sticky (nullable) is None
        # and __fields_set__ contains the field
        if self.is_sticky is None and "is_sticky" in self.__fields_set__:
            _dict['is_sticky'] = None

        # set to None if timeout (nullable) is None
        # and __fields_set__ contains the field
        if self.timeout is None and "timeout" in self.__fields_set__:
            _dict['timeout'] = None

        # set to None if avatar_link (nullable) is None
        # and __fields_set__ contains the field
        if self.avatar_link is None and "avatar_link" in self.__fields_set__:
            _dict['avatar_link'] = None

        # set to None if is_use_proxy (nullable) is None
        # and __fields_set__ contains the field
        if self.is_use_proxy is None and "is_use_proxy" in self.__fields_set__:
            _dict['is_use_proxy'] = None

        # set to None if rules (nullable) is None
        # and __fields_set__ contains the field
        if self.rules is None and "rules" in self.__fields_set__:
            _dict['rules'] = None

        # set to None if ips (nullable) is None
        # and __fields_set__ contains the field
        if self.ips is None and "ips" in self.__fields_set__:
            _dict['ips'] = None

        # set to None if location (nullable) is None
        # and __fields_set__ contains the field
        if self.location is None and "location" in self.__fields_set__:
            _dict['location'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Balancer:
        """Create an instance of Balancer from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Balancer.parse_obj(obj)

        _obj = Balancer.parse_obj({
            "id": obj.get("id"),
            "algo": obj.get("algo"),
            "created_at": obj.get("created_at"),
            "fall": obj.get("fall"),
            "inter": obj.get("inter"),
            "ip": obj.get("ip"),
            "local_ip": obj.get("local_ip"),
            "is_keepalive": obj.get("is_keepalive"),
            "name": obj.get("name"),
            "path": obj.get("path"),
            "port": obj.get("port"),
            "proto": obj.get("proto"),
            "rise": obj.get("rise"),
            "maxconn": obj.get("maxconn"),
            "connect_timeout": obj.get("connect_timeout"),
            "client_timeout": obj.get("client_timeout"),
            "server_timeout": obj.get("server_timeout"),
            "httprequest_timeout": obj.get("httprequest_timeout"),
            "preset_id": obj.get("preset_id"),
            "is_ssl": obj.get("is_ssl"),
            "status": obj.get("status"),
            "is_sticky": obj.get("is_sticky"),
            "timeout": obj.get("timeout"),
            "avatar_link": obj.get("avatar_link"),
            "is_use_proxy": obj.get("is_use_proxy"),
            "rules": obj.get("rules"),
            "ips": obj.get("ips"),
            "location": obj.get("location"),
            "availability_zone": obj.get("availability_zone")
        })
        return _obj

