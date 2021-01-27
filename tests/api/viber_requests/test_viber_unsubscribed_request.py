from datetime import datetime

from viberbot.api.event_type import EventType
from viberbot.api.viber_requests import ViberUnsubscribedRequest
from viberbot.api.viber_requests import create_request

SAMPLE_REQUEST = dict(
	event=EventType.UNSUBSCRIBED,
	timestamp=datetime.now(),
	user_id="01234567890A="
)


def test_create_request():
	request = create_request(SAMPLE_REQUEST)

	assert isinstance(request, ViberUnsubscribedRequest)
	assert request.event_type == SAMPLE_REQUEST['event']
	assert request.timestamp == SAMPLE_REQUEST['timestamp']
	assert request.user_id == SAMPLE_REQUEST['user_id']
