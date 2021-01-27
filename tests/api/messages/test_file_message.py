from viberbot.api.messages import FileMessage
from viberbot.api.messages import MessageType

SAMPLE_TRACKING_DATA = "some tracking data"
SAMPLE_KEYBOARD = """{
  "Type": "keyboard",
  "DefaultHeight": true,
  "BgColor": "#FFFFFF",
  "Buttons": [
   {
     "Columns": 6,
     "Rows": 1,
     "BgColor": "#2db9b9",
     "BgMediaType": "gif",
     "BgMedia": "http://www.url.by/test.gif",
     "BgLoop": true,
     "ActionType": "open-url",
     "ActionBody": "www.tut.by",
     "Image": "www.tut.by/img.jpg",
     "Text": "Key text",
     "TextVAlign": "middle",
     "TextHAlign": "center",
     "TextOpacity": 60,
     "TextSize": "regular"
   }
   ]
   }"""
SAMPLE_MEDIA = "http://www.site.com/research.pdf"
SAMPLE_SIZE = 1000
SAMPLE_FILE_NAME = "research.pdf"


def test_creation():
	file_message = FileMessage(
		tracking_data=SAMPLE_TRACKING_DATA,
		keyboard=SAMPLE_KEYBOARD,
		media=SAMPLE_MEDIA,
		size=SAMPLE_SIZE,
		file_name=SAMPLE_FILE_NAME
	)

	assert file_message.tracking_data == SAMPLE_TRACKING_DATA
	assert file_message.keyboard == SAMPLE_KEYBOARD
	assert file_message.media == SAMPLE_MEDIA
	assert file_message.size == SAMPLE_SIZE
	assert file_message.file_name == SAMPLE_FILE_NAME


def test_from_dict():
	message_dict = dict(
		tracking_data=SAMPLE_TRACKING_DATA,
		keyboard=SAMPLE_KEYBOARD,
		media=SAMPLE_MEDIA,
		size=SAMPLE_SIZE,
		file_name=SAMPLE_FILE_NAME
	)

	file_message = FileMessage().from_dict(message_dict)

	assert file_message.tracking_data == SAMPLE_TRACKING_DATA
	assert file_message.keyboard == SAMPLE_KEYBOARD
	assert file_message.media == SAMPLE_MEDIA
	assert file_message.size == SAMPLE_SIZE
	assert file_message.file_name == SAMPLE_FILE_NAME


def test_to_dict():
	message_dict = dict(
		type=MessageType.FILE,
		tracking_data=SAMPLE_TRACKING_DATA,
		keyboard=SAMPLE_KEYBOARD,
		media=SAMPLE_MEDIA,
		size=SAMPLE_SIZE,
		file_name=SAMPLE_FILE_NAME
	)

	file_message_dict = FileMessage(
		tracking_data=SAMPLE_TRACKING_DATA,
		keyboard=SAMPLE_KEYBOARD,
		media=SAMPLE_MEDIA,
		size=SAMPLE_SIZE,
		file_name=SAMPLE_FILE_NAME
	).to_dict()

	assert message_dict == file_message_dict


def test_validate_success():
	file_message = FileMessage(
		media=SAMPLE_MEDIA,
		size=SAMPLE_SIZE,
		file_name=SAMPLE_FILE_NAME
	)

	assert file_message.validate()


def test_validate_missing_params():
	file_message = FileMessage(
		size=SAMPLE_SIZE,
		file_name=SAMPLE_FILE_NAME
	)

	assert not file_message.validate()

	file_message = FileMessage(
		media=SAMPLE_MEDIA,
		file_name=SAMPLE_FILE_NAME
	)

	assert not file_message.validate()

	file_message = FileMessage(
		media=SAMPLE_MEDIA,
		size=SAMPLE_SIZE
	)

	assert not file_message.validate()


