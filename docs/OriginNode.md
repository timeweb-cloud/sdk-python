# OriginNode

Подсеть узлов CDN, которые обращаются к источнику контента

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipv4_subnet** | **object** | IPv4-адрес или подсеть узлов. &#x60;null&#x60;, если у записи нет IPv4-подсети. | 
**ipv6_subnet** | **object** | IPv6-адрес или подсеть узлов. &#x60;null&#x60;, если у записи нет IPv6-подсети. | 

## Example

```python
from timeweb_cloud_api.models.origin_node import OriginNode

# TODO update the JSON string below
json = "{}"
# create an instance of OriginNode from a JSON string
origin_node_instance = OriginNode.from_json(json)
# print the JSON string representation of the object
print OriginNode.to_json()

# convert the object into a dict
origin_node_dict = origin_node_instance.to_dict()
# create an instance of OriginNode from a dict
origin_node_form_dict = origin_node.from_dict(origin_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


