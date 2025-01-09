# App

Экземпляр приложения.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID для каждого экземпляра приложения. Автоматически генерируется при создании. | 
**type** | **object** | Тип приложения. | 
**name** | **object** | Удобочитаемое имя, установленное для приложения. | 
**status** | **object** | Статус приложения. | 
**provider** | [**AppProvider**](AppProvider.md) |  | 
**ip** | **object** | IPv4-адрес приложения. | 
**domains** | **object** |  | 
**framework** | [**Frameworks**](Frameworks.md) |  | 
**location** | **object** | Локация сервера. | 
**repository** | [**Repository**](Repository.md) |  | 
**env_version** | **object** | Версия окружения. | 
**envs** | **object** | Переменные окружения приложения. Объект с ключами и значениями типа string. | 
**branch_name** | **object** | Название ветки репозитория из которой собрано приложение. | 
**is_auto_deploy** | **object** | Включен ли автоматический деплой. | 
**commit_sha** | **object** | Хэш коммита из которого собрано приложеие. | 
**comment** | **object** | Комментарий к приложению. | 
**preset_id** | **object** | ID тарифа. | 
**index_dir** | **object** | Путь к директории с индексным файлом. Определен для приложений &#x60;type: frontend&#x60;. Для приложений &#x60;type: backend&#x60; всегда null. | 
**build_cmd** | **object** | Команда сборки приложения. | 
**run_cmd** | **object** | Команда для запуска приложения. Определена для приложений &#x60;type: backend&#x60;. Для приложений &#x60;type: frontend&#x60; всегда null. | 
**configuration** | [**AppConfiguration**](AppConfiguration.md) |  | 
**disk_status** | [**AppDiskStatus**](AppDiskStatus.md) |  | 
**is_qemu_agent** | **object** | Включен ли агент QEMU. | 
**language** | **object** | Язык программирования приложения. | 
**start_time** | **object** | Время запуска приложения. | 

## Example

```python
from timeweb_cloud_api.models.app import App

# TODO update the JSON string below
json = "{}"
# create an instance of App from a JSON string
app_instance = App.from_json(json)
# print the JSON string representation of the object
print App.to_json()

# convert the object into a dict
app_dict = app_instance.to_dict()
# create an instance of App from a dict
app_form_dict = app.from_dict(app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


