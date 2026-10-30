# CreateAppV2

Параметры создания приложения. Для Git-репозитория обязательны provider_id, repository_id, branch_name, commit_sha, build_cmd, is_auto_deploy и framework. Для frontend также обязательны index_dir и preset_id. Для backend из Git обязателен run_cmd. Для backend из готового Docker-образа передайте docker_image и docker_image_tag; Git-параметры не требуются. Для любого backend передайте либо preset_id, либо configuration. Эти поля нельзя передавать одновременно.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_id** | **object** | ID провайдера. Обязателен при создании из Git-репозитория. Не требуется для готового Docker-образа. | [optional] 
**type** | **object** | Тип приложения: frontend — статический сайт, backend — серверное приложение или Docker-образ. | 
**repository_id** | **object** | ID репозитория. Обязателен при создании из Git-репозитория. Не требуется для готового Docker-образа. | [optional] 
**build_cmd** | **object** | Команда сборки приложения из Git-репозитория. Обязательна для Git; можно передать пустую строку, если сборка не нужна. | [optional] 
**envs** | **Dict[str, object]** | Переменные окружения приложения. Ключи и значения — строки. Длина ключа — не более 255 символов, значения — не более 10240. По умолчанию пустой объект. | [optional] 
**branch_name** | **object** | Ветка Git-репозитория, из которой необходимо собрать приложение. Обязательна при создании из Git. | [optional] 
**is_auto_deploy** | **object** | Автоматически запускать деплой при изменении Git-репозитория. Поле обязательно при создании из Git. Для провайдера git и готового Docker-образа автодеплой выключен. | [optional] 
**commit_sha** | **object** | Хэш коммита для первого деплоя. Обязателен при создании из Git. | [optional] 
**name** | **object** | Имя приложения, от 1 до 255 символов. Допустимы латинские и русские буквы, цифры, пробелы и символы - . ( ) , &amp; # [ ] _. | 
**comment** | **object** | Комментарий к приложению. Обязательное поле; можно передать пустую строку. Допустимы те же символы, что и в имени приложения. | 
**preset_id** | **object** | ID тарифа приложения. Обязателен для frontend. Для backend передайте либо preset_id, либо configuration. Нельзя передавать вместе с configuration. Доступные тарифы: GET /api/v1/presets/apps. | [optional] 
**env_version** | **object** | Версия окружения для сборки и запуска, например версия Node.js. Можно передать null. | [optional] 
**framework** | **object** | Фреймворк приложения, строка с учётом регистра. Обязателен при создании из Git. Для frontend: &#x60;angular&#x60;, &#x60;astro&#x60;, &#x60;ember&#x60;, &#x60;next.js&#x60;, &#x60;nuxt&#x60;, &#x60;preact&#x60;, &#x60;react&#x60;, &#x60;remix&#x60;, &#x60;solid&#x60;, &#x60;solid-start&#x60;, &#x60;svelte&#x60;, &#x60;sveltekit&#x60;, &#x60;tanstack-start&#x60;, &#x60;vue&#x60;, &#x60;static-nobuild&#x60;, &#x60;another&#x60;. Для backend: &#x60;django&#x60;, &#x60;express&#x60;, &#x60;phoenix&#x60;, &#x60;Spring&#x60;, &#x60;laravel&#x60;, &#x60;beego&#x60;, &#x60;fastapi&#x60;, &#x60;ASP.NET Core&#x60;, &#x60;hapi&#x60;, &#x60;celery&#x60;, &#x60;flask&#x60;, &#x60;gin&#x60;, &#x60;docker&#x60;, &#x60;docker-compose&#x60;, &#x60;fastify&#x60;, &#x60;nest&#x60;, &#x60;symfony&#x60;, &#x60;yii&#x60;, &#x60;next.js&#x60;, &#x60;nuxt&#x60;, &#x60;astro&#x60;, &#x60;tanstack-start&#x60;, &#x60;solid-start&#x60;, &#x60;ktor&#x60;, &#x60;axum&#x60;, &#x60;actix&#x60;, &#x60;tornado&#x60;, &#x60;aiohttp&#x60;, &#x60;fiber&#x60;, &#x60;echo&#x60;, &#x60;Micronaut&#x60;, &#x60;Quarkus&#x60;, &#x60;remix&#x60;, &#x60;sveltekit&#x60;. Для готового Docker-образа не требуется. | [optional] 
**index_dir** | **object** | Путь к каталогу с собранными статическими файлами, например /dist. Обязателен для frontend. Не используется для backend. | [optional] 
**run_cmd** | **object** | Команда запуска backend-приложения из Git. Обязательна для backend из Git. Не требуется для готового Docker-образа и frontend. | [optional] 
**system_dependencies** | **object** | Системные пакеты для установки в окружение приложения. Допустимы строчные латинские буквы, цифры и символы . + - &#x3D;. По умолчанию пустой массив. | [optional] 
**project_id** | **object** | ID проекта, в который необходимо добавить приложение. Проект должен принадлежать аккаунту. | [optional] 
**configuration** | [**CreateAppV2Configuration**](CreateAppV2Configuration.md) |  | [optional] 
**language** | **object** | Язык или способ развёртывания. Обязателен в v2. Для frontend: &#x60;javascript&#x60;. Для backend: &#x60;node&#x60;, &#x60;elixir&#x60;, &#x60;go&#x60;, &#x60;php&#x60;, &#x60;python&#x60;, &#x60;ruby&#x60;, &#x60;docker&#x60;, &#x60;docker-compose&#x60;, &#x60;dotnet&#x60;, &#x60;java&#x60;, &#x60;kotlin&#x60;, &#x60;rust&#x60;, &#x60;bun&#x60;, &#x60;deno&#x60;, &#x60;custom-image&#x60;. Для SSR-приложений из Git используйте node, для готового Docker-образа — custom-image. | 
**build_entry_path** | **object** | Каталог приложения в Git-репозитории, относительно которого выполняется сборка. Непустой путь начинается с /, не содержит .. или двойной начальный /. Допустимы латинские буквы, цифры, . - _ /. Можно передать пустую строку. | [optional] 
**network** | [**CreateAppV2Network**](CreateAppV2Network.md) |  | [optional] 
**health_check** | **object** | HTTP-путь для проверки работоспособности backend-приложения. | [optional] 
**global_env_ids** | **object** | ID глобальных переменных окружения аккаунта, которые необходимо связать с приложением. | [optional] 
**docker_image** | **object** | Имя готового Docker-образа для backend, без тега. Передавайте вместе с docker_image_tag. При указании обоих полей Git-параметры не требуются. | [optional] 
**docker_image_tag** | **object** | Тег готового Docker-образа. Передавайте вместе с docker_image. | [optional] 
**is_russian_trusted_ca** | **object** | Добавить доверенные корневые сертификаты Минцифры в окружение backend-приложения. Применяется в российском регионе. | [optional] 
**is_tci_trusted_ca** | **object** | Добавить доверенные корневые сертификаты ТЦИ в окружение backend-приложения. Применяется в российском регионе. | [optional] 

## Example

```python
from timeweb_cloud_api.models.create_app_v2 import CreateAppV2

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAppV2 from a JSON string
create_app_v2_instance = CreateAppV2.from_json(json)
# print the JSON string representation of the object
print CreateAppV2.to_json()

# convert the object into a dict
create_app_v2_dict = create_app_v2_instance.to_dict()
# create an instance of CreateAppV2 from a dict
create_app_v2_form_dict = create_app_v2.from_dict(create_app_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


