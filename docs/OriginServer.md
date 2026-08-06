# OriginServer

Origin-сервер, с которого CDN забирает контент

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **object** | Домен или IPv4-адрес origin-сервера. | 
**port** | **object** | Порт origin-сервера. | 

## Example

```python
from timeweb_cloud_api.models.origin_server import OriginServer

# TODO update the JSON string below
json = "{}"
# create an instance of OriginServer from a JSON string
origin_server_instance = OriginServer.from_json(json)
# print the JSON string representation of the object
print OriginServer.to_json()

# convert the object into a dict
origin_server_dict = origin_server_instance.to_dict()
# create an instance of OriginServer from a dict
origin_server_form_dict = origin_server.from_dict(origin_server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


