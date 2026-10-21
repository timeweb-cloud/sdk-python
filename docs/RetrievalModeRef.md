# RetrievalModeRef

Привязка базы знаний к агенту

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID агента | 
**retrieval_mode** | [**RetrievalMode**](RetrievalMode.md) |  | 

## Example

```python
from timeweb_cloud_api.models.retrieval_mode_ref import RetrievalModeRef

# TODO update the JSON string below
json = "{}"
# create an instance of RetrievalModeRef from a JSON string
retrieval_mode_ref_instance = RetrievalModeRef.from_json(json)
# print the JSON string representation of the object
print RetrievalModeRef.to_json()

# convert the object into a dict
retrieval_mode_ref_dict = retrieval_mode_ref_instance.to_dict()
# create an instance of RetrievalModeRef from a dict
retrieval_mode_ref_form_dict = retrieval_mode_ref.from_dict(retrieval_mode_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


