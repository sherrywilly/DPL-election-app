# Generated by Django 3.2.7 on 2021-09-16 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0003_alter_candidate_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='desg',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
