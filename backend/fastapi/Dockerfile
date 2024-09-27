FROM minh171532/backend:v1 

WORKDIR /usr/src/app

RUN rm -rf *

RUN pip install python-multipart

RUN pip install pika

COPY ./app ./backend/app

COPY ./.env ./backend/.env

COPY ./setup.py ./backend/setup.py

COPY ./config.py ./backend/config.py

COPY ./main.py ./backend/main.py

# COPY ./producer.py ./bakend/producer.py

CMD ["sh", "-c", "cd backend && python3 main.py"]