import random
from faker import Faker
from app.postgre_utils import get_connection

fake = Faker()


# Function to generate dummy data and insert into the chat_bot_users table
def create_chat_bot_users():
    for _ in range(5):
        name = fake.name()
        viber_id = fake.uuid4()
        created_at = fake.date_time_between(start_date="-1y", end_date="now")
        active = random.choice([True, False])
        cur.execute(
            "INSERT INTO chat_bot_users (name, viber_id, created_at, active) VALUES (%s, %s, %s, %s)",
            (name, viber_id, created_at, active),
        )
        conn.commit()


# Function to generate dummy data and insert into the questions table
def create_questions():
    for user_id in range(1, 6):
        for _ in range(3):
            question = fake.sentence()
            created_at = fake.date_time_between(start_date="-1y", end_date="now")
            cur.execute(
                "INSERT INTO questions (question, user_id, created_at) VALUES (%s, %s, %s)",
                (question, user_id, created_at),
            )
            conn.commit()


# Function to generate dummy data and insert into the answers table
def create_answers():
    for user_id in range(1, 6):
        for _ in range(5):
            question_id = random.randint(1, 15)
            answer = fake.text()
            created_at = fake.date_time_between(start_date="-1y", end_date="now")
            approved = random.choice([True, False])
            cur.execute(
                "INSERT INTO answers (answer, question_id, user_id, created_at, approved) VALUES (%s, %s, %s, %s, %s)",
                (answer, question_id, user_id, created_at, approved),
            )
            conn.commit()


if __name__ == "__main__":
    conn = get_connection()
    cur = conn.cursor()

    create_chat_bot_users()
    create_questions()
    create_answers()

    cur.close()
    conn.close()
