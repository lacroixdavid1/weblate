# Generated by Django 2.2.9 on 2020-01-20 14:34

import django.db.models.deletion
from django.db import migrations, models

import weblate.trans.fields


class Migration(migrations.Migration):

    dependencies = [("trans", "0056_fixup_source_translations")]

    operations = [
        migrations.AddField(
            model_name="component",
            name="shaping_regex",
            field=weblate.trans.fields.RegexField(
                blank=True,
                default="",
                help_text="Regular expression used to determine shapings of a string.",
                max_length=190,
                verbose_name="Shapings regular expression",
            ),
        ),
        migrations.CreateModel(
            name="Shaping",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("shaping_regex", weblate.trans.fields.RegexField(max_length=190)),
                ("key", models.CharField(db_index=True, max_length=190)),
                (
                    "component",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="trans.Component",
                    ),
                ),
            ],
            options={"unique_together": {("key", "component", "shaping_regex")}},
        ),
        migrations.AddField(
            model_name="unit",
            name="shaping",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="trans.Shaping",
            ),
        ),
    ]
