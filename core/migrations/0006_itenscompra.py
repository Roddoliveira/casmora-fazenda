# Generated by Django 4.0.2 on 2022-02-02 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_compra'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItensCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens', to='core.compra')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='core.produto')),
            ],
        ),
    ]
