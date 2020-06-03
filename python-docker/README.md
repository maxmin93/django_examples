# Docker + Flask + REST API

- 참고: [Flask + REST API + Swagger](https://blog.naver.com/PostView.nhn?blogId=wideeyed&logNo=221571623994&parentCategoryNo=&categoryNo=48&viewDate=&isShowPopularPosts=false&from=postView)

## docker & miniconda3

```
# 최신 미니콘다 이미지를 가져온다
docker pull continuumio/miniconda3

# 9991포트(변경 가능) 오픈&매핑한다. 볼륨(변경 가능)을 연결하고 bash를 실행한다
docker run -it -p 9991:9991 -v /Users/bgmin/Workspaces/python/:/workspace/ continuumio/miniconda3 bash

# apt-get 업데이트한다
apt-get update

# vim 을 설치한다
apt-get install -y vim

# alias ll 추가 (없으면 귀찮아서)
alias ll='ls -alF'

# conda 업데이트한다
conda update -y conda

# flask를 설치한다
conda install -y flask

# pip 업데이트한다
pip install --upgrade pip

# flask-restplus 설치한다
pip install flask-restplus
# ... flask-restplus-0.12.1, aniso8601-7.0.0, attrs-19.1.0 설치됨
# ... jsonschema-3.0.1, pyrsistent-0.15.2, pytz-2019.1 설치됨

# Werkzeug 설치 : cached_property ImportError 때문에 (2020.2)
#   - 참고 https://github.com/jarus/flask-testing/issues/143
pip install Werkzeug==0.16.1

# 소스코드를 작성
cd /workspace/django_examples/python-docker
vim app.py

# flask 실행
FLASK_APP=app.py flask run -h 0.0.0.0 -p 9991
```

Browser open : [http://127.0.0.1:9991/](http://127.0.0.1:9991/)

<img height="420px" src="">
