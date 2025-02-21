# Generated by Django 5.0.3 on 2024-04-06 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0002_hotel_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="room",
            name="max_occupants",
        ),
        migrations.AddField(
            model_name="room",
            name="isAC",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="room",
            name="number_of_beds",
            field=models.PositiveIntegerField(default=1, verbose_name="number of beds"),
        ),
        migrations.AddField(
            model_name="room",
            name="type",
            field=models.CharField(
                choices=[
                    ("SUITE", "Suite"),
                    ("DELUXE", "Deluxe"),
                    ("SUPER_DELUXE", "Super_deluxe"),
                ],
                default="SUITE",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="preference",
            field=models.CharField(
                choices=[
                    ("SUITE", "Suite"),
                    ("DELUXE", "Deluxe"),
                    ("SUPER_DELUXE", "Super_deluxe"),
                ],
                max_length=20,
                null=True,
            ),
        ),
        migrations.DeleteModel(
            name="RoomData",
        ),
    ]
