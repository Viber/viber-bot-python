from datetime import datetime

from viberbot.api.event_type import EventType
from viberbot.api.viber_requests import ViberFailedRequest
from viberbot.api.viber_requests import create_request

SAMPLE_REQUEST = dict(
	event=EventType.FAILED,
	timestamp=datetime.now(),
	message_token="912661846655238145",
	user_id="01234567890A=",
	desc="failure desc"
)


def test_create_request():
	request = create_request(SAMPLE_REQUEST)

	assert isinstance(request, ViberFailedRequest)
	assert request.event_type == SAMPLE_REQUEST['event']
	assert request.timestamp == SAMPLE_REQUEST['timestamp']
	assert request.meesage_token == SAMPLE_REQUEST['message_token']
	assert request.user_id == SAMPLE_REQUEST['user_id']
	assert request.desc == SAMPLE_REQUEST['desc']
