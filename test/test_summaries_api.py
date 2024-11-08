"""
    api.video

    api.video is an API that encodes on the go to facilitate immediate playback, enhancing viewer streaming experiences across multiple devices and platforms. You can stream live or on-demand online videos within minutes.  # noqa: E501

    Contact: ecosystem@api.video
"""

from dateutil.parser import parse as dateutil_parser
from urllib3_mock import Responses

from apivideo.api.summaries_api import SummariesApi  # noqa: E501
from apivideo.exceptions import ApiException, NotFoundException
from apivideo.model.metadata import Metadata
from apivideo.model.video_clip import VideoClip
from apivideo.model.video_watermark import VideoWatermark
from apivideo.model.restreams_request_object import RestreamsRequestObject

from apivideo.model.conflict_error import ConflictError
from apivideo.model.not_found import NotFound
from apivideo.model.summaries_list_response import SummariesListResponse
from apivideo.model.summary import Summary
from apivideo.model.summary_creation_payload import SummaryCreationPayload
from apivideo.model.summary_source import SummarySource
from apivideo.model.summary_update_payload import SummaryUpdatePayload

from helper import MainTest


responses = Responses()


class TestSummariesApi(MainTest):
    """SummariesApi unit test"""

    def setUp(self):
        super().setUp()
        self.api = SummariesApi(self.client)  # noqa: E501

    @responses.activate
    def test_create(self):
        """Test case for create

        Generate video summary  # noqa: E501
        """
        for file_name, json in self.load_json('summaries', 'create'):
            status = file_name.split("-")[0]
            responses.reset()

            kwargs = {
                'summary_creation_payload': SummaryCreationPayload(
        video_id="vi4k0jvEUuaTdRAEjQ4Jfrgz",
        origin="auto",
        attributes=[
            "abstract",
        ],
    ),
            }
            url = '/summaries'.format(**kwargs)

            responses.add('POST', url, body=json, status=int(status), content_type='application/json')

            if status[0] == '4':
                with self.assertRaises(ApiException) as context:
                    self.api.create(**kwargs)
                if status == '404':
                    self.assertIsInstance(context.exception, NotFoundException)
            else:
                self.api.create(**kwargs)

    @responses.activate
    def test_update(self):
        """Test case for update

        Update summary details  # noqa: E501
        """
        pass

    @responses.activate
    def test_delete(self):
        """Test case for delete

        Delete video summary  # noqa: E501
        """
        pass

    @responses.activate
    def test_list(self):
        """Test case for list

        List summaries  # noqa: E501
        """
        for file_name, json in self.load_json('summaries', 'list'):
            status = file_name.split("-")[0]
            responses.reset()

            kwargs = {
            }
            url = '/summaries'.format(**kwargs)

            responses.add('GET', url, body=json, status=int(status), content_type='application/json')

            if status[0] == '4':
                with self.assertRaises(ApiException) as context:
                    self.api.list(**kwargs)
                if status == '404':
                    self.assertIsInstance(context.exception, NotFoundException)
            else:
                self.api.list(**kwargs)

    @responses.activate
    def test_get_summary_source(self):
        """Test case for get_summary_source

        Get summary details  # noqa: E501
        """
        pass

