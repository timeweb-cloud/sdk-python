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

class AgentWidgetSettings(BaseModel):
    """
    Настройки виджета чата агента для встраивания на сайт
    """
    whitelist_domains: Optional[Any] = Field(..., description="Домены, на которых разрешено показывать виджет. Пустой массив — без ограничений.")
    name: Optional[Any] = Field(..., description="Отображаемое имя агента в виджете")
    signature: Optional[Any] = Field(None, description="Подпись под именем агента в виджете")
    welcome_message: Optional[Any] = Field(..., description="Приветственное сообщение при открытии виджета")
    primary_color: Optional[Any] = Field(..., description="Основной цвет виджета в формате `#RRGGBB`")
    text_color: Optional[Any] = Field(None, description="Цвет текста в формате `#RRGGBB`")
    background_color: Optional[Any] = Field(None, description="Цвет фона в формате `#RRGGBB`")
    header_footer_color: Optional[Any] = Field(None, description="Цвет шапки и подвала виджета в формате `#RRGGBB`")
    font: Optional[Any] = Field(..., description="Шрифт виджета. Пустая строка — шрифт сайта.")
    icon_url: Optional[Any] = Field(None, description="URL иконки агента в виджете")
    use_avatar: Optional[Any] = Field(None, description="Использовать загруженный в панели аватар как иконку агента")
    show_button: Optional[Any] = Field(None, description="Показывать кнопку открытия виджета")
    show_tool_processing: Optional[Any] = Field(None, description="Показывать в виджете статус выполнения инструментов агента")
    show_confirmation_buttons: Optional[Any] = Field(None, description="Показывать кнопки подтверждения и отмены операций, которые агент выполняет через инструменты")
    chat_position: Optional[Any] = Field(..., description="Положение виджета на странице")
    chat_position_adjustment_x: Optional[Any] = Field(None, description="Смещение виджета по горизонтали в пикселях")
    chat_position_adjustment_y: Optional[Any] = Field(None, description="Смещение виджета по вертикали в пикселях")
    __properties = ["whitelist_domains", "name", "signature", "welcome_message", "primary_color", "text_color", "background_color", "header_footer_color", "font", "icon_url", "use_avatar", "show_button", "show_tool_processing", "show_confirmation_buttons", "chat_position", "chat_position_adjustment_x", "chat_position_adjustment_y"]

    @validator('chat_position')
    def chat_position_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('bottom_right', 'bottom_left', 'top_right', 'top_left'):
            raise ValueError("must be one of enum values ('bottom_right', 'bottom_left', 'top_right', 'top_left')")
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
    def from_json(cls, json_str: str) -> AgentWidgetSettings:
        """Create an instance of AgentWidgetSettings from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if whitelist_domains (nullable) is None
        # and __fields_set__ contains the field
        if self.whitelist_domains is None and "whitelist_domains" in self.__fields_set__:
            _dict['whitelist_domains'] = None

        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict['name'] = None

        # set to None if signature (nullable) is None
        # and __fields_set__ contains the field
        if self.signature is None and "signature" in self.__fields_set__:
            _dict['signature'] = None

        # set to None if welcome_message (nullable) is None
        # and __fields_set__ contains the field
        if self.welcome_message is None and "welcome_message" in self.__fields_set__:
            _dict['welcome_message'] = None

        # set to None if primary_color (nullable) is None
        # and __fields_set__ contains the field
        if self.primary_color is None and "primary_color" in self.__fields_set__:
            _dict['primary_color'] = None

        # set to None if text_color (nullable) is None
        # and __fields_set__ contains the field
        if self.text_color is None and "text_color" in self.__fields_set__:
            _dict['text_color'] = None

        # set to None if background_color (nullable) is None
        # and __fields_set__ contains the field
        if self.background_color is None and "background_color" in self.__fields_set__:
            _dict['background_color'] = None

        # set to None if header_footer_color (nullable) is None
        # and __fields_set__ contains the field
        if self.header_footer_color is None and "header_footer_color" in self.__fields_set__:
            _dict['header_footer_color'] = None

        # set to None if font (nullable) is None
        # and __fields_set__ contains the field
        if self.font is None and "font" in self.__fields_set__:
            _dict['font'] = None

        # set to None if icon_url (nullable) is None
        # and __fields_set__ contains the field
        if self.icon_url is None and "icon_url" in self.__fields_set__:
            _dict['icon_url'] = None

        # set to None if use_avatar (nullable) is None
        # and __fields_set__ contains the field
        if self.use_avatar is None and "use_avatar" in self.__fields_set__:
            _dict['use_avatar'] = None

        # set to None if show_button (nullable) is None
        # and __fields_set__ contains the field
        if self.show_button is None and "show_button" in self.__fields_set__:
            _dict['show_button'] = None

        # set to None if show_tool_processing (nullable) is None
        # and __fields_set__ contains the field
        if self.show_tool_processing is None and "show_tool_processing" in self.__fields_set__:
            _dict['show_tool_processing'] = None

        # set to None if show_confirmation_buttons (nullable) is None
        # and __fields_set__ contains the field
        if self.show_confirmation_buttons is None and "show_confirmation_buttons" in self.__fields_set__:
            _dict['show_confirmation_buttons'] = None

        # set to None if chat_position (nullable) is None
        # and __fields_set__ contains the field
        if self.chat_position is None and "chat_position" in self.__fields_set__:
            _dict['chat_position'] = None

        # set to None if chat_position_adjustment_x (nullable) is None
        # and __fields_set__ contains the field
        if self.chat_position_adjustment_x is None and "chat_position_adjustment_x" in self.__fields_set__:
            _dict['chat_position_adjustment_x'] = None

        # set to None if chat_position_adjustment_y (nullable) is None
        # and __fields_set__ contains the field
        if self.chat_position_adjustment_y is None and "chat_position_adjustment_y" in self.__fields_set__:
            _dict['chat_position_adjustment_y'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AgentWidgetSettings:
        """Create an instance of AgentWidgetSettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AgentWidgetSettings.parse_obj(obj)

        _obj = AgentWidgetSettings.parse_obj({
            "whitelist_domains": obj.get("whitelist_domains"),
            "name": obj.get("name"),
            "signature": obj.get("signature"),
            "welcome_message": obj.get("welcome_message"),
            "primary_color": obj.get("primary_color"),
            "text_color": obj.get("text_color"),
            "background_color": obj.get("background_color"),
            "header_footer_color": obj.get("header_footer_color"),
            "font": obj.get("font"),
            "icon_url": obj.get("icon_url"),
            "use_avatar": obj.get("use_avatar"),
            "show_button": obj.get("show_button"),
            "show_tool_processing": obj.get("show_tool_processing"),
            "show_confirmation_buttons": obj.get("show_confirmation_buttons"),
            "chat_position": obj.get("chat_position"),
            "chat_position_adjustment_x": obj.get("chat_position_adjustment_x"),
            "chat_position_adjustment_y": obj.get("chat_position_adjustment_y")
        })
        return _obj

