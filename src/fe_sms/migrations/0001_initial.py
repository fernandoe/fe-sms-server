# Generated by Django 2.0.4 on 2018-04-08 05:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fe_core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensagem',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('mensagem', models.CharField(max_length=160)),
                ('status', models.CharField(choices=[('criado', 'Criado')], default='criado', max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('pais', models.CharField(default='+55', max_length=10)),
                ('codigo', models.SmallIntegerField()),
                ('numero', models.CharField(max_length=10)),
                ('entidade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fe_core.Entity')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AWSMensagem',
            fields=[
                ('mensagem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='fe_sms.Mensagem')),
                ('message_identifier', models.UUIDField(blank=True, null=True)),
                ('request_identifier', models.UUIDField(blank=True, null=True)),
                ('http_status_code', models.SmallIntegerField(blank=True, null=True)),
                ('retry_attempts', models.SmallIntegerField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('fe_sms.mensagem',),
        ),
        migrations.AddField(
            model_name='mensagem',
            name='entidade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fe_core.Entity'),
        ),
        migrations.AddField(
            model_name='mensagem',
            name='telefone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fe_sms.Telefone'),
        ),
        migrations.AddField(
            model_name='mensagem',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
