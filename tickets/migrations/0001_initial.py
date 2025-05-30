# Generated by Django 5.1.5 on 2025-03-19 12:15

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('code', models.CharField(max_length=32, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('stripe_product_id', models.CharField(max_length=255, unique=True)),
                ('stripe_payment_link_id', models.CharField(blank=True, max_length=255, null=True)),
                ('email_template', models.CharField(blank=True, max_length=255, null=True)),
                ('limit_quantity', models.IntegerField(default=-1)),
                ('achievement', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.achievement')),
            ],
            options={
                'db_table': 'tickets',
                'ordering': ['code'],
            },
        ),
        migrations.CreateModel(
            name='TicketSale',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('customer_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('stripe_payment_id', models.CharField(max_length=255)),
                ('metadata', models.JSONField(default=dict)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales', to='tickets.ticket')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.user')),
            ],
            options={
                'db_table': 'ticket_sales',
                'ordering': ['-created_at'],
            },
        ),
    ]
