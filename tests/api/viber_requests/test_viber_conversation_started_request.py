from datetime import datetime

from viberbot.api.event_type import EventType
from viberbot.api.viber_requests import ViberConversationStartedRequest
from viberbot.api.viber_requests import create_request

SAMPLE_REQUEST = dict(
	event=EventType.CONVERSATION_STARTED,
	timestamp=datetime.now(),
	message_token="912661846655238145",
	type="open",
	context="context info",
	subscribed=True,
	user=dict(
		id="01234567890A=",
		name="viberUser",
		avatar="http://avatar_url",
		country="IL",
		language="en"
	))


def test_create_request():
	request = create_request(SAMPLE_REQUEST)

	assert isinstance(request, ViberConversationStartedRequest)
	assert request.event_type == SAMPLE_REQUEST['event']
	assert request.timestamp == SAMPLE_REQUEST['timestamp']
	assert request.message_token == SAMPLE_REQUEST['message_token']
	assert request.type == SAMPLE_REQUEST['type']
	assert request.context == SAMPLE_REQUEST['context']
	assert request.user.id == SAMPLE_REQUEST['user']['id']
	assert request.user.name == SAMPLE_REQUEST['user']['name']
	assert request.user.avatar == SAMPLE_REQUEST['user']['avatar']
	assert request.user.country == SAMPLE_REQUEST['user']['country']
	assert request.user.language == SAMPLE_REQUEST['user']['language']
	assert request.subscribed == SAMPLE_REQUEST['subscribed']


def test_missing_user_optional_params():
	request_dict = dict(
		event=EventType.CONVERSATION_STARTED,
		timestamp=datetime.now(),
		message_token="912661846655238145",
		type="open",
		context="context info",
		user=dict(
			id="01234567890A=",
			name="viberUser"
		))

	request = create_request(request_dict)  # should not fail

	assert isinstance(request, ViberConversationStartedRequest)
	assert request.event_type == request_dict['event']
	assert request.timestamp == request_dict['timestamp']
	assert request.message_token == request_dict['message_token']
	assert request.type == request_dict['type']
	assert request.context == request_dict['context']
	assert request.user.id == request_dict['user']['id']
	assert request.user.name == request_dict['user']['name']
	assert request.user.avatar is None
	assert request.user.country is None
	assert request.user.language is None
	assert request.subscribed is None
