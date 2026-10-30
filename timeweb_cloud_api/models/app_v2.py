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
from timeweb_cloud_api.models.app_v2_configuration import AppV2Configuration
from timeweb_cloud_api.models.app_v2_disk_status import AppV2DiskStatus
from timeweb_cloud_api.models.app_v2_provider import AppV2Provider
from timeweb_cloud_api.models.repository import Repository

class AppV2(BaseModel):
    """
    Приложение v2. Создание и первый деплой выполняются асинхронно. Поля сервера и инфраструктуры могут отсутствовать, пока соответствующие ресурсы не созданы.
    """
    id: Optional[Any] = Field(..., description="ID для каждого экземпляра приложения. Автоматически генерируется при создании.")
    type: Optional[Any] = Field(..., description="Тип приложения.")
    name: Optional[Any] = Field(..., description="Удобочитаемое имя, установленное для приложения.")
    status: Optional[Any] = Field(..., description="Текущее состояние приложения. После принятия запроса на создание — new. Ответ 201 не означает завершение развёртывания.")
    provider: AppV2Provider = Field(...)
    ip: Optional[Any] = Field(None, description="Публичный IPv4-адрес. Отсутствует, пока сервер и IP-адрес не созданы.")
    domains: Optional[Any] = Field(..., description="Домены приложения. В начальном ответе на создание массив пуст.")
    framework: Optional[Any] = Field(None, description="Фреймворк приложения. Поле может отсутствовать до создания инфраструктуры.")
    location: Optional[Any] = Field(None, description="Локация сервера. Может отсутствовать до создания сервера.")
    repository: Optional[Repository] = None
    env_version: Optional[Any] = Field(None, description="Версия окружения. Поле может отсутствовать до создания инфраструктуры.")
    envs: Optional[Any] = Field(None, description="Переменные окружения приложения. Объект с ключами и значениями типа string. Поле может отсутствовать до создания инфраструктуры.")
    is_auto_deploy: Optional[Any] = Field(..., description="Включен ли автоматический деплой.")
    commit_sha: Optional[Any] = Field(None, description="Хэш коммита, из которого собрано приложение.")
    comment: Optional[Any] = Field(None, description="Комментарий к приложению.")
    preset_id: Optional[Any] = Field(..., description="ID тарифа приложения; 0 при использовании конфигуратора.")
    index_dir: Optional[Any] = Field(None, description="Каталог со статическими файлами frontend-приложения. До создания инфраструктуры поле отсутствует. Для backend — null.")
    build_cmd: Optional[Any] = Field(None, description="Команда сборки приложения. Поле может отсутствовать до создания инфраструктуры.")
    avatar_link: Optional[Any] = Field(..., description="Ссылка на аватар приложения.")
    run_cmd: Optional[Any] = Field(None, description="Команда запуска backend-приложения. До создания инфраструктуры поле отсутствует. Для frontend — null.")
    configuration: Optional[AppV2Configuration] = None
    disk_status: Optional[AppV2DiskStatus] = None
    is_qemu_agent: Optional[Any] = Field(None, description="Включён ли агент QEMU. Для frontend — null. Для backend поле отсутствует до создания сервера.")
    language: Optional[Any] = Field(None, description="Язык или способ развёртывания. Может отсутствовать до создания инфраструктуры. Поле может отсутствовать до создания инфраструктуры.")
    start_time: Optional[Any] = Field(..., description="Время последнего изменения записи приложения.")
    branch: Optional[Any] = Field(None, description="Ветка Git-репозитория. В ответе v2 поле называется branch.")
    configurator_id: Optional[Any] = Field(..., description="ID конфигуратора приложения; null при использовании готового тарифа.")
    project_id: Optional[Any] = Field(None, description="ID проекта приложения. Может отсутствовать, если проект не задан.")
    system_dependencies: Optional[Any] = Field(None, description="Системные пакеты приложения. Поле отсутствует, если зависимости не заданы.")
    created_at: Optional[Any] = Field(..., description="Время создания записи приложения.")
    availability_zone: Optional[Any] = Field(None, description="Зона доступности сервера. Может быть null или отсутствовать до создания сервера.")
    requests_limit: Optional[Any] = Field(..., description="Ограничение количества запросов; null, если индивидуальный лимит не задан.")
    build_entry_path: Optional[Any] = Field(None, description="Каталог приложения в Git-репозитории, относительно которого выполняется сборка. Может отсутствовать до создания инфраструктуры.")
    health_check: Optional[Any] = Field(None, description="HTTP-путь для проверки работоспособности backend-приложения. Может отсутствовать до создания инфраструктуры.")
    docker_image: Optional[Any] = Field(None, description="Имя готового Docker-образа без тега. Присутствует для backend из готового Docker-образа.")
    docker_image_tag: Optional[Any] = Field(None, description="Тег готового Docker-образа. Присутствует для backend из готового Docker-образа.")
    is_russian_trusted_ca: Optional[Any] = Field(None, description="Добавлены ли доверенные корневые сертификаты Минцифры в окружение backend-приложения. Поле возвращается в российском регионе после создания инфраструктуры.")
    is_tci_trusted_ca: Optional[Any] = Field(None, description="Добавлены ли доверенные корневые сертификаты ТЦИ в окружение backend-приложения. Поле возвращается в российском регионе после создания инфраструктуры.")
    blocked_ports: Optional[Any] = Field(None, description="Заблокированные порты backend-приложения. Поле может отсутствовать до создания сервера.")
    reverse_proxy: Optional[Any] = Field(..., description="Настройки обратного прокси. В начальном ответе на создание — null.")
    __properties = ["id", "type", "name", "status", "provider", "ip", "domains", "framework", "location", "repository", "env_version", "envs", "is_auto_deploy", "commit_sha", "comment", "preset_id", "index_dir", "build_cmd", "avatar_link", "run_cmd", "configuration", "disk_status", "is_qemu_agent", "language", "start_time", "branch", "configurator_id", "project_id", "system_dependencies", "created_at", "availability_zone", "requests_limit", "build_entry_path", "health_check", "docker_image", "docker_image_tag", "is_russian_trusted_ca", "is_tci_trusted_ca", "blocked_ports", "reverse_proxy"]

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

        if value not in ('active', 'paused', 'no_paid', 'deploy', 'failure', 'startup_error', 'new', 'reboot', 'blocked', 'request_limit_exceeded'):
            raise ValueError("must be one of enum values ('active', 'paused', 'no_paid', 'deploy', 'failure', 'startup_error', 'new', 'reboot', 'blocked', 'request_limit_exceeded')")
        return value

    @validator('framework')
    def framework_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('django', 'express', 'phoenix', 'Spring', 'laravel', 'beego', 'fastapi', 'ASP.NET Core', 'hapi', 'celery', 'flask', 'gin', 'docker', 'docker-compose', 'fastify', 'nest', 'symfony', 'yii', 'next.js', 'nuxt', 'astro', 'tanstack-start', 'solid-start', 'ktor', 'axum', 'actix', 'tornado', 'aiohttp', 'fiber', 'echo', 'Micronaut', 'Quarkus', 'remix', 'sveltekit', 'angular', 'ember', 'preact', 'react', 'solid', 'svelte', 'vue', 'static-nobuild', 'another'):
            raise ValueError("must be one of enum values ('django', 'express', 'phoenix', 'Spring', 'laravel', 'beego', 'fastapi', 'ASP.NET Core', 'hapi', 'celery', 'flask', 'gin', 'docker', 'docker-compose', 'fastify', 'nest', 'symfony', 'yii', 'next.js', 'nuxt', 'astro', 'tanstack-start', 'solid-start', 'ktor', 'axum', 'actix', 'tornado', 'aiohttp', 'fiber', 'echo', 'Micronaut', 'Quarkus', 'remix', 'sveltekit', 'angular', 'ember', 'preact', 'react', 'solid', 'svelte', 'vue', 'static-nobuild', 'another')")
        return value

    @validator('location')
    def location_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('ru-1', 'ru-2', 'ru-3', 'pl-1', 'kz-1', 'nl-1', 'us-1', 'us-2', 'de-1'):
            raise ValueError("must be one of enum values ('ru-1', 'ru-2', 'ru-3', 'pl-1', 'kz-1', 'nl-1', 'us-1', 'us-2', 'de-1')")
        return value

    @validator('language')
    def language_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('javascript', 'node', 'elixir', 'go', 'php', 'python', 'ruby', 'docker', 'docker-compose', 'dotnet', 'java', 'kotlin', 'rust', 'bun', 'deno', 'custom-image'):
            raise ValueError("must be one of enum values ('javascript', 'node', 'elixir', 'go', 'php', 'python', 'ruby', 'docker', 'docker-compose', 'dotnet', 'java', 'kotlin', 'rust', 'bun', 'deno', 'custom-image')")
        return value

    @validator('availability_zone')
    def availability_zone_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('spb-1', 'spb-2', 'spb-3', 'spb-4', 'nsk-1', 'ams-1', 'gdn-1', 'ala-1', 'nyc-1', 'msk-1'):
            raise ValueError("must be one of enum values ('spb-1', 'spb-2', 'spb-3', 'spb-4', 'nsk-1', 'ams-1', 'gdn-1', 'ala-1', 'nyc-1', 'msk-1')")
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
    def from_json(cls, json_str: str) -> AppV2:
        """Create an instance of AppV2 from a JSON string"""
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

        # set to None if framework (nullable) is None
        # and __fields_set__ contains the field
        if self.framework is None and "framework" in self.__fields_set__:
            _dict['framework'] = None

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

        # set to None if avatar_link (nullable) is None
        # and __fields_set__ contains the field
        if self.avatar_link is None and "avatar_link" in self.__fields_set__:
            _dict['avatar_link'] = None

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

        # set to None if branch (nullable) is None
        # and __fields_set__ contains the field
        if self.branch is None and "branch" in self.__fields_set__:
            _dict['branch'] = None

        # set to None if configurator_id (nullable) is None
        # and __fields_set__ contains the field
        if self.configurator_id is None and "configurator_id" in self.__fields_set__:
            _dict['configurator_id'] = None

        # set to None if project_id (nullable) is None
        # and __fields_set__ contains the field
        if self.project_id is None and "project_id" in self.__fields_set__:
            _dict['project_id'] = None

        # set to None if system_dependencies (nullable) is None
        # and __fields_set__ contains the field
        if self.system_dependencies is None and "system_dependencies" in self.__fields_set__:
            _dict['system_dependencies'] = None

        # set to None if created_at (nullable) is None
        # and __fields_set__ contains the field
        if self.created_at is None and "created_at" in self.__fields_set__:
            _dict['created_at'] = None

        # set to None if availability_zone (nullable) is None
        # and __fields_set__ contains the field
        if self.availability_zone is None and "availability_zone" in self.__fields_set__:
            _dict['availability_zone'] = None

        # set to None if requests_limit (nullable) is None
        # and __fields_set__ contains the field
        if self.requests_limit is None and "requests_limit" in self.__fields_set__:
            _dict['requests_limit'] = None

        # set to None if build_entry_path (nullable) is None
        # and __fields_set__ contains the field
        if self.build_entry_path is None and "build_entry_path" in self.__fields_set__:
            _dict['build_entry_path'] = None

        # set to None if health_check (nullable) is None
        # and __fields_set__ contains the field
        if self.health_check is None and "health_check" in self.__fields_set__:
            _dict['health_check'] = None

        # set to None if docker_image (nullable) is None
        # and __fields_set__ contains the field
        if self.docker_image is None and "docker_image" in self.__fields_set__:
            _dict['docker_image'] = None

        # set to None if docker_image_tag (nullable) is None
        # and __fields_set__ contains the field
        if self.docker_image_tag is None and "docker_image_tag" in self.__fields_set__:
            _dict['docker_image_tag'] = None

        # set to None if is_russian_trusted_ca (nullable) is None
        # and __fields_set__ contains the field
        if self.is_russian_trusted_ca is None and "is_russian_trusted_ca" in self.__fields_set__:
            _dict['is_russian_trusted_ca'] = None

        # set to None if is_tci_trusted_ca (nullable) is None
        # and __fields_set__ contains the field
        if self.is_tci_trusted_ca is None and "is_tci_trusted_ca" in self.__fields_set__:
            _dict['is_tci_trusted_ca'] = None

        # set to None if blocked_ports (nullable) is None
        # and __fields_set__ contains the field
        if self.blocked_ports is None and "blocked_ports" in self.__fields_set__:
            _dict['blocked_ports'] = None

        # set to None if reverse_proxy (nullable) is None
        # and __fields_set__ contains the field
        if self.reverse_proxy is None and "reverse_proxy" in self.__fields_set__:
            _dict['reverse_proxy'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AppV2:
        """Create an instance of AppV2 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AppV2.parse_obj(obj)

        _obj = AppV2.parse_obj({
            "id": obj.get("id"),
            "type": obj.get("type"),
            "name": obj.get("name"),
            "status": obj.get("status"),
            "provider": AppV2Provider.from_dict(obj.get("provider")) if obj.get("provider") is not None else None,
            "ip": obj.get("ip"),
            "domains": obj.get("domains"),
            "framework": obj.get("framework"),
            "location": obj.get("location"),
            "repository": Repository.from_dict(obj.get("repository")) if obj.get("repository") is not None else None,
            "env_version": obj.get("env_version"),
            "is_auto_deploy": obj.get("is_auto_deploy"),
            "commit_sha": obj.get("commit_sha"),
            "comment": obj.get("comment"),
            "preset_id": obj.get("preset_id"),
            "index_dir": obj.get("index_dir"),
            "build_cmd": obj.get("build_cmd"),
            "avatar_link": obj.get("avatar_link"),
            "run_cmd": obj.get("run_cmd"),
            "configuration": AppV2Configuration.from_dict(obj.get("configuration")) if obj.get("configuration") is not None else None,
            "disk_status": AppV2DiskStatus.from_dict(obj.get("disk_status")) if obj.get("disk_status") is not None else None,
            "is_qemu_agent": obj.get("is_qemu_agent"),
            "language": obj.get("language"),
            "start_time": obj.get("start_time"),
            "branch": obj.get("branch"),
            "configurator_id": obj.get("configurator_id"),
            "project_id": obj.get("project_id"),
            "system_dependencies": obj.get("system_dependencies"),
            "created_at": obj.get("created_at"),
            "availability_zone": obj.get("availability_zone"),
            "requests_limit": obj.get("requests_limit"),
            "build_entry_path": obj.get("build_entry_path"),
            "health_check": obj.get("health_check"),
            "docker_image": obj.get("docker_image"),
            "docker_image_tag": obj.get("docker_image_tag"),
            "is_russian_trusted_ca": obj.get("is_russian_trusted_ca"),
            "is_tci_trusted_ca": obj.get("is_tci_trusted_ca"),
            "blocked_ports": obj.get("blocked_ports"),
            "reverse_proxy": obj.get("reverse_proxy")
        })
        return _obj

