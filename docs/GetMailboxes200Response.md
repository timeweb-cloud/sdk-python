# GetMailboxes200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Meta**](Meta.md) |  | 
**mailboxes** | **object** |  | 

## Example

```python
from openapi_client.models.get_mailboxes200_response import GetMailboxes200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetMailboxes200Response from a JSON string
get_mailboxes200_response_instance = GetMailboxes200Response.from_json(json)
# print the JSON string representation of the object
print GetMailboxes200Response.to_json()

# convert the object into a dict
get_mailboxes200_response_dict = get_mailboxes200_response_instance.to_dict()
# create an instance of GetMailboxes200Response from a dict
get_mailboxes200_response_form_dict = get_mailboxes200_response.from_dict(get_mailboxes200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


