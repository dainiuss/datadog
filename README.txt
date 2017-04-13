# Create project:
django-admin.py startproject datadog

# Create application:
python manage.py startapp transportation_management

# Run migrations:
python manage.py migrate

# Run test server:
python manage.py runserver 0.0.0.0:8800

# Create django admin user:
python manage.py createsuperuser

# Access admin:
http://127.0.0.1:8800/admin