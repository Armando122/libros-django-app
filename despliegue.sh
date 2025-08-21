ssh -o StrictHostKeyChecking=no root@$dir_ip <<SSH

su - armando

cd /home/armando/proyectos/libros-django-app

git pull --rebase origin main

SSH