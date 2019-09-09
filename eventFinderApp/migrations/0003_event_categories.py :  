from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventFinderApp', '0002_event_venue'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='categories',
            field=models.ManyToManyField(related_name='events', to='eventFinderApp.Category'),
        ),
    ]