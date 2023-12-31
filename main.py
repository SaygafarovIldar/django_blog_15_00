# библиотеки (django, pillow)
# создание проекта на django
# django-admin - специальная команда для запуска других команд
# django-admin startproject project_name - создание нового проекта
# python manage.py runserver - запускает тестовый сервер
# python manage.py makemigrations - создает файл с миграциями, кодом который нужно отправить в БД
# python manage.py migrate - отправляет файл с миграциями на выполнение в базу данных
# python manage.py createsuperuser - создает администратора сайта
# {%  %} - используется для вызываемых вещей (циклы, условия, функции и тд)
# {{  }} - используются для вывода значений на страницу
# {% extends 'filename' %} используется чтобы забрать весь код из базового шаблона
"""
{% block block_name %}
{% endblock block_name %}

инструкция позволяющая менять контент на каждой странице
всегда уникальное значение, дублировать название в одном шаблоне нельзя
"""