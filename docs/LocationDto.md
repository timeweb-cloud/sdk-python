# LocationDto

Локация

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | [**Location**](Location.md) |  | 
**location_code** | **object** | Код локации в формате &#x60;ISO 3166&#x60; | 
**availability_zones** | **object** | Список зон, доступных в данной локации | 

## Example

```python
from timeweb_cloud_api.models.location_dto import LocationDto

# TODO update the JSON string below
json = "{}"
# create an instance of LocationDto from a JSON string
location_dto_instance = LocationDto.from_json(json)
# print the JSON string representation of the object
print LocationDto.to_json()

# convert the object into a dict
location_dto_dict = location_dto_instance.to_dict()
# create an instance of LocationDto from a dict
location_dto_form_dict = location_dto.from_dict(location_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


