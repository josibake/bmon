# Generated by Django 4.1.2 on 2022-10-26 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bmon', '0010_mempoolreject_reason_code_alter_mempoolreject_peer_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=256, unique=True)),
                ('cpu_info', models.CharField(max_length=1024)),
                ('memory_bytes', models.FloatField()),
                ('nproc', models.IntegerField(help_text='The number of processors')),
                ('region', models.CharField(blank=True, max_length=256, null=True)),
                ('bitcoin_version', models.CharField(help_text='As reported by bitcoind -version', max_length=256)),
                ('bitcoin_gitref', models.CharField(blank=True, max_length=256, null=True)),
                ('bitcoin_gitsha', models.CharField(blank=True, max_length=256, null=True)),
                ('bitcoin_dbcache', models.IntegerField()),
                ('bitcoin_prune', models.IntegerField()),
                ('bitcoin_extra', models.JSONField(help_text='Extra data about this bitcoind instance')),
            ],
        ),
        migrations.AddConstraint(
            model_name='mempoolreject',
            constraint=models.UniqueConstraint(fields=('host', 'timestamp', 'txhash', 'peer_num'), name='unique_reject'),
        ),
        migrations.AddConstraint(
            model_name='host',
            constraint=models.UniqueConstraint(fields=('name', 'cpu_info', 'memory_bytes', 'nproc', 'bitcoin_version', 'bitcoin_gitref', 'bitcoin_gitsha', 'bitcoin_dbcache', 'bitcoin_prune', 'bitcoin_extra'), name='unique_host'),
        ),
    ]
