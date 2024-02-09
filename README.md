# Django-Task-Manager

# Clone the repository

git clone <repository-url>

## Create virtual environment

python -m env env

## Active virtual environment

source venv/bin/activate


## Installation dependencies

pip install -r requirements.txt





## Set up environment variables

Create a .env file in the root directory of the project and define the following variables
```
DATABASE_NAME=<database-name>

DATABASE_USER=<database-user>

DATABASE_PASSWORD=<database-password>

DATABASE_HOST=<database-host>

DATABASE_PORT=<database-port>

```

# Run Migrations
python manage.py makemigrations


# Run Migrate
python manage.py migrate



## API Endpoints
Browsable API || Swagger API

## License

[MIT](https://choosealicense.com/licenses/mit/)