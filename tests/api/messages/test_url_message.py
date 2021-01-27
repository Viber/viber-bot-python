from viberbot.api.messages import MessageType
from viberbot.api.messages import URLMessage

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
SAMPLE_URL = "http://www.google.com"


def test_creation():
	url_message = URLMessage(
		tracking_data=SAMPLE_TRACKING_DATA,
		keyboard=SAMPLE_KEYBOARD,
		media=SAMPLE_URL
	)

	assert url_message.tracking_data == SAMPLE_TRACKING_DATA
	assert url_message.keyboard == SAMPLE_KEYBOARD
	assert url_message.media == SAMPLE_URL


def test_to_dict():
	message_dict = dict(
		type=MessageType.URL,
		tracking_data=SAMPLE_TRACKING_DATA,
		keyboard=SAMPLE_KEYBOARD,
		media=SAMPLE_URL
	)

	url_message_dict = URLMessage(
		tracking_data=SAMPLE_TRACKING_DATA,
		keyboard=SAMPLE_KEYBOARD,
		media=SAMPLE_URL
	).to_dict()

	assert message_dict == url_message_dict


def test_from_dict():
	message_dict = dict(
		tracking_data=SAMPLE_TRACKING_DATA,
		keyboard=SAMPLE_KEYBOARD,
		media=SAMPLE_URL
	)

	url_message = URLMessage().from_dict(message_dict)

	assert url_message.tracking_data == SAMPLE_TRACKING_DATA
	assert url_message.keyboard == SAMPLE_KEYBOARD
	assert url_message.media == SAMPLE_URL


def test_validate_success():
	url_message = URLMessage(
		tracking_data=SAMPLE_TRACKING_DATA,
		keyboard=SAMPLE_KEYBOARD,
		media=SAMPLE_URL
	)

	assert url_message.validate()


def test_validate_failure():
	url_message = URLMessage(
		tracking_data=SAMPLE_TRACKING_DATA,
		keyboard=SAMPLE_KEYBOARD
	)

	assert not url_message.validate()
