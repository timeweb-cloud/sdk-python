# UpdateSettings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_auto_deploy** | **object** | Автоматический деплой. | [optional] 
**build_cmd** | **object** | Команда сборки приложения. | [optional] 
**envs** | **object** | Переменные окружения приложения. Объект с ключами и значениями типа string. | [optional] 
**branch_name** | **object** | Название ветки репозитория из которой необходимо собрать приложение. | [optional] 
**commit_sha** | **object** | Хэш коммита. | [optional] 
**env_version** | **object** | Версия окружения. | [optional] 
**index_dir** | **object** | Путь к директории с индексным файлом. Используется для приложений &#x60;type: frontend&#x60;. Не используется для приложений &#x60;type: backend&#x60;. Значение всегда должно начинаться с &#x60;/&#x60;. | [optional] 
**run_cmd** | **object** | Команда для запуска приложения. Используется для приложений &#x60;type: backend&#x60;. Не используется для приложений &#x60;type: frontend&#x60;. | [optional] 
**framework** | [**Frameworks**](Frameworks.md) |  | [optional] 
**name** | **object** | Имя приложения. | [optional] 
**comment** | **object** | Комментарий к приложению. | [optional] 
**preset_id** | **object** | ID тарифа. | [optional] 

## Example

```python
from timeweb_cloud_api.models.update_settings import UpdateSettings

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSettings from a JSON string
update_settings_instance = UpdateSettings.from_json(json)
# print the JSON string representation of the object
print UpdateSettings.to_json()

# convert the object into a dict
update_settings_dict = update_settings_instance.to_dict()
# create an instance of UpdateSettings from a dict
update_settings_form_dict = update_settings.from_dict(update_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


