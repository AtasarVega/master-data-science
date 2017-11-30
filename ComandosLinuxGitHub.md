# Primeros pasos con linux y GitHub

### ls 
Da información del contenido del directorio actual. 
### cd Data
Vamos al directorio Data
### cd ..
Vuelve al directorio anterior
### pwd
Nos dice el directorio actual
### git 
Nos da información acerca del uso del github
### git clone https://github.com/AtasarVega/master-data-science.git
Para clonar nuestro trabajo de github en la consola
### kwrite .gitconfig
Abre el editor de texto para poner nuestro usuario del github 
### cat README.md
Muestra el contenido del archivo .md
### kwrite README.md
Abre el archivo en un editor de texto
### git status 
Muestra el estado del archivo, si está actualizado y listo para subir o necesitamos confirmar los cambios
### git add README.md
Prepara la versión del archivo para subir los cambios. 
### git commit -m "Poner un mensaje" 
Confirma los cambios 
### git push 
Sube el archivo a github con los cambios realizados. 
### git log 
Enumera el historial de cambios de archivos que hay en el directorio
### git pull
Descarga los archivos de github con los cambios que hayan tenido 
### whoami 
Nombre de usuario 
### echo "Welcome"
Devuelve lo que escribimos entre comillas: Welcome
### cat /etc/os-release
Muestra el nombre y la versión del sistema operativo. 
### cat Data/shell/Text_example.txt
Muestra el contenido del archivo
### cat -n ~/Data/shell/Text_example.txt
Muestra el contenido del archivo enumerando cada línea
### ls -a 
Muestra todo el contenido del directorio, incluido archivos y directorios ocultos
### ls -1
Muestra los directorios en columna
### ls -s 
Muestra los directorios con el tamaño que tiene cada uno. 
### history
Muestra el historial de comandos utilizados
### ls -l 
Muestra los directorios con los permisos que tiene cada uno
### type ll 
Nos dice que es un alias 
### alias gs= "git status"
Creamos un alias llamado gs para git status
### cd ~Repositories/data-science-toolbox
Cambia el directorio 
### chmod 777 README.md
Da permisos de leer, escribir y ejecutar
### chmod u+g,g-x,o-x
Cambia los permisos para usuarios, grupos y otros.
### chmod 600 README.md
Da permisos de leer y ejecutar
### ll README.md
Muestra el tipo de permisos que tiene el archivo
### mkdir my_dir
crea el directorio my_dir
### mkdir -p my_dir/ata/first_class
crea los directorios ata y first_class. HAY QUE PONER -p
### touch my_dir/first_file.txt
crea el archivo first_file.txt
### cp first_file.txt second_file.txt
copia el archivo y le cambia el nombre a second_file.txt
### cp -r ata ata2
copia el directorio y le cambia el nombre a ata2








