# GetLinkCardPayment200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confirmation_url** | **object** | URL для подтверждения оплаты | 
**response_id** | **object** | ID запроса, который можно указывать при обращении в службу технической поддержки, чтобы помочь определить проблему. | 

## Example

```python
from timeweb_cloud_api.models.get_link_card_payment200_response import GetLinkCardPayment200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetLinkCardPayment200Response from a JSON string
get_link_card_payment200_response_instance = GetLinkCardPayment200Response.from_json(json)
# print the JSON string representation of the object
print GetLinkCardPayment200Response.to_json()

# convert the object into a dict
get_link_card_payment200_response_dict = get_link_card_payment200_response_instance.to_dict()
# create an instance of GetLinkCardPayment200Response from a dict
get_link_card_payment200_response_form_dict = get_link_card_payment200_response.from_dict(get_link_card_payment200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


