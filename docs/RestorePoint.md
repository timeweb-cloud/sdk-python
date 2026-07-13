# RestorePoint


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID снапшота. | 
**created_at** | **object** | Дата и время создания снапшота в формате ISO 8601. | 
**expired_at** | **object** | Дата и время истечения снапшота в формате ISO 8601. | 
**status** | **object** | Статус снапшота.  - &#x60;creating&#x60; — создаётся; - &#x60;created&#x60; — создан; - &#x60;committed&#x60; — зафиксирован; - &#x60;rolled_back&#x60; — откачен; - &#x60;error&#x60; — ошибка; - &#x60;deleted&#x60; — удалён. | 
**vds_id** | **object** | ID облачного сервера (VDS), к которому относится снапшот. | 
**account_id** | **object** | ID аккаунта-владельца снапшота. | 

## Example

```python
from timeweb_cloud_api.models.restore_point import RestorePoint

# TODO update the JSON string below
json = "{}"
# create an instance of RestorePoint from a JSON string
restore_point_instance = RestorePoint.from_json(json)
# print the JSON string representation of the object
print RestorePoint.to_json()

# convert the object into a dict
restore_point_dict = restore_point_instance.to_dict()
# create an instance of RestorePoint from a dict
restore_point_form_dict = restore_point.from_dict(restore_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


