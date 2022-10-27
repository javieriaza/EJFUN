FROM python:3.10.7
COPY ./ejercicio.py /app/
COPY ./docker.txt /app/

WORKDIR /app/
RUN mkdir General
RUN mkdir Homer
RUN mkdir Lisa
RUN pip3 install -r ./docker.txt 

CMD ["python","ejercicio.py"]