from viberbot.api.messages import KeyboardMessage

SAMPLE_TRACKING_DATA = "some tracking data"
SAMPLE_KEYBOARD = {
	"Type": "keyboard",
	"Revision": 1,
	"Buttons": [
		{
			"Columns": 3,
			"Rows": 2,
			"BgColor": "#e6f5ff",
			"BgMedia": "http://www.jqueryscript.net/images/Simplest-Responsive-jQuery-Image-Lightbox-Plugin-simple-lightbox.jpg",
			"BgMediaType": "picture",
			"BgLoop": True,
			"ActionType": "reply",
			"ActionBody": "whatwhatwhatwhatwhatwhat"
		}
	]
}


def test_creation():
	keyboard_message = KeyboardMessage(
		tracking_data=SAMPLE_TRACKING_DATA,
		keyboard=SAMPLE_KEYBOARD
	)

	assert keyboard_message.tracking_data == SAMPLE_TRACKING_DATA
	assert keyboard_message.keyboard == SAMPLE_KEYBOARD


def test_to_dict():
	message_dict = dict(
		tracking_data=SAMPLE_TRACKING_DATA,
		keyboard=SAMPLE_KEYBOARD
	)

	keyboard_message_dict = KeyboardMessage(
		tracking_data=SAMPLE_TRACKING_DATA,
		keyboard=SAMPLE_KEYBOARD
	).to_dict()

	assert message_dict == keyboard_message_dict


def test_from_dict():
	message_dict = dict(
		tracking_data=SAMPLE_TRACKING_DATA,
		keyboard=SAMPLE_KEYBOARD
	)

	keyboard_message = KeyboardMessage().from_dict(message_dict)

	assert keyboard_message.tracking_data == SAMPLE_TRACKING_DATA
	assert keyboard_message.keyboard == SAMPLE_KEYBOARD


def test_validate_success():
	keyboard_message = KeyboardMessage(
		tracking_data=SAMPLE_TRACKING_DATA,
		keyboard=SAMPLE_KEYBOARD
	)

	assert keyboard_message.validate()


def test_validate_failure():
	keyboard_message = KeyboardMessage(
		tracking_data=SAMPLE_TRACKING_DATA
	)

	assert not keyboard_message.validate()
