# Generated by Django 3.1.4 on 2022-04-18 15:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pred', '0005_post_replie'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_heading',
            field=models.CharField(max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='post/images'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_content',
            field=models.CharField(max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='user1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='replie',
            name='image',
            field=models.ImageField(null=True, upload_to='post/images'),
        ),
        migrations.AlterField(
            model_name='replie',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pred.post'),
        ),
        migrations.AlterField(
            model_name='replie',
            name='reply_content',
            field=models.CharField(max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='replie',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]