import json

from viberbot.api.consts import BOT_API_ENDPOINT


class MessageSender(object):
    def __init__(self, logger, request_sender, bot_configuration):
        self._logger = logger
        self._request_sender = request_sender
        self._bot_configuration = bot_configuration

    def prepare_payload(self, sender_name, sender_avatar, message):
        if not message.validate():
            self._logger.error(u"failed validating message: {0}".format(message))
            raise Exception("failed validating message: {0}".format(message))

        payload = message.to_dict()
        payload.update({
            'auth_token': self._bot_configuration.auth_token,
            "sender": {
                "name": sender_name,
                "avatar": sender_avatar
            }
        })
        return payload

    def send(self, payload, bot_api_endpoint):
        self._logger.debug(u"going to send message: {0}".format(payload))
        result = self._request_sender.post_request(bot_api_endpoint,
                                                   json.dumps(self.remove_empty_fields(payload)))

        if not result['status'] == 0:
            raise Exception(u"failed with status: {0}, message: {1}".format(result['status'], result['status_message']))

        return result

    def send_message(self, sender_name, sender_avatar, message, to):
        payload = self.prepare_payload(sender_name, sender_avatar, message)
        payload.update({
            "receiver": to
        })
        result = self.send(payload, BOT_API_ENDPOINT.SEND_MESSAGE)
        return result['message_token']

    def post(self, sender_name, sender_avatar, message, from_admin):
        payload = self.prepare_payload(sender_name, sender_avatar, message)
        payload.update({
            "from": from_admin
        })
        result = self.send(payload, BOT_API_ENDPOINT.POST)
        return result['message_token']

    def remove_empty_fields(self, message):
        return {k: v for k, v in message.items() if v is not None}
