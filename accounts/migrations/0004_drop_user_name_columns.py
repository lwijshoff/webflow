from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_remove_profile_fields"),
    ]

    # Note: This migration will attempt to drop `first_name` and `last_name`
    # columns from the default `auth_user` table. This is irreversible in
    # many databases without restoring a backup. The reverse SQL attempts to
    # re-add the columns with a default empty string.
    operations = [
        migrations.RunSQL(
            sql=(
                "ALTER TABLE auth_user DROP COLUMN IF EXISTS first_name;"
                "ALTER TABLE auth_user DROP COLUMN IF EXISTS last_name;"
            ),
            reverse_sql=(
                "ALTER TABLE auth_user ADD COLUMN IF NOT EXISTS first_name varchar(150) NOT NULL DEFAULT '';"
                "ALTER TABLE auth_user ADD COLUMN IF NOT EXISTS last_name varchar(150) NOT NULL DEFAULT '';"
            ),
        ),
    ]
