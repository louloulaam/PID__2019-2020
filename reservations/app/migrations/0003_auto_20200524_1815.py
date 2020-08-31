# Generated by Django 3.0.5 on 2020-05-24 16:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0002_auto_20200518_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='firstname',
            field=models.CharField(max_length=60, verbose_name='Prénom'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='lastname',
            field=models.CharField(max_length=60, verbose_name='Nom de famille'),
        ),
        migrations.AlterField(
            model_name='artisttype',
            name='types',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Types', verbose_name="Type d'artiste"),
        ),
        migrations.AlterField(
            model_name='collaboration',
            name='artist_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ArtistType', verbose_name='Type dartiste'),
        ),
        migrations.AlterField(
            model_name='collaboration',
            name='show',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Show', verbose_name='Spectacle'),
        ),
        migrations.AlterField(
            model_name='locality',
            name='locality',
            field=models.CharField(max_length=60, unique=True, verbose_name='Localité'),
        ),
        migrations.AlterField(
            model_name='locality',
            name='postal_code',
            field=models.CharField(max_length=6, unique=True, verbose_name='Code postal'),
        ),
        migrations.AlterField(
            model_name='location',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Adresse'),
        ),
        migrations.AlterField(
            model_name='location',
            name='designation',
            field=models.CharField(max_length=60, verbose_name="Nom de l'emplacement"),
        ),
        migrations.AlterField(
            model_name='location',
            name='locality',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Locality', verbose_name='Localité'),
        ),
        migrations.AlterField(
            model_name='location',
            name='phone',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Téléphone'),
        ),
        migrations.AlterField(
            model_name='location',
            name='website',
            field=models.URLField(blank=True, max_length=255, null=True, verbose_name='Site internet'),
        ),
        migrations.AlterField(
            model_name='representation',
            name='available_seats',
            field=models.PositiveIntegerField(verbose_name='Nombre de         sièges libres'),
        ),
        migrations.AlterField(
            model_name='representation',
            name='time',
            field=models.DateTimeField(verbose_name='Début de la réprésentation'),
        ),
        migrations.AlterField(
            model_name='representation',
            name='total_seats',
            field=models.PositiveIntegerField(verbose_name='Nombre total         de sièges'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='price',
            field=models.FloatField(verbose_name='Prix total (EUR)'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='seats',
            field=models.PositiveIntegerField(verbose_name='Nombre de sièges'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('Ongoing', 'En cours'), ('Completed', 'Terminée'), ('Cancelled', 'Annulée')], default='Ongoing', max_length=9, verbose_name='Statut'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='time',
            field=models.DateField(auto_now_add=True, verbose_name='Date de réservation'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur'),
        ),
        migrations.AlterField(
            model_name='show',
            name='bookable',
            field=models.BooleanField(default=True, verbose_name='Réservable'),
        ),
        migrations.AlterField(
            model_name='show',
            name='date_created',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Date de création'),
        ),
        migrations.AlterField(
            model_name='show',
            name='description',
            field=models.TextField(verbose_name='Déscription'),
        ),
        migrations.AlterField(
            model_name='show',
            name='poster',
            field=models.URLField(blank=True, max_length=255, null=True, verbose_name='URL du poster'),
        ),
        migrations.AlterField(
            model_name='show',
            name='price',
            field=models.FloatField(verbose_name="Prix d'une place (EUR)"),
        ),
        migrations.AlterField(
            model_name='show',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Titre'),
        ),
        migrations.AlterField(
            model_name='types',
            name='types',
            field=models.CharField(max_length=60, verbose_name="Type d'artiste"),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='language',
            field=models.CharField(choices=[('EN', 'Anglais'), ('FR', 'Français'), ('NL', 'Néerlandais'), ('GE', 'Allemand'), ('SP', 'Espagnol'), ('IT', 'Italien'), ('PO', 'Portugais')], default='FR', max_length=2, verbose_name='Langue'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur'),
        ),
    ]