FROM python:alpine3.7
COPY . /app
WORKDIR /app
COPY ./numbers.csv .
RUN pip install -r ./env/requirements.txt
EXPOSE 5000
CMD python ./env/flask_app.py
