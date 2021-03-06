# Generated by Django 3.2.11 on 2022-02-03 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discussions', '0009_discussiontopiclink_ordering'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalprogramliveconfiguration',
            name='history_user',
        ),
        migrations.RemoveField(
            model_name='historicalprogramliveconfiguration',
            name='lti_configuration',
        ),
        migrations.RemoveField(
            model_name='programdiscussionsconfiguration',
            name='lti_configuration',
        ),
        migrations.RemoveField(
            model_name='programliveconfiguration',
            name='lti_configuration',
        ),
        migrations.DeleteModel(
            name='HistoricalProgramDiscussionsConfiguration',
        ),
        migrations.DeleteModel(
            name='HistoricalProgramLiveConfiguration',
        ),
        migrations.DeleteModel(
            name='ProgramDiscussionsConfiguration',
        ),
        migrations.DeleteModel(
            name='ProgramLiveConfiguration',
        ),
    ]
