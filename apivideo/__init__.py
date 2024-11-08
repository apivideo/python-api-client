# flake8: noqa

"""
    api.video

    api.video is an API that encodes on the go to facilitate immediate playback, enhancing viewer streaming experiences across multiple devices and platforms. You can stream live or on-demand online videos within minutes.  # noqa: E501

    Contact: ecosystem@api.video
"""


__version__ = "1.4.7"

# import ApiVideoClient
from apivideo.auth_api_client import AuthenticatedApiClient

# import exceptions
from apivideo.exceptions import OpenApiException
from apivideo.exceptions import ApiAttributeError
from apivideo.exceptions import ApiTypeError
from apivideo.exceptions import ApiValueError
from apivideo.exceptions import ApiKeyError
from apivideo.exceptions import ApiException
