# CreateAppV2Network

Настройки сети backend-приложения.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID VPC, к которой необходимо подключить приложение. | [optional] 
**local_ip** | **object** | Локальный IP-адрес приложения в выбранной VPC. | [optional] 
**floating_ip** | **object** | Публичный IPv4-адрес свободного плавающего IP аккаунта или create_ip для создания нового IP (оплачивается отдельно). IP остаётся на аккаунте и привязывается к приложению. Доступно для аккаунтов, которым включена эта возможность; для остальных поле игнорируется. Если поле не передано, публичный IP выделяется автоматически. | [optional] 

## Example

```python
from timeweb_cloud_api.models.create_app_v2_network import CreateAppV2Network

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAppV2Network from a JSON string
create_app_v2_network_instance = CreateAppV2Network.from_json(json)
# print the JSON string representation of the object
print CreateAppV2Network.to_json()

# convert the object into a dict
create_app_v2_network_dict = create_app_v2_network_instance.to_dict()
# create an instance of CreateAppV2Network from a dict
create_app_v2_network_form_dict = create_app_v2_network.from_dict(create_app_v2_network_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


