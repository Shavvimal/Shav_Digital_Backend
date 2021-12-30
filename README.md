# Blog Backend Django

## Blog

| Method | Endpoint            | Function                                | Header/Body Example                                          |
| ------ | ------------------- | --------------------------------------- | ------------------------------------------------------------ |
| GET    | /api/blog           | Return all blog posts                   | n/a                                                          |
| GET    | /api/blog/asdasdasd | Return individual article based on slug | n/a                                                          |
| POST   | /api/blog/post      | Post a list of blogs                    | Content-Type: application/json { "category": "BUSINESS" } [{ |

        "category": "Stocks",
        "chapter": 1,
        "chapter_title": "Introduction",
        "sub_chapter": 20,
        "title": "What is this all about?",
        "excerpt": "Stocks outperform things like bonds and cash and other asset categories so they're a great way to grow your money",
        "month": "12",
        "day": "27",
        "content": "insert here"

},
{
"category": "Stocks",
"chapter": 1,
"chapter_title": "Introduction",
"sub_chapter": 20,
"title": "What is this all about?",
"excerpt": "Stocks outperform things like bonds and cash and other asset categories so they're a great way to grow your money",
"month": "12",
"day": "27",
"content": "insert here"
}]
|
| POST | /api/blog/category | Return all blogs of a category | Content-Type: application/json { "category": "BUSINESS" } |
| POST | /api/blog/categorychapter | Return all blogs of a category & Chapter | Content-Type: application/json { "category": "BUSINESS", "chapter": "5" } |

## Contact

| Method | Endpoint          | Function                       | Header/Body Example                                                                                                                   |
| ------ | ----------------- | ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| GET    | /api/contact      | Return all contact submissions | n/a                                                                                                                                   |
| POST   | /api/contact/post | Post a contact submission      | Content-Type: application/json { "name": "Another one shav", "email": "shavw2@email.com", "content": "First post Test without date" } |

## Commands Django

python manage.py makemigrations
python manage.py migrate
python manage.py runserver

## Commands Docker

$ docker build -t web:latest .
$ docker run -d --name django-backend -e "PORT=8000" -e "DEBUG=1" -p 8000:8000 web:latest
$ docker exec -it web bash
$ docker exec -it django-backend //bin//sh

Delete all containers && Delete all volumes

$ docker rm -f $(docker ps -a -q) && docker volume ls -qf dangling=true | xargs -r docker volume rm

# Heroku Commands

$ heroku login
$ heroku container:login
$ heroku create shavbackend
$ heroku container:push web --app shavbackend2
$ heroku container:release web --app shavbackend2
$ heroku open -a shavbackend

$ heroku login
$ heroku container:login
$ heroku create shavbackend
$ heroku config:set SECRET_KEY=85AFCF4859ED7BC4B992B27C12D1DB688DB4DE3631C2B4DA576FE13372 -a shavbackend
$ docker build -t registry.heroku.com/shavbackend/web .
$ docker push registry.heroku.com/shavbackend/web
$ heroku container:release -a shavbackend web
$ heroku open -a shavbackend

docker build -t registry.heroku.com/shavbackend/web . && docker push registry.heroku.com/shavbackend/web && heroku container:release -a shavbackend web && heroku open -a shavbackend

Destroy:
$ heroku apps:destroy

# Heroku CLI Docker exec

$ Heroku features:enable runtime-heroku-exec
heroku ps
heroku ps:exec --dyno=web.1

https://testdriven.io/blog/deploying-django-to-heroku-with-docker/

condaon && conda activate django && python manage.py runserver
