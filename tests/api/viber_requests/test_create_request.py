from datetime import datetime

import pytest
from viberbot.api.messages import MessageType
from viberbot.api.viber_requests import create_request


def test_create_request_missing_event():
	sample_request = dict(
		timestamp=datetime.now(),
		message_token="912661846655238145",
		sender=dict(
			id="01234567890A=",
			name="viberUser",
			avatar="http://avatar_url"
		),
		message=dict(
			type=MessageType.TEXT,
			text="HI!"
		))

	with pytest.raises(Exception) as exc:
		create_request(sample_request)
		assert exc.value.message.startswith("request is missing field 'event'")