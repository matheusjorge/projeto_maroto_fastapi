FROM python:3.8

WORKDIR /projeto_maroto

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "model_api:app", "--host", "0.0.0.0"]