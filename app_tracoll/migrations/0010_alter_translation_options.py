# Generated by Django 4.2 on 2023-07-14 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_tracoll', '0009_alter_translation_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='translation',
            options={'ordering': ['translated_title'], 'permissions': (('permession_of_edit_text_with_every_status', 'You can edit every text in every status'),)},
        ),
    ]
