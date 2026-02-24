from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0004_drop_user_name_columns"),
    ]

    operations = [
        migrations.RunSQL(
            sql=(
                "ALTER TABLE auth_user ADD COLUMN IF NOT EXISTS first_name varchar(150) NOT NULL DEFAULT '';"
                "ALTER TABLE auth_user ADD COLUMN IF NOT EXISTS last_name varchar(150) NOT NULL DEFAULT '';"
            ),
            reverse_sql=(
                "ALTER TABLE auth_user DROP COLUMN IF EXISTS first_name;"
                "ALTER TABLE auth_user DROP COLUMN IF EXISTS last_name;"
            ),
        ),
    ]
