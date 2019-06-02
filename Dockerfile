FROM python:2.7-slim

WORKDIR /app

COPY . .

EXPOSE 50

RUN pip install --trusted-host pypi.python.org -r requirements.txt

CMD ["python", "app.py"]