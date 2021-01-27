from viberbot.api.messages import MessageType
from viberbot.api.messages import TextMessage

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
SAMPLE_TEXT = "sample text"


def test_creation():
	text_message = TextMessage(
		tracking_data=SAMPLE_TRACKING_DATA,
		keyboard=SAMPLE_KEYBOARD,
		text=SAMPLE_TEXT
	)

	assert text_message.tracking_data == SAMPLE_TRACKING_DATA
	assert text_message.keyboard == SAMPLE_KEYBOARD
	assert text_message.text == SAMPLE_TEXT


def test_to_dict():
	message_dict = dict(
		type=MessageType.TEXT,
		tracking_data=SAMPLE_TRACKING_DATA,
		keyboard=SAMPLE_KEYBOARD,
		text=SAMPLE_TEXT
	)

	text_message_dict = TextMessage(
		tracking_data=SAMPLE_TRACKING_DATA,
		keyboard=SAMPLE_KEYBOARD,
		text=SAMPLE_TEXT
	).to_dict()

	assert message_dict == text_message_dict


def test_from_dict():
	message_dict = dict(
		tracking_data=SAMPLE_TRACKING_DATA,
		keyboard=SAMPLE_KEYBOARD,
		text=SAMPLE_TEXT
	)

	text_message = TextMessage().from_dict(message_dict)

	assert text_message.tracking_data == SAMPLE_TRACKING_DATA
	assert text_message.keyboard == SAMPLE_KEYBOARD
	assert text_message.text == SAMPLE_TEXT


def test_validate_success():
	text_message = TextMessage(
		tracking_data=SAMPLE_TRACKING_DATA,
		keyboard=SAMPLE_KEYBOARD,
		text=SAMPLE_TEXT
	)

	assert text_message.validate()


def test_validate_failure():
	text_message = TextMessage(
		tracking_data=SAMPLE_TRACKING_DATA,
		keyboard=SAMPLE_KEYBOARD
	)

	assert not text_message.validate()
