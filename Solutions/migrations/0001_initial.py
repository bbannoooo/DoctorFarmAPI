# Generated by Django 4.0.5 on 2022-09-15 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dist_id', models.IntegerField()),
                ('crop_id', models.IntegerField()),
            ],
            options={
                'db_table': 'Code',
            },
        ),
        migrations.CreateModel(
            name='Pesticide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_id', models.IntegerField()),
                ('item_name', models.TextField()),
                ('igr_content', models.TextField()),
                ('purpose', models.TextField()),
                ('formulation', models.TextField()),
                ('company', models.TextField()),
            ],
            options={
                'db_table': 'Pesticide',
            },
        ),
        migrations.CreateModel(
            name='Solutions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_id', models.IntegerField()),
                ('symptom', models.TextField()),
                ('solution_default', models.TextField()),
            ],
            options={
                'db_table': 'Solutions',
            },
        ),
    ]
