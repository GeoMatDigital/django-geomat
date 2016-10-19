# GeoMat _digital_

Folgt.


## Mitarbeit

Das aktuelle Layout dieser Repository basiert auf [cookiecutter-django](https://github.com/pydanny/cookiecutter-django). Dementsprechend findet sich die generelle Nutzungsanleitung in [deren ReadTheDocs](http://cookiecutter-django.readthedocs.org/en/latest/developing-locally.html).

### Anleitung

Hier für muss die aktuelle Version von Docker installiert sein. Abhängig vom Betriebssystem und dem zur Entwicklung genutzten Rechner wird hierbei eine andere Version gebraucht. Zu bevorzugen ist immer das Paket ``Docker for Windows`` bzw. ``Docker for OS X``. Ersteres setzt allerdings Windows 10, sowie Hyper-V Unterstützung voraus.

Nutzer von Docker Toolbox folgen führen den Schritt 2a aus, während man sich das bei ``Docker for $OS`` sparen kann.

#### 1. Develop branch klonen

    git clone https://github.com/mimischi/django-geomat.git --branch develop

#### 2: Nur für Nutzer von Docker Toolbox

Aktuell muss auf OS X (und Windows) eine extra VM eingerichtet werden, damit Docker läuft. Dazu muss auch [VirtualBox](https://www.virtualbox.org/) installiert sein.

    docker-machine create --driver virtualbox geomat
    
Danach muss die soeben erstellte Maschine zur aktuell genutzten gesetzt werden:

    eval "$(docker-machine env geomat)"

#### 3. System aufbauen & starten

    docker-compose -f dev.yml build
    docker-compose -f dev.yml up -d
   
#### 4. Datenbank migrieren

    docker-compose -f dev.yml run django python manage.py migrate


Dazu kann jetzt noch ein Superuser erstellt werden. Grundsätzlich läuft das System jetzt. Unter Linux ist die Seite nun unter localhost:8000 aufrufbar. Unter OS X/Windows führt man folgenden Befehl aus und findet die zugehörige IP heraus:

    docker-machine env clock

Für weitere Hilfe einfach der [offiziellen Anleitung von cookiecutter-django](http://cookiecutter-django.readthedocs.org/en/latest/developing-locally-docker.html) folgen.
