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
from timeweb_cloud_api.models.mailbox_auto_reply import MailboxAutoReply
from timeweb_cloud_api.models.mailbox_forwarding_incoming import MailboxForwardingIncoming
from timeweb_cloud_api.models.mailbox_forwarding_outgoing import MailboxForwardingOutgoing
from timeweb_cloud_api.models.mailbox_spam_filter import MailboxSpamFilter

class Mailbox(BaseModel):
    """
    Почтовый ящик
    """
    auto_reply: MailboxAutoReply = Field(...)
    spam_filter: MailboxSpamFilter = Field(...)
    forwarding_incoming: MailboxForwardingIncoming = Field(...)
    forwarding_outgoing: MailboxForwardingOutgoing = Field(...)
    comment: Optional[Any] = Field(..., description="Комментарий к почтовому ящику")
    fqdn: Optional[Any] = Field(..., description="Домен почты")
    mailbox: Optional[Any] = Field(..., description="Название почтового ящика")
    password: Optional[Any] = Field(..., description="Пароль почтового ящика")
    usage_space: Optional[Any] = Field(..., description="Использованное место на почтовом ящике (в Мб)")
    is_webmail: Optional[Any] = Field(..., description="Доступен ли Webmail")
    idn_name: Optional[Any] = Field(..., description="IDN домен почтового ящика")
    is_dovecot: Optional[Any] = Field(..., description="Есть ли доступ через dovecot")
    __properties = ["auto_reply", "spam_filter", "forwarding_incoming", "forwarding_outgoing", "comment", "fqdn", "mailbox", "password", "usage_space", "is_webmail", "idn_name", "is_dovecot"]

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
    def from_json(cls, json_str: str) -> Mailbox:
        """Create an instance of Mailbox from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of auto_reply
        if self.auto_reply:
            _dict['auto_reply'] = self.auto_reply.to_dict()
        # override the default output from pydantic by calling `to_dict()` of spam_filter
        if self.spam_filter:
            _dict['spam_filter'] = self.spam_filter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of forwarding_incoming
        if self.forwarding_incoming:
            _dict['forwarding_incoming'] = self.forwarding_incoming.to_dict()
        # override the default output from pydantic by calling `to_dict()` of forwarding_outgoing
        if self.forwarding_outgoing:
            _dict['forwarding_outgoing'] = self.forwarding_outgoing.to_dict()
        # set to None if comment (nullable) is None
        # and __fields_set__ contains the field
        if self.comment is None and "comment" in self.__fields_set__:
            _dict['comment'] = None

        # set to None if fqdn (nullable) is None
        # and __fields_set__ contains the field
        if self.fqdn is None and "fqdn" in self.__fields_set__:
            _dict['fqdn'] = None

        # set to None if mailbox (nullable) is None
        # and __fields_set__ contains the field
        if self.mailbox is None and "mailbox" in self.__fields_set__:
            _dict['mailbox'] = None

        # set to None if password (nullable) is None
        # and __fields_set__ contains the field
        if self.password is None and "password" in self.__fields_set__:
            _dict['password'] = None

        # set to None if usage_space (nullable) is None
        # and __fields_set__ contains the field
        if self.usage_space is None and "usage_space" in self.__fields_set__:
            _dict['usage_space'] = None

        # set to None if is_webmail (nullable) is None
        # and __fields_set__ contains the field
        if self.is_webmail is None and "is_webmail" in self.__fields_set__:
            _dict['is_webmail'] = None

        # set to None if idn_name (nullable) is None
        # and __fields_set__ contains the field
        if self.idn_name is None and "idn_name" in self.__fields_set__:
            _dict['idn_name'] = None

        # set to None if is_dovecot (nullable) is None
        # and __fields_set__ contains the field
        if self.is_dovecot is None and "is_dovecot" in self.__fields_set__:
            _dict['is_dovecot'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Mailbox:
        """Create an instance of Mailbox from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Mailbox.parse_obj(obj)

        _obj = Mailbox.parse_obj({
            "auto_reply": MailboxAutoReply.from_dict(obj.get("auto_reply")) if obj.get("auto_reply") is not None else None,
            "spam_filter": MailboxSpamFilter.from_dict(obj.get("spam_filter")) if obj.get("spam_filter") is not None else None,
            "forwarding_incoming": MailboxForwardingIncoming.from_dict(obj.get("forwarding_incoming")) if obj.get("forwarding_incoming") is not None else None,
            "forwarding_outgoing": MailboxForwardingOutgoing.from_dict(obj.get("forwarding_outgoing")) if obj.get("forwarding_outgoing") is not None else None,
            "comment": obj.get("comment"),
            "fqdn": obj.get("fqdn"),
            "mailbox": obj.get("mailbox"),
            "password": obj.get("password"),
            "usage_space": obj.get("usage_space"),
            "is_webmail": obj.get("is_webmail"),
            "idn_name": obj.get("idn_name"),
            "is_dovecot": obj.get("is_dovecot")
        })
        return _obj

