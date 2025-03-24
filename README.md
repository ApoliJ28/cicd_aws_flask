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
## 5. Ingresar a la carpeta opt y clonar el proyecto y además otogar permiso al usuario ubuntu al directorio del proyecto.
```
sudo git clone "ruta de el repositorio a clonar"
sudo chown -R ubuntu:ubuntu /nombre_de_la_ruta_de_tu_proyecto
```
## 6. El siguiente paso es crear la credencial de acceso rsa para el github actions, abajo el código y adicional guarda la key.
```
ssh-keygen -t rsa -b 4096 -C "nombre de tú proyecto"
```
- Ahora como se genero la llae ssh rsa
```
cat /home/ubuntu/.ssh/id_rsa.pub >> /home/ubuntu/.ssh/authorized_keys
```
Agregas la nueva llave a las llaves authorizadas del server para que cuando hagamos la integracion con git actions se pueda conectar al server sin problemas.
## 7. Dentro del directorio del proyecto crear un entorno virtual y descargar las dependencias:
```
python3 -m venv venv
source venv/bin/actívate
sudo venv/bin/python3 -m pip install -r requirements.txt
```
## 8. Crear un servicio para la ejecución del servidor en la ruta: /etc/systemd/system/nombre-del-servicio.service con nano en modo super usuario.
```
[Unit]
Description=Nombre de tú Servicio Aquí
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/opt/nombre_del_directorio_de_tu_proyecto
Environment="PATH=/opt/nombre_del_directorio_de_tu_proyecto/venv/bin:/usr/bin"
ExecStart=/opt/nombre_del_directorio_de_tu_proyecto/venv/bin/python3 /opt/nombre_del_directorio_de_tu_proyecto/app.py
Restart=always

[Install]
WantedBy=multi-user.target
```
##9. Recargar los servicios para que linux reconozca el nuevo servicio antes creado:
```
sudo systemctl daemon-reload
sudo systemctl start my-flask-app.service 
```
##10. ir a github y crear las credenciales:
- EC2_PRIVATE_KEY = pega la key generada del rsa
- EC2_HOST = dirección pública de la instancia de ec2
- EC2_USER_NAME = al ser ubuntu el usuario se llama igual: ubuntu
