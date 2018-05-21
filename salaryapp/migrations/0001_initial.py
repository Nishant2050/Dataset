# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-16 14:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.FloatField(blank=True, null=True)),
                ('workclass', models.CharField(blank=True, choices=[('PR', 'Private'), ('SENI', 'Self-emp-not-inc'), ('SEI', 'Self-emp-inc'), ('FG', 'Federal-gov'), ('LG', 'Local-gov'), ('SG', 'State-gov'), ('WP', 'Without-pay'), ('NW', 'Never-worked')], max_length=3, null=True)),
                ('education', models.CharField(blank=True, choices=[('BA', 'Bachelors'), ('SC', 'Some-college'), ('11', '11th'), ('HG', 'HS-grad'), ('PS', 'Prof-school'), ('AA', 'Assoc-acdm'), ('AV', 'Assoc-voc'), ('9', '9th'), ('7', '7th-8th'), ('12', '12th'), ('MS', 'Masters'), ('1', '1st-4th'), ('10', '10th'), ('DOC', 'Doctorate'), ('5', '5th-6th'), ('PRE', 'Preschool')], max_length=3, null=True)),
                ('martial_status', models.CharField(blank=True, choices=[('MCS', 'Married-civ-spouse'), ('D', 'Divorced'), ('NM', 'Never-married'), ('S', 'Separated'), ('W', 'Widowed'), ('MSA', 'Married-spouse-absent'), ('MAS', 'Married-AF-spouse')], max_length=3, null=True)),
                ('occupation', models.CharField(blank=True, choices=[('TS', 'Tech-support'), ('CR', 'Craft-repair'), ('OS', 'Other-service'), ('SA', 'Sales'), ('EM', 'Exec-managerial'), ('PS', 'Prof-specialty'), ('HC', 'Handlers-cleaners'), ('MOI', 'Machine-op-inspct'), ('AC', 'Adm-clerical'), ('FF', 'Farming-fishing'), ('TM', 'Transport-moving'), ('PHS', 'Priv-house-serv'), ('PS', 'Protective-serv'), ('AF', 'Armed-Forces')], max_length=3, null=True)),
                ('relationship', models.CharField(blank=True, choices=[('W', 'Wife'), ('OC', 'Own-child'), ('H', 'Husband'), ('NIF', 'Not-in-family'), ('OR', 'Other-relative'), ('U', 'Unmarried')], max_length=3, null=True)),
                ('race', models.CharField(blank=True, choices=[('WT', 'White'), ('API', 'Asian-Pac-Islander'), ('AIE', 'Amer-Indian-Eskimo'), ('O', 'Other'), ('B', 'Black')], max_length=3, null=True)),
                ('sex', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True)),
                ('capital_gain', models.PositiveIntegerField(blank=True, null=True)),
                ('capital_loss', models.PositiveIntegerField(blank=True, null=True)),
                ('hours_per_week', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('native_country', models.CharField(choices=[('US', 'United-States'), ('CA', 'Cambodia'), ('E', 'England'), ('PR', 'Puerto-Rico'), ('CD', 'Canada'), ('G', 'Germany'), ('OU', 'Outlying-US(Guam-USVI-etc)'), ('I', 'India'), ('JP', 'Japan'), ('GR', 'Greece'), ('SO', 'South'), ('CH', 'China'), ('CU', 'Cuba'), ('IR', 'Iran'), ('HO', 'Honduras'), ('PH', 'Philippines'), ('IT', 'Italy'), ('PO', 'Poland'), ('JA', 'Jamaica'), ('VI', 'Vietnam'), ('ME', 'Mexico'), ('POR', 'Portugal'), ('IR', 'Ireland'), ('FR', 'France'), ('DR', 'Dominican-Republic'), ('LA', 'Laos'), ('EC', 'Ecuador'), ('TW', 'Taiwan'), ('HT', 'Haiti'), ('CO', 'Columbia'), ('HU', 'Hungary'), ('GU', 'Guatemala'), ('NR', 'Nicaragua'), ('SL', 'Scotland'), ('TH', 'Thailand'), ('YU', 'Yugoslavia'), ('ES', 'El-Salvador'), ('TT', 'Trinadad&Tobago'), ('PR', 'Peru'), ('HG', 'Hong'), ('HN', 'Holand-Netherlands')], max_length=3)),
                ('salary_choices', models.CharField(choices=[('GT', '>50K'), ('LT', '<=50K')], max_length=2)),
            ],
        ),
    ]