Blog Backend Django

| Method | Endpoint                  | Function                                 | Header/Body Example                                                       |
|--------|---------------------------|------------------------------------------|---------------------------------------------------------------------------|
| GET    | /api/blog                 | Return all blog posts                    | n/a                                                                       |
| GET    | /api/blog/featured        | Return featured                          | n/a                                                                       |
| GET    | /api/blog/asdasdasd       | Return individual article based on slug  | n/a                                                                       |
| POST   | /api/blog/category        | Return all blogs of a category           | Content-Type: application/json { "category": "BUSINESS" }                 |
| POST   | /api/blog/categorychapter | Return all blogs of a category & Chapter | Content-Type: application/json { "category": "BUSINESS", "chapter": "5" } |


| Method | Endpoint          | Function                       | Header/Body Example                                                                                                                   |
|--------|-------------------|--------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| GET    | /api/contact      | Return all contact submissions | n/a                                                                                                                                   |
| POST   | /api/contact/post | Post a contact submission      | Content-Type: application/json { "name": "Another one shav", "email": "shavw2@email.com", "content": "First post Test without date" } |

$ docker build -t web:latest .
$ docker run --name web -d -p 8000:8000 web:latest

Delete all containers  && Delete all volumes

$ docker rm -f $(docker ps -a -q) && docker volume ls -qf dangling=true | xargs -r docker volume rm
