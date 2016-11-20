from viber.api.event_type import EventType
from viber.api.viber_requests.viber_conversation_started_request import ViberConversationStartedRequest
from viber.api.viber_requests.viber_delivered_request import ViberDeliveredRequest
from viber.api.viber_requests.viber_failed_request import ViberFailedRequest
from viber.api.viber_requests.viber_message_request import ViberMessageRequest
from viber.api.viber_requests.viber_request import ViberRequest
from viber.api.viber_requests.viber_seen_request import ViberSeenRequest
from viber.api.viber_requests.viber_subscribed_request import ViberSubscribedRequest
from viber.api.viber_requests.viber_unsubscribed_request import ViberUnsubscribedRequest


EVENT_TYPE_TO_CLASS = {
	EventType.MESSAGE: ViberMessageRequest,
	EventType.FAILED: ViberFailedRequest,
	EventType.CONVERSATION_STARTED: ViberConversationStartedRequest,
	EventType.DELIVERED: ViberDeliveredRequest,
	EventType.SEEN: ViberSeenRequest,
	EventType.SUBSCRIBED: ViberSubscribedRequest,
	EventType.UNSUBSCRIBED: ViberUnsubscribedRequest,
	EventType.WEBHOOK: ViberRequest
}


def create_request(request_dict):
	if request_dict['event'] not in EVENT_TYPE_TO_CLASS:
		raise Exception("event type '{0}' is not supported".format(request_dict['event']))

	return EVENT_TYPE_TO_CLASS[request_dict['event']]().from_dict(request_dict)


