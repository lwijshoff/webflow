from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_userprofile_lunch_eligible"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userprofile",
            name="bio",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="location",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="website",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="avatar",
        ),
    ]
