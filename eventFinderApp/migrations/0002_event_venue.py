from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventFinderApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='venue',
            field=models.CharField(default='n/a', max_length=200),
            preserve_default=False,
        ),
    ]