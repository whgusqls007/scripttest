FROM python:3.11

COPY . /

ENTRYPOINT ["python", "./test.py"]
CMD ["--text", "HELLO WORLD!"]
# "--workers", "5" 멀티스레드