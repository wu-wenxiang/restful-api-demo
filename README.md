# Rest API Web Service

## 本地调试

```bash
# 创建 python 虚拟环境
python -m virtualenv .venv
# 进入 python 虚拟环境
. .venv/bin/activate

# 安装依赖
pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
# 清理 sqlite 数据库 && 初始化数据库
rm -rf /tmp/rest-demo.db && python datainit.py

# 启动 web 服务
python run.py
# python run.py 0.0.0.0 8080
# 尝试访问
curl http://localhost:8080/
```

## 测试

```bash
# python setup.py test -q
# stestr run
tox
```

## 容器镜像制作和部署

```bash
docker build -t rest-demo .
docker stop rest-demo; docker rm rest-demo
docker run -d --name rest-demo -p 8888:8080 rest-demo
curl http://localhost:8888/
```

## Details

1. [如何搭建一个用于生产的 Restful API 框架？](doc/how-to-build-rest-api-web-service.md)