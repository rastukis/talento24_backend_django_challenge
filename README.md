# talento24_backend_django_challenge

```shell
curl -X POST http://localhost:8000/api/v1/users/ \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: req-001" \
  -d '{
    "first_name": "Nombre",
    "last_name": "Apellido",
    "email": "correo@test.com",
    "age": 25,
    "country": 1
}'
```