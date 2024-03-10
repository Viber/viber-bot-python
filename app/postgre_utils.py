import os
import random
from typing import List

from dotenv import load_dotenv
from faker import Faker
import psycopg2

from app.entities import Answer, ChatBotUser, Question


load_dotenv()


class DatabaseConnection:
    def __enter__(self):
        self.conn = psycopg2.connect(os.environ["DATABASE_URL"], sslmode="require")
        self.cur = self.conn.cursor()
        return self.cur

    def __exit__(self, exc_type, exc_value, traceback):
        self.cur.close()
        self.conn.close()


def get_connection():
    DATABASE_URL = os.environ["DATABASE_URL"]

    conn = psycopg2.connect(DATABASE_URL, sslmode="require")

    return conn


def get_chat_bot_users() -> List[ChatBotUser]:
    with DatabaseConnection() as cur:
        # Connect to the PostgreSQL database
        cur.execute(
            "SELECT user_id, name, viber_id, created_at, active FROM chat_bot_users"
        )
        rows = cur.fetchall()

        # Convert rows to list of ChatBotUser objects
        chat_bot_users = []
        for row in rows:
            chat_bot_user = ChatBotUser(*row)
            chat_bot_users.append(chat_bot_user)

    return chat_bot_users


def get_questions() -> List[Question]:
    with DatabaseConnection() as cur:
        # Connect to the PostgreSQL database
        cur.execute("SELECT question_id, question, user_id, created_at FROM questions")

        rows = cur.fetchall()

        # Convert rows to list of ChatBotUser objects
        questions = []
        for row in rows:
            question = Question(*row)
            questions.append(question)

    return questions


def get_answers() -> List[Answer]:
    with DatabaseConnection() as cur:
        # Connect to the PostgreSQL database
        cur.execute(
            "SELECT answer_id, answer, question_id, user_id, created_at, approved FROM answers"
        )

        rows = cur.fetchall()

        # Convert rows to list of ChatBotUser objects
        answers = []
        for row in rows:
            answer = Answer(*row)
            answers.append(answer)

    return answers


def add_user(name, viber_id):
    cur.execute(
        "INSERT INTO chat_bot_users (name, viber_id) VALUES (%s, %s)", (name, viber_id)
    )
    conn.commit()


def make_user_inactive(user_id):
    cur.execute(
        "UPDATE chat_bot_users SET active = FALSE WHERE user_id = %s", (user_id,)
    )


def add_question(user_id, question):
    cur.execute(
        "INSERT INTO questions (question, user_id) VALUES (%s,  %s)",
        (question, user_id),
    )
    conn.commit()


def add_answer(user_id, question_id, answer_text):
    cur.execute(
        "INSERT INTO answers (answer_text, question_id, user_id) VALUES (%s, %s, %s)",
        (answer_text, question_id, user_id),
    )
    conn.commit()


def approve_answer(answer_id):
    cur.execute("UPDATE answers SET approved = TRUE WHERE answer_id = %s", (answer_id,))
    conn.commit()


if __name__ == "__main__":
    conn = get_connection()
    cur = conn.cursor()

    users = get_chat_bot_users()
    questions = get_questions()
    answers = get_answers()

    cur.close()
    conn.close()
