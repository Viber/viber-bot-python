import json
import logging

import pytest

from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.consts import BOT_API_ENDPOINT
from viberbot.api.message_sender import MessageSender
from viberbot.api.messages import TextMessage

LOGGER = logging.getLogger('.')
VIBER_BOT_CONFIGURATION = BotConfiguration("auth-token-sample", "testbot", "http://avatars.com/")

class Stub(object): pass


def stub(*args): pass


def test_send_message_sanity():
	to = "012345A="
	text = "hi!"
	message_token = "a token"
	chat_id = 'my chat id sample'

	def post_request(endpoint, payload):
		data = json.loads(payload)
		assert endpoint == BOT_API_ENDPOINT.SEND_MESSAGE
		assert data['auth_token'] == VIBER_BOT_CONFIGURATION.auth_token
		assert data['receiver'] == to
		assert data['sender']['name'] == VIBER_BOT_CONFIGURATION.name
		assert data['sender']['avatar'] == VIBER_BOT_CONFIGURATION.avatar
		assert data['text'] == text
		assert data['chat_id'] == chat_id
		return dict(status=0, message_token=message_token)

	request_sender = Stub()
	request_sender.post_request = post_request

	text_message = TextMessage(text=text)

	message_sender = MessageSender(LOGGER, request_sender, VIBER_BOT_CONFIGURATION)
	token = message_sender.send_message(
		to, VIBER_BOT_CONFIGURATION.name, VIBER_BOT_CONFIGURATION.avatar, text_message, chat_id)
	assert token == message_token


def test_post_to_public_account_sanity():
	sender = "012345A="
	text = "hi!"
	message_token = "a token"

	def post_request(endpoint, payload):
		data = json.loads(payload)
		assert endpoint == BOT_API_ENDPOINT.POST
		assert data['auth_token'] == VIBER_BOT_CONFIGURATION.auth_token
		assert data['from'] == sender
		assert data['sender']['name'] == VIBER_BOT_CONFIGURATION.name
		assert data['sender']['avatar'] == VIBER_BOT_CONFIGURATION.avatar
		assert data['text'] == text
		return dict(status=0, message_token=message_token)

	request_sender = Stub()
	request_sender.post_request = post_request

	text_message = TextMessage(text=text)

	message_sender = MessageSender(LOGGER, request_sender, VIBER_BOT_CONFIGURATION)
	token = message_sender.post_to_public_account(
		sender, VIBER_BOT_CONFIGURATION.name, VIBER_BOT_CONFIGURATION.avatar, text_message)
	assert token == message_token


def test_message_invalid():
	to = "012345A="

	def post_request(endpoint, payload):
		pytest.fail("message sender not supposed to call post_request")

	request_sender = Stub()
	request_sender.post_request = post_request

	text_message = TextMessage(text=None)

	message_sender = MessageSender(LOGGER, request_sender, VIBER_BOT_CONFIGURATION)
	with pytest.raises(Exception) as exc:
		message_sender.send_message(to, VIBER_BOT_CONFIGURATION.name, VIBER_BOT_CONFIGURATION.avatar, text_message)

		assert exc.value.message.startswith("failed validating message:")


def test_send_result_failed():
	to = "012345A="
	text = "hi!"

	def post_request(endpoint, payload):
		data = json.loads(payload)
		return dict(status=1, status_message="failed")

	request_sender = Stub()
	request_sender.post_request = post_request

	text_message = TextMessage(text=text)

	message_sender = MessageSender(LOGGER, request_sender, VIBER_BOT_CONFIGURATION)
	with pytest.raises(Exception) as exc:
		message_sender.send_message(to, VIBER_BOT_CONFIGURATION.name, VIBER_BOT_CONFIGURATION.avatar, text_message)

		assert exc.value.message.startswith("failed with status: 1, message: failed")


def test_post_message_to_public_account_failed():
	sender = "012345A="
	text = "hi!"

	def post_request(endpoint, payload):
		data = json.loads(payload)
		return dict(status=1, status_message="failed")

	request_sender = Stub()
	request_sender.post_request = post_request

	text_message = TextMessage(text=text)

	message_sender = MessageSender(LOGGER, request_sender, VIBER_BOT_CONFIGURATION)
	with pytest.raises(Exception) as exc:
		message_sender.post_to_public_account(
			sender, VIBER_BOT_CONFIGURATION.name, VIBER_BOT_CONFIGURATION.avatar, text_message)

		assert exc.value.message.startswith("failed with status: 1, message: failed")