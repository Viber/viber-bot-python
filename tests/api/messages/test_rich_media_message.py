from viberbot.api.messages import MessageType
from viberbot.api.messages import RichMediaMessage

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
SAMPLE_RICH_MEDIA = """{
  "DefaultHeight": true,
  "BgColor": "#69C48A",
  "Buttons": [
    {
      "Columns": 6,
      "Rows": 1,
      "BgColor": "#454545",
      "BgMediaType": "gif",
      "BgMedia": "http://www.url.by/test.gif",
      "BgLoop": true,
      "ActionType": "open-url",
      "Silent": true,
      "ActionBody": "www.tut.by",
      "Image": "www.tut.by/img.jpg",
      "TextVAlign": "middle",
      "TextHAlign": "left",
      "Text": "<b>Viber</b> is the best company",
      "TextOpacity": 10,
      "TextSize": "regular"
    }
  ]
}"""
SAMPLE_ALT_TEXT = "upgrade now!"


def test_creation():
	text_message = RichMediaMessage(
		tracking_data=SAMPLE_TRACKING_DATA,
		keyboard=SAMPLE_KEYBOARD,
		rich_media=SAMPLE_RICH_MEDIA,
		alt_text=SAMPLE_ALT_TEXT
	)

	assert text_message.tracking_data == SAMPLE_TRACKING_DATA
	assert text_message.keyboard == SAMPLE_KEYBOARD
	assert text_message.rich_media == SAMPLE_RICH_MEDIA
	assert text_message.alt_text == SAMPLE_ALT_TEXT


def test_to_dict():
	message_dict = dict(
		type=MessageType.RICH_MEDIA,
		tracking_data=SAMPLE_TRACKING_DATA,
		keyboard=SAMPLE_KEYBOARD,
		rich_media=SAMPLE_RICH_MEDIA,
		alt_text=SAMPLE_ALT_TEXT
	)

	rich_media_message_dict = RichMediaMessage(
		tracking_data=SAMPLE_TRACKING_DATA,
		keyboard=SAMPLE_KEYBOARD,
		rich_media=SAMPLE_RICH_MEDIA,
		alt_text=SAMPLE_ALT_TEXT
	).to_dict()

	assert message_dict == rich_media_message_dict


def test_from_dict():
	message_dict = dict(
		tracking_data=SAMPLE_TRACKING_DATA,
		keyboard=SAMPLE_KEYBOARD,
		rich_media=SAMPLE_RICH_MEDIA,
		alt_text=SAMPLE_ALT_TEXT
	)

	text_message = RichMediaMessage().from_dict(message_dict)

	assert text_message.tracking_data == SAMPLE_TRACKING_DATA
	assert text_message.keyboard == SAMPLE_KEYBOARD
	assert text_message.rich_media == SAMPLE_RICH_MEDIA
	assert text_message.alt_text == SAMPLE_ALT_TEXT


def test_validate_success():
	text_message = RichMediaMessage(
		tracking_data=SAMPLE_TRACKING_DATA,
		keyboard=SAMPLE_KEYBOARD,
		rich_media=SAMPLE_RICH_MEDIA
	)

	assert text_message.validate()


def test_validate_failure():
	text_message = RichMediaMessage(
		tracking_data=SAMPLE_TRACKING_DATA,
		keyboard=SAMPLE_KEYBOARD
	)

	assert not text_message.validate()
