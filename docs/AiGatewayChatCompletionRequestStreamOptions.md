# AiGatewayChatCompletionRequestStreamOptions

Настройки стриминга

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_usage** | **object** | Отправить перед &#x60;data: [DONE]&#x60; последний чанк с расходом токенов в &#x60;usage&#x60; | [optional] 

## Example

```python
from timeweb_cloud_api.models.ai_gateway_chat_completion_request_stream_options import AiGatewayChatCompletionRequestStreamOptions

# TODO update the JSON string below
json = "{}"
# create an instance of AiGatewayChatCompletionRequestStreamOptions from a JSON string
ai_gateway_chat_completion_request_stream_options_instance = AiGatewayChatCompletionRequestStreamOptions.from_json(json)
# print the JSON string representation of the object
print AiGatewayChatCompletionRequestStreamOptions.to_json()

# convert the object into a dict
ai_gateway_chat_completion_request_stream_options_dict = ai_gateway_chat_completion_request_stream_options_instance.to_dict()
# create an instance of AiGatewayChatCompletionRequestStreamOptions from a dict
ai_gateway_chat_completion_request_stream_options_form_dict = ai_gateway_chat_completion_request_stream_options.from_dict(ai_gateway_chat_completion_request_stream_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


