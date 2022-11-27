# Modify this Procfile to fit your needs
release: python src/init_db.py
web: gunicorn --chdir src index:app
