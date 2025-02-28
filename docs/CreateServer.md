# CreateServer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration** | [**CreateServerConfiguration**](CreateServerConfiguration.md) |  | [optional] 
**is_ddos_guard** | **object** | Защита от DDoS. Серверу выдается защищенный IP-адрес с защитой уровня L3 / L4. Для включения защиты уровня L7 необходимо создать тикет в техническую поддержку. | [optional] 
**os_id** | **object** | ID операционной системы, которая будет установлена на облачный сервер. Нельзя передавать вместе с &#x60;image_id&#x60;. | [optional] 
**image_id** | **object** | ID образа, который будет установлен на облачный сервер. Нельзя передавать вместе с &#x60;os_id&#x60;. | [optional] 
**software_id** | **object** | ID программного обеспечения сервера. | [optional] 
**preset_id** | **object** | ID тарифа сервера. Нельзя передавать вместе с ключом &#x60;configurator&#x60;. | [optional] 
**bandwidth** | **object** | Пропускная способность тарифа. Доступные значения от 100 до 1000 с шагом 100. | [optional] 
**name** | **object** | Имя облачного сервера. Максимальная длина — 255 символов, имя должно быть уникальным. | 
**avatar_id** | **object** | ID аватара сервера. Описание методов работы с аватарами появится позднее. | [optional] 
**comment** | **object** | Комментарий к облачному серверу. Максимальная длина — 255 символов. | [optional] 
**ssh_keys_ids** | **object** | Список SSH-ключей. | [optional] 
**is_local_network** | **object** | Локальная сеть. | [optional] 
**network** | [**Network**](Network.md) |  | [optional] 
**cloud_init** | **object** | Cloud-init скрипт | [optional] 
**availability_zone** | [**AvailabilityZone**](AvailabilityZone.md) |  | [optional] 

## Example

```python
from timeweb_cloud_api.models.create_server import CreateServer

# TODO update the JSON string below
json = "{}"
# create an instance of CreateServer from a JSON string
create_server_instance = CreateServer.from_json(json)
# print the JSON string representation of the object
print CreateServer.to_json()

# convert the object into a dict
create_server_dict = create_server_instance.to_dict()
# create an instance of CreateServer from a dict
create_server_form_dict = create_server.from_dict(create_server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


