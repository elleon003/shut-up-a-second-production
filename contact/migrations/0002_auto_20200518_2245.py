# Generated by Django 3.0.6 on 2020-05-18 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formfield',
            name='field_type',
            field=models.CharField(choices=[('singleline', 'Single line text'), ('multiline', 'Multi-line text'), ('email', 'Email'), ('hidden', 'Hidden field')], max_length=16, verbose_name='Field Type'),
        ),
    ]
