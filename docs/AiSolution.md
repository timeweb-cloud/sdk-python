# AiSolution

AI-решение

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID решения | 
**account_id** | **object** | ID аккаунта, которому принадлежит решение | 
**name** | **object** | Название решения | 
**description** | **object** | Описание решения | 
**type** | **object** | Тип решения. Сейчас всегда &#x60;openclaw&#x60; | 
**vds_id** | **object** | ID облачного сервера, на котором развёрнуто решение. Сведения о сервере — в разделе «Облачные серверы» | 
**ai_key_id** | **object** | ID ключа AI Gateway, выпущенного для решения. Сведения о ключе — в разделе AI Gateway; перевыпустить ключ можно только через решение | 
**model_id** | **object** | ID модели, с которой работает решение | 
**status** | **object** | Статус решения, выводится из состояния его сервера: &#x60;creating&#x60; — сервер разворачивается или выполняет длительную операцию; &#x60;active&#x60; — сервер работает; &#x60;stopped&#x60; — сервер выключен или перезагружается; &#x60;blocked&#x60; — сервер заблокирован или не оплачен; &#x60;error&#x60; — сервер в состоянии ошибки или не найден; &#x60;deleted&#x60; — сервер удаляется. Готовность агента к общению показывает метод получения статуса чата | 
**created_at** | **object** | Дата создания | 
**updated_at** | **object** | Дата последнего изменения | 

## Example

```python
from timeweb_cloud_api.models.ai_solution import AiSolution

# TODO update the JSON string below
json = "{}"
# create an instance of AiSolution from a JSON string
ai_solution_instance = AiSolution.from_json(json)
# print the JSON string representation of the object
print AiSolution.to_json()

# convert the object into a dict
ai_solution_dict = ai_solution_instance.to_dict()
# create an instance of AiSolution from a dict
ai_solution_form_dict = ai_solution.from_dict(ai_solution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


