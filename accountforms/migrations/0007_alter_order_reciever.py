# Generated by Django 4.1.5 on 2023-02-11 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accountforms', '0006_order_alter_doctor_email_delete_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='reciever',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reciever', to='accountforms.pharmacist'),
        ),
    ]