# Generated by Django 4.1.2 on 2022-10-07 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0004_audit_audit_app_audit_event_ec8231_idx_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="daily_email_updates",
            field=models.BooleanField(null=True),
        ),
    ]
