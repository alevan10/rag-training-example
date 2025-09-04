from pathlib import Path

from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_community.llms.ollama import Ollama

from langchain.vectorstores import Chroma
from langchain_ollama  import OllamaEmbeddings


DOCUMENT_DIR = Path(__file__).parent.joinpath("documents")


if __name__ == "__main__":
    loader = DirectoryLoader(str(DOCUMENT_DIR), glob="./*.pdf", loader_cls=PyPDFLoader)
    processed_pdf_documents = loader.load()

    vector_store = Chroma.from_documents(documents=processed_pdf_documents, embedding=OllamaEmbeddings(base_url="http://host.docker.internal:7869", model="nomic-embed-text:v1.5"))

    llm = Ollama(base_url="http://host.docker.internal:7869", model="gpt-oss:20b", verbose=True)
    qa_chain = RetrievalQA.from_chain_type(llm, retriever=vector_store.as_retriever())
    result = qa_chain({"query": "Your job is to look for numbers within the provided context. We want to find the largest number anywhere in the provided context. The unit is not important (could be dollars, years, pounds, etc), we're just looking for the greatest numerical value in the document. When the number is found return it, you are required to return it as well as the page number of the document and the surrounding text to help verify the result."})
    print(result["result"])