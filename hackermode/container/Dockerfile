FROM ubuntu

RUN apt-get update \
    && apt-get install python3 -y \
    && apt install -y python3-pip \
    && pip3 install pymysql

RUN apt-get install cron bc -y

RUN mkdir /scripts /app

COPY server.py client.py /app/

COPY scripts /scripts

WORKDIR /scripts/

RUN bash /scripts/initialsetup.sh

ENTRYPOINT ["/scripts/serverstart.sh"]

