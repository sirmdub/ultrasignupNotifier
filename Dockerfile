FROM python:2-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . /usr/src/app
RUN chmod +x *.py
RUN pip install -r requirements.txt -t .

RUN apk add --no-cache --virtual zip
RUN zip -r ultrasignupNotifier.zip . -x *.git*

ENTRYPOINT [ "python" ]
CMD [ "./run.py" ]
