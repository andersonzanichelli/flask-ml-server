FROM python:3.9

ENV VIRTUAL_ENV=/opt/flaskvenv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ENV FLASK_APP=/app/src/app/server

WORKDIR /app

COPY requirements.txt .

RUN python3 -m venv $VIRTUAL_ENV
RUN pip3 install -r requirements.txt

COPY src ./src

CMD ["flask", "run", "--host", "0.0.0.0"]