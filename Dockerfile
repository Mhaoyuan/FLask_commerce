FROM python:3.5
ADD . /Flask-Commerce
WORKDIR /Flask-Commerce
RUN pip install --trusted-host pypi.python.org -r requirements.txt
EXPOSE 5000
ENV NAME world
CMD ["python", "manage.py","runserver"]
