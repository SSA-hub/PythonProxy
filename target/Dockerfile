FROM python:3.10-slim-buster

WORKDIR /src

COPY src/requirements.txt requirements.txt
COPY src/main.py ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "-m", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "70"]