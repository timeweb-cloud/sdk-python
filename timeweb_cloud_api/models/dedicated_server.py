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

class DedicatedServer(BaseModel):
    """
    Выделенный сервер
    """
    id: Optional[Any] = Field(..., description="ID для каждого экземпляра выделенного сервера. Автоматически генерируется при создании.")
    cpu_description: Optional[Any] = Field(..., description="Описание параметров процессора выделенного сервера.")
    hdd_description: Optional[Any] = Field(..., description="Описание параметров жёсткого диска выделенного сервера.")
    ram_description: Optional[Any] = Field(..., description="Описание ОЗУ выделенного сервера.")
    created_at: Optional[Any] = Field(..., description="Значение времени, указанное в комбинированном формате даты и времени ISO8601, которое представляет, когда был создан выделенный сервер.")
    ip: Optional[Any] = Field(..., description="IP-адрес сетевого интерфейса IPv4.")
    ipmi_ip: Optional[Any] = Field(..., description="IP-адрес сетевого интерфейса IPMI.")
    ipmi_login: Optional[Any] = Field(..., description="Логин, используемый для входа в IPMI-консоль.")
    ipmi_password: Optional[Any] = Field(..., description="Пароль, используемый для входа в IPMI-консоль.")
    ipv6: Optional[Any] = Field(..., description="IP-адрес сетевого интерфейса IPv6.")
    node_id: Optional[Any] = Field(..., description="Внутренний дополнительный ID сервера.")
    name: Optional[Any] = Field(..., description="Удобочитаемое имя, установленное для выделенного сервера.")
    comment: Optional[Any] = Field(..., description="Комментарий к выделенному серверу.")
    vnc_pass: Optional[Any] = Field(..., description="Пароль для подключения к VNC-консоли выделенного сервера.")
    status: Optional[Any] = Field(..., description="Строка состояния, указывающая состояние выделенного сервера. Может быть «installing», «installed», «on» или «off».")
    os_id: Optional[Any] = Field(..., description="ID операционной системы, установленной на выделенный сервер.")
    cp_id: Optional[Any] = Field(..., description="ID панели управления, установленной на выделенный сервер.")
    bandwidth_id: Optional[Any] = Field(..., description="ID интернет-канала, установленного на выделенный сервер.")
    network_drive_id: Optional[Any] = Field(..., description="Массив уникальных ID сетевых дисков, подключенных к выделенному серверу.")
    additional_ip_addr_id: Optional[Any] = Field(..., description="Массив уникальных ID дополнительных IP-адресов, подключенных к выделенному серверу.")
    plan_id: Optional[Any] = Field(..., description="ID списка дополнительных услуг выделенного сервера.")
    price: Optional[Any] = Field(..., description="Стоимость выделенного сервера.")
    location: Optional[Any] = Field(..., description="Локация сервера.")
    autoinstall_ready: Optional[Any] = Field(..., description="Количество готовых к автоматической выдаче серверов. Если значение равно 0, сервер будет установлен через инженеров.")
    password: Optional[Any] = Field(..., description="Пароль root сервера или пароль Администратора для серверов Windows.")
    __properties = ["id", "cpu_description", "hdd_description", "ram_description", "created_at", "ip", "ipmi_ip", "ipmi_login", "ipmi_password", "ipv6", "node_id", "name", "comment", "vnc_pass", "status", "os_id", "cp_id", "bandwidth_id", "network_drive_id", "additional_ip_addr_id", "plan_id", "price", "location", "autoinstall_ready", "password"]

    @validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('installing', 'installed', 'on', 'off'):
            raise ValueError("must be one of enum values ('installing', 'installed', 'on', 'off')")
        return value

    @validator('location')
    def location_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('ru-1', 'pl-1', 'kz-1', 'nl-1', 'tr-1', 'us-2', 'de-1', 'fi-1'):
            raise ValueError("must be one of enum values ('ru-1', 'pl-1', 'kz-1', 'nl-1', 'tr-1', 'us-2', 'de-1', 'fi-1')")
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
    def from_json(cls, json_str: str) -> DedicatedServer:
        """Create an instance of DedicatedServer from a JSON string"""
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

        # set to None if cpu_description (nullable) is None
        # and __fields_set__ contains the field
        if self.cpu_description is None and "cpu_description" in self.__fields_set__:
            _dict['cpu_description'] = None

        # set to None if hdd_description (nullable) is None
        # and __fields_set__ contains the field
        if self.hdd_description is None and "hdd_description" in self.__fields_set__:
            _dict['hdd_description'] = None

        # set to None if ram_description (nullable) is None
        # and __fields_set__ contains the field
        if self.ram_description is None and "ram_description" in self.__fields_set__:
            _dict['ram_description'] = None

        # set to None if created_at (nullable) is None
        # and __fields_set__ contains the field
        if self.created_at is None and "created_at" in self.__fields_set__:
            _dict['created_at'] = None

        # set to None if ip (nullable) is None
        # and __fields_set__ contains the field
        if self.ip is None and "ip" in self.__fields_set__:
            _dict['ip'] = None

        # set to None if ipmi_ip (nullable) is None
        # and __fields_set__ contains the field
        if self.ipmi_ip is None and "ipmi_ip" in self.__fields_set__:
            _dict['ipmi_ip'] = None

        # set to None if ipmi_login (nullable) is None
        # and __fields_set__ contains the field
        if self.ipmi_login is None and "ipmi_login" in self.__fields_set__:
            _dict['ipmi_login'] = None

        # set to None if ipmi_password (nullable) is None
        # and __fields_set__ contains the field
        if self.ipmi_password is None and "ipmi_password" in self.__fields_set__:
            _dict['ipmi_password'] = None

        # set to None if ipv6 (nullable) is None
        # and __fields_set__ contains the field
        if self.ipv6 is None and "ipv6" in self.__fields_set__:
            _dict['ipv6'] = None

        # set to None if node_id (nullable) is None
        # and __fields_set__ contains the field
        if self.node_id is None and "node_id" in self.__fields_set__:
            _dict['node_id'] = None

        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict['name'] = None

        # set to None if comment (nullable) is None
        # and __fields_set__ contains the field
        if self.comment is None and "comment" in self.__fields_set__:
            _dict['comment'] = None

        # set to None if vnc_pass (nullable) is None
        # and __fields_set__ contains the field
        if self.vnc_pass is None and "vnc_pass" in self.__fields_set__:
            _dict['vnc_pass'] = None

        # set to None if status (nullable) is None
        # and __fields_set__ contains the field
        if self.status is None and "status" in self.__fields_set__:
            _dict['status'] = None

        # set to None if os_id (nullable) is None
        # and __fields_set__ contains the field
        if self.os_id is None and "os_id" in self.__fields_set__:
            _dict['os_id'] = None

        # set to None if cp_id (nullable) is None
        # and __fields_set__ contains the field
        if self.cp_id is None and "cp_id" in self.__fields_set__:
            _dict['cp_id'] = None

        # set to None if bandwidth_id (nullable) is None
        # and __fields_set__ contains the field
        if self.bandwidth_id is None and "bandwidth_id" in self.__fields_set__:
            _dict['bandwidth_id'] = None

        # set to None if network_drive_id (nullable) is None
        # and __fields_set__ contains the field
        if self.network_drive_id is None and "network_drive_id" in self.__fields_set__:
            _dict['network_drive_id'] = None

        # set to None if additional_ip_addr_id (nullable) is None
        # and __fields_set__ contains the field
        if self.additional_ip_addr_id is None and "additional_ip_addr_id" in self.__fields_set__:
            _dict['additional_ip_addr_id'] = None

        # set to None if plan_id (nullable) is None
        # and __fields_set__ contains the field
        if self.plan_id is None and "plan_id" in self.__fields_set__:
            _dict['plan_id'] = None

        # set to None if price (nullable) is None
        # and __fields_set__ contains the field
        if self.price is None and "price" in self.__fields_set__:
            _dict['price'] = None

        # set to None if location (nullable) is None
        # and __fields_set__ contains the field
        if self.location is None and "location" in self.__fields_set__:
            _dict['location'] = None

        # set to None if autoinstall_ready (nullable) is None
        # and __fields_set__ contains the field
        if self.autoinstall_ready is None and "autoinstall_ready" in self.__fields_set__:
            _dict['autoinstall_ready'] = None

        # set to None if password (nullable) is None
        # and __fields_set__ contains the field
        if self.password is None and "password" in self.__fields_set__:
            _dict['password'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DedicatedServer:
        """Create an instance of DedicatedServer from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DedicatedServer.parse_obj(obj)

        _obj = DedicatedServer.parse_obj({
            "id": obj.get("id"),
            "cpu_description": obj.get("cpu_description"),
            "hdd_description": obj.get("hdd_description"),
            "ram_description": obj.get("ram_description"),
            "created_at": obj.get("created_at"),
            "ip": obj.get("ip"),
            "ipmi_ip": obj.get("ipmi_ip"),
            "ipmi_login": obj.get("ipmi_login"),
            "ipmi_password": obj.get("ipmi_password"),
            "ipv6": obj.get("ipv6"),
            "node_id": obj.get("node_id"),
            "name": obj.get("name"),
            "comment": obj.get("comment"),
            "vnc_pass": obj.get("vnc_pass"),
            "status": obj.get("status"),
            "os_id": obj.get("os_id"),
            "cp_id": obj.get("cp_id"),
            "bandwidth_id": obj.get("bandwidth_id"),
            "network_drive_id": obj.get("network_drive_id"),
            "additional_ip_addr_id": obj.get("additional_ip_addr_id"),
            "plan_id": obj.get("plan_id"),
            "price": obj.get("price"),
            "location": obj.get("location"),
            "autoinstall_ready": obj.get("autoinstall_ready"),
            "password": obj.get("password")
        })
        return _obj

