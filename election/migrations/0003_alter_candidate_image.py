# Generated by Django 3.2.7 on 2021-09-16 09:01

from django.db import migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0002_candidate_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='image',
            field=versatileimagefield.fields.VersatileImageField(upload_to='candidates'),
        ),
    ]
