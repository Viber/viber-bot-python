from dataclasses import dataclass


@dataclass
class ChatBotUser:
    user_id: int
    name: str
    viber_id: str
    created_at: str
    active: bool


@dataclass
class Question:
    question_id: int
    question_text: str
    user_id: int
    created_at: str


@dataclass
class Answer:
    answer_id: int
    answer_text: str
    question_id: int
    user_id: int
    created_at: str
    approved: bool
