from viber.api.messages.contact_message import ContactMessage
from viber.api.messages.file_message import FileMessage
from viber.api.messages.location_message import LocationMessage
from viber.api.messages.picture_message import PictureMessage
from viber.api.messages.sticker_message import StickerMessage
from viber.api.messages.url_message import URLMessage
from viber.api.messages.video_message import VideoMessage
from viber.api.messages.message_type import MessageType
from viber.api.messages.text_message import TextMessage
from viber.api.messages.location_message import LocationMessage

MESSAGE_TYPE_TO_CLASS = {
	MessageType.URL: URLMessage,
	MessageType.LOCATION: LocationMessage,
	MessageType.PICTURE: PictureMessage,
	MessageType.CONTACT: ContactMessage,
	MessageType.FILE: FileMessage,
	MessageType.TEXT: TextMessage,
	MessageType.VIDEO: VideoMessage
}


def get_message(message_dict):
	if 'type' not in message_dict:
		raise Exception("message data doesn't contain a type")

	if message_dict['type'] not in MESSAGE_TYPE_TO_CLASS:
		raise Exception(u"message type '{0}' is not supported".format(message_dict['type']))

	return MESSAGE_TYPE_TO_CLASS[message_dict['type']]().from_dict(message_dict)


