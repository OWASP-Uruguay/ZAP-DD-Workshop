# ZAP-DD-Workshop

Repository for [OWASP Uruguay](https://owasp.org/uruguay) Meetup: [ZAP and Defect Dojo Workshop]((https://www.meetup.com/es/OWASP-Uruguay-Chapter/events/272569351/))

Repositorio para el Meetup organizado por [OWASP Uruguay](https://owasp.org/uruguay): [Workshop ZAP y Defect Dojo](https://www.meetup.com/es/OWASP-Uruguay-Chapter/events/272569351/)

## Introducción
En este workshop aprenderemos acerca de estos dos proyectos Flagships de OWASP. Además, para probar ZAP utilizaremos otro proyecto Flagship de OWASP, OWASP Juice Shop.

Link a la presentación [aquí](https://docs.google.com/presentation/d/1qhvtCQTBHwQQ9NS7_VQZh8r67kC4DyQZCpTHqA7sy2w/edit?usp=sharing)

## ZAP

### ZAP - Demo GUI
Para levantar el ambiente ejecutar el comando "docker-compose up -d" en la raíz del repositorio.

Para abrir la GUI de ZAP: acceder a http://localhost:8080/zap/

Descargar certificado: Tools -> Options -> Dynamic SSL Certificate -> Save (instalarlo en el navegador de preferencia)
* Chromium: https://www.xataka.com/basics/como-importar-exportar-certificado-digital-chrome
* Firefox:  https://www.xataka.com/basics/como-importar-exportar-certificado-digital-firefox

Acceder a juice-shop http://localhost:3000

Acceder a webgoat http://localhost:8888
## DD
<!--
Para probar Defect Dojo puede hacerlo de alguna de las dos maneras a continuación:
### Demo Online
Ingresar al [ambiente de test](https://defectdojo.herokuapp.com/) con las siguiente crerdenciales.
* admin / defectdojo@demo#appsec
* product_manager / defectdojo@demo#product
-->
### Inicio rápido local
```sh
git clone https://github.com/DefectDojo/django-DefectDojo
cd django-DefectDojo
# Buildear
docker-compose build
# Correr
docker-compose up -d
```

Navegar a <http://localhost:8080> (esperar un rato que levante o si aparece un error refrescar hasta que termine de levantar todo).

Ejecutar el siguente comando para averiguar la contraseña del ususuario admin:
docker-compose logs initializer | grep "Admin password:" 

### Creando un nuevo usuario administrador

Puede pasar, sobre todo al hacer pruebas, que el password de admin se les olvide.
Esta es una forma simple de crear un nuevo usuario con privilegios.

```bash
❯ docker-compose exec uwsgi /bin/bash -c 'python manage.py createsuperuser'
enabling audit logging
patching TagDescriptor
Popen(['git', 'version'], cwd=/app, universal_newlines=False, shell=None, istream=None)
Popen(['git', 'version'], cwd=/app, universal_newlines=False, shell=None, istream=None)
Username: fzipi
Email address: felipe.zipitria@owasp.org
Password:
Password (again):
Superuser created successfully.
```

### Términos usados en DD

Estos son los términos básicos que se usan en DefectDojo, que van a ser útiles a medida que se trabaja con el.

#### `Products` (productos)

Este es el nombre de cualquier proyecto, programa, equipo, o empresa que se está testeando.

Ejemplos:
-  Wordpress
-  Wiki Interno
-  Slack

#### `Product types` (tipos de producto)

Pueden ser unidades de negocio, oficinas o lugares distintos, o cualquier cosa que sirva para distinguir lógicamente los "tipos" de productos.

Ejemplos:
-  Internal / 3rd party
-  Main company / Acquisition
-  San Francisco / New York offices

#### `Engagement` (interacciones/contratos)

Son momentos en el tiempo en los que el test se realiza. Se asocian a un nombre para fácil referencia, un plazo de tiempo, un líder, una estrategia de test y un estatus.

Ejemplos:
-  Beta
-  Quarterly PCI Scan
-  Release Version X

#### `Test Types` (tipos de tests)

Características del tipo de test que se hizo durante la interacción.

Ejemplos:
-  Funcional
-  Seguridad
-  Nessus Scan
-  API test

#### `Environments` (entornos)

El entorno que fue testeado durante la interacción.

Ejemplos:
-  Producción
-  PreProd
-  Desarrollo


## Links de interés
### OWASP ZAP (Zed Attack Proxy)
- Project URL: https://www.zaproxy.org/
- Docker (stable version): https://hub.docker.com/r/owasp/zap2docker-stable/

### OWASP DefectDojo
- Project URL: https://owasp.org/defectdojo

### OWASP Juice Shop
- Project URL: https://owasp.org/juice-shop
- Docker: https://hub.docker.com/r/bkimminich/juice-shop

### OWASP Webgoat
- Project URL: https://owasp.org/www-project-webgoat/
- Docker: https://hub.docker.com/r/webgoat/webgoat-8.0/

### All OWASP Projects
- URL: https://owasp.org/projects/
