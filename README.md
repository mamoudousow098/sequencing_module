# digital_sequencing_platform

## Table of Contents
- [sequencing_module](#sequencing_module)
  - [Table of Contents](#table-of-contents)
  - [General Info](#general-info)
    - [1.Contextualization of the project](#1contextualization-of-the-project)
    - [2.Presentation of the project](#2presentation-of-the-project)
      - [2.1 configuration of ftp protocol](#21-configuration-of-ftp-protocol)
    - [Screenshot](#screenshot)
  - [Technologies](#technologies)
  - [Installation](#installation)
    - [1. A little intro about the installation.](#1-a-little-intro-about-the-installation)
    - [2.Side information:](#2side-information)
  - [FAQs](#faqs)
    - [1. **general documentation**](#1-general-documentation)
    - [2. Contact the developers](#2-contact-the-developers)


## General Info
***
### 1.Contextualization of the project
The Institute Pasteur has positioned itself as a hub in the field of sequencing and genomic monitoring in Africa. Many steps in this part are still manual (moving data on hard disk, freeing memory on the server)

### 2.Presentation of the project
The project consists in having a platform or a sequencing module that allows to overcome the problem linked to the sequencing process, i.e the sending of data after an action has been taken and to access and view data in real time on the platform
To do this, the project has a few objectives, which are :
* have a listener to notify if a run is finished.
* retrieve the metadata and the .fasta file
* give a description analysis on the trends(pathogen/variant) link with the teranga sample base for more exhaustive data (epidemio, clinical, data)

our project has 3 stages :
* for the first stage, we have to configure a ftp protocol for the sequencers in the virology lab and trying to automate the sending process when the run is finished
* next stage: for this stage, we are going to receive and manage files and data received from the virology lab(sequencers) and this step we are going to process and analyze the file with extension fasta
* the third and last stage: in this step: we develop a platform that can show us the descriptive analysis and manage files and data hosted on the server 

#### 2.1 configuration of ftp protocol
first of we need to create a user on the machine(sequencers) for the ftp protocol and we use that user to connect on the ftp server and retrieve data from the sequencers provided by the run executed.
for the configuration we have some tutoriel of [how to create a user on windows machine](https://techozu.com/how-to-create-a-local-account-on-windows-10/) because the sequencers'system is windows platform
after that we are going to going to setup a software named [xlight ftp server](https://www.xlightftpd.com/download.htm) with enabling on the windows defender the ability to open the 21 port with the the xlight ftp server and allow inbound trafic


### Screenshot
* screenshot 1
![swagger documentation 1](./sequencing_module_api/static/docs_for_readme/images/s_module_1.png)

* screenshot 2
![swagger documentation 2](./sequencing_module_api/static/docs_for_readme/images/s_module_2.png)

* screenshot 3
![swagger documentation 3](./sequencing_module_api/static/docs_for_readme/images/s_module_3.png)

* screenshot 4
![swagger documentation 4](./sequencing_module_api/static/docs_for_readme/images/s_module_4.png)

* screenshot 5
![swagger documentation 5](./sequencing_module_api/static/docs_for_readme/images/s_module_5.png)

* screenshot 6
![swagger documentation 6](./sequencing_module_api/static/docs_for_readme/images/s_module_6.png)


## Technologies
***
A list of technologies used within the project:
* [Django](https://www.djangoproject.com): Version 12.3
* [django rest framework](https://www.django-rest-framework.org/): Version 2.34
* [mysqlclient](https://pypi.org/project/mysqlclient/):  Version 2.1.1
* [pyJWT](https://pypi.org/project/PyJWT/):  Version 2.5.0
* [drf-yasg swagger ui and redocs ui](https://pypi.org/project/drf-yasg/): Version 1.21.4
* [django-environ](https://pypi.org/project/django-environ/): Version 0.9.0


## Installation
***

### 1. A little intro about the installation.
```
$ git clone https://github.com/mamoudousow098/sequencing_module.git
$ cd ../path/to/the/file
$ pip install -r requirement.txt
$ python manage.py make migrations
$ python manage.py migrate
$ python manage.py runserver
```
### 2.Side information: 
To use the application in a special environment use 
```
after cloning the project and change the directory to the root directory of the project, you can create a  virtual environmment in python with these commands:
$ python -m venv nameOftheVitualEnv
if your plaftorm is windows , you can activate your virtual environment already created by the following command
$ path-to-the-virtual-env-directory\Scripts\activate.bat

Otherwise, if your plaftorm is UNix system, you can activate your virtual envrionment by these commands:
$source path-to-the-virtual-env-directory/bin/activate

after creating and activating your virtual environment, you can start the project by executing the steps in the introduction of the installation
``` 



## FAQs
***
A list of frequently asked questions
### 1. **general documentation**
you can debug or mastering any project with the offical website of the django and the django rest framework
* [Django](https://www.djangoproject.com)
* [django rest framework](https://www.django-rest-framework.org/)
  
list of faqs you might need to consult
* [installing mysql python](https://stackoverflow.com/questions/5178292/pip-install-mysql-python-fails-with-environmenterror-mysql-config-not-found)
* [configuring mysql for remote access if needed](https://www.hostinger.com/tutorials/mysql/how-create-mysql-user-and-grant-permissions-command-line)
* [mysql debug](https://stackoverflow.com/questions/1885101/delete-data-from-all-tables-in-mysql)
* [deploy app with django](https://vahiwe.medium.com/deploy-django-and-flask-applications-in-the-cloud-using-nginx-gunicorn-and-systemd-centos-7-4b6aef3a8578)
* [deploy django application](https://dev.to/sayam753/deploy-django-4k0d)
* [ssh server intalling on windows](https://winscp.net/eng/docs/guide_windows_openssh_server)

### 2. Contact the developers
For further information you can directly contact the two developers of the project
* [Mamoudou Mamadou Sow](<MAILTO:smamadoumamoudou@ept.sn>)
* [Kadia Bassoum](<MAILTO:bkadia@ept.sn>)


