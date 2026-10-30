# AppV2

Приложение v2. Создание и первый деплой выполняются асинхронно. Поля сервера и инфраструктуры могут отсутствовать, пока соответствующие ресурсы не созданы.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID для каждого экземпляра приложения. Автоматически генерируется при создании. | 
**type** | **object** | Тип приложения. | 
**name** | **object** | Удобочитаемое имя, установленное для приложения. | 
**status** | **object** | Текущее состояние приложения. После принятия запроса на создание — new. Ответ 201 не означает завершение развёртывания. | 
**provider** | [**AppV2Provider**](AppV2Provider.md) |  | 
**ip** | **object** | Публичный IPv4-адрес. Отсутствует, пока сервер и IP-адрес не созданы. | [optional] 
**domains** | **object** | Домены приложения. В начальном ответе на создание массив пуст. | 
**framework** | **object** | Фреймворк приложения. Поле может отсутствовать до создания инфраструктуры. | [optional] 
**location** | **object** | Локация сервера. Может отсутствовать до создания сервера. | [optional] 
**repository** | [**Repository**](Repository.md) |  | [optional] 
**env_version** | **object** | Версия окружения. Поле может отсутствовать до создания инфраструктуры. | [optional] 
**envs** | **Dict[str, object]** | Переменные окружения приложения. Объект с ключами и значениями типа string. Поле может отсутствовать до создания инфраструктуры. | [optional] 
**is_auto_deploy** | **object** | Включен ли автоматический деплой. | 
**commit_sha** | **object** | Хэш коммита, из которого собрано приложение. | [optional] 
**comment** | **object** | Комментарий к приложению. | [optional] 
**preset_id** | **object** | ID тарифа приложения; 0 при использовании конфигуратора. | 
**index_dir** | **object** | Каталог со статическими файлами frontend-приложения. До создания инфраструктуры поле отсутствует. Для backend — null. | [optional] 
**build_cmd** | **object** | Команда сборки приложения. Поле может отсутствовать до создания инфраструктуры. | [optional] 
**avatar_link** | **object** | Ссылка на аватар приложения. | 
**run_cmd** | **object** | Команда запуска backend-приложения. До создания инфраструктуры поле отсутствует. Для frontend — null. | [optional] 
**configuration** | [**AppV2Configuration**](AppV2Configuration.md) |  | [optional] 
**disk_status** | [**AppV2DiskStatus**](AppV2DiskStatus.md) |  | [optional] 
**is_qemu_agent** | **object** | Включён ли агент QEMU. Для frontend — null. Для backend поле отсутствует до создания сервера. | [optional] 
**language** | **object** | Язык или способ развёртывания. Может отсутствовать до создания инфраструктуры. Поле может отсутствовать до создания инфраструктуры. | [optional] 
**start_time** | **object** | Время последнего изменения записи приложения. | 
**branch** | **object** | Ветка Git-репозитория. В ответе v2 поле называется branch. | [optional] 
**configurator_id** | **object** | ID конфигуратора приложения; null при использовании готового тарифа. | 
**project_id** | **object** | ID проекта приложения. Может отсутствовать, если проект не задан. | [optional] 
**system_dependencies** | **object** | Системные пакеты приложения. Поле отсутствует, если зависимости не заданы. | [optional] 
**created_at** | **object** | Время создания записи приложения. | 
**availability_zone** | **object** | Зона доступности сервера. Может быть null или отсутствовать до создания сервера. | [optional] 
**requests_limit** | **object** | Ограничение количества запросов; null, если индивидуальный лимит не задан. | 
**build_entry_path** | **object** | Каталог приложения в Git-репозитории, относительно которого выполняется сборка. Может отсутствовать до создания инфраструктуры. | [optional] 
**health_check** | **object** | HTTP-путь для проверки работоспособности backend-приложения. Может отсутствовать до создания инфраструктуры. | [optional] 
**docker_image** | **object** | Имя готового Docker-образа без тега. Присутствует для backend из готового Docker-образа. | [optional] 
**docker_image_tag** | **object** | Тег готового Docker-образа. Присутствует для backend из готового Docker-образа. | [optional] 
**is_russian_trusted_ca** | **object** | Добавлены ли доверенные корневые сертификаты Минцифры в окружение backend-приложения. Поле возвращается в российском регионе после создания инфраструктуры. | [optional] 
**is_tci_trusted_ca** | **object** | Добавлены ли доверенные корневые сертификаты ТЦИ в окружение backend-приложения. Поле возвращается в российском регионе после создания инфраструктуры. | [optional] 
**blocked_ports** | **object** | Заблокированные порты backend-приложения. Поле может отсутствовать до создания сервера. | [optional] 
**reverse_proxy** | **object** | Настройки обратного прокси. В начальном ответе на создание — null. | 

## Example

```python
from timeweb_cloud_api.models.app_v2 import AppV2

# TODO update the JSON string below
json = "{}"
# create an instance of AppV2 from a JSON string
app_v2_instance = AppV2.from_json(json)
# print the JSON string representation of the object
print AppV2.to_json()

# convert the object into a dict
app_v2_dict = app_v2_instance.to_dict()
# create an instance of AppV2 from a dict
app_v2_form_dict = app_v2.from_dict(app_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


