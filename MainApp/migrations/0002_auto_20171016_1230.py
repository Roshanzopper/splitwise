# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-16 07:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpenseGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ExpenseGroupName', models.CharField(max_length=250)),
                ('SimplifyGroupDebts', models.BooleanField(default=False)),
                ('ExpenseGroupType', models.CharField(choices=[('Apartment', 'Apartment'), ('House', 'House'), ('Trip', 'Trip'), ('Other', 'Other')], default='Apartment', max_length=50)),
                ('CreatedOn', models.DateTimeField(auto_now_add=True)),
                ('IsDelete', models.BooleanField(default=False)),
                ('DeletedOn', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='splituser',
            options={'ordering': ('createdon',)},
        ),
        migrations.AddField(
            model_name='expensegroup',
            name='CreatedBy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ExpenseGroup_CreatedBy', to='MainApp.SplitUser'),
        ),
        migrations.AddField(
            model_name='expensegroup',
            name='DeletedBy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ExpenseGroup_DeletedBy', to='MainApp.SplitUser'),
        ),
    ]
