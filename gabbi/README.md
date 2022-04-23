# Gabbi 接口测试

## 1. 准备

```bash
pip3 install gabbi
```

## 2. 运行

```bash
ls *.yaml | xargs gabbi-run localhost:8080 --

# show verbose
gabbi-run -v all localhost:8080 -- crud-user.yaml
```
