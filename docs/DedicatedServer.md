# DedicatedServer

Выделенный сервер

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID для каждого экземпляра выделенного сервера. Автоматически генерируется при создании. | 
**cpu_description** | **object** | Описание параметров процессора выделенного сервера. | 
**hdd_description** | **object** | Описание параметров жёсткого диска выделенного сервера. | 
**ram_description** | **object** | Описание ОЗУ выделенного сервера. | 
**created_at** | **object** | Значение времени, указанное в комбинированном формате даты и времени ISO8601, которое представляет, когда был создан выделенный сервер. | 
**ip** | **object** | IP-адрес сетевого интерфейса IPv4. | 
**ipmi_ip** | **object** | IP-адрес сетевого интерфейса IPMI. | 
**ipmi_login** | **object** | Логин, используемый для входа в IPMI-консоль. | 
**ipmi_password** | **object** | Пароль, используемый для входа в IPMI-консоль. | 
**ipv6** | **object** | IP-адрес сетевого интерфейса IPv6. | 
**node_id** | **object** | Внутренний дополнительный ID сервера. | 
**name** | **object** | Удобочитаемое имя, установленное для выделенного сервера. | 
**comment** | **object** | Комментарий к выделенному серверу. | 
**vnc_pass** | **object** | Пароль для подключения к VNC-консоли выделенного сервера. | 
**status** | **object** | Строка состояния, указывающая состояние выделенного сервера. Может быть «installing», «installed», «on» или «off». | 
**os_id** | **object** | ID операционной системы, установленной на выделенный сервер. | 
**cp_id** | **object** | ID панели управления, установленной на выделенный сервер. | 
**bandwidth_id** | **object** | ID интернет-канала, установленного на выделенный сервер. | 
**network_drive_id** | **object** | Массив уникальных ID сетевых дисков, подключенных к выделенному серверу. | 
**additional_ip_addr_id** | **object** | Массив уникальных ID дополнительных IP-адресов, подключенных к выделенному серверу. | 
**plan_id** | **object** | ID списка дополнительных услуг выделенного сервера. | 
**price** | **object** | Стоимость выделенного сервера. | 
**location** | **object** | Локация сервера. | 
**autoinstall_ready** | **object** | Количество готовых к автоматической выдаче серверов. Если значение равно 0, сервер будет установлен через инженеров. | 
**password** | **object** | Пароль root сервера или пароль Администратора для серверов Windows. | 
**avatar_link** | **object** | Ссылка на аватар сервера. | 
**is_pre_installed** | **object** | Это логическое значение, которое показывает, готов ли выделенный сервер к моментальной выдаче. | 
**preset_id** | **object** | ID тарифа сервера. | 
**project_id** | **object** | ID проекта | 

## Example

```python
from timeweb_cloud_api.models.dedicated_server import DedicatedServer

# TODO update the JSON string below
json = "{}"
# create an instance of DedicatedServer from a JSON string
dedicated_server_instance = DedicatedServer.from_json(json)
# print the JSON string representation of the object
print DedicatedServer.to_json()

# convert the object into a dict
dedicated_server_dict = dedicated_server_instance.to_dict()
# create an instance of DedicatedServer from a dict
dedicated_server_form_dict = dedicated_server.from_dict(dedicated_server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


