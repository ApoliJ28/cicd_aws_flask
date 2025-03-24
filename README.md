# cicd_aws_flask - Victor Apolinares
Proyecto Final - Social Oplesk

## 1. Ir a la consola de aws y crear un servidor ec2 con ubuntu:
- Lanzar una instancia en Ubuntu
- Crear par de llaves, rsa en formato .pem para ssh y guardar el archivo .pem que te delvuelve AWS
## 2. Ingresar con Putty key Generator
- Cargar el archivo .pem
- Generar la llave privada (RSA) y te devuelve un .ppk
## 3. Ingresas con Putty a la instancia creada por ssh
- Colocar el host name de la instalcia "Dirección IPv4 pública".
- Asegurar que en el grupo se seguridad este libre el puerto 22 para ingresar por ssh
- Desde la app de Putty ir a la parte de SSH -> AUTH -> CREDENTIALS y ahi cargar la llave privada que generaraste con Putty key Generator.
- Verificar el usuario que se creo la instancia aunque por defecto es "ubuntu" si se crea la instancia de ubuntu.
## 4. Ingresar a la instancia de ubuntu anteriormente creada y hacer lo siguiente:
```
sudo apt update
sudo apt install python3
sudo apt install python3-pip
sudo apt install python3.12-venv`
```
## 5. Ingresar a la carpeta opt y clonar el proyecto.
