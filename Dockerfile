FROM python:3.8

RUN pip install Flask

COPY app.py /app.py

WORKDIR /

ENV FLASK_APP=/app.py

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]