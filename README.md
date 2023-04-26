# Python Web Server

## Run http server

```shell
python http_server.py # http://0.0.0.0
python http_server.py -h 127.0.0.1 -p 9600 # http://127.0.0.1:9600
python http_server.py -p 10600 # http://0.0.0.0:10600
python http_server.py -h 0.0.0.0 -p 9600 # http://0.0.0.0:9600
```

## Run https server

```shell
python https_server.py # https://0.0.0.0
python https_server.py -p 9600 # https://0.0.0.0:9600
python https_server.py -h 127.0.0.1 # https://127.0.0.1
```
