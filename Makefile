# Variables
COMPOSER=docker-compose

.PHONY: build up down restart logs shell \
        migrate makemigrations superuser \
        redis-cli

help:
	@echo "----- Comandos disponibles -----"
	@echo "- Docker -"
	@echo " make status              - Estatus de los contenedores de Docker"
	@echo " make build               - Compilar o crear las imágenes de Docker"
	@echo " make up                  - Levantar y ejecutar las aplicaciones de Docker"
	@echo " make down                - Detener y eliminar los contenedores, redes e imágenes creadas"
	@echo " make logs                - Visualizar la actividad de eventos y errores generados por los contenedores"
	@echo "- Django -"
	@echo " make make-migrations     - Busca cambios en los modelos y genera el archivo de instrucciones"
	@echo " make migrate             - Sincroniza los cambios en los modelos con el esquema de la base de datos (Crear tablas, nuevas columnas, etc)"
	@echo " make superuser           - Crear una cuenta de administrador con todos los permisos"
	@echo " make load-data-countries - Cargar datos a la tabla de Paises"
	@echo "- Redis -"
	@echo " make redis-cli           - Abre la Shell de Redis"


status:
	$(COMPOSE) ps -a

build:
	$(COMPOSER) build

up:
	$(COMPOSER) up -d

down:
	$(COMPOSER) down

logs:
	$(COMPOSER) logs -f

make-migrations:
	$(COMPOSER) exec web python manage.py makemigrations

migrate:
	$(COMPOSER) exec web python manage.py migrate

superuser:
	$(COMPOSER) exec web python manage.py createsuperuser

load-data-countries:
	$(COMPOSER) exec web python manage.py loaddata apps/countries/countries.json

redis-cli:
	$(COMPOSER) exec redis redis-cli