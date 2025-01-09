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
from timeweb_cloud_api.models.app_configuration import AppConfiguration
from timeweb_cloud_api.models.app_disk_status import AppDiskStatus
from timeweb_cloud_api.models.app_provider import AppProvider
from timeweb_cloud_api.models.frameworks import Frameworks
from timeweb_cloud_api.models.repository import Repository

class App(BaseModel):
    """
    Экземпляр приложения.
    """
    id: Optional[Any] = Field(..., description="ID для каждого экземпляра приложения. Автоматически генерируется при создании.")
    type: Optional[Any] = Field(..., description="Тип приложения.")
    name: Optional[Any] = Field(..., description="Удобочитаемое имя, установленное для приложения.")
    status: Optional[Any] = Field(..., description="Статус приложения.")
    provider: AppProvider = Field(...)
    ip: Optional[Any] = Field(..., description="IPv4-адрес приложения.")
    domains: Optional[Any] = Field(...)
    framework: Frameworks = Field(...)
    location: Optional[Any] = Field(..., description="Локация сервера.")
    repository: Repository = Field(...)
    env_version: Optional[Any] = Field(..., description="Версия окружения.")
    envs: Optional[Any] = Field(..., description="Переменные окружения приложения. Объект с ключами и значениями типа string.")
    branch_name: Optional[Any] = Field(..., description="Название ветки репозитория из которой собрано приложение.")
    is_auto_deploy: Optional[Any] = Field(..., description="Включен ли автоматический деплой.")
    commit_sha: Optional[Any] = Field(..., description="Хэш коммита из которого собрано приложеие.")
    comment: Optional[Any] = Field(..., description="Комментарий к приложению.")
    preset_id: Optional[Any] = Field(..., description="ID тарифа.")
    index_dir: Optional[Any] = Field(..., description="Путь к директории с индексным файлом. Определен для приложений `type: frontend`. Для приложений `type: backend` всегда null.")
    build_cmd: Optional[Any] = Field(..., description="Команда сборки приложения.")
    run_cmd: Optional[Any] = Field(..., description="Команда для запуска приложения. Определена для приложений `type: backend`. Для приложений `type: frontend` всегда null.")
    configuration: AppConfiguration = Field(...)
    disk_status: AppDiskStatus = Field(...)
    is_qemu_agent: Optional[Any] = Field(..., description="Включен ли агент QEMU.")
    language: Optional[Any] = Field(..., description="Язык программирования приложения.")
    start_time: Optional[Any] = Field(..., description="Время запуска приложения.")
    __properties = ["id", "type", "name", "status", "provider", "ip", "domains", "framework", "location", "repository", "env_version", "envs", "branch_name", "is_auto_deploy", "commit_sha", "comment", "preset_id", "index_dir", "build_cmd", "run_cmd", "configuration", "disk_status", "is_qemu_agent", "language", "start_time"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('backend', 'frontend'):
            raise ValueError("must be one of enum values ('backend', 'frontend')")
        return value

    @validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('active', 'paused', 'no_paid', 'deploy', 'failure', 'startup_error', 'new', 'reboot'):
            raise ValueError("must be one of enum values ('active', 'paused', 'no_paid', 'deploy', 'failure', 'startup_error', 'new', 'reboot')")
        return value

    @validator('location')
    def location_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('ru-1', 'pl-1', 'nl-1'):
            raise ValueError("must be one of enum values ('ru-1', 'pl-1', 'nl-1')")
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
    def from_json(cls, json_str: str) -> App:
        """Create an instance of App from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of provider
        if self.provider:
            _dict['provider'] = self.provider.to_dict()
        # override the default output from pydantic by calling `to_dict()` of repository
        if self.repository:
            _dict['repository'] = self.repository.to_dict()
        # override the default output from pydantic by calling `to_dict()` of configuration
        if self.configuration:
            _dict['configuration'] = self.configuration.to_dict()
        # override the default output from pydantic by calling `to_dict()` of disk_status
        if self.disk_status:
            _dict['disk_status'] = self.disk_status.to_dict()
        # set to None if id (nullable) is None
        # and __fields_set__ contains the field
        if self.id is None and "id" in self.__fields_set__:
            _dict['id'] = None

        # set to None if type (nullable) is None
        # and __fields_set__ contains the field
        if self.type is None and "type" in self.__fields_set__:
            _dict['type'] = None

        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict['name'] = None

        # set to None if status (nullable) is None
        # and __fields_set__ contains the field
        if self.status is None and "status" in self.__fields_set__:
            _dict['status'] = None

        # set to None if ip (nullable) is None
        # and __fields_set__ contains the field
        if self.ip is None and "ip" in self.__fields_set__:
            _dict['ip'] = None

        # set to None if domains (nullable) is None
        # and __fields_set__ contains the field
        if self.domains is None and "domains" in self.__fields_set__:
            _dict['domains'] = None

        # set to None if location (nullable) is None
        # and __fields_set__ contains the field
        if self.location is None and "location" in self.__fields_set__:
            _dict['location'] = None

        # set to None if env_version (nullable) is None
        # and __fields_set__ contains the field
        if self.env_version is None and "env_version" in self.__fields_set__:
            _dict['env_version'] = None

        # set to None if envs (nullable) is None
        # and __fields_set__ contains the field
        if self.envs is None and "envs" in self.__fields_set__:
            _dict['envs'] = None

        # set to None if branch_name (nullable) is None
        # and __fields_set__ contains the field
        if self.branch_name is None and "branch_name" in self.__fields_set__:
            _dict['branch_name'] = None

        # set to None if is_auto_deploy (nullable) is None
        # and __fields_set__ contains the field
        if self.is_auto_deploy is None and "is_auto_deploy" in self.__fields_set__:
            _dict['is_auto_deploy'] = None

        # set to None if commit_sha (nullable) is None
        # and __fields_set__ contains the field
        if self.commit_sha is None and "commit_sha" in self.__fields_set__:
            _dict['commit_sha'] = None

        # set to None if comment (nullable) is None
        # and __fields_set__ contains the field
        if self.comment is None and "comment" in self.__fields_set__:
            _dict['comment'] = None

        # set to None if preset_id (nullable) is None
        # and __fields_set__ contains the field
        if self.preset_id is None and "preset_id" in self.__fields_set__:
            _dict['preset_id'] = None

        # set to None if index_dir (nullable) is None
        # and __fields_set__ contains the field
        if self.index_dir is None and "index_dir" in self.__fields_set__:
            _dict['index_dir'] = None

        # set to None if build_cmd (nullable) is None
        # and __fields_set__ contains the field
        if self.build_cmd is None and "build_cmd" in self.__fields_set__:
            _dict['build_cmd'] = None

        # set to None if run_cmd (nullable) is None
        # and __fields_set__ contains the field
        if self.run_cmd is None and "run_cmd" in self.__fields_set__:
            _dict['run_cmd'] = None

        # set to None if is_qemu_agent (nullable) is None
        # and __fields_set__ contains the field
        if self.is_qemu_agent is None and "is_qemu_agent" in self.__fields_set__:
            _dict['is_qemu_agent'] = None

        # set to None if language (nullable) is None
        # and __fields_set__ contains the field
        if self.language is None and "language" in self.__fields_set__:
            _dict['language'] = None

        # set to None if start_time (nullable) is None
        # and __fields_set__ contains the field
        if self.start_time is None and "start_time" in self.__fields_set__:
            _dict['start_time'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> App:
        """Create an instance of App from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return App.parse_obj(obj)

        _obj = App.parse_obj({
            "id": obj.get("id"),
            "type": obj.get("type"),
            "name": obj.get("name"),
            "status": obj.get("status"),
            "provider": AppProvider.from_dict(obj.get("provider")) if obj.get("provider") is not None else None,
            "ip": obj.get("ip"),
            "domains": obj.get("domains"),
            "framework": obj.get("framework"),
            "location": obj.get("location"),
            "repository": Repository.from_dict(obj.get("repository")) if obj.get("repository") is not None else None,
            "env_version": obj.get("env_version"),
            "envs": obj.get("envs"),
            "branch_name": obj.get("branch_name"),
            "is_auto_deploy": obj.get("is_auto_deploy"),
            "commit_sha": obj.get("commit_sha"),
            "comment": obj.get("comment"),
            "preset_id": obj.get("preset_id"),
            "index_dir": obj.get("index_dir"),
            "build_cmd": obj.get("build_cmd"),
            "run_cmd": obj.get("run_cmd"),
            "configuration": AppConfiguration.from_dict(obj.get("configuration")) if obj.get("configuration") is not None else None,
            "disk_status": AppDiskStatus.from_dict(obj.get("disk_status")) if obj.get("disk_status") is not None else None,
            "is_qemu_agent": obj.get("is_qemu_agent"),
            "language": obj.get("language"),
            "start_time": obj.get("start_time")
        })
        return _obj

