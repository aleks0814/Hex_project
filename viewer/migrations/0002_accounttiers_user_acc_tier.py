# Generated by Django 4.0.5 on 2022-06-27 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountTiers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('BS', 'Basic'), ('PR', 'Premium'), ('EP', 'Enterprise')], default='BS', max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='acc_tier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='viewer.accounttiers'),
        ),
    ]