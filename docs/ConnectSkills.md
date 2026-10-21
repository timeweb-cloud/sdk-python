# ConnectSkills

Навыки для подключения. Нужно передать `skills` или `skill_ids`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skill_ids** | **object** | ID навыков. Агент закрепляется на их текущих версиях. Обязателен, если не передан &#x60;skills&#x60; | [optional] 
**skills** | **object** | Навыки с версиями. Если передан, &#x60;skill_ids&#x60; не используется | [optional] 

## Example

```python
from timeweb_cloud_api.models.connect_skills import ConnectSkills

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectSkills from a JSON string
connect_skills_instance = ConnectSkills.from_json(json)
# print the JSON string representation of the object
print ConnectSkills.to_json()

# convert the object into a dict
connect_skills_dict = connect_skills_instance.to_dict()
# create an instance of ConnectSkills from a dict
connect_skills_form_dict = connect_skills.from_dict(connect_skills_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


