# UpdateServerNATRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nat_mode** | **object** | Правило для маршрутизации трафика. \\  Досутпные правила: &#x60;dnat_and_snat&#x60; – разрешен входящий и исходящий трафик, &#x60;snat&#x60; – разрешен только исходящий трафик, &#x60;no_nat&#x60; – разрешен трафик только в локальной сети. | 

## Example

```python
from openapi_client.models.update_server_nat_request import UpdateServerNATRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateServerNATRequest from a JSON string
update_server_nat_request_instance = UpdateServerNATRequest.from_json(json)
# print the JSON string representation of the object
print UpdateServerNATRequest.to_json()

# convert the object into a dict
update_server_nat_request_dict = update_server_nat_request_instance.to_dict()
# create an instance of UpdateServerNATRequest from a dict
update_server_nat_request_form_dict = update_server_nat_request.from_dict(update_server_nat_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


