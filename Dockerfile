FROM ubuntu:16.04

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y \
    python3 python3-pip python3-dev  \
    nginx libmysqlclient-dev supervisor virtualenv
COPY nginx/flask.conf /etc/nginx/sites-available/
COPY supervisor/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY .  /var/www/app




RUN mkdir -p /var/log/nginx/app /var/log/uwsgi/app /var/log/supervisor \
    && rm /etc/nginx/sites-enabled/default \
    && ln -s /etc/nginx/sites-available/flask.conf /etc/nginx/sites-enabled/flask.conf \
    && echo "daemon off;" >> /etc/nginx/nginx.conf \
    && chown -R www-data:www-data /var/www/app \
    && chown -R www-data:www-data /var/log
RUN cd /var/www/app \
    && virtualenv -p /usr/bin/python3.5 venv \
    && /bin/bash -c "source venv/bin/activate && pip3 install -r /var/www/app/requirements.txt -i http://pypi.douban.com/simple --trusted-host=pypi.douban.com && deactivate"

#RUN pip3 install virtualenv \
#    && virtualenv venv -p /usr/bin/python2.7


CMD ["/usr/bin/supervisord"]