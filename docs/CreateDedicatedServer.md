# CreateDedicatedServer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_id** | **object** | Уникальный идентификатор списка дополнительных услуг выделенного сервера. | 
**preset_id** | **object** | Уникальный идентификатор тарифа выделенного сервера. | 
**os_id** | **object** | Уникальный идентификатор операционной системы, которая будет установлена на выделенный сервер. | [optional] 
**cp_id** | **object** | Уникальный идентификатор панели управления, которая будет установлена на выделенный сервер. | [optional] 
**bandwidth_id** | **object** | Уникальный идентификатор интернет-канала, который будет установлен на выделенный сервер. | [optional] 
**network_drive_id** | **object** | Уникальный идентификатор сетевого диска, который будет установлен на выделенный сервер. | [optional] 
**additional_ip_addr_id** | **object** | Уникальный идентификатор дополнительного IP-адреса, который будет установлен на выделенный сервер. | [optional] 
**payment_period** | **object** | Период оплаты. | 
**name** | **object** | Удобочитаемое имя выделенного сервера. Максимальная длина — 255 символов, имя должно быть уникальным. | 
**comment** | **object** | Комментарий к выделенному серверу. Максимальная длина — 255 символов. | [optional] 

## Example

```python
from timeweb_cloud_api.models.create_dedicated_server import CreateDedicatedServer

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDedicatedServer from a JSON string
create_dedicated_server_instance = CreateDedicatedServer.from_json(json)
# print the JSON string representation of the object
print CreateDedicatedServer.to_json()

# convert the object into a dict
create_dedicated_server_dict = create_dedicated_server_instance.to_dict()
# create an instance of CreateDedicatedServer from a dict
create_dedicated_server_form_dict = create_dedicated_server.from_dict(create_dedicated_server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


