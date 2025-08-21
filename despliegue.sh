ssh -o StrictHostKeyChecking=no root@$dir_ip <<SSH

cd /home/armando/proyectos/libros-django-app

git pull --rebase origin main

SSH