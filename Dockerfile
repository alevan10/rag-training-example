FROM python:3.12
LABEL authors="levan"

WORKDIR /code

RUN pip install uv

COPY pyproject.toml .
COPY uv.lock .
COPY run_in_cli.py .

EXPOSE 8000

CMD ["uv", "run", "run_in_cli.py"]