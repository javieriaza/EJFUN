FROM python:3.10.7
COPY ./lisa.py /app/
COPY ./requirements.txt /app/

WORKDIR /app/
RUN pip3 install -r ./requirements.txt 

CMD ["python","lisa.py"]