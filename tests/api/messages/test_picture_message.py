from viberbot.api.messages import MessageType
from viberbot.api.messages import PictureMessage

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
SAMPLE_TEXT = "bridge"
SAMPLE_MEDIA = "http://www.site.com/bridge.jpg"
SAMPLE_THUMBNAIL = "http://www.site.com/bridgethumb.jpg"


def test_creation():
	picture_message = PictureMessage(
		tracking_data=SAMPLE_TRACKING_DATA,
		keyboard=SAMPLE_KEYBOARD,
		text=SAMPLE_TEXT,
		media=SAMPLE_MEDIA,
		thumbnail=SAMPLE_THUMBNAIL
	)

	assert picture_message.tracking_data == SAMPLE_TRACKING_DATA
	assert picture_message.keyboard == SAMPLE_KEYBOARD
	assert picture_message.media == SAMPLE_MEDIA
	assert picture_message.text == SAMPLE_TEXT
	assert picture_message.thumbnail == SAMPLE_THUMBNAIL


def test_from_dict():
	message_dict = dict(
		tracking_data=SAMPLE_TRACKING_DATA,
		keyboard=SAMPLE_KEYBOARD,
		text=SAMPLE_TEXT,
		media=SAMPLE_MEDIA,
		thumbnail=SAMPLE_THUMBNAIL
	)

	picture_message = PictureMessage().from_dict(message_dict)

	assert picture_message.tracking_data == SAMPLE_TRACKING_DATA
	assert picture_message.keyboard == SAMPLE_KEYBOARD
	assert picture_message.media == SAMPLE_MEDIA
	assert picture_message.text == SAMPLE_TEXT
	assert picture_message.thumbnail == SAMPLE_THUMBNAIL


def test_to_dict():
	message_dict = dict(
		type=MessageType.PICTURE,
		tracking_data=SAMPLE_TRACKING_DATA,
		keyboard=SAMPLE_KEYBOARD,
		text=SAMPLE_TEXT,
		media=SAMPLE_MEDIA,
		thumbnail=SAMPLE_THUMBNAIL
	)

	picture_message_dict = PictureMessage(
		tracking_data=SAMPLE_TRACKING_DATA,
		keyboard=SAMPLE_KEYBOARD,
		text=SAMPLE_TEXT,
		media=SAMPLE_MEDIA,
		thumbnail=SAMPLE_THUMBNAIL
	).to_dict()

	assert message_dict == picture_message_dict


def test_validate_success():
	picture_message = PictureMessage(
		tracking_data=SAMPLE_TRACKING_DATA,
		keyboard=SAMPLE_KEYBOARD,
		text=SAMPLE_TEXT,
		media=SAMPLE_MEDIA,
		thumbnail=SAMPLE_THUMBNAIL
	)

	assert picture_message.validate()


def test_validate_failure():
	picture_message = PictureMessage(
		tracking_data=SAMPLE_TRACKING_DATA,
		keyboard=SAMPLE_KEYBOARD,
		text=SAMPLE_TEXT,
		thumbnail=SAMPLE_THUMBNAIL
	)

	assert not picture_message.validate()
