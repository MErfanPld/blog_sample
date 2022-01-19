# Cfarm

source .venv/bin/activate

pip install -r requ.txt

./manage.py migrate

./manage.py createsuperuser

./manage.py runserver ```
