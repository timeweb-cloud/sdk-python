# StreamError

Ошибка потокового чата, возникшая до начала потока

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **object** | Код ошибки | [optional] 
**message** | **object** | Текст ошибки | [optional] 
**status_code** | **object** | Код HTTP-статуса (у ошибок валидации и внутренних ошибок) | [optional] 
**error** | **object** | Название HTTP-статуса (только у ошибок валидации) | [optional] 

## Example

```python
from timeweb_cloud_api.models.stream_error import StreamError

# TODO update the JSON string below
json = "{}"
# create an instance of StreamError from a JSON string
stream_error_instance = StreamError.from_json(json)
# print the JSON string representation of the object
print StreamError.to_json()

# convert the object into a dict
stream_error_dict = stream_error_instance.to_dict()
# create an instance of StreamError from a dict
stream_error_form_dict = stream_error.from_dict(stream_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


