# Generated by Django 3.0.6 on 2020-05-18 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20200518_0117'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='facebook_link',
            field=models.URLField(blank=True, help_text='Enter your full Facebook URL', verbose_name='Facebook link'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='twitter_link',
            field=models.URLField(blank=True, help_text='Enter your full Twitter URL', verbose_name='Twitter link'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='section_text',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='section_title',
            field=models.CharField(default='Contact Me', max_length=100),
        ),
    ]
