# Generated by Django 3.1.2 on 2021-02-28 01:30

import crud.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_auto_20210130_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='picture',
            field=models.FileField(default='person/picture/profile.jpg', upload_to=crud.models.full_path),
        ),
        migrations.CreateModel(
            name='ImageCatalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to=crud.models.full_path)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.person')),
            ],
        ),
    ]