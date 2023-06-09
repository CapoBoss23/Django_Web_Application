# Generated by Django 4.2 on 2023-07-07 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_text', models.CharField(choices=[('P', 'Poem'), ('S', 'Song')], help_text='Type of text', max_length=1)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(max_length=2000)),
                ('original_language', models.CharField(choices=[('E', 'English'), ('F', 'French'), ('S', 'Spanish')], help_text='language of the original text', max_length=1)),
                ('status', models.CharField(choices=[('W', 'Waiting for translation'), ('L', 'Under revision by administrator'), ('E', 'Existing translation and editable by authenticated users'), ('V', 'Final translation NOT editable anymore')], default='W', help_text='State of traslation', max_length=1)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
