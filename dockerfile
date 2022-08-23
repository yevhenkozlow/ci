FROM eugene191/flask32

WORKDIR /app

COPY . .

CMD [ "python3", "app.py" ]
