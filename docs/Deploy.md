# Deploy


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **object** | ID приложения. | 
**commit_sha** | **object** | Хэш коммита. | 
**id** | **object** | ID. | 
**started_at** | **object** | Время запуска деплоя. | 
**ended_at** | **object** | Время окончания деплоя. Определено для завершенных деплоев | 
**status** | [**DeployStatus**](DeployStatus.md) |  | 
**commit_msg** | **object** | Сообщение коммита. | 

## Example

```python
from timeweb_cloud_api.models.deploy import Deploy

# TODO update the JSON string below
json = "{}"
# create an instance of Deploy from a JSON string
deploy_instance = Deploy.from_json(json)
# print the JSON string representation of the object
print Deploy.to_json()

# convert the object into a dict
deploy_dict = deploy_instance.to_dict()
# create an instance of Deploy from a dict
deploy_form_dict = deploy.from_dict(deploy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


