# Generated by Django 5.0.6 on 2024-06-14 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0005_tag"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="tags",
            field=models.ManyToManyField(blank=True, null=True, to="courses.tag"),
        ),
    ]
