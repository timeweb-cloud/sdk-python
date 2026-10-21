# SendAiSolutionMessage200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ai_solution_chat_reply** | [**AiSolutionChatReply**](AiSolutionChatReply.md) |  | 

## Example

```python
from timeweb_cloud_api.models.send_ai_solution_message200_response import SendAiSolutionMessage200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SendAiSolutionMessage200Response from a JSON string
send_ai_solution_message200_response_instance = SendAiSolutionMessage200Response.from_json(json)
# print the JSON string representation of the object
print SendAiSolutionMessage200Response.to_json()

# convert the object into a dict
send_ai_solution_message200_response_dict = send_ai_solution_message200_response_instance.to_dict()
# create an instance of SendAiSolutionMessage200Response from a dict
send_ai_solution_message200_response_form_dict = send_ai_solution_message200_response.from_dict(send_ai_solution_message200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


