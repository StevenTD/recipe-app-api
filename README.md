# recipe-app-api
Recipe API Project

To run as development
```
docker compose up
```

Tun as deployment
```
docker compose -f docker-compose-deploy.yml up -d
```

To access Admin go to:
```
http://localhost:8000/admin
or
http://localhost:8000
```

To access Swagger API go to:
```
/api/docs/
```

If used in blank database this will generate a new user with following creds.
```
email: admin1@example.com
password: admin
```
To run test:
```
python manage.py test
```
To run lint:
```
flake8
```
Notes:
Installing Psycopg2, dependencies

Acc. to doc:
    * C compiler
    * python3-dev
    * libpq-dev

Equivalent for Alpine
    * postgresql-client
    * build-base
    * postgresql-dev
    * musl-dev

Docker best practice
    * Clean-up dependencies