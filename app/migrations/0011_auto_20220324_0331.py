# Generated by Django 2.2 on 2022-03-23 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20220323_1639'),
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='customer',
            name='screen',
        ),
        migrations.DeleteModel(
            name='Selection',
        ),
        migrations.AddField(
            model_name='folder',
            name='editor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Customer'),
        ),
        migrations.AddField(
            model_name='folder',
            name='fav_avatar',
            field=models.ManyToManyField(to='app.Avatar'),
        ),
        migrations.AddField(
            model_name='folder',
            name='fav_item',
            field=models.ManyToManyField(to='app.Item'),
        ),
    ]
