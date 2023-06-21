# Generated by Django 4.2.2 on 2023-06-19 14:36

from django.db import migrations, models
import store.validators


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_alter_orderitem_order_productimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to='store/images', validators=[store.validators.validate_file_size]),
        ),
    ]
