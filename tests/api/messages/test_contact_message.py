from viberbot.api.messages import ContactMessage
from viberbot.api.messages import MessageType
from viberbot.api.messages.data_types.contact import Contact

SAMPLE_TRACKING_DATA = "tracking data!"
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
SAMPLE_CONTACT_NAME = "contact name"
SAMPLE_PHONE_NUMBER = "052947378493"
SAMPLE_AVATAR = "awesomeavatar"
SAMPLE_CONTACT = Contact(SAMPLE_CONTACT_NAME, SAMPLE_PHONE_NUMBER, SAMPLE_AVATAR)


def test_creation():
	contact_message = ContactMessage(
		tracking_data=SAMPLE_TRACKING_DATA,
		keyboard=SAMPLE_KEYBOARD,
		contact=SAMPLE_CONTACT)

	assert contact_message.keyboard == SAMPLE_KEYBOARD
	assert contact_message.tracking_data == SAMPLE_TRACKING_DATA
	assert contact_message.contact == SAMPLE_CONTACT


def test_from_dict():
	message_dict = dict(
		tracking_data=SAMPLE_TRACKING_DATA,
		keyboard=SAMPLE_KEYBOARD,
		contact=dict(name=SAMPLE_CONTACT_NAME, phone_number=SAMPLE_PHONE_NUMBER)
	)

	contact_message = ContactMessage().from_dict(message_dict)

	assert contact_message.keyboard == SAMPLE_KEYBOARD
	assert contact_message.tracking_data == SAMPLE_TRACKING_DATA
	assert contact_message.contact == SAMPLE_CONTACT


def test_to_dict():
	message_dict = dict(
		type=MessageType.CONTACT,
		tracking_data=SAMPLE_TRACKING_DATA,
		keyboard=SAMPLE_KEYBOARD,
		contact=dict(name=SAMPLE_CONTACT_NAME, phone_number=SAMPLE_PHONE_NUMBER, avatar=SAMPLE_AVATAR))

	contact_message_dict = ContactMessage(tracking_data=SAMPLE_TRACKING_DATA,
										  keyboard=SAMPLE_KEYBOARD,
										  contact=SAMPLE_CONTACT).to_dict()

	assert message_dict == contact_message_dict


def test_validate_no_contact():
	contact_message = ContactMessage(tracking_data=SAMPLE_TRACKING_DATA)
	assert not contact_message.validate()


def test_validate_success():
	contact_message = ContactMessage(tracking_data=SAMPLE_TRACKING_DATA, contact=SAMPLE_CONTACT)
	assert contact_message.validate()


def test_validate_missing_contact_param():
	contact_message = ContactMessage(tracking_data=SAMPLE_TRACKING_DATA, contact=Contact(name=SAMPLE_CONTACT_NAME))
	assert not contact_message.validate()

	contact_message = ContactMessage(tracking_data=SAMPLE_TRACKING_DATA, contact=Contact(phone_number=SAMPLE_PHONE_NUMBER))
	assert not contact_message.validate()