#создание виртуального окружения
python -m venv venv  


#активируем виртуальное окружение
venv/scripts/activate

#обновляем пакетный менеджер 
python -m pip install --upgrade pip  

#устанавливаем framework
pip install django

#создание проекта
django-admin startproject common

#переходим в папку с проектом для доступа к manage.py
cd common 

#создание приложения
python manage.py startapp store

#запуск сервера
python manage.py runserver

#подключаем базу данных и создаём встроенные таблицы
python manage.py migrate 

#при изменении базы данных 
python manage.py makemigrations
python manage.py migrate

#регистрация админа
python manage.py createsuperuser

