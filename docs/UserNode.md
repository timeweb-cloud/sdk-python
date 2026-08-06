# UserNode

Узел CDN, который раздает контент ресурса пользователям

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipv4_address** | **object** | IPv4-адрес раздающего узла. | 

## Example

```python
from timeweb_cloud_api.models.user_node import UserNode

# TODO update the JSON string below
json = "{}"
# create an instance of UserNode from a JSON string
user_node_instance = UserNode.from_json(json)
# print the JSON string representation of the object
print UserNode.to_json()

# convert the object into a dict
user_node_dict = user_node_instance.to_dict()
# create an instance of UserNode from a dict
user_node_form_dict = user_node.from_dict(user_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


