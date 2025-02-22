# Generated by Django 5.1.4 on 2024-12-26 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcercaDe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('contenido', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='author',
            new_name='autor',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='created_at',
            new_name='creado_en',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='body',
            new_name='cuerpo',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='subtitle',
            new_name='subtitulo',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='title',
            new_name='titulo',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='image',
        ),
        migrations.AddField(
            model_name='blog',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes_blog/'),
        ),
    ]
