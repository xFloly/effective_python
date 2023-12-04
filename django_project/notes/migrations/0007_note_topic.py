# Generated by Django 4.2.7 on 2023-12-03 23:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("notes", "0006_topic_is_public"),
    ]

    operations = [
        migrations.AddField(
            model_name="note",
            name="topic",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="notes.topic"
            ),
            preserve_default=False,
        ),
    ]