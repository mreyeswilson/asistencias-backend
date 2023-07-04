FROM python:alpine 

WORKDIR /app

COPY ./backend/. .

RUN pip install -r ./app/requirements.txt

EXPOSE 5001

CMD ["python", "-u", "app/init.py"]
