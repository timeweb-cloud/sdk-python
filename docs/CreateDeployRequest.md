# CreateDeployRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commit_sha** | **object** | Хэш коммита. | [optional] 

## Example

```python
from timeweb_cloud_api.models.create_deploy_request import CreateDeployRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDeployRequest from a JSON string
create_deploy_request_instance = CreateDeployRequest.from_json(json)
# print the JSON string representation of the object
print CreateDeployRequest.to_json()

# convert the object into a dict
create_deploy_request_dict = create_deploy_request_instance.to_dict()
# create an instance of CreateDeployRequest from a dict
create_deploy_request_form_dict = create_deploy_request.from_dict(create_deploy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


