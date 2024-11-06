# apivideo.VideosApi

All URIs are relative to *https://ws.api.video*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](VideosApi.md#create) | **POST** /videos | Create a video object
[**upload**](VideosApi.md#upload) | **POST** /videos/{videoId}/source | Upload a video
[**upload_with_upload_token**](VideosApi.md#upload_with_upload_token) | **POST** /upload | Upload with an delegated upload token
[**get**](VideosApi.md#get) | **GET** /videos/{videoId} | Retrieve a video object
[**update**](VideosApi.md#update) | **PATCH** /videos/{videoId} | Update a video object
[**delete**](VideosApi.md#delete) | **DELETE** /videos/{videoId} | Delete a video object
[**list**](VideosApi.md#list) | **GET** /videos | List all video objects
[**upload_thumbnail**](VideosApi.md#upload_thumbnail) | **POST** /videos/{videoId}/thumbnail | Upload a thumbnail
[**pick_thumbnail**](VideosApi.md#pick_thumbnail) | **PATCH** /videos/{videoId}/thumbnail | Set a thumbnail
[**get_discarded**](VideosApi.md#get_discarded) | **GET** /discarded/videos/{videoId} | Retrieve a discarded video object
[**get_status**](VideosApi.md#get_status) | **GET** /videos/{videoId}/status | Retrieve video status and details
[**list_discarded**](VideosApi.md#list_discarded) | **GET** /discarded/videos | List all discarded video objects
[**update_discarded**](VideosApi.md#update_discarded) | **PATCH** /discarded/videos/{videoId} | Update a discarded video object


# **create**
> Video create(video_creation_payload)

Create a video object

Creates a video object. More information on video objects can be found [here](https://docs.api.video/reference/api/Videos). 

### Example

```python
import apivideo
from apivideo.api import videos_api
from apivideo.model.too_many_requests import TooManyRequests
from apivideo.model.video_creation_payload import VideoCreationPayload
from apivideo.model.bad_request import BadRequest
from apivideo.model.video import Video
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = videos_api.VideosApi(api_client)
    video_creation_payload = VideoCreationPayload(
        title="Maths video",
        description="A video about string theory.",
        source="https://www.myvideo.url.com/video.mp4 OR vi4k0jvEUuaTdRAEjQ4JfOyl",
        public=True,
        panoramic=False,
        mp4_support=True,
        player_id="pl45KFKdlddgk654dspkze",
        tags=["maths", "string theory", "video"],
        metadata=[
            Metadata(
                key="Color",
                value="Green",
            ),
        ],
        clip=VideoClip(
            start_timecode="00:01:15",
            end_timecode="00:02:33",
        ),
        watermark=VideoWatermark(
            id="watermark_1BWr2L5MTQwxGkuxKjzh6i",
            top="10px",
            left="10px",
            bottom="10px",
            right="10px",
            width="initial",
            height="initial",
            opacity="70%",
        ),
        language="fr",
        transcript=True,
        transcript_summary=True,
        transcript_summary_attributes=[
            "abstract",
        ],
    ) # VideoCreationPayload | video to create

    # example passing only required values which don't have defaults set
    try:
        # Create a video object
        api_response = api_instance.create(video_creation_payload)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling VideosApi->create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_creation_payload** | [**VideoCreationPayload**](VideoCreationPayload.md)| video to create |

### Return type

[**Video**](Video.md)


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |
**202** | Accepted |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |
**400** | Bad Request |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |
**429** | Too Many Requests |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload**
> Video upload(video_id, file)

Upload a video

To upload a video to the videoId you created. You can only upload your video to the videoId once.



We offer 2 types of upload: 

* Regular upload 

* Progressive upload

The latter allows you to split a video source into X chunks and send those chunks independently (concurrently or sequentially). The 2 main goals for our users are to

  * allow the upload of video sources > 200 MiB (200 MiB = the max. allowed file size for regular upload)

  * allow to send a video source "progressively", i.e., before before knowing the total size of the video.

  Once all chunks have been sent, they are reaggregated to one source file. The video source is considered as "completely sent" when the "last" chunk is sent (i.e., the chunk that "completes" the upload).



### Example

```python
import apivideo
from apivideo.api import videos_api
from apivideo.model.too_many_requests import TooManyRequests
from apivideo.model.bad_request import BadRequest
from apivideo.model.not_found import NotFound
from apivideo.model.video import Video
from apivideo.configuration import Configuration
from pprint import pprint

# Enter a context with an instance of the API client
# When uploading a file you can change the chunk size (in octet)
configuration = Configuration(chunk_size=10 * 1024 * 1024)
with apivideo.AuthenticatedApiClient(__API_KEY__, configuration=configuration) as api_client:
    # Create an instance of the API class
    api_instance = videos_api.VideosApi(api_client)
    video_id = "vi4k0jvEUuaTdRAEjQ4Jfrgz" # str | Enter the videoId you want to use to upload your video.
    file = open('/path/to/file', 'rb') # file_type | The path to the video you would like to upload. The path must be local. If you want to use a video from an online source, you must use the \\\"/videos\\\" endpoint and add the \\\"source\\\" parameter when you create a new video.

    # example passing only required values which don't have defaults set
    try:
        # Upload a video
        api_response = api_instance.upload(video_id, file)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling VideosApi->upload: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| Enter the videoId you want to use to upload your video. |
 **file** | **file_type**| The path to the video you would like to upload. The path must be local. If you want to use a video from an online source, you must use the \\\&quot;/videos\\\&quot; endpoint and add the \\\&quot;source\\\&quot; parameter when you create a new video. |

### Return type

[**Video**](Video.md)

### Progressive uploads

Progressive uploads make it possible to upload a video source "progressively," i.e., before knowing the total size of the video. This is done by sending chunks of the video source file sequentially.
The last chunk is sent by calling a different method, so api.video knows that it is time to reassemble the different chunks that were received.


```python
video_id = "vi4k0jvEUuaTdRAEjQ4Jfrgz"; // Enter the videoId you want to use to upload your video.;

part1 = open('10m.mp4.part.a', 'rb')
part2 = open('10m.mp4.part.b', 'rb')
part3 = open('10m.mp4.part.c', 'rb')

session = api_instance.create_upload_progressive_session(video_id)

session.uploadPart(part1)
session.uploadPart(part2)

video = session.uploadLastPart(part3)

part1.close()
part2.close()
part3.close()

```

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |
**400** | Bad Request |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |
**404** | Not Found |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |
**429** | Too Many Requests |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_with_upload_token**
> Video upload_with_upload_token(token, file)

Upload with an delegated upload token

This method allows you to send a video using an upload token. Upload tokens are especially useful when the upload is done from the client side. If you want to upload a video from your server-side application, you'd better use the [standard upload method](#upload).

### Example

```python
import apivideo
from apivideo.api import videos_api
from apivideo.model.too_many_requests import TooManyRequests
from apivideo.model.bad_request import BadRequest
from apivideo.model.video import Video
from apivideo.configuration import Configuration
from pprint import pprint

# Enter a context with an instance of the API client
# When uploading a file you can change the chunk size (in octet)
configuration = Configuration(chunk_size=10 * 1024 * 1024)
with apivideo.AuthenticatedApiClient(__API_KEY__, configuration=configuration) as api_client:
    # Create an instance of the API class
    api_instance = videos_api.VideosApi(api_client)
    token = "to1tcmSFHeYY5KzyhOqVKMKb" # str | The unique identifier for the token you want to use to upload a video.
    file = open('/path/to/file', 'rb') # file_type | The path to the video you want to upload.
    video_id = "video_id_example" # str | The video id returned by the first call to this endpoint in a large video upload scenario. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Upload with an delegated upload token
        api_response = api_instance.upload_with_upload_token(token, file)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling VideosApi->upload_with_upload_token: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Upload with an delegated upload token
        api_response = api_instance.upload_with_upload_token(token, file, video_id=video_id)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling VideosApi->upload_with_upload_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The unique identifier for the token you want to use to upload a video. |
 **file** | **file_type**| The path to the video you want to upload. |
 **video_id** | **str**| The video id returned by the first call to this endpoint in a large video upload scenario. | [optional]

### Return type

[**Video**](Video.md)

### Progressive uploads

Progressive uploads make it possible to upload a video source "progressively," i.e., before knowing the total size of the video. This is done by sending chunks of the video source file sequentially.
The last chunk is sent by calling a different method, so api.video knows that it is time to reassemble the different chunks that were received.


```python
token = "to1tcmSFHeYY5KzyhOqVKMKb"; // The unique identifier for the token you want to use to upload a video.;

part1 = open('10m.mp4.part.a', 'rb')
part2 = open('10m.mp4.part.b', 'rb')
part3 = open('10m.mp4.part.c', 'rb')

session = api_instance.create_upload_with_upload_token_progressive_session(token)

session.uploadPart(part1)
session.uploadPart(part2)

video = session.uploadLastPart(part3)

part1.close()
part2.close()
part3.close()

```

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |
**400** | Bad Request |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |
**429** | Too Many Requests |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> Video get(video_id)

Retrieve a video object

This call provides the same information provided on video creation. For private videos, it will generate a unique token url. Use this to retrieve any details you need about a video, or set up a private viewing URL.

### Example

```python
import apivideo
from apivideo.api import videos_api
from apivideo.model.too_many_requests import TooManyRequests
from apivideo.model.not_found import NotFound
from apivideo.model.video import Video
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = videos_api.VideosApi(api_client)
    video_id = "videoId_example" # str | The unique identifier for the video you want details about.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a video object
        api_response = api_instance.get(video_id)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling VideosApi->get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| The unique identifier for the video you want details about. |

### Return type

[**Video**](Video.md)


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |
**404** | Not Found |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |
**429** | Too Many Requests |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> Video update(video_id, video_update_payload)

Update a video object

Updates the parameters associated with a video ID. The video object you are updating is determined by the video ID you provide. 



NOTE: If you are updating an array, you must provide the entire array as what you provide here overwrites what is in the system rather than appending to it.



### Example

```python
import apivideo
from apivideo.api import videos_api
from apivideo.model.conflict_error import ConflictError
from apivideo.model.too_many_requests import TooManyRequests
from apivideo.model.video_update_payload import VideoUpdatePayload
from apivideo.model.bad_request import BadRequest
from apivideo.model.not_found import NotFound
from apivideo.model.video import Video
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = videos_api.VideosApi(api_client)
    video_id = "vi4k0jvEUuaTdRAEjQ4Jfrgz" # str | The video ID for the video you want to update.
    video_update_payload = VideoUpdatePayload(
        player_id="pl4k0jvEUuaTdRAEjQ4Jfrgz",
        title="title_example",
        description="A film about good books.",
        public=True,
        panoramic=False,
        mp4_support=True,
        tags=["maths", "string theory", "video"],
        metadata=[
            Metadata(
                key="Color",
                value="Green",
            ),
        ],
        language="fr",
        transcript=True,
        transcript_summary=True,
        transcript_summary_attributes=[
            "abstract",
        ],
    ) # VideoUpdatePayload | 

    # example passing only required values which don't have defaults set
    try:
        # Update a video object
        api_response = api_instance.update(video_id, video_update_payload)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling VideosApi->update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| The video ID for the video you want to update. |
 **video_update_payload** | [**VideoUpdatePayload**](VideoUpdatePayload.md)|  |

### Return type

[**Video**](Video.md)


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |
**400** | Bad Request |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |
**404** | Not Found |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |
**409** | Conflict |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |
**429** | Too Many Requests |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(video_id)

Delete a video object

If you do not need a video any longer, you can send a request to delete it. All you need is the videoId. By default, deleted videos cannot be recovered. If you have the Video Restore feature enabled, this operation will discard the video instead of permanently deleting it. Make sure you subscribe to the Video Restore feature if you want to be able to restore deleted videos! The Video Restore feature retains videos for 90 days, after which the videos are permanently deleted

### Example

```python
import apivideo
from apivideo.api import videos_api
from apivideo.model.too_many_requests import TooManyRequests
from apivideo.model.not_found import NotFound
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = videos_api.VideosApi(api_client)
    video_id = "vi4k0jvEUuaTdRAEjQ4Jfrgz" # str | The video ID for the video you want to delete.

    # example passing only required values which don't have defaults set
    try:
        # Delete a video object
        api_instance.delete(video_id)
    except apivideo.ApiException as e:
        print("Exception when calling VideosApi->delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| The video ID for the video you want to delete. |

### Return type

void (empty response body)


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |
**404** | Not Found |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |
**429** | Too Many Requests |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> VideosListResponse list()

List all video objects

This method returns a list of your videos (with all their details). With no parameters added, the API returns the first page of all videos. You can filter videos using the parameters described below.

### Example

```python
import apivideo
from apivideo.api import videos_api
from apivideo.model.too_many_requests import TooManyRequests
from apivideo.model.videos_list_response import VideosListResponse
from apivideo.model.bad_request import BadRequest
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = videos_api.VideosApi(api_client)
    title = "My Video.mp4" # str | The title of a specific video you want to find. The search will match exactly to what term you provide and return any videos that contain the same term as part of their titles. (optional)
    tags = ["captions", "dialogue"] # [str] | A tag is a category you create and apply to videos. You can search for videos with particular tags by listing one or more here. Only videos that have all the tags you list will be returned. (optional)
    metadata = {
        "key": "key_example",
    } # {str: (str,)} | Videos can be tagged with metadata tags in key:value pairs. You can search for videos with specific key value pairs using this parameter. (optional)
    description = "New Zealand" # str | Retrieve video objects by `description`. (optional)
    live_stream_id = "li400mYKSgQ6xs7taUeSaEKr" # str | Retrieve video objects that were recorded from a live stream by `liveStreamId`. (optional)
    sort_by = "publishedAt" # str | Use this parameter to sort videos by the their created time, published time, updated time, or by title. (optional)
    sort_order = "asc" # str | Use this parameter to sort results. `asc` is ascending and sorts from A to Z. `desc` is descending and sorts from Z to A. (optional)
    current_page = 2 # int | Choose the number of search results to return per page. Minimum value: 1 (optional) if omitted the server will use the default value of 1
    page_size = 30 # int | Results per page. Allowed values 1-100, default is 25. (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all video objects
        api_response = api_instance.list(title=title, tags=tags, metadata=metadata, description=description, live_stream_id=live_stream_id, sort_by=sort_by, sort_order=sort_order, current_page=current_page, page_size=page_size)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling VideosApi->list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title** | **str**| The title of a specific video you want to find. The search will match exactly to what term you provide and return any videos that contain the same term as part of their titles. | [optional]
 **tags** | **[str]**| A tag is a category you create and apply to videos. You can search for videos with particular tags by listing one or more here. Only videos that have all the tags you list will be returned. | [optional]
 **metadata** | **{str: (str,)}**| Videos can be tagged with metadata tags in key:value pairs. You can search for videos with specific key value pairs using this parameter. | [optional]
 **description** | **str**| Retrieve video objects by &#x60;description&#x60;. | [optional]
 **live_stream_id** | **str**| Retrieve video objects that were recorded from a live stream by &#x60;liveStreamId&#x60;. | [optional]
 **sort_by** | **str**| Use this parameter to sort videos by the their created time, published time, updated time, or by title. | [optional]
 **sort_order** | **str**| Use this parameter to sort results. &#x60;asc&#x60; is ascending and sorts from A to Z. &#x60;desc&#x60; is descending and sorts from Z to A. | [optional]
 **current_page** | **int**| Choose the number of search results to return per page. Minimum value: 1 | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| Results per page. Allowed values 1-100, default is 25. | [optional] if omitted the server will use the default value of 25

### Return type

[**VideosListResponse**](VideosListResponse.md)


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |
**400** | Bad Request |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |
**429** | Too Many Requests |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_thumbnail**
> Video upload_thumbnail(video_id, file)

Upload a thumbnail

The thumbnail is the poster that appears in the player window before video playback begins.



This endpoint allows you to upload an image for the thumbnail.



To select a still frame from the video using a time stamp, use the [dedicated method](#pickThumbnail) to pick a time in the video.



Note: There may be a short delay before the new thumbnail is delivered to our CDN.

### Example

```python
import apivideo
from apivideo.api import videos_api
from apivideo.model.too_many_requests import TooManyRequests
from apivideo.model.bad_request import BadRequest
from apivideo.model.not_found import NotFound
from apivideo.model.video import Video
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = videos_api.VideosApi(api_client)
    video_id = "videoId_example" # str | Unique identifier of the chosen video 
    file = open('/path/to/file', 'rb') # file_type | The image to be added as a thumbnail. The mime type should be image/jpeg, image/png or image/webp. The max allowed size is 8 MiB.

    # example passing only required values which don't have defaults set
    try:
        # Upload a thumbnail
        api_response = api_instance.upload_thumbnail(video_id, file)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling VideosApi->upload_thumbnail: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| Unique identifier of the chosen video  |
 **file** | **file_type**| The image to be added as a thumbnail. The mime type should be image/jpeg, image/png or image/webp. The max allowed size is 8 MiB. |

### Return type

[**Video**](Video.md)


### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |
**400** | Bad Request |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |
**404** | Not Found |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |
**429** | Too Many Requests |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pick_thumbnail**
> Video pick_thumbnail(video_id, video_thumbnail_pick_payload)

Set a thumbnail

Pick a thumbnail from the given time code. 



If you'd like to upload an image for your thumbnail, use the dedicated [method](#uploadThumbnail). 



There may be a short delay for the thumbnail to update.



### Example

```python
import apivideo
from apivideo.api import videos_api
from apivideo.model.too_many_requests import TooManyRequests
from apivideo.model.video_thumbnail_pick_payload import VideoThumbnailPickPayload
from apivideo.model.not_found import NotFound
from apivideo.model.video import Video
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = videos_api.VideosApi(api_client)
    video_id = "vi4k0jvEUuaTdRAEjQ4Jfrgz" # str | Unique identifier of the video you want to add a thumbnail to, where you use a section of your video as the thumbnail.
    video_thumbnail_pick_payload = VideoThumbnailPickPayload(
        timecode="04:80:72",
    ) # VideoThumbnailPickPayload | 

    # example passing only required values which don't have defaults set
    try:
        # Set a thumbnail
        api_response = api_instance.pick_thumbnail(video_id, video_thumbnail_pick_payload)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling VideosApi->pick_thumbnail: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| Unique identifier of the video you want to add a thumbnail to, where you use a section of your video as the thumbnail. |
 **video_thumbnail_pick_payload** | [**VideoThumbnailPickPayload**](VideoThumbnailPickPayload.md)|  |

### Return type

[**Video**](Video.md)


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |
**404** | Not Found |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |
**429** | Too Many Requests |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_discarded**
> Video get_discarded(video_id)

Retrieve a discarded video object

This call provides the same information provided on video creation. For private videos, it will generate a unique token url. Use this to retrieve any details you need about a video, or set up a private viewing URL.

### Example

```python
import apivideo
from apivideo.api import videos_api
from apivideo.model.too_many_requests import TooManyRequests
from apivideo.model.not_found import NotFound
from apivideo.model.video import Video
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = videos_api.VideosApi(api_client)
    video_id = "videoId_example" # str | The unique identifier for the video you want details about.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a discarded video object
        api_response = api_instance.get_discarded(video_id)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling VideosApi->get_discarded: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| The unique identifier for the video you want details about. |

### Return type

[**Video**](Video.md)


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |
**404** | Not Found |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |
**429** | Too Many Requests |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_status**
> VideoStatus get_status(video_id)

Retrieve video status and details

This method provides upload status & encoding status to determine when the video is uploaded or ready to playback. Once encoding is completed, the response also lists the available stream qualities.

### Example

```python
import apivideo
from apivideo.api import videos_api
from apivideo.model.too_many_requests import TooManyRequests
from apivideo.model.video_status import VideoStatus
from apivideo.model.not_found import NotFound
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = videos_api.VideosApi(api_client)
    video_id = "vi4k0jvEUuaTdRAEjQ4Jfrgz" # str | The unique identifier for the video you want the status for.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve video status and details
        api_response = api_instance.get_status(video_id)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling VideosApi->get_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| The unique identifier for the video you want the status for. |

### Return type

[**VideoStatus**](VideoStatus.md)


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |
**404** | Not Found |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |
**429** | Too Many Requests |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_discarded**
> VideosListResponse list_discarded()

List all discarded video objects

This method returns a list of your discarded videos (with all their details). With no parameters added, the API returns the first page of all discarded videos. You can filter discarded videos using the parameters described below.

### Example

```python
import apivideo
from apivideo.api import videos_api
from apivideo.model.too_many_requests import TooManyRequests
from apivideo.model.videos_list_response import VideosListResponse
from apivideo.model.bad_request import BadRequest
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = videos_api.VideosApi(api_client)
    title = "My Video.mp4" # str | The title of a specific video you want to find. The search will match exactly to what term you provide and return any videos that contain the same term as part of their titles. (optional)
    tags = ["captions", "dialogue"] # [str] | A tag is a category you create and apply to videos. You can search for videos with particular tags by listing one or more here. Only videos that have all the tags you list will be returned. (optional)
    metadata = {
        "key": "key_example",
    } # {str: (str,)} | Videos can be tagged with metadata tags in key:value pairs. You can search for videos with specific key value pairs using this parameter. (optional)
    description = "New Zealand" # str | Retrieve video objects by `description`. (optional)
    live_stream_id = "li400mYKSgQ6xs7taUeSaEKr" # str | Retrieve video objects that were recorded from a live stream by `liveStreamId`. (optional)
    sort_by = "publishedAt" # str | Use this parameter to sort videos by the their created time, published time, updated time, or by title. (optional)
    sort_order = "asc" # str | Use this parameter to sort results. `asc` is ascending and sorts from A to Z. `desc` is descending and sorts from Z to A. (optional)
    current_page = 2 # int | Choose the number of search results to return per page. Minimum value: 1 (optional) if omitted the server will use the default value of 1
    page_size = 30 # int | Results per page. Allowed values 1-100, default is 25. (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all discarded video objects
        api_response = api_instance.list_discarded(title=title, tags=tags, metadata=metadata, description=description, live_stream_id=live_stream_id, sort_by=sort_by, sort_order=sort_order, current_page=current_page, page_size=page_size)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling VideosApi->list_discarded: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title** | **str**| The title of a specific video you want to find. The search will match exactly to what term you provide and return any videos that contain the same term as part of their titles. | [optional]
 **tags** | **[str]**| A tag is a category you create and apply to videos. You can search for videos with particular tags by listing one or more here. Only videos that have all the tags you list will be returned. | [optional]
 **metadata** | **{str: (str,)}**| Videos can be tagged with metadata tags in key:value pairs. You can search for videos with specific key value pairs using this parameter. | [optional]
 **description** | **str**| Retrieve video objects by &#x60;description&#x60;. | [optional]
 **live_stream_id** | **str**| Retrieve video objects that were recorded from a live stream by &#x60;liveStreamId&#x60;. | [optional]
 **sort_by** | **str**| Use this parameter to sort videos by the their created time, published time, updated time, or by title. | [optional]
 **sort_order** | **str**| Use this parameter to sort results. &#x60;asc&#x60; is ascending and sorts from A to Z. &#x60;desc&#x60; is descending and sorts from Z to A. | [optional]
 **current_page** | **int**| Choose the number of search results to return per page. Minimum value: 1 | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| Results per page. Allowed values 1-100, default is 25. | [optional] if omitted the server will use the default value of 25

### Return type

[**VideosListResponse**](VideosListResponse.md)


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |
**400** | Bad Request |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |
**429** | Too Many Requests |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_discarded**
> Video update_discarded(video_id, discarded_video_update_payload)

Update a discarded video object

Use this endpoint to restore a discarded video when you have the Video Restore feature enabled.



### Example

```python
import apivideo
from apivideo.api import videos_api
from apivideo.model.too_many_requests import TooManyRequests
from apivideo.model.bad_request import BadRequest
from apivideo.model.not_found import NotFound
from apivideo.model.discarded_video_update_payload import DiscardedVideoUpdatePayload
from apivideo.model.video import Video
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = videos_api.VideosApi(api_client)
    video_id = "vi4k0jvEUuaTdRAEjQ4Jfrgz" # str | The video ID for the video you want to restore.
    discarded_video_update_payload = DiscardedVideoUpdatePayload(
        discarded=True,
    ) # DiscardedVideoUpdatePayload | 

    # example passing only required values which don't have defaults set
    try:
        # Update a discarded video object
        api_response = api_instance.update_discarded(video_id, discarded_video_update_payload)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling VideosApi->update_discarded: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| The video ID for the video you want to restore. |
 **discarded_video_update_payload** | [**DiscardedVideoUpdatePayload**](DiscardedVideoUpdatePayload.md)|  |

### Return type

[**Video**](Video.md)


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |
**400** | Bad Request |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |
**404** | Not Found |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |
**429** | Too Many Requests |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

