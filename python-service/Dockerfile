FROM python:3.11

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 50051

ENV NAME World

CMD ["python", "./run.py"]