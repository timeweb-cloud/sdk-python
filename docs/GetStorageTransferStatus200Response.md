# GetStorageTransferStatus200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transfer_status** | [**TransferStatus**](TransferStatus.md) |  | 

## Example

```python
from timeweb_cloud_api.models.get_storage_transfer_status200_response import GetStorageTransferStatus200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetStorageTransferStatus200Response from a JSON string
get_storage_transfer_status200_response_instance = GetStorageTransferStatus200Response.from_json(json)
# print the JSON string representation of the object
print GetStorageTransferStatus200Response.to_json()

# convert the object into a dict
get_storage_transfer_status200_response_dict = get_storage_transfer_status200_response_instance.to_dict()
# create an instance of GetStorageTransferStatus200Response from a dict
get_storage_transfer_status200_response_form_dict = get_storage_transfer_status200_response.from_dict(get_storage_transfer_status200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


