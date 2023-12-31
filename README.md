# WEBSITE TESTS FRAMEWORK

## Installation requirements

* [Docker + Docker Compose](https://www.docker.com/) >= v24.0.4.

## Framework installation guide

  - Clone this repository (or download the source code);
  - Copy .env file from .env.template and change the project configurations;
  - Launch `docker compose up`: this will create the images and start the containers;
  - Wait for all the services to start, then browse your domain to use the app. 

## ENV VARIABLES

The most important environment configurations to set are:
  - DOMAIN: modify it with the domain you want to use;
  - Change all "your-project-name" strings with the name you want to give to your project;
  - Change all logins settings: modify all "admin" with your username and password for all the services.


### COMPONENTS

* TRAEFIK (Proxy)
* FRONTEND (ReactJS)
* BACKEND (Python FastAPI)
* CELERY WORKER(S)
* REDIS (CELERY BROKER/DB)
* DB (POSTGRESQL)
* FLOWER (CELERY GUI) - Optional

### [DEVELOPMENT GUIDE](docs/DEV.md)

