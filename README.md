# Restful API Web Service

该项目用于 Demo 如何搭建一个生产可用的 Restful API 服务

## 1. 代码规范

项目测试接口：<https://governance.openstack.org/tc/reference/pti/python.html>

1. 单元测试：`stestr` & `pytest` / `unittest`
2. 代码风格检查：`tox -e pep8`
3. 覆盖率测试报告：`coverage` / `tox -e cover`
4. 源码包生成：`python setup.py sdist` / `python setup.py bdist_wheel`
5.  国际化：`babel`
6. 文档生成：`sphinx-build`
7. 自动格式化代码风格 `pylint`
8. API 接口文档：`API Doc` / `Swagger`

## 2. CI/CD

1. 容器镜像：`Dockerfile`
2. `.drone` 自动打包 / 部署
3. 数据初始化 `datainit.py`
4. 自动化接口测试 `gabbi`

开发流程规范化：

1. 先用户故事，前后端对齐
2. 数据库 + API，提交通过
3. YAML 测试用例提交通过
4. 最后代码实现

## 3. ORM

1. SqlAlchemy：`Session Hook` / `Transaction` / `Relationship`
2. 支持 Sqlite3 做测试，MySQL 上生产
3. 数据库三范式，三表法
4. 级联删除

## 4. 认证、鉴权和准入

1. 认证：本地认证和 OAUTH2
2. 鉴权：Casbin
3. 准入：API 计量，API Gateway，Kong

## 5. 框架数据处理

1. API URL 定制化
2. 输入校验
3. 后端分页、排序、筛选框架
