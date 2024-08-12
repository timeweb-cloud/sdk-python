# Commit


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sha** | **object** | Хэш коммита. | 
**created_at** | **object** | Значение времени, указанное в комбинированном формате даты и времени ISO8601, которое представляет, когда был создан коммит. | 
**message** | **object** | Сообщение коммита. | 

## Example

```python
from timeweb_cloud_api.models.commit import Commit

# TODO update the JSON string below
json = "{}"
# create an instance of Commit from a JSON string
commit_instance = Commit.from_json(json)
# print the JSON string representation of the object
print Commit.to_json()

# convert the object into a dict
commit_dict = commit_instance.to_dict()
# create an instance of Commit from a dict
commit_form_dict = commit.from_dict(commit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


