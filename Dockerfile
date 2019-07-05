FROM python:3.7

WORKDIR /tmp
COPY . .
RUN pip install -U .
WORKDIR /app
CMD ["python"]