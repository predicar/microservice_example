FROM python:3.7
ENV PYTHONPATH .
COPY requirements.txt /
RUN pip install -r /requirements.txt
COPY . server
WORKDIR /server
RUN python -m unittest server/tests/*.py
ENTRYPOINT ["python"]
CMD ["server/app.py"]
