# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-20 11:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0023_alter_page_revision_on_delete_behaviour'),
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TemplateSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_template', models.CharField(help_text='Defines the basic layout of the site. A template with this name must be present in the source code.', max_length=127, verbose_name='Base template')),
                ('basic_page_template', models.CharField(help_text='This template is used to render basic content pages. A template with this name must be present in the source code.', max_length=127, verbose_name='Basic page template')),
                ('blog_index_template', models.CharField(help_text='This template is used to render the blog index. A template with this name must be present in the source code.', max_length=127, verbose_name='Blog index template')),
                ('blog_post_template', models.CharField(help_text='This template is used to render a single blog post. A template with this name must be present in the source code.', max_length=127, verbose_name='Blog post template')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
