Blog Backend Django

| Method | Endpoint                  | Function                                 | Header/Body Example                                                       |
|--------|---------------------------|------------------------------------------|---------------------------------------------------------------------------|
| GET    | /api/blog                 | Return all blog posts                    | n/a                                                                       |
| GET    | /api/blog/featured        | Return featured                          | n/a                                                                       |
| GET    | /api/blog/asdasdasd       | Return individual article based on slug  | n/a                                                                       |
| POST   | /api/blog/category        | Return all blogs of a category           | Content-Type: application/json { "category": "BUSINESS" }                 |
| POST   | /api/blog/categorychapter | Return all blogs of a category & Chapter | Content-Type: application/json { "category": "BUSINESS", "chapter": "5" } |