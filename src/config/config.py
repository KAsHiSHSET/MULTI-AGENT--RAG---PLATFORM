"""Configuration module"""

import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()


class Config:

    # Default API key (fallback)
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    # Default model
    DEFAULT_MODEL = "llama-3.3-70b-versatile"

    # Current model
    MODEL_NAME = DEFAULT_MODEL

    # Models shown in UI
    AVAILABLE_MODELS = [
        "llama-3.3-70b-versatile",
        "llama-3.1-8b-instant",
        "gemma2-9b-it",
        "meta-llama/llama-4-scout-17b-16e-instruct",
    ]

    # Embeddings
    EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

    # Chunking
    CHUNK_SIZE = 500
    CHUNK_OVERLAP = 50

    # Default documents
    DEFAULT_URLS = [
        "https://lilianweng.github.io/posts/2023-06-23-agent/",
        "https://lilianweng.github.io/posts/2024-04-12-diffusion-video/",
    ]

    @classmethod
    def get_llm(cls, api_key=None, model_name=None):

     print("=" * 60)
     print("API KEY:", api_key)
     print("MODEL:", model_name)
     print("=" * 60)

     return ChatGroq(
        groq_api_key=api_key or cls.GROQ_API_KEY,
        model=model_name or cls.MODEL_NAME,
        temperature=0,
     )