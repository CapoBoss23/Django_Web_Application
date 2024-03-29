# Generated by Django 4.2.3 on 2023-07-15 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_tracoll', '0011_alter_translation_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_language', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['name_of_language'],
            },
        ),
        migrations.AlterField(
            model_name='text',
            name='original_language',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_tracoll.language'),
        ),
    ]
