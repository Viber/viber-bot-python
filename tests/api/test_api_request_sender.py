import json
import logging

import pytest

from viberbot.api.api_request_sender import ApiRequestSender
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.consts import BOT_API_ENDPOINT, VIBER_BOT_USER_AGENT
from viberbot.api.event_type import EventType


class Stub(object): pass


def stub(*args): pass


VIBER_BOT_API_URL = "http://site.com"
VIBER_BOT_CONFIGURATION = BotConfiguration("auth-token-sample", "testbot", "http://avatars.com/")


def test_set_webhook_sanity():
	webhook_events = [EventType.DELIVERED, EventType.UNSUBSCRIBED, EventType.SEEN]
	url = "http://sample.url.com"

	def post_request(endpoint, payload):
		request = json.loads(payload)
		assert endpoint == BOT_API_ENDPOINT.SET_WEBHOOK
		assert request['auth_token'] == VIBER_BOT_CONFIGURATION.auth_token
		assert request['event_types'] == webhook_events
		assert request['url'] == url
		return dict(status=0, event_types=webhook_events)

	request_sender = ApiRequestSender(logging.getLogger(), VIBER_BOT_API_URL, VIBER_BOT_CONFIGURATION, VIBER_BOT_USER_AGENT)
	request_sender.post_request = post_request

	request_sender.set_webhook(url=url, webhook_events=webhook_events)


def test_set_webhook_failure():
	webhook_events = [EventType.DELIVERED, EventType.UNSUBSCRIBED, EventType.SEEN]
	url = "http://sample.url.com"

	def post_request(endpoint, payload):
		return dict(status=1, status_message="failed")

	request_sender = ApiRequestSender(logging.getLogger(), VIBER_BOT_API_URL, VIBER_BOT_CONFIGURATION, VIBER_BOT_USER_AGENT)
	request_sender.post_request = post_request
	with pytest.raises(Exception) as exc:
		request_sender.set_webhook(url=url, webhook_events=webhook_events)

		assert exc.value.message.startswith("failed with status: 1, message: failed")


def test_post_request_success(monkeypatch):
	def callback(endpoint, data, headers):
		request = json.loads(data)
		assert endpoint == VIBER_BOT_API_URL + "/" + BOT_API_ENDPOINT.GET_ACCOUNT_INFO
		assert request['auth_token'] == VIBER_BOT_CONFIGURATION.auth_token
		assert headers['User-Agent'] == VIBER_BOT_USER_AGENT
		response = Stub()
		response.raise_for_status = stub
		response.text = "{}"

		return response

	monkeypatch.setattr("requests.post", callback)

	request_sender = ApiRequestSender(logging.getLogger(), VIBER_BOT_API_URL, VIBER_BOT_CONFIGURATION, VIBER_BOT_USER_AGENT)
	request_sender.get_account_info()


def test_post_request_json_exception(monkeypatch):
	def callback(endpoint, data, headers):
		request = json.loads(data)
		assert endpoint == VIBER_BOT_API_URL + "/" + BOT_API_ENDPOINT.GET_ACCOUNT_INFO
		assert request['auth_token'] == VIBER_BOT_CONFIGURATION.auth_token
		assert headers['User-Agent'] == VIBER_BOT_USER_AGENT
		response = Stub()
		response.raise_for_status = stub
		response.text = "not a json{/"

		return response

	monkeypatch.setattr("requests.post", callback)
	request_sender = ApiRequestSender(logging.getLogger(), VIBER_BOT_API_URL, VIBER_BOT_CONFIGURATION, VIBER_BOT_USER_AGENT)

	with pytest.raises(Exception) as exc:
		request_sender.get_account_info()


def test_get_online_status_fail(monkeypatch):
	def callback(endpoint, data, headers):
		request = json.loads(data)
		assert endpoint == VIBER_BOT_API_URL + "/" + BOT_API_ENDPOINT.GET_ONLINE
		assert request['auth_token'] == VIBER_BOT_CONFIGURATION.auth_token
		assert headers['User-Agent'] == VIBER_BOT_USER_AGENT
		response = Stub()
		response.raise_for_status = stub
		response.text = "{\"status\": 1, \"status_message\": \"fail\"}"

		return response

	monkeypatch.setattr("requests.post", callback)
	request_sender = ApiRequestSender(logging.getLogger(), VIBER_BOT_API_URL, VIBER_BOT_CONFIGURATION, VIBER_BOT_USER_AGENT)

	with pytest.raises(Exception) as exc:
		request_sender.get_online_status(ids=["0123456789="])

		assert exc.value.message.startswith("failed with status:")


def test_get_online_missing_ids(monkeypatch):
	monkeypatch.setattr("requests.post", stub)
	request_sender = ApiRequestSender(logging.getLogger(), VIBER_BOT_API_URL, VIBER_BOT_CONFIGURATION, VIBER_BOT_USER_AGENT)

	with pytest.raises(Exception) as exc:
		request_sender.get_online_status(ids=None)

		assert exc.value.message.startswith("missing parameter ids, should be a list of viber memberIds")


def test_get_online_success(monkeypatch):
	def callback(endpoint, data, headers):
		request = json.loads(data)
		assert endpoint == VIBER_BOT_API_URL + "/" + BOT_API_ENDPOINT.GET_ONLINE
		assert request['auth_token'] == VIBER_BOT_CONFIGURATION.auth_token
		response = Stub()
		response.raise_for_status = stub
		response.text = "{\"status\": 0, \"status_message\": \"OK\", \"users\": []}"

		return response

	monkeypatch.setattr("requests.post", callback)
	request_sender = ApiRequestSender(logging.getLogger(), VIBER_BOT_API_URL, VIBER_BOT_CONFIGURATION, VIBER_BOT_USER_AGENT)

	request_sender.get_online_status(ids=["03249305A="])


def test_get_user_details_success(monkeypatch):
	def callback(endpoint, data, headers):
		request = json.loads(data)
		assert endpoint == VIBER_BOT_API_URL + "/" + BOT_API_ENDPOINT.GET_USER_DETAILS
		assert request['auth_token'] == VIBER_BOT_CONFIGURATION.auth_token
		response = Stub()
		response.raise_for_status = stub
		response.text = "{\"status\": 0, \"status_message\": \"OK\", \"user\": {}}"

		return response

	monkeypatch.setattr("requests.post", callback)
	request_sender = ApiRequestSender(logging.getLogger(), VIBER_BOT_API_URL, VIBER_BOT_CONFIGURATION, VIBER_BOT_USER_AGENT)

	request_sender.get_user_details(user_id="03249305A=")
