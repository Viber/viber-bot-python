from future.utils import python_2_unicode_compatible
from viberbot.api.event_type import EventType
from viberbot.api.user_profile import UserProfile
from viberbot.api.viber_requests.viber_request import ViberRequest


class ViberSubscribedRequest(ViberRequest):
	def __init__(self):
		super(ViberSubscribedRequest, self).__init__(EventType.SUBSCRIBED)
		self._user = None

	def from_dict(self, request_dict):
		super(ViberSubscribedRequest, self).from_dict(request_dict)
		self._user = UserProfile(request_dict['user']['name'],
								 request_dict['user']['avatar'],
								 request_dict['user']['id'],
								 request_dict['user']['country'],
								 request_dict['user']['language'])
		return self

	@property
	def user(self):
		return self._user

	@python_2_unicode_compatible
	def __str__(self):
		return u"ViberSubscribedRequest [{0}, user={1}]" \
			.format(super(ViberSubscribedRequest, self).__str__(),
					self._user)
