FROM python:3.8
WORKDIR /app
ENV PROCESSES 1
ENV PORT 80
ENV THREAD true
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt && rm requirements.txt
COPY server.py .
COPY wsgi.ini .
EXPOSE ${PORT}
CMD ["uwsgi", "--ini", "/app/wsgi.ini"]

