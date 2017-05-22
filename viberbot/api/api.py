import hashlib
import hmac
import json
import logging

from viberbot.api.consts import VIBER_BOT_API_URL, VIBER_BOT_USER_AGENT
from viberbot.api.viber_requests import create_request
from viberbot.api.api_request_sender import ApiRequestSender
from viberbot.api.message_sender import MessageSender


class Api(object):
    def __init__(self, bot_configuration):
        self._logger = logging.getLogger('viber.bot.api')
        self._bot_configuration = bot_configuration
        self._request_sender = ApiRequestSender(self._logger, VIBER_BOT_API_URL, bot_configuration,
                                                VIBER_BOT_USER_AGENT)
        self._message_sender = MessageSender(self._logger, self._request_sender, bot_configuration)

    @property
    def name(self):
        return self._bot_configuration.name

    @property
    def avatar(self):
        return self._bot_configuration.avatar

    def set_webhook(self, url, webhook_events=None):
        self._logger.debug(u"setting webhook to url: {0}".format(url))
        return self._request_sender.set_webhook(url, webhook_events)

    def unset_webhook(self):
        self._logger.debug("unsetting webhook")
        return self._request_sender.set_webhook('')

    def get_online(self, ids):
        return self._request_sender.get_online_status(ids)

    def get_user_details(self, user_id):
        return self._request_sender.get_user_details(user_id)

    def get_account_info(self):
        self._logger.debug("requesting account info")
        account_info = self._request_sender.get_account_info()
        self._logger.debug(u"received account info: {0}".format(account_info))
        return account_info

    def verify_signature(self, request_data, signature):
        return signature == self._calculate_message_signature(request_data)

    def parse_request(self, request_data):
        self._logger.debug("parsing request")
        request_dict = json.loads(request_data)
        request = create_request(request_dict)
        self._logger.debug(u"parsed request={0}".format(request))
        return request

    def send(self, method, messages, *args):
        if not isinstance(messages, list):
            messages = [messages]

        sent_messages_tokens = []

        for message in messages:
            token = method(self._bot_configuration.name, self._bot_configuration.avatar, message, *args)
            sent_messages_tokens.append(token)

        return sent_messages_tokens

    def send_messages(self, to, messages):
        """
        :param to: Viber user id
        :param messages: list of Message objects to be sent
        :return: list of tokens of the sent messages
        """
        self._logger.debug("going to send messages: {0}, to: {1}".format(messages, to))
        return self.send(self._message_sender.send_message, messages, to)

    def post(self, from_admin, messages):
        """
        :param from_admin: Unique Viber user ID of one of the accounts admins. 
        A list of admins and IDs is available in get_account_info response
        :param messages: list of Message objects to be sent
        :return: list of tokens of the sent messages
        """
        self._logger.debug("going to post messages to public chat: {0}, from: {1}".format(messages, from_admin))
        return self.send(self._message_sender.post, messages, from_admin)

    def _calculate_message_signature(self, message):
        return hmac.new(bytes(self._bot_configuration.auth_token.encode('ascii')),
                        msg=message,
                        digestmod=hashlib.sha256) \
            .hexdigest()
