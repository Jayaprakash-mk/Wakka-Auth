# Generated by Django 5.0.2 on 2024-03-14 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wakka', '0004_user_deleted_at_alter_application_server_api_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
