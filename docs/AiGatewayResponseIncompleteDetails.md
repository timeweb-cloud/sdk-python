# AiGatewayResponseIncompleteDetails

Почему ответ неполный

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **object** | Причина | [optional] 

## Example

```python
from timeweb_cloud_api.models.ai_gateway_response_incomplete_details import AiGatewayResponseIncompleteDetails

# TODO update the JSON string below
json = "{}"
# create an instance of AiGatewayResponseIncompleteDetails from a JSON string
ai_gateway_response_incomplete_details_instance = AiGatewayResponseIncompleteDetails.from_json(json)
# print the JSON string representation of the object
print AiGatewayResponseIncompleteDetails.to_json()

# convert the object into a dict
ai_gateway_response_incomplete_details_dict = ai_gateway_response_incomplete_details_instance.to_dict()
# create an instance of AiGatewayResponseIncompleteDetails from a dict
ai_gateway_response_incomplete_details_form_dict = ai_gateway_response_incomplete_details.from_dict(ai_gateway_response_incomplete_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


