## **Text matching**
- Technologies: Python, Django, Postgres, Redis, Docker, Docker Compose
- Matching based on levenshtein distance https://en.wikipedia.org/wiki/Levenshtein_distance
- Throttling applied 5/m
- ![alt text](./dummy_data/screen.png)
## Setup
1) Install docker desktop https://www.docker.com/products/docker-desktop/
2) Build the docker containers by running `docker-compose build`
3) Run the container by running `docker-compose up`
4) Run the migrations by running `docker-compose exec web python manage.py migrate`
5) Import the data by running `docker-compose exec web python manage.py import_data`
6) Run the container by running `docker-compose up`
7) The Project will be up and running on `http://localhost:8000`

## Pre-commit
1) create a python3 virtual-env and activate it.
2) Run pip install pre-commit and install in via `pre-commit install`
3) Now it will execute when you commit the code and run in manually by `pre-commit run`
