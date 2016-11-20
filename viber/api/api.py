import hashlib
import hmac
import json
import logging

from viber.api.consts import VIBER_BOT_API_URL
from viber.api.viber_requests import create_request
from viber.api.api_request_sender import ApiRequestSender
from viber.api.message_sender import MessageSender


class Api(object):
	def __init__(self, bot_configuration):
		self._logger = logging.getLogger('viber.bot.api')
		self._bot_configuration = bot_configuration
		self._request_sender = ApiRequestSender(self._logger, VIBER_BOT_API_URL, bot_configuration)
		self._message_sender = MessageSender(self._logger, self._request_sender, bot_configuration)

	def set_webhook(self, url, webhook_events=None):
		self._logger.debug("setting webhook to url: {0}".format(url))
		return self._request_sender.set_webhook(url, webhook_events)

	def unset_webhook(self):
		self._logger.debug("unsetting webhook")
		return self._request_sender.set_webhook('')

	def get_account_info(self):
		self._logger.debug("requesting account info")
		account_info = self._request_sender.get_account_info()
		self._logger.debug("received account info: {0}".format(account_info))
		return account_info

	def verify_signature(self, request_data, signature):
		return signature == self._calculate_message_signature(request_data)

	def parse_request(self, request_data):
		self._logger.debug("parsing request")
		request_dict = json.loads(request_data.decode('utf-8'))
		request = create_request(request_dict)
		self._logger.debug("parsed request={0}".format(request))
		return request

	def send_messages(self, to, messages):
		"""
		:param to: Viber user id
		:param messages: list of Message objects to be sent
		:return: list of tokens of the sent messages
		"""
		if not isinstance(messages, list):
			messages = [messages]

		sent_messages_tokens = []

		for message in messages:
			token = self._message_sender.send_message(to, self._bot_configuration.get_name(), self._bot_configuration.get_avatar(), message)
			sent_messages_tokens.append(token)

		return sent_messages_tokens

	def _calculate_message_signature(self, message):
		return hmac.new(bytes(self._bot_configuration.get_auth_token().encode('ascii')),
						msg=message,
						digestmod=hashlib.sha256)\
			.hexdigest()

