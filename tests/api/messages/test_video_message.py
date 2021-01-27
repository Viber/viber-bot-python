from viberbot.api.messages import MessageType
from viberbot.api.messages import VideoMessage

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
SAMPLE_MEDIA = "http://www.site.com/bridge.mp4"
SAMPLE_THUMBNAIL = "http://www.site.com/bridgethumb.jpg"
SAMPLE_SIZE = 1000
SAMPLE_DURATION = 10
SAMPLE_TEXT = "see my video!"


def test_creation():
	video_message = VideoMessage(
		tracking_data=SAMPLE_TRACKING_DATA,
		keyboard=SAMPLE_KEYBOARD,
		media=SAMPLE_MEDIA,
		thumbnail=SAMPLE_THUMBNAIL,
		size=SAMPLE_SIZE,
		duration=SAMPLE_DURATION,
		text=SAMPLE_TEXT
	)

	assert video_message.tracking_data == SAMPLE_TRACKING_DATA
	assert video_message.keyboard == SAMPLE_KEYBOARD
	assert video_message.media == SAMPLE_MEDIA
	assert video_message.size == SAMPLE_SIZE
	assert video_message.thumbnail == SAMPLE_THUMBNAIL
	assert video_message.duration == SAMPLE_DURATION
	assert video_message.text == SAMPLE_TEXT


def test_from_dict():
	message_dict = dict(
		tracking_data=SAMPLE_TRACKING_DATA,
		keyboard=SAMPLE_KEYBOARD,
		media=SAMPLE_MEDIA,
		thumbnail=SAMPLE_THUMBNAIL,
		size=SAMPLE_SIZE,
		duration=SAMPLE_DURATION,
		text=SAMPLE_TEXT
	)

	video_message = VideoMessage().from_dict(message_dict)

	assert video_message.tracking_data == SAMPLE_TRACKING_DATA
	assert video_message.keyboard == SAMPLE_KEYBOARD
	assert video_message.media == SAMPLE_MEDIA
	assert video_message.size == SAMPLE_SIZE
	assert video_message.thumbnail == SAMPLE_THUMBNAIL
	assert video_message.duration == SAMPLE_DURATION
	assert video_message.text == SAMPLE_TEXT


def test_to_dict():
	message_dict = dict(
		type=MessageType.VIDEO,
		tracking_data=SAMPLE_TRACKING_DATA,
		keyboard=SAMPLE_KEYBOARD,
		media=SAMPLE_MEDIA,
		thumbnail=SAMPLE_THUMBNAIL,
		size=SAMPLE_SIZE,
		duration=SAMPLE_DURATION,
		text=SAMPLE_TEXT
	)

	video_message_dict = VideoMessage(
		tracking_data=SAMPLE_TRACKING_DATA,
		keyboard=SAMPLE_KEYBOARD,
		media=SAMPLE_MEDIA,
		thumbnail=SAMPLE_THUMBNAIL,
		size=SAMPLE_SIZE,
		duration=SAMPLE_DURATION,
		text=SAMPLE_TEXT
	).to_dict()

	assert message_dict == video_message_dict


def test_validate_success():
	video_message = VideoMessage(
		media=SAMPLE_MEDIA,
		size=SAMPLE_SIZE
	)

	assert video_message.validate()


def test_validate_failure():
	video_message = VideoMessage(
		tracking_data=SAMPLE_TRACKING_DATA,
		keyboard=SAMPLE_KEYBOARD,
		thumbnail=SAMPLE_THUMBNAIL,
		size=SAMPLE_SIZE,
		duration=SAMPLE_DURATION
	)

	assert not video_message.validate()

	video_message = VideoMessage(
		tracking_data=SAMPLE_TRACKING_DATA,
		keyboard=SAMPLE_KEYBOARD,
		media=SAMPLE_MEDIA,
		thumbnail=SAMPLE_THUMBNAIL,
		duration=SAMPLE_DURATION
	)

	assert not video_message.validate()
