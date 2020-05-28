FROM python:3.8-slim

WORKDIR /tmp
COPY . .
RUN pip install -U .

ENTRYPOINT ["pma"]
CMD ["--help"]
