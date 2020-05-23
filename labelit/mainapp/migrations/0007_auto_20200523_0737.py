# Generated by Django 3.0.5 on 2020-05-23 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_auto_20200523_0702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='dataset_format',
            field=models.CharField(choices=[('text-dir', 'Directory containing text files'), ('image-dir', 'Directory containing image files'), ('audio-dir', 'Directory containing audio files')], default='text-dir', help_text='Format of your dataset', max_length=20),
        ),
    ]