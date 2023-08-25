# Vds

Сервер

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | Уникальный идентификатор для каждого экземпляра сервера. Автоматически генерируется при создании. | 
**name** | **object** | Удобочитаемое имя, установленное для выделенного сервера. | 
**comment** | **object** | Комментарий к выделенному серверу. | 
**created_at** | **object** | Дата создания сервера в формате ISO8061. | 
**os** | [**VdsOs**](VdsOs.md) |  | 
**software** | [**VdsSoftware**](VdsSoftware.md) |  | 
**preset_id** | **object** | Уникальный идентификатор тарифа сервера. | 
**location** | **object** | Локация сервера. | 
**configurator_id** | **object** | Уникальный идентификатор конфигуратора сервера. | 
**boot_mode** | **object** | Режим загрузки ОС сервера. | 
**status** | **object** | Статус сервера. | 
**start_at** | **object** | Значение времени, указанное в комбинированном формате даты и времени ISO8601, которое представляет, когда был запущен сервер. | 
**is_ddos_guard** | **object** | Это логическое значение, которое показывает, включена ли защита от DDOS у данного сервера. | 
**cpu** | **object** | Количество ядер процессора сервера. | 
**cpu_frequency** | **object** | Частота ядер процессора сервера. | 
**ram** | **object** | Размер (в Мб) ОЗУ сервера. | 
**disks** | **object** | Список дисков сервера. | 
**avatar_id** | **object** | Уникальный идентификатор аватара сервера. Описание методов работы с аватарами появится позднее. | 
**vnc_pass** | **object** | Пароль от VNC. | 
**root_pass** | **object** | Пароль root сервера или пароль Администратора для серверов Windows. | 
**image** | [**VdsImage**](VdsImage.md) |  | 
**networks** | **object** | Список сетей диска. | 

## Example

```python
from timeweb_cloud_api.models.vds import Vds

# TODO update the JSON string below
json = "{}"
# create an instance of Vds from a JSON string
vds_instance = Vds.from_json(json)
# print the JSON string representation of the object
print Vds.to_json()

# convert the object into a dict
vds_dict = vds_instance.to_dict()
# create an instance of Vds from a dict
vds_form_dict = vds.from_dict(vds_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


