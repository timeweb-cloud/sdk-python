# ResourceTransfer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to_project** | **object** | Идентификатор проекта, куда переносится ресурс. | 
**resource_id** | **object** | Идентификатор перемещаемого ресурса (сервера, хранилища, кластера, балансировщика, базы данных или выделенного сервера). | 
**resource_type** | **object** | Тип перемещаемого ресурса. | 

## Example

```python
from timeweb_cloud_api.models.resource_transfer import ResourceTransfer

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceTransfer from a JSON string
resource_transfer_instance = ResourceTransfer.from_json(json)
# print the JSON string representation of the object
print ResourceTransfer.to_json()

# convert the object into a dict
resource_transfer_dict = resource_transfer_instance.to_dict()
# create an instance of ResourceTransfer from a dict
resource_transfer_form_dict = resource_transfer.from_dict(resource_transfer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


