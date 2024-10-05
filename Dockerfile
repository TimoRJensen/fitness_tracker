# Verwenden Sie das offizielle Python-Image
FROM python:3.11-slim

# Arbeitsverzeichnis im Container festlegen
WORKDIR /app/fitness_tracker

# Abhängigkeiten installieren
COPY requirements.txt ../
RUN pip install --no-cache-dir -r ../requirements.txt

# Projektdateien kopieren
COPY . ../

# Port 8000 freigeben
EXPOSE 8000

# Statische Dateien sammeln
RUN python manage.py collectstatic --noinput

# Datenbankmigrationen durchführen
RUN python manage.py migrate

# Django-Server starten
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]