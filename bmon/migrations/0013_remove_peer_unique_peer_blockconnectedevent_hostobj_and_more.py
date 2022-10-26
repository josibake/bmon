# Generated by Django 4.1.2 on 2022-10-26 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bmon', '0012_rename_host_logprogress_hostname'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='peer',
            name='unique_peer',
        ),
        migrations.AddField(
            model_name='blockconnectedevent',
            name='hostobj',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bmon.host'),
        ),
        migrations.AddField(
            model_name='blockdisconnectedevent',
            name='hostobj',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bmon.host'),
        ),
        migrations.AddField(
            model_name='connectblockdetails',
            name='hostobj',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bmon.host'),
        ),
        migrations.AddField(
            model_name='connectblockevent',
            name='hostobj',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bmon.host'),
        ),
        migrations.AddField(
            model_name='mempoolreject',
            name='hostobj',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bmon.host'),
        ),
        migrations.AddField(
            model_name='peer',
            name='hostobj',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bmon.host'),
        ),
        migrations.AddField(
            model_name='reorgevent',
            name='hostobj',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bmon.host'),
        ),
        migrations.AddField(
            model_name='requestblockevent',
            name='hostobj',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bmon.host'),
        ),
        migrations.AddConstraint(
            model_name='peer',
            constraint=models.UniqueConstraint(fields=('host', 'hostobj', 'num', 'addr', 'connection_type', 'inbound', 'network', 'services', 'subver', 'version', 'relaytxes', 'bip152_hb_from', 'bip152_hb_to'), name='unique_peer'),
        ),
    ]
