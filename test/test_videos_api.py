"""
    api.video

    api.video is an API that encodes on the go to facilitate immediate playback, enhancing viewer streaming experiences across multiple devices and platforms. You can stream live or on-demand online videos within minutes.  # noqa: E501

    Contact: ecosystem@api.video
"""

from dateutil.parser import parse as dateutil_parser
from urllib3_mock import Responses

from apivideo.api.videos_api import VideosApi  # noqa: E501
from apivideo.exceptions import ApiException, NotFoundException
from apivideo.model.metadata import Metadata
from apivideo.model.video_clip import VideoClip
from apivideo.model.video_watermark import VideoWatermark
from apivideo.model.restreams_request_object import RestreamsRequestObject

from apivideo.model.bad_request import BadRequest
from apivideo.model.conflict_error import ConflictError
from apivideo.model.discarded_video_update_payload import DiscardedVideoUpdatePayload
from apivideo.model.not_found import NotFound
from apivideo.model.too_many_requests import TooManyRequests
from apivideo.model.video import Video
from apivideo.model.video_creation_payload import VideoCreationPayload
from apivideo.model.video_status import VideoStatus
from apivideo.model.video_thumbnail_pick_payload import VideoThumbnailPickPayload
from apivideo.model.video_update_payload import VideoUpdatePayload
from apivideo.model.videos_list_response import VideosListResponse

from helper import MainTest


responses = Responses()


