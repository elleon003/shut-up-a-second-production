# Generated by Django 3.0.6 on 2020-05-16 04:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('home', '0004_auto_20200504_0118'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='second_image',
            field=models.ForeignKey(help_text='The top, primary image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]
