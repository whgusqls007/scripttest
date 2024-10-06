FROM python:3.11

COPY . /

CMD ["bash"]
# "--workers", "5" 멀티스레드