1. Docker-compose

Загрузить репозиторий:
```
git clone git@github.com:Dbl4/lexicom.git
```
Добавить .env в lexicom/fastapi/

Далее выполнить команды:
```
cd fastapi
docker-compose build
docker-compose up --detach --build
```
Удалить докер-сборку:

```
docker-compose down
```

2. Python
```
git clone git@github.com:Dbl4/lexicom.git
cd fastapi
pip install -r requirements.txt
uvicorn main:app --host localhost --port 8000
```

Перейти в сваггер после запуска можно по адресу: 
http://localhost:8000/api/openap