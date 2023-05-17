from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('barber_name', models.CharField(max_length=100)),
                ('client_name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
