from datetime import datetime

from viberbot.api.event_type import EventType
from viberbot.api.viber_requests import ViberSubscribedRequest
from viberbot.api.viber_requests import create_request

SAMPLE_REQUEST = dict(
	event=EventType.SUBSCRIBED,
	timestamp=datetime.now(),
	user=dict(
		id="01234567890A=",
		name="viberUser",
		avatar="http://avatar_url",
		country="IL",
		language="en"
	))


def test_create_request():
	request = create_request(SAMPLE_REQUEST)

	assert isinstance(request, ViberSubscribedRequest)
	assert request.event_type == SAMPLE_REQUEST['event']
	assert request.timestamp == SAMPLE_REQUEST['timestamp']
	assert request.user.id == SAMPLE_REQUEST['user']['id']
	assert request.user.name == SAMPLE_REQUEST['user']['name']
	assert request.user.avatar == SAMPLE_REQUEST['user']['avatar']
	assert request.user.country == SAMPLE_REQUEST['user']['country']
	assert request.user.language == SAMPLE_REQUEST['user']['language']
