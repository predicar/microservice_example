FROM python:3.7
ENV PYTHONPATH .
COPY . /server
WORKDIR /server
RUN pip install -r requirements.txt
RUN python -m unittest server/tests/*.py
ENTRYPOINT ["python"]
CMD ["server/app.py"]
