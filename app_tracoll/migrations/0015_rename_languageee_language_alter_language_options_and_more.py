# Generated by Django 4.2.3 on 2023-07-15 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_tracoll', '0014_rename_original_languageee_text_lingua'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Languageee',
            new_name='Language',
        ),
        migrations.AlterModelOptions(
            name='language',
            options={'ordering': ['name_of_language']},
        ),
        migrations.RenameField(
            model_name='language',
            old_name='name_of_languageee',
            new_name='name_of_language',
        ),
        migrations.RenameField(
            model_name='text',
            old_name='lingua',
            new_name='original_language',
        ),
    ]
