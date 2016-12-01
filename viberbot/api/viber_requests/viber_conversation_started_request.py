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
		return self

	def get_user(self):
		return self._user

	def get_type(self):
		return self._type

	def get_context(self):
		return self._context

	def get_message_token(self):
		return self._message_token

	@python_2_unicode_compatible
	def __str__(self):
		return u"ViberConversationStartedRequest [{0}, message_token={1}, type={2}, context{3}, user={4}]"\
			.format(super(ViberConversationStartedRequest, self).__str__(),
					self._message_token,
					self._type,
					self._context,
					self._user)
