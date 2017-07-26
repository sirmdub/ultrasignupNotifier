FROM python:2-alpine

RUN apk add --no-cache --virtual zip

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app
RUN pip install -r requirements.txt -t .

COPY . /usr/src/app
RUN chmod +x *.py

RUN zip -r ultrasignupNotifier.zip . -x *.git* *tests\/*

ENTRYPOINT [ "python" ]
CMD [ "./run.py" ]
