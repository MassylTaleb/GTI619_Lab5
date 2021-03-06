# Generated by Django 3.0.4 on 2020-03-29 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lab5', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='params',
            name='cannotUsePreviousPass',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='params',
            name='contactAdminAfterFailure',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='params',
            name='delayBetweenAttemps',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='params',
            name='isPeriodicChange',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='params',
            name='needLowercase',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='params',
            name='needNumericChar',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='params',
            name='needSpecialChar',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='params',
            name='needUppercase',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='params',
            name='numberOfAttemps',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='params',
            name='passMaxLength',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='params',
            name='passMinLength',
            field=models.PositiveIntegerField(),
        ),
    ]
