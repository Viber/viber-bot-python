import os

import pytest

from viberbot import Api
from viberbot import BotConfiguration
from viberbot.api.viber_requests import ViberMessageRequest

VIBER_BOT_CONFIGURATION = BotConfiguration("44dafb7e0f40021e-61a47a1e6778d187-f2c5a676a07050b3", "testbot", "http://avatars.com/")


def test_verify_signature():
	valid_signature = 'd21b343448c8aee33b8e93768ef6ceb64a6ba6163099973a2b8bd028fea510ef'
	message = "{\"event\":\"webhook\",\"timestamp\":4977069964384421269,\"message_token\":1478683725125}".encode("utf-8")

	viber = Api(VIBER_BOT_CONFIGURATION)
	assert viber.verify_signature(message, valid_signature)


def test_verify_signature_failure():
	invalid_signature = 'aaaaaaaaaaaaaaaaaaaaaa'
	message = "{\"event\":\"webhook\"}".encode("utf-8")

	viber = Api(VIBER_BOT_CONFIGURATION)
	assert not viber.verify_signature(message, invalid_signature)


def test_parse_request_not_json():
	viber = Api(VIBER_BOT_CONFIGURATION)

	with pytest.raises(ValueError) as exc:
		viber.parse_request("dsfdfdsf\#")


def test_parse_request_unicode():
	viber = Api(VIBER_BOT_CONFIGURATION)

	with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'test_data', 'unicode_request')) as f:
		req = f.read()
		viber_request = viber.parse_request(req)
		assert isinstance(viber_request, ViberMessageRequest)
