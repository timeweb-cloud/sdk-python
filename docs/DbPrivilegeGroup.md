# DbPrivilegeGroup

Привилегия, доступная для кластера базы данных, и её группа доступа

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**privilege** | [**PropertiesMysql**](PropertiesMysql.md) |  | 
**group** | **object** | Группа доступа, к которой относится привилегия: &#x60;GLOBAL&#x60; — привилегии уровня всего кластера, &#x60;DATA&#x60; — доступ к данным, &#x60;STRUCTURE&#x60; — изменение структуры, &#x60;OTHERS&#x60; — прочие привилегии. | 

## Example

```python
from timeweb_cloud_api.models.db_privilege_group import DbPrivilegeGroup

# TODO update the JSON string below
json = "{}"
# create an instance of DbPrivilegeGroup from a JSON string
db_privilege_group_instance = DbPrivilegeGroup.from_json(json)
# print the JSON string representation of the object
print DbPrivilegeGroup.to_json()

# convert the object into a dict
db_privilege_group_dict = db_privilege_group_instance.to_dict()
# create an instance of DbPrivilegeGroup from a dict
db_privilege_group_form_dict = db_privilege_group.from_dict(db_privilege_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


