# Generated by Django 4.1 on 2023-02-12 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vocab', '0004_profilevocabulary'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profilevocabulary',
            options={'verbose_name_plural': 'Profile Vocabularies'},
        ),
        migrations.AlterModelOptions(
            name='vocabulary',
            options={'verbose_name_plural': 'Vocabularies'},
        ),
    ]
