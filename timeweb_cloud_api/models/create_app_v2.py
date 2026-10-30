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
from timeweb_cloud_api.models.create_app_v2_configuration import CreateAppV2Configuration
from timeweb_cloud_api.models.create_app_v2_network import CreateAppV2Network

class CreateAppV2(BaseModel):
    """
    Параметры создания приложения. Для Git-репозитория обязательны provider_id, repository_id, branch_name, commit_sha, build_cmd, is_auto_deploy и framework. Для frontend также обязательны index_dir и preset_id. Для backend из Git обязателен run_cmd. Для backend из готового Docker-образа передайте docker_image и docker_image_tag; Git-параметры не требуются. Для любого backend передайте либо preset_id, либо configuration. Эти поля нельзя передавать одновременно.
    """
    provider_id: Optional[Any] = Field(None, description="ID провайдера. Обязателен при создании из Git-репозитория. Не требуется для готового Docker-образа.")
    type: Optional[Any] = Field(..., description="Тип приложения: frontend — статический сайт, backend — серверное приложение или Docker-образ.")
    repository_id: Optional[Any] = Field(None, description="ID репозитория. Обязателен при создании из Git-репозитория. Не требуется для готового Docker-образа.")
    build_cmd: Optional[Any] = Field(None, description="Команда сборки приложения из Git-репозитория. Обязательна для Git; можно передать пустую строку, если сборка не нужна.")
    envs: Optional[Any] = Field(None, description="Переменные окружения приложения. Ключи и значения — строки. Длина ключа — не более 255 символов, значения — не более 10240. По умолчанию пустой объект.")
    branch_name: Optional[Any] = Field(None, description="Ветка Git-репозитория, из которой необходимо собрать приложение. Обязательна при создании из Git.")
    is_auto_deploy: Optional[Any] = Field(None, description="Автоматически запускать деплой при изменении Git-репозитория. Поле обязательно при создании из Git. Для провайдера git и готового Docker-образа автодеплой выключен.")
    commit_sha: Optional[Any] = Field(None, description="Хэш коммита для первого деплоя. Обязателен при создании из Git.")
    name: Optional[Any] = Field(..., description="Имя приложения, от 1 до 255 символов. Допустимы латинские и русские буквы, цифры, пробелы и символы - . ( ) , & # [ ] _.")
    comment: Optional[Any] = Field(..., description="Комментарий к приложению. Обязательное поле; можно передать пустую строку. Допустимы те же символы, что и в имени приложения.")
    preset_id: Optional[Any] = Field(None, description="ID тарифа приложения. Обязателен для frontend. Для backend передайте либо preset_id, либо configuration. Нельзя передавать вместе с configuration. Доступные тарифы: GET /api/v1/presets/apps.")
    env_version: Optional[Any] = Field(None, description="Версия окружения для сборки и запуска, например версия Node.js. Можно передать null.")
    framework: Optional[Any] = Field(None, description="Фреймворк приложения, строка с учётом регистра. Обязателен при создании из Git. Для frontend: `angular`, `astro`, `ember`, `next.js`, `nuxt`, `preact`, `react`, `remix`, `solid`, `solid-start`, `svelte`, `sveltekit`, `tanstack-start`, `vue`, `static-nobuild`, `another`. Для backend: `django`, `express`, `phoenix`, `Spring`, `laravel`, `beego`, `fastapi`, `ASP.NET Core`, `hapi`, `celery`, `flask`, `gin`, `docker`, `docker-compose`, `fastify`, `nest`, `symfony`, `yii`, `next.js`, `nuxt`, `astro`, `tanstack-start`, `solid-start`, `ktor`, `axum`, `actix`, `tornado`, `aiohttp`, `fiber`, `echo`, `Micronaut`, `Quarkus`, `remix`, `sveltekit`. Для готового Docker-образа не требуется.")
    index_dir: Optional[Any] = Field(None, description="Путь к каталогу с собранными статическими файлами, например /dist. Обязателен для frontend. Не используется для backend.")
    run_cmd: Optional[Any] = Field(None, description="Команда запуска backend-приложения из Git. Обязательна для backend из Git. Не требуется для готового Docker-образа и frontend.")
    system_dependencies: Optional[Any] = Field(None, description="Системные пакеты для установки в окружение приложения. Допустимы строчные латинские буквы, цифры и символы . + - =. По умолчанию пустой массив.")
    project_id: Optional[Any] = Field(None, description="ID проекта, в который необходимо добавить приложение. Проект должен принадлежать аккаунту.")
    configuration: Optional[CreateAppV2Configuration] = None
    language: Optional[Any] = Field(..., description="Язык или способ развёртывания. Обязателен в v2. Для frontend: `javascript`. Для backend: `node`, `elixir`, `go`, `php`, `python`, `ruby`, `docker`, `docker-compose`, `dotnet`, `java`, `kotlin`, `rust`, `bun`, `deno`, `custom-image`. Для SSR-приложений из Git используйте node, для готового Docker-образа — custom-image.")
    build_entry_path: Optional[Any] = Field(None, description="Каталог приложения в Git-репозитории, относительно которого выполняется сборка. Непустой путь начинается с /, не содержит .. или двойной начальный /. Допустимы латинские буквы, цифры, . - _ /. Можно передать пустую строку.")
    network: Optional[CreateAppV2Network] = None
    health_check: Optional[Any] = Field(None, description="HTTP-путь для проверки работоспособности backend-приложения.")
    global_env_ids: Optional[Any] = Field(None, description="ID глобальных переменных окружения аккаунта, которые необходимо связать с приложением.")
    docker_image: Optional[Any] = Field(None, description="Имя готового Docker-образа для backend, без тега. Передавайте вместе с docker_image_tag. При указании обоих полей Git-параметры не требуются.")
    docker_image_tag: Optional[Any] = Field(None, description="Тег готового Docker-образа. Передавайте вместе с docker_image.")
    is_russian_trusted_ca: Optional[Any] = Field(None, description="Добавить доверенные корневые сертификаты Минцифры в окружение backend-приложения. Применяется в российском регионе.")
    is_tci_trusted_ca: Optional[Any] = Field(None, description="Добавить доверенные корневые сертификаты ТЦИ в окружение backend-приложения. Применяется в российском регионе.")
    __properties = ["provider_id", "type", "repository_id", "build_cmd", "envs", "branch_name", "is_auto_deploy", "commit_sha", "name", "comment", "preset_id", "env_version", "framework", "index_dir", "run_cmd", "system_dependencies", "project_id", "configuration", "language", "build_entry_path", "network", "health_check", "global_env_ids", "docker_image", "docker_image_tag", "is_russian_trusted_ca", "is_tci_trusted_ca"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('frontend', 'backend'):
            raise ValueError("must be one of enum values ('frontend', 'backend')")
        return value

    @validator('framework')
    def framework_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('django', 'express', 'phoenix', 'Spring', 'laravel', 'beego', 'fastapi', 'ASP.NET Core', 'hapi', 'celery', 'flask', 'gin', 'docker', 'docker-compose', 'fastify', 'nest', 'symfony', 'yii', 'next.js', 'nuxt', 'astro', 'tanstack-start', 'solid-start', 'ktor', 'axum', 'actix', 'tornado', 'aiohttp', 'fiber', 'echo', 'Micronaut', 'Quarkus', 'remix', 'sveltekit', 'angular', 'ember', 'preact', 'react', 'solid', 'svelte', 'vue', 'static-nobuild', 'another'):
            raise ValueError("must be one of enum values ('django', 'express', 'phoenix', 'Spring', 'laravel', 'beego', 'fastapi', 'ASP.NET Core', 'hapi', 'celery', 'flask', 'gin', 'docker', 'docker-compose', 'fastify', 'nest', 'symfony', 'yii', 'next.js', 'nuxt', 'astro', 'tanstack-start', 'solid-start', 'ktor', 'axum', 'actix', 'tornado', 'aiohttp', 'fiber', 'echo', 'Micronaut', 'Quarkus', 'remix', 'sveltekit', 'angular', 'ember', 'preact', 'react', 'solid', 'svelte', 'vue', 'static-nobuild', 'another')")
        return value

    @validator('language')
    def language_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('javascript', 'node', 'elixir', 'go', 'php', 'python', 'ruby', 'docker', 'docker-compose', 'dotnet', 'java', 'kotlin', 'rust', 'bun', 'deno', 'custom-image'):
            raise ValueError("must be one of enum values ('javascript', 'node', 'elixir', 'go', 'php', 'python', 'ruby', 'docker', 'docker-compose', 'dotnet', 'java', 'kotlin', 'rust', 'bun', 'deno', 'custom-image')")
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
    def from_json(cls, json_str: str) -> CreateAppV2:
        """Create an instance of CreateAppV2 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of configuration
        if self.configuration:
            _dict['configuration'] = self.configuration.to_dict()
        # override the default output from pydantic by calling `to_dict()` of network
        if self.network:
            _dict['network'] = self.network.to_dict()
        # set to None if provider_id (nullable) is None
        # and __fields_set__ contains the field
        if self.provider_id is None and "provider_id" in self.__fields_set__:
            _dict['provider_id'] = None

        # set to None if type (nullable) is None
        # and __fields_set__ contains the field
        if self.type is None and "type" in self.__fields_set__:
            _dict['type'] = None

        # set to None if repository_id (nullable) is None
        # and __fields_set__ contains the field
        if self.repository_id is None and "repository_id" in self.__fields_set__:
            _dict['repository_id'] = None

        # set to None if build_cmd (nullable) is None
        # and __fields_set__ contains the field
        if self.build_cmd is None and "build_cmd" in self.__fields_set__:
            _dict['build_cmd'] = None

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

        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict['name'] = None

        # set to None if comment (nullable) is None
        # and __fields_set__ contains the field
        if self.comment is None and "comment" in self.__fields_set__:
            _dict['comment'] = None

        # set to None if preset_id (nullable) is None
        # and __fields_set__ contains the field
        if self.preset_id is None and "preset_id" in self.__fields_set__:
            _dict['preset_id'] = None

        # set to None if env_version (nullable) is None
        # and __fields_set__ contains the field
        if self.env_version is None and "env_version" in self.__fields_set__:
            _dict['env_version'] = None

        # set to None if framework (nullable) is None
        # and __fields_set__ contains the field
        if self.framework is None and "framework" in self.__fields_set__:
            _dict['framework'] = None

        # set to None if index_dir (nullable) is None
        # and __fields_set__ contains the field
        if self.index_dir is None and "index_dir" in self.__fields_set__:
            _dict['index_dir'] = None

        # set to None if run_cmd (nullable) is None
        # and __fields_set__ contains the field
        if self.run_cmd is None and "run_cmd" in self.__fields_set__:
            _dict['run_cmd'] = None

        # set to None if system_dependencies (nullable) is None
        # and __fields_set__ contains the field
        if self.system_dependencies is None and "system_dependencies" in self.__fields_set__:
            _dict['system_dependencies'] = None

        # set to None if project_id (nullable) is None
        # and __fields_set__ contains the field
        if self.project_id is None and "project_id" in self.__fields_set__:
            _dict['project_id'] = None

        # set to None if language (nullable) is None
        # and __fields_set__ contains the field
        if self.language is None and "language" in self.__fields_set__:
            _dict['language'] = None

        # set to None if build_entry_path (nullable) is None
        # and __fields_set__ contains the field
        if self.build_entry_path is None and "build_entry_path" in self.__fields_set__:
            _dict['build_entry_path'] = None

        # set to None if health_check (nullable) is None
        # and __fields_set__ contains the field
        if self.health_check is None and "health_check" in self.__fields_set__:
            _dict['health_check'] = None

        # set to None if global_env_ids (nullable) is None
        # and __fields_set__ contains the field
        if self.global_env_ids is None and "global_env_ids" in self.__fields_set__:
            _dict['global_env_ids'] = None

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

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateAppV2:
        """Create an instance of CreateAppV2 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateAppV2.parse_obj(obj)

        _obj = CreateAppV2.parse_obj({
            "provider_id": obj.get("provider_id"),
            "type": obj.get("type"),
            "repository_id": obj.get("repository_id"),
            "build_cmd": obj.get("build_cmd"),
            "branch_name": obj.get("branch_name"),
            "is_auto_deploy": obj.get("is_auto_deploy"),
            "commit_sha": obj.get("commit_sha"),
            "name": obj.get("name"),
            "comment": obj.get("comment"),
            "preset_id": obj.get("preset_id"),
            "env_version": obj.get("env_version"),
            "framework": obj.get("framework"),
            "index_dir": obj.get("index_dir"),
            "run_cmd": obj.get("run_cmd"),
            "system_dependencies": obj.get("system_dependencies"),
            "project_id": obj.get("project_id"),
            "configuration": CreateAppV2Configuration.from_dict(obj.get("configuration")) if obj.get("configuration") is not None else None,
            "language": obj.get("language"),
            "build_entry_path": obj.get("build_entry_path"),
            "network": CreateAppV2Network.from_dict(obj.get("network")) if obj.get("network") is not None else None,
            "health_check": obj.get("health_check"),
            "global_env_ids": obj.get("global_env_ids"),
            "docker_image": obj.get("docker_image"),
            "docker_image_tag": obj.get("docker_image_tag"),
            "is_russian_trusted_ca": obj.get("is_russian_trusted_ca"),
            "is_tci_trusted_ca": obj.get("is_tci_trusted_ca")
        })
        return _obj