class TestVideosApi(MainTest):
    """VideosApi unit test"""

    def setUp(self):
        super().setUp()
        self.api = VideosApi(self.client)  # noqa: E501

    @responses.activate
    def test_create(self):
        """Test case for create

        Create a video object  # noqa: E501
        """
        for file_name, json in self.load_json('videos', 'create'):
            status = file_name.split("-")[0]
            responses.reset()

            kwargs = {
                'video_creation_payload': VideoCreationPayload(
        title="Maths video",
        subtitle="A great subtitle.",
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
    ),
            }
            url = '/videos'.format(**kwargs)

            responses.add('POST', url, body=json, status=int(status), content_type='application/json')

            if status[0] == '4':
                with self.assertRaises(ApiException) as context:
                    self.api.create(**kwargs)
                if status == '404':
                    self.assertIsInstance(context.exception, NotFoundException)
            else:
                self.api.create(**kwargs)

    @responses.activate
    def test_upload(self):
        """Test case for upload

        Upload a video  # noqa: E501
        """
        for file_name, json in self.load_json('videos', 'upload'):
            status = file_name.split("-")[0]
            responses.reset()

            kwargs = {
                'video_id': "vi4k0jvEUuaTdRAEjQ4Jfrgz",
                'file': open('test_file', 'rb'),
            }
            url = '/videos/{video_id}/source'.format(**kwargs)

            responses.add('POST', url, body=json, status=int(status), content_type='application/json')

            if status[0] == '4':
                with self.assertRaises(ApiException) as context:
                    self.api.upload(**kwargs)
                if status == '404':
                    self.assertIsInstance(context.exception, NotFoundException)
            else:
                self.api.upload(**kwargs)

    @responses.activate
    def test_upload_with_upload_token(self):
        """Test case for upload_with_upload_token

        Upload with an delegated upload token  # noqa: E501
        """
        for file_name, json in self.load_json('videos', 'upload_with_upload_token'):
            status = file_name.split("-")[0]
            responses.reset()

            kwargs = {
                'token': "to1tcmSFHeYY5KzyhOqVKMKb",
                'file': open('test_file', 'rb'),
            }
            url = '/upload'.format(**kwargs)

            responses.add('POST', url, body=json, status=int(status), content_type='application/json')

            if status[0] == '4':
                with self.assertRaises(ApiException) as context:
                    self.api.upload_with_upload_token(**kwargs)
                if status == '404':
                    self.assertIsInstance(context.exception, NotFoundException)
            else:
                self.api.upload_with_upload_token(**kwargs)

    @responses.activate
    def test_get(self):
        """Test case for get

        Retrieve a video object  # noqa: E501
        """
        for file_name, json in self.load_json('videos', 'get'):
            status = file_name.split("-")[0]
            responses.reset()

            kwargs = {
                'video_id': "videoId_example",
            }
            url = '/videos/{video_id}'.format(**kwargs)

            responses.add('GET', url, body=json, status=int(status), content_type='application/json')

            if status[0] == '4':
                with self.assertRaises(ApiException) as context:
                    self.api.get(**kwargs)
                if status == '404':
                    self.assertIsInstance(context.exception, NotFoundException)
            else:
                self.api.get(**kwargs)

    @responses.activate
    def test_update(self):
        """Test case for update

        Update a video object  # noqa: E501
        """
        for file_name, json in self.load_json('videos', 'update'):
            status = file_name.split("-")[0]
            responses.reset()

            kwargs = {
                'video_id': "vi4k0jvEUuaTdRAEjQ4Jfrgz",
                'video_update_payload': VideoUpdatePayload(
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
    ),
            }
            url = '/videos/{video_id}'.format(**kwargs)

            responses.add('PATCH', url, body=json, status=int(status), content_type='application/json')

            if status[0] == '4':
                with self.assertRaises(ApiException) as context:
                    self.api.update(**kwargs)
                if status == '404':
                    self.assertIsInstance(context.exception, NotFoundException)
            else:
                self.api.update(**kwargs)

    @responses.activate
    def test_delete(self):
        """Test case for delete

        Delete a video object  # noqa: E501
        """
        pass

    @responses.activate
    def test_list(self):
        """Test case for list

        List all video objects  # noqa: E501
        """
        for file_name, json in self.load_json('videos', 'list'):
            status = file_name.split("-")[0]
            responses.reset()

            kwargs = {
            }
            url = '/videos'.format(**kwargs)

            responses.add('GET', url, body=json, status=int(status), content_type='application/json')

            if status[0] == '4':
                with self.assertRaises(ApiException) as context:
                    self.api.list(**kwargs)
                if status == '404':
                    self.assertIsInstance(context.exception, NotFoundException)
            else:
                self.api.list(**kwargs)

    @responses.activate
    def test_upload_thumbnail(self):
        """Test case for upload_thumbnail

        Upload a thumbnail  # noqa: E501
        """
        for file_name, json in self.load_json('videos', 'upload_thumbnail'):
            status = file_name.split("-")[0]
            responses.reset()

            kwargs = {
                'video_id': "videoId_example",
                'file': open('test_file', 'rb'),
            }
            url = '/videos/{video_id}/thumbnail'.format(**kwargs)

            responses.add('POST', url, body=json, status=int(status), content_type='application/json')

            if status[0] == '4':
                with self.assertRaises(ApiException) as context:
                    self.api.upload_thumbnail(**kwargs)
                if status == '404':
                    self.assertIsInstance(context.exception, NotFoundException)
            else:
                self.api.upload_thumbnail(**kwargs)

    @responses.activate
    def test_pick_thumbnail(self):
        """Test case for pick_thumbnail

        Set a thumbnail  # noqa: E501
        """
        for file_name, json in self.load_json('videos', 'pick_thumbnail'):
            status = file_name.split("-")[0]
            responses.reset()

            kwargs = {
                'video_id': "vi4k0jvEUuaTdRAEjQ4Jfrgz",
                'video_thumbnail_pick_payload': VideoThumbnailPickPayload(
        timecode="04:80:72",
    ),
            }
            url = '/videos/{video_id}/thumbnail'.format(**kwargs)

            responses.add('PATCH', url, body=json, status=int(status), content_type='application/json')

            if status[0] == '4':
                with self.assertRaises(ApiException) as context:
                    self.api.pick_thumbnail(**kwargs)
                if status == '404':
                    self.assertIsInstance(context.exception, NotFoundException)
            else:
                self.api.pick_thumbnail(**kwargs)

    @responses.activate
    def test_get_discarded(self):
        """Test case for get_discarded

        Retrieve a discarded video object  # noqa: E501
        """
        for file_name, json in self.load_json('videos', 'get_discarded'):
            status = file_name.split("-")[0]
            responses.reset()

            kwargs = {
                'video_id': "videoId_example",
            }
            url = '/discarded/videos/{video_id}'.format(**kwargs)

            responses.add('GET', url, body=json, status=int(status), content_type='application/json')

            if status[0] == '4':
                with self.assertRaises(ApiException) as context:
                    self.api.get_discarded(**kwargs)
                if status == '404':
                    self.assertIsInstance(context.exception, NotFoundException)
            else:
                self.api.get_discarded(**kwargs)

    @responses.activate
    def test_get_status(self):
        """Test case for get_status

        Retrieve video status and details  # noqa: E501
        """
        for file_name, json in self.load_json('videos', 'get_status'):
            status = file_name.split("-")[0]
            responses.reset()

            kwargs = {
                'video_id': "vi4k0jvEUuaTdRAEjQ4Jfrgz",
            }
            url = '/videos/{video_id}/status'.format(**kwargs)

            responses.add('GET', url, body=json, status=int(status), content_type='application/json')

            if status[0] == '4':
                with self.assertRaises(ApiException) as context:
                    self.api.get_status(**kwargs)
                if status == '404':
                    self.assertIsInstance(context.exception, NotFoundException)
            else:
                self.api.get_status(**kwargs)

    @responses.activate
    def test_list_discarded(self):
        """Test case for list_discarded

        List all discarded video objects  # noqa: E501
        """
        for file_name, json in self.load_json('videos', 'list_discarded'):
            status = file_name.split("-")[0]
            responses.reset()

            kwargs = {
            }
            url = '/discarded/videos'.format(**kwargs)

            responses.add('GET', url, body=json, status=int(status), content_type='application/json')

            if status[0] == '4':
                with self.assertRaises(ApiException) as context:
                    self.api.list_discarded(**kwargs)
                if status == '404':
                    self.assertIsInstance(context.exception, NotFoundException)
            else:
                self.api.list_discarded(**kwargs)

    @responses.activate
    def test_update_discarded(self):
        """Test case for update_discarded

        Update a discarded video object  # noqa: E501
        """
        for file_name, json in self.load_json('videos', 'update_discarded'):
            status = file_name.split("-")[0]
            responses.reset()

            kwargs = {
                'video_id': "vi4k0jvEUuaTdRAEjQ4Jfrgz",
                'discarded_video_update_payload': DiscardedVideoUpdatePayload(
        discarded=True,
    ),
            }
            url = '/discarded/videos/{video_id}'.format(**kwargs)

            responses.add('PATCH', url, body=json, status=int(status), content_type='application/json')

            if status[0] == '4':
                with self.assertRaises(ApiException) as context:
                    self.api.update_discarded(**kwargs)
                if status == '404':
                    self.assertIsInstance(context.exception, NotFoundException)
            else:
                self.api.update_discarded(**kwargs)

