# django-channels tutorial

[Official Tutorial](https://channels.readthedocs.io/en/latest/tutorial/part_1.html)

--------------

## python manage.py shell 인터페이스 선택

```
python manage.py shell -i ipython       # default
python manage.py shell -i python        # interactive console
```


## pull and run redis image by docker

```
$ docker pull redis:5.0.3

$ docker images

$ docker run --name myredis -d -p 6379:6379 redis:5

## redis running process 조회
$ docker ps -a
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
4815f5ad0425        redis:5             "docker-entrypoint.s…"   12 minutes ago      Up 12 minutes       0.0.0.0:6379->6379/tcp   myredis

## redis-cli 접속해보기 (docker 중지시 자동 삭제 옵션)
$ docker run -it --link myredis:redis --rm redis redis-cli -h redis -p 6379

redis:6379> set key value
OK
redis:6379> get key
"value"
redis:6379> exit

## local 에 redis 설치 되어 있으면 직접 접속
$ redis-cli -p 6379
127.0.0.1:6379>

$ docker kill myredis

$ docker rm myredis

```

## install ChromDriver for selenium test

```
brew cask install chromedriver

## 보안 때문에 'Mac>설정>보안' 들어가서 개발자 확인없이 사용 확인을 해주어야 함
chromedriver --version
=> ChromeDriver 83.0.4103.39
```