FROM python:3.11-alpine

WORKDIR sturdy_palm_tree

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

CMD ["reflex", "run", "--frontend-port", "3000", "--backend-host", "127.0.0.1", "--backend-port", "8080"]