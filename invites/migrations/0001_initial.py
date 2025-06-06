# Generated by Django 3.2.13 on 2024-12-26 18:17

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=32, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('used_at', models.DateTimeField(null=True)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('used', 'used')], default='pending', max_length=16)),
                ('invited_email', models.CharField(max_length=255, null=True)),
                ('invited_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='my_invite', to='users.user')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invites', to='users.user')),
            ],
            options={
                'db_table': 'invites',
            },
        ),
    ]
