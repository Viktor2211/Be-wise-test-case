
# В корне проекта создать файл .env со следующими данными
'''
## Database
DB_HOST=db  
DB_PORT=5432  
DB_USER=db_user  
DB_PASSWORD=db_password  
DB_NAME=db_name  

## Web
WEB_INTERNAL_PORT=8000  
WEB_EXTERNAL_PORT=8000  
'''

## Для запуска проекта, находясь к корне проекта прописать команду
docker-compose up -d --build  


## Документация API по адресу http://127.0.0.1:8000/docs
'''  
method: POST  
endpoint: 127.0.0.1:8000/questions  
body: {'questions_num': integer}  
'''