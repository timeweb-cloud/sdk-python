# timeweb_cloud_api.ImagesApi

All URIs are relative to *https://api.timeweb.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_image**](ImagesApi.md#create_image) | **POST** /api/v1/images | Создание образа
[**create_image_download_url**](ImagesApi.md#create_image_download_url) | **POST** /api/v1/images/{image_id}/download-url | Создание ссылки на скачивание образа
[**delete_image**](ImagesApi.md#delete_image) | **DELETE** /api/v1/images/{image_id} | Удаление образа
[**delete_image_download_url**](ImagesApi.md#delete_image_download_url) | **DELETE** /api/v1/images/{image_id}/download-url/{image_url_id} | Удаление ссылки на образ
[**get_image**](ImagesApi.md#get_image) | **GET** /api/v1/images/{image_id} | Получение информации о образе
[**get_image_download_url**](ImagesApi.md#get_image_download_url) | **GET** /api/v1/images/{image_id}/download-url/{image_url_id} | Получение информации о ссылке на скачивание образа
[**get_image_download_urls**](ImagesApi.md#get_image_download_urls) | **GET** /api/v1/images/{image_id}/download-url | Получение информации о ссылках на скачивание образов
[**get_images**](ImagesApi.md#get_images) | **GET** /api/v1/images | Получение списка образов
[**update_image**](ImagesApi.md#update_image) | **PATCH** /api/v1/images/{image_id} | Обновление информации о образе
[**upload_image**](ImagesApi.md#upload_image) | **POST** /api/v1/images/{image_id} | Загрузка образа


# **create_image**
> ImageOutResponse create_image(image_in_api)

Создание образа

Чтобы создать образ, отправьте POST запрос в `/api/v1/images`, задав необходимые атрибуты.   Для загрузки собственного образа вам нужно отправить параметры `location`, `os` и не указывать `disk_id`. Поддерживается два способа загрузки:  1. По ссылке. Для этого укажите `upload_url` с ссылкой на загрузку образа 2. Из файла. Для этого воспользуйтесь методом POST `/api/v1/images/{image_id}` Образ будет создан с использованием предоставленной информации.    Тело ответа будет содержать объект JSON с информацией о созданном образе.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.image_in_api import ImageInAPI
from timeweb_cloud_api.models.image_out_response import ImageOutResponse
from timeweb_cloud_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.timeweb.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = timeweb_cloud_api.Configuration(
    host = "https://api.timeweb.cloud"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = timeweb_cloud_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with timeweb_cloud_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = timeweb_cloud_api.ImagesApi(api_client)
    image_in_api = timeweb_cloud_api.ImageInAPI() # ImageInAPI | 

    try:
        # Создание образа
        api_response = api_instance.create_image(image_in_api)
        print("The response of ImagesApi->create_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->create_image: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_in_api** | [**ImageInAPI**](ImageInAPI.md)|  | 

### Return type

[**ImageOutResponse**](ImageOutResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Образ создан |  -  |
**400** |  |  -  |
**401** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_image_download_url**
> ImageDownloadResponse create_image_download_url(image_id, image_url_in)

Создание ссылки на скачивание образа

Чтобы создать ссылку на скачивание образа, отправьте запрос POST в `/api/v1/images/{image_id}/download-url`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.image_download_response import ImageDownloadResponse
from timeweb_cloud_api.models.image_url_in import ImageUrlIn
from timeweb_cloud_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.timeweb.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = timeweb_cloud_api.Configuration(
    host = "https://api.timeweb.cloud"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = timeweb_cloud_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with timeweb_cloud_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = timeweb_cloud_api.ImagesApi(api_client)
    image_id = None # object | ID образа
    image_url_in = timeweb_cloud_api.ImageUrlIn() # ImageUrlIn | 

    try:
        # Создание ссылки на скачивание образа
        api_response = api_instance.create_image_download_url(image_id, image_url_in)
        print("The response of ImagesApi->create_image_download_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->create_image_download_url: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | [**object**](.md)| ID образа | 
 **image_url_in** | [**ImageUrlIn**](ImageUrlIn.md)|  | 

### Return type

[**ImageDownloadResponse**](ImageDownloadResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Ссылка успешно создана |  -  |
**400** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |
**409** | Образ уже загружен в облачное хранилище |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_image**
> delete_image(image_id)

Удаление образа

Чтобы удалить образ, отправьте запрос DELETE в `/api/v1/images/{image_id}`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.timeweb.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = timeweb_cloud_api.Configuration(
    host = "https://api.timeweb.cloud"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = timeweb_cloud_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with timeweb_cloud_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = timeweb_cloud_api.ImagesApi(api_client)
    image_id = None # object | ID образа

    try:
        # Удаление образа
        api_instance.delete_image(image_id)
    except Exception as e:
        print("Exception when calling ImagesApi->delete_image: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | [**object**](.md)| ID образа | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Образ удален |  -  |
**400** |  |  -  |
**401** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_image_download_url**
> delete_image_download_url(image_id, image_url_id)

Удаление ссылки на образ

Чтобы удалить ссылку на образ, отправьте DELETE запрос в `/api/v1/images/{image_id}/download-url/{image_url_id}`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.timeweb.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = timeweb_cloud_api.Configuration(
    host = "https://api.timeweb.cloud"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = timeweb_cloud_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with timeweb_cloud_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = timeweb_cloud_api.ImagesApi(api_client)
    image_id = None # object | ID образа
    image_url_id = None # object | ID ссылки

    try:
        # Удаление ссылки на образ
        api_instance.delete_image_download_url(image_id, image_url_id)
    except Exception as e:
        print("Exception when calling ImagesApi->delete_image_download_url: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | [**object**](.md)| ID образа | 
 **image_url_id** | [**object**](.md)| ID ссылки | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Ссылка удалена |  -  |
**400** |  |  -  |
**401** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image**
> ImageOutResponse get_image(image_id)

Получение информации о образе

Чтобы получить образ, отправьте запрос GET в `/api/v1/images/{image_id}`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.image_out_response import ImageOutResponse
from timeweb_cloud_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.timeweb.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = timeweb_cloud_api.Configuration(
    host = "https://api.timeweb.cloud"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = timeweb_cloud_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with timeweb_cloud_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = timeweb_cloud_api.ImagesApi(api_client)
    image_id = None # object | ID образа

    try:
        # Получение информации о образе
        api_response = api_instance.get_image(image_id)
        print("The response of ImagesApi->get_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->get_image: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | [**object**](.md)| ID образа | 

### Return type

[**ImageOutResponse**](ImageOutResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Информация о образе |  -  |
**400** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_download_url**
> ImageDownloadResponse get_image_download_url(image_id, image_url_id)

Получение информации о ссылке на скачивание образа

Чтобы получить информацию о ссылке на скачивание образа, отправьте запрос GET в `/api/v1/images/{image_id}/download-url/{image_url_id}`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.image_download_response import ImageDownloadResponse
from timeweb_cloud_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.timeweb.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = timeweb_cloud_api.Configuration(
    host = "https://api.timeweb.cloud"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = timeweb_cloud_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with timeweb_cloud_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = timeweb_cloud_api.ImagesApi(api_client)
    image_id = None # object | ID образа
    image_url_id = None # object | ID ссылки

    try:
        # Получение информации о ссылке на скачивание образа
        api_response = api_instance.get_image_download_url(image_id, image_url_id)
        print("The response of ImagesApi->get_image_download_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->get_image_download_url: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | [**object**](.md)| ID образа | 
 **image_url_id** | [**object**](.md)| ID ссылки | 

### Return type

[**ImageDownloadResponse**](ImageDownloadResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Информация о ссылке на загрузку |  -  |
**400** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_download_urls**
> ImageDownloadsResponse get_image_download_urls(image_id, limit=limit, offset=offset)

Получение информации о ссылках на скачивание образов

Чтобы получить информацию о ссылках на скачивание образов, отправьте запрос GET в `/api/v1/images/{image_id}/download-url`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.image_downloads_response import ImageDownloadsResponse
from timeweb_cloud_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.timeweb.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = timeweb_cloud_api.Configuration(
    host = "https://api.timeweb.cloud"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = timeweb_cloud_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with timeweb_cloud_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = timeweb_cloud_api.ImagesApi(api_client)
    image_id = None # object | ID образа
    limit = None # object |  (optional)
    offset = None # object |  (optional)

    try:
        # Получение информации о ссылках на скачивание образов
        api_response = api_instance.get_image_download_urls(image_id, limit=limit, offset=offset)
        print("The response of ImagesApi->get_image_download_urls:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->get_image_download_urls: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | [**object**](.md)| ID образа | 
 **limit** | [**object**](.md)|  | [optional] 
 **offset** | [**object**](.md)|  | [optional] 

### Return type

[**ImageDownloadsResponse**](ImageDownloadsResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Информация о ссылке на загрузку |  -  |
**400** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_images**
> ImagesOutResponse get_images(limit=limit, offset=offset)

Получение списка образов

Чтобы получить список образов, отправьте GET запрос на `/api/v1/images`

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.images_out_response import ImagesOutResponse
from timeweb_cloud_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.timeweb.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = timeweb_cloud_api.Configuration(
    host = "https://api.timeweb.cloud"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = timeweb_cloud_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with timeweb_cloud_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = timeweb_cloud_api.ImagesApi(api_client)
    limit = None # object |  (optional)
    offset = None # object |  (optional)

    try:
        # Получение списка образов
        api_response = api_instance.get_images(limit=limit, offset=offset)
        print("The response of ImagesApi->get_images:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->get_images: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | [**object**](.md)|  | [optional] 
 **offset** | [**object**](.md)|  | [optional] 

### Return type

[**ImagesOutResponse**](ImagesOutResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом images |  -  |
**400** |  |  -  |
**401** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_image**
> ImageOutResponse update_image(image_id, image_update_api)

Обновление информации о образе

Чтобы обновить только определенные атрибуты образа, отправьте запрос PATCH в `/api/v1/images/{image_id}`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.image_out_response import ImageOutResponse
from timeweb_cloud_api.models.image_update_api import ImageUpdateAPI
from timeweb_cloud_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.timeweb.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = timeweb_cloud_api.Configuration(
    host = "https://api.timeweb.cloud"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = timeweb_cloud_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with timeweb_cloud_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = timeweb_cloud_api.ImagesApi(api_client)
    image_id = None # object | ID образа
    image_update_api = timeweb_cloud_api.ImageUpdateAPI() # ImageUpdateAPI | 

    try:
        # Обновление информации о образе
        api_response = api_instance.update_image(image_id, image_update_api)
        print("The response of ImagesApi->update_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->update_image: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | [**object**](.md)| ID образа | 
 **image_update_api** | [**ImageUpdateAPI**](ImageUpdateAPI.md)|  | 

### Return type

[**ImageOutResponse**](ImageOutResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Образ обновлен |  -  |
**400** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_image**
> UploadSuccessfulResponse upload_image(image_id, content_disposition=content_disposition)

Загрузка образа

Чтобы загрузить свой образ, отправьте POST запрос в `/api/v1/images/{image_id}`, отправив файл как `multipart/form-data`, указав имя файла в заголовке `Content-Disposition`.   Перед загрузкой, нужно создать образ используя POST `/api/v1/images`, указав параметры `location`, `os`   Тело ответа будет содержать объект JSON с информацией о загруженном образе.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.upload_successful_response import UploadSuccessfulResponse
from timeweb_cloud_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.timeweb.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = timeweb_cloud_api.Configuration(
    host = "https://api.timeweb.cloud"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = timeweb_cloud_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with timeweb_cloud_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = timeweb_cloud_api.ImagesApi(api_client)
    image_id = None # object | 
    content_disposition = None # object |  (optional)

    try:
        # Загрузка образа
        api_response = api_instance.upload_image(image_id, content_disposition=content_disposition)
        print("The response of ImagesApi->upload_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->upload_image: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | [**object**](.md)|  | 
 **content_disposition** | [**object**](.md)|  | [optional] 

### Return type

[**UploadSuccessfulResponse**](UploadSuccessfulResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Информация о загрузке |  -  |
**400** |  |  -  |
**401** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

