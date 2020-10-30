```
# 进入容器内部:
docker exec -it mymysql /bin/bash

# 连接mysql
mysql -uroot -pTristan123

# 修改访问设置
ALTER USER 'laashub'@'%' IDENTIFIED WITH mysql_native_password BY 'tristan123';

# 刷新权限
FLUSH PRIVILEGES;
```