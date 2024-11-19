FROM python:alpine

WORKDIR /app

COPY ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

COPY ./src .

EXPOSE 3000

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3000", "--workers", "4"]