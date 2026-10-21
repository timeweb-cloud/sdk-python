# SkillCatalogItem

Навык из каталога Timeweb Cloud

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID навыка в каталоге | 
**key** | **object** | Уникальный ключ навыка в каталоге | 
**category** | **object** | Назначение: &#x60;communication&#x60; — манера общения, &#x60;support&#x60; — регламенты обслуживания, &#x60;sales&#x60; — продажи, &#x60;content&#x60; — документы и база знаний, &#x60;safety&#x60; — ограничения и безопасность | 
**name** | **object** | Название навыка | 
**description** | **object** | Краткое описание навыка | 
**when_to_use** | **object** | Когда применять навык | 
**instruction** | **object** | Полная инструкция навыка | 
**version** | **object** | Версия навыка в каталоге | 
**is_installed** | **object** | Навык уже установлен в аккаунте | 
**installed_skill_id** | **object** | ID установленного навыка в аккаунте | 
**is_modified** | **object** | Установленный навык изменялся владельцем | 
**has_catalog_update** | **object** | В каталоге есть версия новее установленной | 

## Example

```python
from timeweb_cloud_api.models.skill_catalog_item import SkillCatalogItem

# TODO update the JSON string below
json = "{}"
# create an instance of SkillCatalogItem from a JSON string
skill_catalog_item_instance = SkillCatalogItem.from_json(json)
# print the JSON string representation of the object
print SkillCatalogItem.to_json()

# convert the object into a dict
skill_catalog_item_dict = skill_catalog_item_instance.to_dict()
# create an instance of SkillCatalogItem from a dict
skill_catalog_item_form_dict = skill_catalog_item.from_dict(skill_catalog_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


