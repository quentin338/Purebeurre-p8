# Generated by Django 2.2.5 on 2019-10-21 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20190919_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='nutriscore_grade',
            field=models.CharField(default='d', max_length=1),
            preserve_default=False,
        ),
    ]
