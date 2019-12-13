# Generated by Django 2.2.7 on 2019-12-13 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0004_url_clicked'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClickDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('url', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shortener.Url')),
            ],
        ),
    ]
