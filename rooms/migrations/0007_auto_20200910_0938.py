# Generated by Django 2.2.5 on 2020-09-10 00:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0006_auto_20200909_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='rooms.Room'),
        ),
        migrations.AlterField(
            model_name='room',
            name='amenities',
            field=models.ManyToManyField(blank=True, related_name='rooms', to='rooms.Amenity'),
        ),
        migrations.AlterField(
            model_name='room',
            name='facilities',
            field=models.ManyToManyField(blank=True, related_name='rooms', to='rooms.Facility'),
        ),
        migrations.AlterField(
            model_name='room',
            name='houseRules',
            field=models.ManyToManyField(blank=True, related_name='rooms', to='rooms.HouseRule'),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rooms', to='rooms.RoomType'),
        ),
    ]