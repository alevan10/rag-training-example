# rag-training-example
A simple example of rag training against n-documents for querying

## Requirements

- A Python 3.12 virtual environment with `uv` installed

This project is built on `uv`, using `FastAPI` running on `uvicorn` for the API layer. Additionally, the preferred running environment uses a GPU with enough memory to run larger models.
This can be run on CPU by commenting out the `deploy` requirments in the `docker-compose.yaml` file.

## Running

This project is an example of RAG training an LLM for data retrieve and research assistance, using Ollama to host the models and handle the training for us.
A local copy of OpenWebUI is included as well for a GUI experience, as well as a simple API for checking model status, pulling models, and making queries.
