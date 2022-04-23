FROM docker.io/library/python:3.9.10-alpine

LABEL purpose="Industrial AI API Server"

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories
RUN apk update && apk add sqlite && apk add build-base && apk add npm && apk add nginx
RUN mkdir -p /home/www/rest_demo
RUN mkdir -p /etc/nginx/conf.d
WORKDIR /home/www/rest_demo
COPY . /home/www/rest_demo
COPY ./start.sh /usr/local/bin/start.sh
COPY ./deploy/nginx.conf /etc/nginx
COPY ./deploy/default.conf /etc/nginx/conf.d

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r /home/www/rest_demo/requirements.txt
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple gunicorn==20.0.0
RUN pip install /home/www/rest_demo
# RUN npm install apidoc -g
# RUN apidoc -i rest_demo/api/controllers -o api-doc
# RUN cp -r /home/www/rest_demo/api-doc/. /usr/share/nginx/html

CMD ["sh", "/usr/local/bin/start.sh"]
