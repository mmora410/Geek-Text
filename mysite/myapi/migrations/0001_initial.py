# Generated by Django 4.1.1 on 2022-09-26 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Addresses',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('type', models.TextField(db_column='Type')),
                ('address', models.TextField(db_column='Address')),
                ('country', models.TextField(db_column='Country')),
                ('state', models.TextField(db_column='State')),
                ('city', models.TextField(db_column='City')),
                ('zipcode', models.IntegerField(db_column='ZipCode')),
            ],
            options={
                'db_table': 'Addresses',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('firstname', models.TextField(db_column='firstName')),
                ('lastname', models.TextField(db_column='lastName')),
                ('biography', models.TextField()),
                ('publisher', models.TextField()),
            ],
            options={
                'db_table': 'Authors',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('isbn', models.TextField(db_column='ISBN', unique=True)),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('price', models.TextField()),
                ('publisher', models.TextField()),
                ('yearpublished', models.IntegerField(db_column='yearPublished')),
                ('copiessold', models.IntegerField(db_column='copiesSold')),
            ],
            options={
                'db_table': 'Books',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Creditcards',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('type', models.TextField(db_column='Type')),
                ('number', models.IntegerField(db_column='Number')),
                ('expirationdate', models.TextField(db_column='ExpirationDate')),
                ('cvv', models.IntegerField(db_column='CVV')),
            ],
            options={
                'db_table': 'CreditCards',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('genre', models.TextField()),
            ],
            options={
                'db_table': 'Genres',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Purchasedbooks',
            fields=[
                ('orderhistory', models.AutoField(db_column='orderHistory', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'PurchasedBooks',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Shoppingcarts',
            fields=[
                ('ordernumber', models.AutoField(db_column='orderNumber', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'ShoppingCarts',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('username', models.TextField(db_column='userName', unique=True)),
                ('password', models.TextField()),
                ('firstname', models.TextField(blank=True, db_column='firstName', null=True)),
                ('lastname', models.TextField(blank=True, db_column='lastName', null=True)),
            ],
            options={
                'db_table': 'Users',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Bookratings',
            fields=[
                ('userid', models.OneToOneField(db_column='UserID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='myapi.users')),
                ('rating', models.IntegerField()),
                ('ratingtimestamp', models.TextField(db_column='ratingTimeStamp')),
                ('comment', models.TextField()),
                ('commenttimestamp', models.TextField(db_column='commentTimeStamp')),
            ],
            options={
                'db_table': 'BookRatings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Wishlists',
            fields=[
                ('userid', models.OneToOneField(db_column='UserID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='myapi.users')),
                ('name', models.TextField(unique=True)),
            ],
            options={
                'db_table': 'WishLists',
                'managed': False,
            },
        ),
    ]