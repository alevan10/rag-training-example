# rag-training-example
A simple example of rag training against n-documents for querying

## Requirements

- A Python 3.12 virtual environment with `uv` installed

This project is built on `uv`. Additionally, the preferred running environment uses a GPU with enough memory to run larger models.
This can be run on CPU by commenting out the `deploy` requirments in the `docker-compose.yaml` file.

## Running

This project is an example of RAG training an LLM for data retrieve and research assistance, using Ollama to host the models and handle the training for us.
A local copy of OpenWebUI is included as well for a GUI experience, but the main `app` container runs a simple script to generate a vector database based on the documents included in `documents`, then generate a response based on that vector database.

On initial run it's recommended to just run the `ollama` container and pull some models.

```bash
ollama pull nomic-embed-text:v1.5
ollama pull <some reasoning or generation model like gpt-oss:20b>
```

Then you can run the full `app` container.