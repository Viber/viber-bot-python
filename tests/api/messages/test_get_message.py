# coding=utf-8
import json

import pytest

from viberbot.api.messages import ContactMessage
from viberbot.api.messages import FileMessage
from viberbot.api.messages import LocationMessage
from viberbot.api.messages import PictureMessage
from viberbot.api.messages import TextMessage
from viberbot.api.messages import URLMessage
from viberbot.api.messages import VideoMessage
from viberbot.api.messages import get_message


def test_contact_message():
	contact_message_data = """
	{
	   "auth_token": "4453b6ac1s345678-e02c5f12174805f9-daec9cbb5448c51r",
	   "receiver": "01234567890A=",
	   "sender":
	   {
		   "name": "yarden from the pa",
		   "avatar": "http://avatar_url"
	   },
	   "tracking_data": "tracking data",
		"type": "contact",
	   "contact": {
		   "name": "Alex",
		   "phone_number": "+972511123123"
	   }
	}
	"""

	contact_message = get_message(json.loads(contact_message_data))
	assert isinstance(contact_message, ContactMessage)


def test_file_message():
	file_message_data = """
	{
	   "auth_token": "4453b6ac1s345678-e02c5f12174805f9-daec9cbb5448c51r",
	   "receiver": "01234567890A=",
	   "sender":
	   {
		   "name": "yarden from the pa",
		   "avatar": "http://avatar_url"
	   },
	   "tracking_data": "tracking data",
		"type": "file",
	   "media": "http://www.images.com/file.doc",
	   "size": 10000,
	   "file_name": "name_of_file.doc"
	}
	"""

	file_message = get_message(json.loads(file_message_data))
	assert isinstance(file_message, FileMessage)


def test_location_message():
	location_message_data = """
	{
	   "auth_token": "4453b6ac1s345678-e02c5f12174805f9-daec9cbb5448c51r",
	   "receiver": "01234567890A=",
	   "sender":
	   {
		   "name": "yarden from the pa",
		   "avatar": "http://avatar_url"
	   },
	   "tracking_data": "tracking data",
		"type": "location",
	   "location": {"lat": "37.7898", "lon": "-122.3942"}
	}
	"""

	location_message = get_message(json.loads(location_message_data))
	assert isinstance(location_message, LocationMessage)


def test_picture_message():
	picture_message_data = """
	{
	"auth_token": "4453b6ac1s345678-e02c5f12174805f9-daec9cbb5448c51r",
	"receiver": "01234567890A=",
	"sender":
	{
		"name": "yarden from the pa",
		"avatar": "http://avatar_url"
	},
	"tracking_data": "tracking data",
	"type": "picture",
	"text": "Photo description",
	"media": "http://www.images.com/img.jpg",
	"thumbnail": "http://www.images.com/thumb.jpg"
	}
	"""

	picture_message = get_message(json.loads(picture_message_data))
	assert isinstance(picture_message, PictureMessage)


def test_text_message():
	text_message_data = """
	{
	"auth_token": "4453b6ac1s345678-e02c5f12174805f9-daec9cbb5448c51r",
	"receiver": "01234567890A=",
	"sender":
	{
		"name": "yarden from the pa",
		"avatar": "http://avatar_url"
	},
	"tracking_data": "tracking data",
	"type": "text",
	"text": "a message from pa"
	}
	"""

	text_message = get_message(json.loads(text_message_data))
	assert isinstance(text_message, TextMessage)


def test_url_message():
	url_message_data = """
	{
	   "auth_token": "4453b6ac1s345678-e02c5f12174805f9-daec9cbb5448c51r",
	   "receiver": "01234567890A=",
	   "sender":
	   {
		   "name": "yarden from the pa",
		   "avatar": "http://avatar_url"
	   },
	   "tracking_data": "tracking data",
		"type": "url",
	   "media": "http://www.website.com/go_here"
	}
	"""

	url_message = get_message(json.loads(url_message_data))
	assert isinstance(url_message, URLMessage)


def test_video_message():
	video_message_data = """
	{
   "auth_token": "4453b6ac1s345678-e02c5f12174805f9-daec9cbb5448c51r",
   "receiver": "01234567890A=",
   "sender":
   {
       "name": "yarden from the pa",
       "avatar": "http://avatar_url"
   },
   "tracking_data": "tracking data",
    "type": "video",
    "media": "http://www.images.com/video.mp4",
    "thumbnail": "http://www.images.com/thumb.jpg",
    "size": 10000,
    "duration": 10
	}
	"""

	video_message = get_message(json.loads(video_message_data))
	assert isinstance(video_message, VideoMessage)


def test_unknown_type():
	with pytest.raises(Exception) as exc:
		message_data = """
		{
		   "auth_token": "4453b6ac1s345678-e02c5f12174805f9-daec9cbb5448c51r",
		   "receiver": "01234567890A=",
		   "sender":
		   {
			   "name": "yarden from the pa",
			   "avatar": "http://avatar_url"
		   },
		   "tracking_data": "tracking data",
			"type": "NotExists"
		}
		"""

		get_message(json.loads(message_data))
		assert exc.value.message.startswith("message type 'NotExists' is not supported")


def test_get_text_message_unicode():
	text_message_data = u"""
	{
	"auth_token": "4453b6ac1s345678-e02c5f12174805f9-daec9cbb5448c51r",
	"receiver": "01234567890A=",
	"sender":
	{
		"name": "שם בעברית",
		"avatar": "http://avatar_url"
	},
	"tracking_data": "へぶる。塞末タヨハ協責ウワ格子しむ",
	"type": "text",
	"text": "הודעה יפה"
	}
	"""

	text_message = get_message(json.loads(text_message_data))
	assert isinstance(text_message, TextMessage)


def test_get_message_missing_type():
	with pytest.raises(Exception) as exc:
		message_data = """
		{
		   "auth_token": "4453b6ac1s345678-e02c5f12174805f9-daec9cbb5448c51r",
		   "receiver": "01234567890A=",
		   "sender":
		   {
			   "name": "yarden from the pa",
			   "avatar": "http://avatar_url"
		   }
		}
		"""

		get_message(json.loads(message_data))
		assert exc.value.message.startswith("message data doesn't contain a type")
