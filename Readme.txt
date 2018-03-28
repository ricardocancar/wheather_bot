#####################################################################################
este documento es una guia de instalacion para realizar el seminario.
En el cual están los pasos para realizar la instalacion de dos librerias de python
python-telegram-bot y pymongo.
Así como la instalacion de el sistema de base de datos Mongodb.

#####################################################################################
guía para realizar la instalación de mongodb-communit edition
https://docs.mongodb.com/manual/administration/install-community/


#####instalar libreria python-telegram-bot

se realiza un git clone del repositorio de git hub
$ git clone https://github.com/python-telegram-bot/python-telegram-bot --recursive
nos dirigimos a la carpeta donde se encuentra el setpu.py
$ cd python-telegram-bot
ejecutamos el siguiente comando para realizar la configuracion de la libreria.
$ python setup.py install

##### instalar libreria pymongo
http://api.mongodb.com/python/current/installation.html
se clona el repositorio de pymongo mediante un git clone
$ git clone git://github.com/mongodb/mongo-python-driver.git pymongo
nos dirigimos a la carpta donde se encuentra el setup.py
$ cd pymongo/
ejecutamos el siguiente comando para realizar la configuracion de la libreria
$ python setup.py install
