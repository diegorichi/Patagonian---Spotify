rmdir -r songs\migrations\

python.exe .\manage.py makemigrations
python.exe .\manage.py migrate
python.exe .\manage.py migrate --run-syncdb

rem optional
python.exe .\manage.py createsuperuser
