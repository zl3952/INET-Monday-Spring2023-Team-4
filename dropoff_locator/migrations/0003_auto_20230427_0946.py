# Generated by Django 3.2 on 2023-04-27 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dropoff_locator', '0002_siteschedule_siteseason'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.IntegerField(choices=[(1, 'Fruit and vegetable scraps, eggshells, nuts'), (2, 'Rice, pasta, bread, grains, cereal'), (3, 'Beans, flour, spices'), (4, 'Meat, fish, dairy, whole eggs, bones'), (5, 'Fat, oil, greasy food scraps'), (6, 'Paper products, pizza boxes'), (7, 'Coffee grounds, tea bags'), (8, 'Plant and yard waste'), (9, 'Commercial food scraps')])),
            ],
        ),
        migrations.AlterField(
            model_name='site',
            name='is_always_open',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='site',
            name='lat',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='lon',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='notes',
            field=models.TextField(null=True),
        ),
        migrations.CreateModel(
            name='AcceptedItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dropoff_locator.item')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dropoff_locator.site')),
            ],
        ),
        migrations.AddField(
            model_name='site',
            name='accepted_items',
            field=models.ManyToManyField(related_name='accepts', through='dropoff_locator.AcceptedItems', to='dropoff_locator.Item'),
        ),
    ]
