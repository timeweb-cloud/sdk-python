# ConfigOriginAws

Ключи для доступа к источнику, совместимому с Amazon S3 API. `null` — не использовать авторизацию AWS.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key** | **object** | Access key. | 
**secret_key** | **object** | Secret key. | 

## Example

```python
from timeweb_cloud_api.models.config_origin_aws import ConfigOriginAws

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigOriginAws from a JSON string
config_origin_aws_instance = ConfigOriginAws.from_json(json)
# print the JSON string representation of the object
print ConfigOriginAws.to_json()

# convert the object into a dict
config_origin_aws_dict = config_origin_aws_instance.to_dict()
# create an instance of ConfigOriginAws from a dict
config_origin_aws_form_dict = config_origin_aws.from_dict(config_origin_aws_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


