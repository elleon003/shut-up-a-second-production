# Generated by Django 3.0.8 on 2020-08-01 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('home', '0007_auto_20200518_0134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='second_image',
            field=models.ForeignKey(blank=True, help_text='The top, primary image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]
