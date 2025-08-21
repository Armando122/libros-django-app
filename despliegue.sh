ssh -o StrictHostKeyChecking=no root@$IP_SERVIDOR <<SSH

cd /home/armando/proyectos/libros-django-app

git pull --rebase origin main

SSH