# Db

База данных

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | Уникальный идентификатор для каждого экземпляра базы данных. Автоматически генерируется при создании. | 
**created_at** | **object** | Значение времени, указанное в комбинированном формате даты и времени ISO8601, которое представляет, когда была создана база данных. | 
**account_id** | **object** | Идентификатор пользователя. | 
**login** | **object** | Логин для подключения к базе данных. | 
**location** | **object** | Локация сервера. | [optional] 
**password** | **object** | Пароль для подключения к базе данных. | 
**name** | **object** | Название базы данных. | 
**host** | **object** | Хост. | 
**type** | [**DbType**](DbType.md) |  | 
**hash_type** | **object** | Тип хеширования базы данных (mysql5 | mysql | postgres). | 
**port** | **object** | Порт | 
**ip** | **object** | IP-адрес сетевого интерфейса IPv4. | 
**local_ip** | **object** | IP-адрес локального сетевого интерфейса IPv4. | 
**status** | **object** | Текущий статус базы данных. | 
**preset_id** | **object** | Идентификатор тарифа. | 
**disk_stats** | [**DbDiskStats**](DbDiskStats.md) |  | 
**config_parameters** | [**ConfigParameters**](ConfigParameters.md) |  | 
**is_only_local_ip_access** | **object** | Это логическое значение, которое показывает, доступна ли база данных только по локальному IP адресу. | 
**availability_zone** | [**AvailabilityZone**](AvailabilityZone.md) |  | 

## Example

```python
from timeweb_cloud_api.models.db import Db

# TODO update the JSON string below
json = "{}"
# create an instance of Db from a JSON string
db_instance = Db.from_json(json)
# print the JSON string representation of the object
print Db.to_json()

# convert the object into a dict
db_dict = db_instance.to_dict()
# create an instance of Db from a dict
db_form_dict = db.from_dict(db_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


