# Generated by Django 4.2.4 on 2023-08-18 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_group_number_alter_user_student_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='student_year',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
    ]