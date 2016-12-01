from future.utils import python_2_unicode_compatible
from viberbot.api.messages.message import Message
from viberbot.api.messages.message_type import MessageType


class URLMessage(Message):
	def __init__(self, tracking_data=None, keyboard=None, media=None):
		super(URLMessage, self).__init__(MessageType.URL, tracking_data, keyboard)
		self._media = media

	def to_dict(self):
		message_data = super(URLMessage, self).to_dict()
		message_data['media'] = self._media
		return message_data

	def from_dict(self, message_data):
		super(URLMessage, self).from_dict(message_data)
		if 'media' in message_data:
			self._media = message_data['media']
		return self

	def get_media(self):
		return self._media

	def validate(self):
		return self._media is not None

	@python_2_unicode_compatible
	def __str__(self):
		return u"URLMessage [{0}, media={1}]".format(super(URLMessage, self).__str__(), self._media)
