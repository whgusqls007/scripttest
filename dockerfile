FROM python:3.11

COPY . /

CMD ["python", "./test.py", "--text"]
# "--workers", "5" 멀티스레드