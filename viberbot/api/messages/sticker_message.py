from future.utils import python_2_unicode_compatible
from viberbot.api.messages.message import Message
from viberbot.api.messages.message_type import MessageType


# currently not supported
class StickerMessage(Message):
	def __init__(self, tracking_data=None, keyboard=None, sticker_id=None):
		super(StickerMessage, self).__init__(MessageType.STICKER, tracking_data, keyboard)
		self._sticker_id = sticker_id

	def to_dict(self):
		message_data = super(StickerMessage, self).to_dict()
		message_data['sticker_id'] = self._sticker_id
		return message_data

	def from_dict(self, message_data):
		super(StickerMessage, self).from_dict(message_data)
		if 'sticker_id' in message_data:
			self._sticker_id = message_data['sticker_id']
		return self

	def get_sticker_id(self):
		return self._sticker_id

	def validate(self):
		return self._sticker_id is not None

	@python_2_unicode_compatible
	def __str__(self):
		return u"StickerMessage [{0}, sticker_id={1}]".format(super(StickerMessage, self).__str__(), self._sticker_id)
