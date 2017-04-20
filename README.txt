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

# Add some data to the database
from transportation_management.models import *

vehicle = Vehicle.objects.create(vehicle_name='2010 Honda CRV',
                                 takes_fuel_while_standing=5,
                                 takes_fuel_while_moving=32,
                                 takes_fuel_while_unloading=20)
vehicle = Vehicle.objects.create(vehicle_name='2015 Chevy Tahoe',
                                 takes_fuel_while_standing=10,
                                 takes_fuel_while_moving=38,
                                 takes_fuel_while_unloading=25)

tr = TravelReport.objects.create(vehicle=vehicle,
                                 route='Costco',
                                 date=datetime.date(2017,4,10),
                                 time_left_terminal=datetime.time(10,00),
                                 time_arrived_to_client=datetime.time(10,55),
                                 time_left_client=datetime.time(11,20),
                                 time_back_to_terminal=datetime.time(12,20),
                                 time_unloading=10,
                                 speedometer_at_leaving=200200,
                                 speedometer_at_arrival=200250)

# URLS:
http://127.0.0.1:8800/logout
http://127.0.0.1:8800/list
http://127.0.0.1:8800/create
http://127.0.0.1:8800/read/1