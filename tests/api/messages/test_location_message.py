from viberbot.api.messages import LocationMessage
from viberbot.api.messages import MessageType
from viberbot.api.messages.data_types.location import Location

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
SAMPLE_LATITUDE = 10.7
SAMPLE_LONGITUDE = -10.1
SAMPLE_LOCATION = Location(SAMPLE_LATITUDE, SAMPLE_LONGITUDE)


def test_creation():
	location_message = LocationMessage(
		tracking_data=SAMPLE_TRACKING_DATA,
		keyboard=SAMPLE_KEYBOARD,
		location=SAMPLE_LOCATION
	)

	assert location_message.tracking_data == SAMPLE_TRACKING_DATA
	assert location_message.keyboard == SAMPLE_KEYBOARD
	assert location_message.location == SAMPLE_LOCATION


def test_from_dict():
	message_dict = dict(
		tracking_data=SAMPLE_TRACKING_DATA,
		keyboard=SAMPLE_KEYBOARD,
		location=dict(lat=SAMPLE_LATITUDE, lon=SAMPLE_LONGITUDE)
	)

	location_message = LocationMessage().from_dict(message_dict)

	assert location_message.tracking_data == SAMPLE_TRACKING_DATA
	assert location_message.keyboard == SAMPLE_KEYBOARD
	assert location_message.location == SAMPLE_LOCATION


def test_to_dict():
	message_dict = dict(
		type=MessageType.LOCATION,
		tracking_data=SAMPLE_TRACKING_DATA,
		keyboard=SAMPLE_KEYBOARD,
		location=dict(lat=SAMPLE_LATITUDE, lon=SAMPLE_LONGITUDE)
	)

	location_message_dict = LocationMessage(
		tracking_data=SAMPLE_TRACKING_DATA,
		keyboard=SAMPLE_KEYBOARD,
		location=SAMPLE_LOCATION
	).to_dict()

	assert message_dict == location_message_dict


def test_validate_success():
	location_message = LocationMessage(
		tracking_data=SAMPLE_TRACKING_DATA,
		keyboard=SAMPLE_KEYBOARD,
		location=SAMPLE_LOCATION
	)

	assert location_message.validate()


def test_validate_failure():
	location_message = LocationMessage(
		tracking_data=SAMPLE_TRACKING_DATA,
		keyboard=SAMPLE_KEYBOARD
	)
	assert not location_message.validate()

	location_message = LocationMessage(
		tracking_data=SAMPLE_TRACKING_DATA,
		keyboard=SAMPLE_KEYBOARD,
		location=Location()
	)
	assert not location_message.validate()

	location_message = LocationMessage(
		tracking_data=SAMPLE_TRACKING_DATA,
		keyboard=SAMPLE_KEYBOARD,
		location=Location(lat=SAMPLE_LATITUDE)
	)
	assert not location_message.validate()

	location_message = LocationMessage(
		tracking_data=SAMPLE_TRACKING_DATA,
		keyboard=SAMPLE_KEYBOARD,
		location=Location(lon=SAMPLE_LONGITUDE)
	)
	assert not location_message.validate()


def test_validate_out_of_range():
	OUT_OF_RANGE_LATITUDE = 200
	OUT_OF_RANGE_LONGITUDE = 200

	location_message = LocationMessage(
		tracking_data=SAMPLE_TRACKING_DATA,
		keyboard=SAMPLE_KEYBOARD,
		location=Location(lat=SAMPLE_LATITUDE, lon=OUT_OF_RANGE_LONGITUDE)
	)
	assert not location_message.validate()

	location_message = LocationMessage(
		tracking_data=SAMPLE_TRACKING_DATA,
		keyboard=SAMPLE_KEYBOARD,
		location=Location(lat=OUT_OF_RANGE_LATITUDE, lon=SAMPLE_LONGITUDE)
	)
	assert not location_message.validate()


