from datetime import datetime

from viberbot.api.event_type import EventType
from viberbot.api.messages import MessageType
from viberbot.api.messages import TextMessage
from viberbot.api.viber_requests import ViberMessageRequest
from viberbot.api.viber_requests import create_request

SAMPLE_REQUEST = dict(
	event=EventType.MESSAGE,
	timestamp=datetime.now(),
	message_token="912661846655238145",
	sender=dict(
		id="01234567890A=",
		name="viberUser",
		avatar="http://avatar_url"
	),
	message=dict(
		type=MessageType.TEXT,
		text="HI!"
	),
	silent=True)


def test_create_request():
	request = create_request(SAMPLE_REQUEST)

	assert isinstance(request, ViberMessageRequest)
	assert request.event_type == SAMPLE_REQUEST['event']
	assert request.timestamp == SAMPLE_REQUEST['timestamp']
	assert request.message_token == SAMPLE_REQUEST['message_token']
	assert request.silent == SAMPLE_REQUEST['silent']
	assert request.sender.id == SAMPLE_REQUEST['sender']['id']
	assert request.sender.name == SAMPLE_REQUEST['sender']['name']
	assert request.sender.avatar == SAMPLE_REQUEST['sender']['avatar']
	assert isinstance(request.message, TextMessage)


def test_user_has_no_avatar():
	SAMPLE_REQUEST = dict(
		event=EventType.MESSAGE,
		timestamp=datetime.now(),
		message_token="912661846655238145",
		sender=dict(
			id="01234567890A=",
			name="viberUser"
		),
		message=dict(
			type=MessageType.TEXT,
			text="HI!"
		),
		silent=False)
	request = create_request(SAMPLE_REQUEST)

	assert isinstance(request, ViberMessageRequest)
	assert request.event_type == SAMPLE_REQUEST['event']
	assert request.timestamp == SAMPLE_REQUEST['timestamp']
	assert request.message_token == SAMPLE_REQUEST['message_token']
	assert request.sender.id == SAMPLE_REQUEST['sender']['id']
	assert request.sender.name == SAMPLE_REQUEST['sender']['name']
	assert isinstance(request.message, TextMessage)


def test_request_is_chat_extension():
	SAMPLE_REQUEST = dict(
		event=EventType.MESSAGE,
		timestamp=datetime.now(),
		message_token="912661846655238145",
		chat_id=5048086924903818307,
		reply_type='message',
		sender=dict(
			id="01234567890A=",
			name="viberUser"
		),
		message=dict(
			type=MessageType.TEXT,
			text="HI!"
		),
		silent=False)
	request = create_request(SAMPLE_REQUEST)

	assert isinstance(request, ViberMessageRequest)
	assert request.event_type == SAMPLE_REQUEST['event']
	assert request.timestamp == SAMPLE_REQUEST['timestamp']
	assert request.message_token == SAMPLE_REQUEST['message_token']
	assert request.sender.id == SAMPLE_REQUEST['sender']['id']
	assert request.sender.name == SAMPLE_REQUEST['sender']['name']
	assert request.chat_id == SAMPLE_REQUEST['chat_id']
	assert request.reply_type == SAMPLE_REQUEST['reply_type']
	assert isinstance(request.message, TextMessage)