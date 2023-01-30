## 使用`minio`搭建文件储存服务器

##### windows端下载地址

```txt
https://dl.min.io/server/minio/release/windows-amd64/minio.exe
https://dl.min.io/client/mc/release/windows-amd64/mc.exe (mc)
```

##### 启动server服务

```properties
# 在minio.exe
.\minio.exe server D:\ftp\data 
```

##### 输出获取账号密码等密匙

```txt
Endpoint:  http://169.254.215.181:9000  http://169.254.120.145:9000  http://172.18.4.113:9000  http://169.254.6.96:9000  http://192.168.190.38:9000  http://127.0.0.1:9000
AccessKey: minioadmin
SecretKey: minioadmin

Browser Access:
   http://169.254.215.181:9000  http://169.254.120.145:9000  http://172.18.4.113:9000  http://169.254.6.96:9000  http://192.168.190.38:9000  http://127.0.0.1:9000

Command-line Access: https://docs.min.io/docs/minio-client-quickstart-guide
   $ mc.exe alias set myminio http://169.254.215.181:9000 minioadmin minioadmin

Object API (Amazon S3 compatible):
   Go:         https://docs.min.io/docs/golang-client-quickstart-guide
   Java:       https://docs.min.io/docs/java-client-quickstart-guide
   Python:     https://docs.min.io/docs/python-client-quickstart-guide
   JavaScript: https://docs.min.io/docs/javascript-client-quickstart-guide
   .NET:       https://docs.min.io/docs/dotnet-client-quickstart-guide
Detected default credentials 'minioadmin:minioadmin', please change the credentials immediately using 'MINIO_ACCESS_KEY' and 'MINIO_SECRET_KEY'
```

##### 进入浏览器访问

```txt
http://127.0.0.1:9000/minio/login
```

##### 储存桶的命名规则

储存桶名称的必须唯一

### 开放桶设置为永久下载

mc.exe连接服务

```properties
mc config host add minio http://localhost:9000 key password --api s3v4
```

设置桶为永久下载

```properties
mc policy set public minio/test
```

