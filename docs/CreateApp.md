# CreateApp


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_id** | **object** | Уникальный идентификатор провайдера. | 
**type** | **object** | Тип приложения. | 
**repository_id** | **object** | Уникальный идентификатор репозитория. | 
**build_cmd** | **object** | Команда сборки приложения. | 
**envs** | **object** | Переменные окружения приложения. Объект с ключами и значениями типа string. | [optional] 
**branch_name** | **object** | Название ветки репозитория из которой необходимо собрать приложение. | 
**is_auto_deploy** | **object** | Автоматический деплой. | 
**commit_sha** | **object** | Хэш коммита из которого необходимо собрать приложение. | 
**name** | **object** | Имя приложения. | 
**comment** | **object** | Комментарий к приложения. | 
**preset_id** | **object** | Идентификатор тарифа. | 
**env_version** | **object** | Версия окружения. | [optional] 
**framework** | [**Frameworks**](Frameworks.md) |  | 
**index_dir** | **object** | Путь к директории с индексным файлом. Обязателен для приложений &#x60;type: frontend&#x60;. Не используется для приложений &#x60;type: backend&#x60;. Значение всегда должно начинаться с &#x60;/&#x60;. | [optional] 
**run_cmd** | **object** | Команда для запуска приложения. Обязателен для приложений &#x60;type: backend&#x60;. Не используется для приложений &#x60;type: frontend&#x60;. | [optional] 

## Example

```python
from timeweb_cloud_api.models.create_app import CreateApp

# TODO update the JSON string below
json = "{}"
# create an instance of CreateApp from a JSON string
create_app_instance = CreateApp.from_json(json)
# print the JSON string representation of the object
print CreateApp.to_json()

# convert the object into a dict
create_app_dict = create_app_instance.to_dict()
# create an instance of CreateApp from a dict
create_app_form_dict = create_app.from_dict(create_app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


