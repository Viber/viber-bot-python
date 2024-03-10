from dataclasses import asdict
from flask import Flask, jsonify, render_template, request, Response, send_file
from app.postgre_utils import get_chat_bot_users

from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages.text_message import TextMessage
from viberbot.api.viber_requests import ViberConversationStartedRequest
from viberbot.api.viber_requests import ViberFailedRequest
from viberbot.api.viber_requests import ViberMessageRequest
from viberbot.api.viber_requests import ViberSubscribedRequest
from viberbot.api.viber_requests import ViberUnsubscribedRequest

import time
import logging
import sched
import threading


import os


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

app = Flask(__name__)

viber = Api(
    BotConfiguration(
        name="FoxBot",
        avatar="https://viber-fox-bot-9d12996926ae.herokuapp.com/foxbot_face",
        auth_token=os.environ["VIBER_AUTH_KEY"],
    )
)


def set_webhook(viber):
    viber.set_webhook("https://viber-fox-bot-9d12996926ae.herokuapp.com/")


scheduler = sched.scheduler(time.time, time.sleep)
scheduler.enter(5, 1, set_webhook, (viber,))
t = threading.Thread(target=scheduler.run)
t.start()


@app.route("/", methods=["GET"])
def hello_world():
    return "Hello world!"


@app.route("/chatbot_users", methods=["GET"])
def display_chat_bot_users():
    users = get_chat_bot_users()
    users_simple_types = [asdict(user) for user in users]
    return render_template("json_template.html", json_data=users_simple_types)


@app.route("/", methods=["POST"])
def incoming():
    logger.debug("received request. post data: {0}".format(request.get_data()))

    viber_request = viber.parse_request(request.get_data().decode("utf8"))

    if isinstance(viber_request, ViberMessageRequest):
        message = viber_request.message
        viber.send_messages(viber_request.sender.id, [message])
    elif (
        isinstance(viber_request, ViberConversationStartedRequest)
        or isinstance(viber_request, ViberSubscribedRequest)
        or isinstance(viber_request, ViberUnsubscribedRequest)
    ):
        viber.send_messages(
            viber_request.user.id,
            [TextMessage(None, None, viber_request.event_type)],
        )
    elif isinstance(viber_request, ViberFailedRequest):
        logger.warn(
            "client failed receiving message. failure: {0}".format(viber_request)
        )

    return Response(status=200)


@app.route("/foxbot_face")
def show_foxbot_face():
    # Imagine that user_image is determined dynamically for each user
    face_path = "static/images/resized_foxbot_image.png"
    return send_file(face_path, mimetype="image/png")
