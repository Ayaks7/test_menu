# test_menu

Запуск:<br/>
docker-compose -f docker-compose.dev.yml build<br/>
docker-compose -f docker-compose.dev.yml up -d<br/>

Вывод всех блюд:<br/>
***curl -H "Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b" http://0.0.0.0:8000/api/dishes/***

Добавление нового:<br/>
***curl --dump-header - -H "Content-Type: multipart/form-data" -H "Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b" -X POST -F "image=@image.png" -F "name=" -F "price=" -F "calorie_content=" http://0.0.0.0:8000/api/dishes/***
