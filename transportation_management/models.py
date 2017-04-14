from datetime import timedelta
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Vehicle(models.Model):
    class Meta:
        verbose_name = _('Vehicle')
        verbose_name_plural = _('Vehicle')

    vehicle_name = models.CharField(max_length=254)
    takes_fuel_while_standing = models.PositiveIntegerField()  # liter/hour
    takes_fuel_while_moving = models.PositiveIntegerField()  # liter/hour
    takes_fuel_while_unloading = models.PositiveIntegerField()  # liter/hour

    def __str__(self):
        return '<Vehicle: {}>'.format(self.vehicle_name)


class TravelReport(models.Model):
    class Meta:
        verbose_name = _('Travel Report')
        verbose_name_plural = _('Travel Report')

    vehicle = models.ForeignKey(Vehicle)
    route = models.CharField(max_length=254)
    date = models.DateField()
    time_left_terminal = models.TimeField()
    time_arrived_to_client = models.TimeField()
    time_left_client = models.TimeField()
    time_back_to_terminal = models.TimeField()
    time_unloading = models.PositiveIntegerField()  # in minutes
    speedometer_at_leaving = models.PositiveIntegerField()
    speedometer_at_arrival = models.PositiveIntegerField()

    @property
    def distance(self):
        return self.speedometer_at_arrival - self.speedometer_at_leaving

    @property
    def fuel_consumed(self):
        t1 = timedelta(hours=self.time_left_terminal.hour, minutes=self.time_left_terminal.minute)
        t2 = timedelta(hours=self.time_arrived_to_client.hour, minutes=self.time_arrived_to_client.minute)
        t3 = timedelta(hours=self.time_left_client.hour, minutes=self.time_left_client.minute)
        t4 = timedelta(hours=self.time_back_to_terminal.hour, minutes=self.time_back_to_terminal.minute)
        timedelta_standing = (t3 - t2 - timedelta(minutes=self.time_unloading))
        timedelta_moving = (t2 - t1) + (t4 - t3)
        time_standing_sec = self._timedelta_to_sec(timedelta_standing)
        time_moving_sec = self._timedelta_to_sec(timedelta_moving)
        time_unloading_sec = self.time_unloading * 60
        fuel_consumed_standing = self._fual_consumption(self.vehicle.takes_fuel_while_standing, time_standing_sec)
        fuel_consumed_moving = self._fual_consumption(self.vehicle.takes_fuel_while_moving, time_moving_sec)
        fuel_consumed_unloading = self._fual_consumption(self.vehicle.takes_fuel_while_unloading, time_unloading_sec)
        return round(fuel_consumed_standing + fuel_consumed_moving + fuel_consumed_unloading, 2)

    def _timedelta_to_sec(self, time_delta):
        """
        :param time_delta: 
        :return: int seconds:
        """
        t = str(time_delta)
        h, m, s = t.split(':')
        time_in_sec = int(h) * 3600 + int(m) * 60 + int(s)
        return time_in_sec

    def _fual_consumption(self, consumes_per_hour, time_consuming_in_seconds):
        return round(float(consumes_per_hour) / float(60 * 60) * time_consuming_in_seconds, 2)

    def __str__(self):
        return '<TravelReport: {}>'.format(self.id)
