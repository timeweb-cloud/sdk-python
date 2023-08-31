# UpdateServer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configurator** | [**UpdateServerConfigurator**](UpdateServerConfigurator.md) |  | [optional] 
**os_id** | **object** | Уникальный идентификатор операционной системы, которая будет установлена на облачный сервер. | [optional] 
**software_id** | **object** | Уникальный идентификатор программного обеспечения сервера. | [optional] 
**preset_id** | **object** | Уникальный идентификатор тарифа сервера. Нельзя передавать вместе с ключом &#x60;configurator&#x60;. | [optional] 
**bandwidth** | **object** | Пропускная способность тарифа. Доступные значения от 100 до 1000 с шагом 100. | [optional] 
**name** | **object** | Имя облачного сервера. Максимальная длина — 255 символов, имя должно быть уникальным. | [optional] 
**avatar_id** | **object** | Уникальный идентификатор аватара сервера. Описание методов работы с аватарами появится позднее. | [optional] 
**comment** | **object** | Комментарий к облачному серверу. Максимальная длина — 255 символов. | [optional] 
**image_id** | **object** | Уникальный идентификатор образа, который будет установлен на облачный сервер. Нельзя передавать вместе с &#x60;os_id&#x60;. | [optional] 
**cloud_init** | **object** | Cloud-init скрипт | [optional] 

## Example

```python
from timeweb_cloud_api.models.update_server import UpdateServer

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateServer from a JSON string
update_server_instance = UpdateServer.from_json(json)
# print the JSON string representation of the object
print UpdateServer.to_json()

# convert the object into a dict
update_server_dict = update_server_instance.to_dict()
# create an instance of UpdateServer from a dict
update_server_form_dict = update_server.from_dict(update_server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


