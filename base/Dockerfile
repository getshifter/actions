FROM python:3.8-alpine
LABEL maintener="sawaonboriyu@higanworks.com"

ENV SHIFTER_USER NOT_PRESENT
ENV SHIFTER_PASS NOT_PRESENT
ENV SHIFTER_SITE_ID NOT_PRESENT
ENV SHIFTER_APP_KEEP false

WORKDIR /srv/src/
COPY src/requirements.txt /srv/src/requirements.txt
RUN pip install -r requirements.txt
COPY src /srv/src

ENTRYPOINT [ "/srv/src/run.py" ]

