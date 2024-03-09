from dataclasses import dataclass

from typing import Any
from pymongo import MongoClient
from pymongo.server_api import ServerApi


class CollectionNames:
    qa: str = "QA"
    users: str = "users"
    answers: str = "answers"
    questions: str = "questions"


collection_names = CollectionNames()


def get_collection_connection(collection_name: str = "QA") -> Any:
    uri = "mongodb+srv://fox-bot-mongodb.dwdgpjs.mongodb.net/?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
    client = MongoClient(
        uri,
        tls=True,
        tlsCertificateKeyFile="../certificates/X509-cert-1196297643430257384.pem",
        server_api=ServerApi("1"),
    )

    db = client["fox-bot-mongodb"]
    collection = db[collection_name]
    return collection


def test_connection(collection_name: str = "QA") -> None:
    collection = get_collection_connection(collection_name=collection_name)
    doc_count = collection.count_documents({})
    print(doc_count)


def insert_document(document: dict, collection_name: str = "QA") -> Any:
    collection = get_collection_connection(collection_name=collection_name)
    document_id = collection.insert_one(document)
    return document_id
