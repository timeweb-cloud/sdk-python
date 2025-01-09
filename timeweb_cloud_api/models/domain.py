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

class Domain(BaseModel):
    """
    Домен
    """
    allowed_buy_periods: Optional[Any] = Field(..., description="Допустимые периоды продления домена.")
    days_left: Optional[Any] = Field(..., description="Количество дней, оставшихся до конца срока регистрации домена.")
    domain_status: Optional[Any] = Field(..., description="Статус домена.")
    expiration: Optional[Any] = Field(..., description="Дата окончания срока регистрации домена, для доменов без срока окончания регистрации будет приходить 0000-00-00.")
    fqdn: Optional[Any] = Field(..., description="Полное имя домена.")
    id: Optional[Any] = Field(..., description="ID домена.")
    is_autoprolong_enabled: Optional[Any] = Field(..., description="Это логическое значение, которое показывает, включено ли автопродление домена.")
    is_premium: Optional[Any] = Field(..., description="Это логическое значение, которое показывает, является ли домен премиальным.")
    is_prolong_allowed: Optional[Any] = Field(..., description="Это логическое значение, которое показывает, можно ли сейчас продлить домен.")
    is_technical: Optional[Any] = Field(..., description="Это логическое значение, которое показывает, является ли домен техническим.")
    is_whois_privacy_enabled: Optional[Any] = Field(..., description="Это логическое значение, которое показывает, включено ли скрытие данных администратора домена для whois. Если приходит null, значит для данной зоны эта услуга не доступна.")
    linked_ip: Optional[Any] = Field(..., description="Привязанный к домену IP-адрес.")
    paid_till: Optional[Any] = Field(..., description="До какого числа оплачен домен.")
    person_id: Optional[Any] = Field(..., description="ID администратора, на которого зарегистрирован домен.")
    premium_prolong_cost: Optional[Any] = Field(..., description="Стоимость премиального домена.")
    provider: Optional[Any] = Field(..., description="ID регистратора домена.")
    request_status: Optional[Any] = Field(..., description="Статус заявки на продление/регистрацию/трансфер домена.")
    subdomains: Optional[Any] = Field(..., description="Список поддоменов.")
    tld_id: Optional[Any] = Field(..., description="ID доменной зоны.")
    __properties = ["allowed_buy_periods", "days_left", "domain_status", "expiration", "fqdn", "id", "is_autoprolong_enabled", "is_premium", "is_prolong_allowed", "is_technical", "is_whois_privacy_enabled", "linked_ip", "paid_till", "person_id", "premium_prolong_cost", "provider", "request_status", "subdomains", "tld_id"]

    @validator('domain_status')
    def domain_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('awaiting_payment', 'expired', 'final_expired', 'free', 'no_paid', 'ns_based', 'paid', 'soon_expire', 'today_expired'):
            raise ValueError("must be one of enum values ('awaiting_payment', 'expired', 'final_expired', 'free', 'no_paid', 'ns_based', 'paid', 'soon_expire', 'today_expired')")
        return value

    @validator('request_status')
    def request_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('prolongation_fail', 'prolongation_request', 'registration_fail', 'registration_request', 'transfer_fail', 'transfer_request', 'awaiting_person'):
            raise ValueError("must be one of enum values ('prolongation_fail', 'prolongation_request', 'registration_fail', 'registration_request', 'transfer_fail', 'transfer_request', 'awaiting_person')")
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
    def from_json(cls, json_str: str) -> Domain:
        """Create an instance of Domain from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if allowed_buy_periods (nullable) is None
        # and __fields_set__ contains the field
        if self.allowed_buy_periods is None and "allowed_buy_periods" in self.__fields_set__:
            _dict['allowed_buy_periods'] = None

        # set to None if days_left (nullable) is None
        # and __fields_set__ contains the field
        if self.days_left is None and "days_left" in self.__fields_set__:
            _dict['days_left'] = None

        # set to None if domain_status (nullable) is None
        # and __fields_set__ contains the field
        if self.domain_status is None and "domain_status" in self.__fields_set__:
            _dict['domain_status'] = None

        # set to None if expiration (nullable) is None
        # and __fields_set__ contains the field
        if self.expiration is None and "expiration" in self.__fields_set__:
            _dict['expiration'] = None

        # set to None if fqdn (nullable) is None
        # and __fields_set__ contains the field
        if self.fqdn is None and "fqdn" in self.__fields_set__:
            _dict['fqdn'] = None

        # set to None if id (nullable) is None
        # and __fields_set__ contains the field
        if self.id is None and "id" in self.__fields_set__:
            _dict['id'] = None

        # set to None if is_autoprolong_enabled (nullable) is None
        # and __fields_set__ contains the field
        if self.is_autoprolong_enabled is None and "is_autoprolong_enabled" in self.__fields_set__:
            _dict['is_autoprolong_enabled'] = None

        # set to None if is_premium (nullable) is None
        # and __fields_set__ contains the field
        if self.is_premium is None and "is_premium" in self.__fields_set__:
            _dict['is_premium'] = None

        # set to None if is_prolong_allowed (nullable) is None
        # and __fields_set__ contains the field
        if self.is_prolong_allowed is None and "is_prolong_allowed" in self.__fields_set__:
            _dict['is_prolong_allowed'] = None

        # set to None if is_technical (nullable) is None
        # and __fields_set__ contains the field
        if self.is_technical is None and "is_technical" in self.__fields_set__:
            _dict['is_technical'] = None

        # set to None if is_whois_privacy_enabled (nullable) is None
        # and __fields_set__ contains the field
        if self.is_whois_privacy_enabled is None and "is_whois_privacy_enabled" in self.__fields_set__:
            _dict['is_whois_privacy_enabled'] = None

        # set to None if linked_ip (nullable) is None
        # and __fields_set__ contains the field
        if self.linked_ip is None and "linked_ip" in self.__fields_set__:
            _dict['linked_ip'] = None

        # set to None if paid_till (nullable) is None
        # and __fields_set__ contains the field
        if self.paid_till is None and "paid_till" in self.__fields_set__:
            _dict['paid_till'] = None

        # set to None if person_id (nullable) is None
        # and __fields_set__ contains the field
        if self.person_id is None and "person_id" in self.__fields_set__:
            _dict['person_id'] = None

        # set to None if premium_prolong_cost (nullable) is None
        # and __fields_set__ contains the field
        if self.premium_prolong_cost is None and "premium_prolong_cost" in self.__fields_set__:
            _dict['premium_prolong_cost'] = None

        # set to None if provider (nullable) is None
        # and __fields_set__ contains the field
        if self.provider is None and "provider" in self.__fields_set__:
            _dict['provider'] = None

        # set to None if request_status (nullable) is None
        # and __fields_set__ contains the field
        if self.request_status is None and "request_status" in self.__fields_set__:
            _dict['request_status'] = None

        # set to None if subdomains (nullable) is None
        # and __fields_set__ contains the field
        if self.subdomains is None and "subdomains" in self.__fields_set__:
            _dict['subdomains'] = None

        # set to None if tld_id (nullable) is None
        # and __fields_set__ contains the field
        if self.tld_id is None and "tld_id" in self.__fields_set__:
            _dict['tld_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Domain:
        """Create an instance of Domain from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Domain.parse_obj(obj)

        _obj = Domain.parse_obj({
            "allowed_buy_periods": obj.get("allowed_buy_periods"),
            "days_left": obj.get("days_left"),
            "domain_status": obj.get("domain_status"),
            "expiration": obj.get("expiration"),
            "fqdn": obj.get("fqdn"),
            "id": obj.get("id"),
            "is_autoprolong_enabled": obj.get("is_autoprolong_enabled"),
            "is_premium": obj.get("is_premium"),
            "is_prolong_allowed": obj.get("is_prolong_allowed"),
            "is_technical": obj.get("is_technical"),
            "is_whois_privacy_enabled": obj.get("is_whois_privacy_enabled"),
            "linked_ip": obj.get("linked_ip"),
            "paid_till": obj.get("paid_till"),
            "person_id": obj.get("person_id"),
            "premium_prolong_cost": obj.get("premium_prolong_cost"),
            "provider": obj.get("provider"),
            "request_status": obj.get("request_status"),
            "subdomains": obj.get("subdomains"),
            "tld_id": obj.get("tld_id")
        })
        return _obj

