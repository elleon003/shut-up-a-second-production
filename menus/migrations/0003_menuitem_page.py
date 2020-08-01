# Generated by Django 3.0.6 on 2020-05-18 02:41

from django.db import migrations
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0002_menuitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='page',
            field=modelcluster.fields.ParentalKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='menu_items', to='menus.Menu'),
            preserve_default=False,
        ),
    ]