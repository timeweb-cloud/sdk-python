# TransferStatus

Статус трансфера.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **object** | Общий статус трансфера. | 
**tries** | **object** | Количество попыток. | 
**total_count** | **object** | Общее количество затронутых объектов. | 
**total_size** | **object** | Общий размер затронутых объектов. | 
**uploaded_count** | **object** | Количество перемещенных объектов. | 
**uploaded_size** | **object** | Размер перемещенных объектов. | 
**errors** | **object** |  | 

## Example

```python
from openapi_client.models.transfer_status import TransferStatus

# TODO update the JSON string below
json = "{}"
# create an instance of TransferStatus from a JSON string
transfer_status_instance = TransferStatus.from_json(json)
# print the JSON string representation of the object
print TransferStatus.to_json()

# convert the object into a dict
transfer_status_dict = transfer_status_instance.to_dict()
# create an instance of TransferStatus from a dict
transfer_status_form_dict = transfer_status.from_dict(transfer_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


