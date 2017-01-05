from future.utils import python_2_unicode_compatible
from viberbot.api.event_type import EventType
from viberbot.api.user_profile import UserProfile
from viberbot.api.viber_requests.viber_request import ViberRequest


class ViberConversationStartedRequest(ViberRequest):
	def __init__(self):
		super(ViberConversationStartedRequest, self).__init__(EventType.CONVERSATION_STARTED)
		self._message_token = None
		self._type = None
		self._context = None
		self._user = None
		self._api_version = None

	def from_dict(self, request_dict):
		super(ViberConversationStartedRequest, self).from_dict(request_dict)
		self._message_token = request_dict['message_token']
		self._type = request_dict['type']
		if 'context' in request_dict:
			self._context = request_dict['context']
		self._user = UserProfile(request_dict['user']['name'],
								 request_dict['user']['avatar'],
								 request_dict['user']['id'],
								 request_dict['user']['country'],
								 request_dict['user']['language'])
		if 'api_version' in request_dict:
			self._api_version = request_dict['api_version']
		return self

	@property
	def user(self):
		return self._user

	@property
	def type(self):
		return self._type

	@property
	def context(self):
		return self._context

	@property
	def message_token(self):
		return self._message_token

	@property
	def api_version(self):
		return self._api_version

	@python_2_unicode_compatible
	def __str__(self):
		return u"ViberConversationStartedRequest [{0}, message_token={1}, type={2}, context{3}, user={4}]"\
			.format(super(ViberConversationStartedRequest, self).__str__(),
					self._message_token,
					self._type,
					self._context,
					self._user)

