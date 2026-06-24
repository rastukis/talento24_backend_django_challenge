# Prueba Técnica para Talento24 - Backend

> Backend para administrar usuarios 


---

## Características

- Endpoint para registrar un usuario
  - Validación de datos
  - Guardado en DB
- Endpoint para obtener usuarios
  - Filtrar por país
  - Buscar por nombre o email


---

## Requisitos

Antes de comenzar asegúrate de tener instalado:

- make
- docker
- python

Verificar instalación:

```shell
make --version
```

```shell
docker --version
```

```shell
python --version
```

---

## Instalación y uso

1. Clona el repositorio:

```shell
git clone git@github.com:rastukis/talento24_backend_django_challenge.git .
```

2. Construye los contenedores e imágenes:

```shell
make build
```

3. Actualiza el archivo `.env`


4. Levantar y ejecutar las aplicaciones de Docker

```shell
make up
```

5. Sincroniza los cambios en los modelos con la Base de datos

```shell
make migrate
```

6. Cargar los datos de Países

```shell
make load-data-countries
```

7. Crear un Usuario para Login (sigue las instrucciones que se te piden)

```shell
make superuser
```

---

## Help

Muestra la lista de comandos disponibles

```shell
make help
```

