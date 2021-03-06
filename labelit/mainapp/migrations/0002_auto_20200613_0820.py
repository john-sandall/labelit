# Generated by Django 3.0.5 on 2020-06-13 08:20

from django.db import migrations, models
import mainapp.validators


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='config',
            field=models.TextField(help_text="Label studio config, you can find templates and test the config <a target='_blank' rel='noopener noreferrer' href='https://labelstud.io/playground/'>here</a>", validators=[mainapp.validators.validate_label_config], verbose_name='Label Studio XML'),
        ),
    ]
