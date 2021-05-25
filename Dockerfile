FROM python:3.7

RUN pip install virtualenv
ENV VIRTUAL_ENV = /venv
RUN virtualenv venv -p python3
ENV PATH = "$VIRTUAL_ENV/bin:$PATH"

WORKDIR /California_Housing
ADD . /California_Housing

#Install Dependencies
RUN pip install -r requirements.txt

#Run the Application
CMD ["python","app.py"]
