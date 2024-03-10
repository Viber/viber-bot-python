from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    ForeignKey,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Create the SQLAlchemy engine
engine = create_engine("postgresql://username:password@localhost:5432/database_name")

# Create a base class for declarative class definitions
Base = declarative_base()


# Define the ChatBotUser table
class ChatBotUser(Base):
    __tablename__ = "chat_bot_users"

    user_id = Column(Integer, primary_key=True)
    name = Column(String)
    viber_id = Column(String)
    created_at = Column(DateTime)
    active = Column(Boolean)


# Define the Question table
class Question(Base):
    __tablename__ = "questions"

    question_id = Column(Integer, primary_key=True)
    question_text = Column(String)
    user_id = Column(Integer, ForeignKey("chat_bot_users.user_id"))
    created_at = Column(DateTime)

    user = relationship("ChatBotUser")


# Define the Answer table
class Answer(Base):
    __tablename__ = "answers"

    answer_id = Column(Integer, primary_key=True)
    answer_text = Column(String)
    question_id = Column(Integer, ForeignKey("questions.question_id"))
    user_id = Column(Integer, ForeignKey("chat_bot_users.user_id"))
    created_at = Column(DateTime)
    approved = Column(Boolean)

    question = relationship("Question")
    user = relationship("ChatBotUser")


# Create the tables in the database
Base.metadata.create_all(engine)
