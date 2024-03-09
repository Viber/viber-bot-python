from app.postgre_utils import get_connection


def create_chat_bot_users_table():
    cur.execute(
        """
        CREATE TABLE chat_bot_users (
            user_id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            viber_id VARCHAR(255) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            active BOOLEAN DEFAULT TRUE
        );
        """
    )
    conn.commit()


def create_questions_table():
    cur.execute(
        """
        CREATE TABLE questions (
    question_id SERIAL PRIMARY KEY,
    question TEXT NOT NULL,
    user_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

        """
    )
    conn.commit()


def create_answers_table():
    cur.execute(
        """
CREATE TABLE answers (
    answer_id SERIAL PRIMARY KEY,
    answer TEXT NOT NULL,
    question_id INT NOT NULL,
    user_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    approved BOOLEAN DEFAULT FALSE
);

"""
    )
    conn.commit()


if __name__ == "__main__":
    conn = get_connection()
    cur = conn.cursor()

    create_chat_bot_users_table()
    create_questions_table()
    create_answers_table()

    cur.close()
    conn.close()
