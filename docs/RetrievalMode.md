# RetrievalMode

Режим поиска по базе знаний: - `agentic` — агент сам решает, когда искать в базе знаний, и формирует запрос (поиск вызывается как инструмент) - `classic` — поиск по базе знаний выполняется для каждого сообщения пользователя, найденные фрагменты добавляются в контекст

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from timeweb_cloud_api.models.retrieval_mode import RetrievalMode

# TODO update the JSON string below
json = "{}"
# create an instance of RetrievalMode from a JSON string
retrieval_mode_instance = RetrievalMode.from_json(json)
# print the JSON string representation of the object
print RetrievalMode.to_json()

# convert the object into a dict
retrieval_mode_dict = retrieval_mode_instance.to_dict()
# create an instance of RetrievalMode from a dict
retrieval_mode_form_dict = retrieval_mode.from_dict(retrieval_mode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


