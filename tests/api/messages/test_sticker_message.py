from viberbot.api.messages import MessageType
from viberbot.api.messages import StickerMessage

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
SAMPLE_STICKER_ID = 40100


def test_creation():
	sticker_message = StickerMessage(
		tracking_data=SAMPLE_TRACKING_DATA,
		keyboard=SAMPLE_KEYBOARD,
		sticker_id=SAMPLE_STICKER_ID
	)

	assert sticker_message.tracking_data == SAMPLE_TRACKING_DATA
	assert sticker_message.keyboard == SAMPLE_KEYBOARD
	assert sticker_message.sticker_id == SAMPLE_STICKER_ID


def test_to_dict():
	message_dict = dict(
		type=MessageType.STICKER,
		tracking_data=SAMPLE_TRACKING_DATA,
		keyboard=SAMPLE_KEYBOARD,
		sticker_id=SAMPLE_STICKER_ID
	)

	sticker_message_dict = StickerMessage(
		tracking_data=SAMPLE_TRACKING_DATA,
		keyboard=SAMPLE_KEYBOARD,
		sticker_id=SAMPLE_STICKER_ID
	).to_dict()

	assert message_dict == sticker_message_dict


def test_from_dict():
	message_dict = dict(
		tracking_data=SAMPLE_TRACKING_DATA,
		keyboard=SAMPLE_KEYBOARD,
		sticker_id=SAMPLE_STICKER_ID
	)

	sticker_message = StickerMessage().from_dict(message_dict)

	assert sticker_message.tracking_data == SAMPLE_TRACKING_DATA
	assert sticker_message.keyboard == SAMPLE_KEYBOARD
	assert sticker_message.sticker_id == SAMPLE_STICKER_ID


def test_validate_success():
	sticker_message = StickerMessage(
		tracking_data=SAMPLE_TRACKING_DATA,
		keyboard=SAMPLE_KEYBOARD,
		sticker_id=SAMPLE_STICKER_ID
	)

	assert sticker_message.validate()


def test_validate_failure():
	sticker_message = StickerMessage(
		tracking_data=SAMPLE_TRACKING_DATA,
		keyboard=SAMPLE_KEYBOARD
	)

	assert not sticker_message.validate()
