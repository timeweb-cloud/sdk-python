# Document

Документ базы знаний

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID документа | 
**name** | **object** | Название документа | 
**size** | **object** | Размер в байтах. Для документа по ссылке — значение заголовка &#x60;Content-Length&#x60; на момент добавления, &#x60;0&#x60;, если сервер его не вернул | 
**status** | **object** | Статус индексации: - &#x60;new&#x60; — документ добавлен и ждёт индексации - &#x60;indexing&#x60; — индексируется - &#x60;indexed&#x60; — проиндексирован, используется в поиске - &#x60;error&#x60; — ошибка индексации, подробности в &#x60;status_info&#x60; | 
**type** | **object** | Тип документа: &#x60;file&#x60; — загруженный файл, &#x60;link&#x60; — документ по ссылке | 
**indexing_schedule** | [**IndexingSchedule**](IndexingSchedule.md) |  | 
**indexing_version** | **object** | Версия индексации документа | 
**status_info** | [**DocumentStatusInfo**](DocumentStatusInfo.md) |  | 
**link** | **object** | URL документа. Только для документов типа &#x60;link&#x60; | [optional] 
**created_at** | **object** | Дата и время добавления документа | 
**updated_at** | **object** | Дата и время последнего изменения документа | 

## Example

```python
from timeweb_cloud_api.models.document import Document

# TODO update the JSON string below
json = "{}"
# create an instance of Document from a JSON string
document_instance = Document.from_json(json)
# print the JSON string representation of the object
print Document.to_json()

# convert the object into a dict
document_dict = document_instance.to_dict()
# create an instance of Document from a dict
document_form_dict = document.from_dict(document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


