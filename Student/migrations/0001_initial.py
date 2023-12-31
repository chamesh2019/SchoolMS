# Generated by Django 5.0 on 2023-12-10 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Subject', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index_number', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('full_name', models.CharField(max_length=255)),
                ('name_with_initials', models.CharField(max_length=255)),
                ('date_of_birth', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=6)),
                ('enrolled_date', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('special_notes', models.TextField(blank=True, null=True)),
                ('selected_subjects', models.ManyToManyField(blank=True, related_name='selected_subjects', to='Subject.subject')),
            ],
        ),
    ]
