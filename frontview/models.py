from django.db import models

# Create your models here.

event_type = (
                ("local","local"),
                ("foreign","foreign"),
            )

class Events(models.Model):
    """Model definition for Events."""

    # TODO: Define fields here
    conference = models.CharField(max_length=250)
    host = models.CharField(max_length=250)
    theme = models.CharField(max_length=250)
    paper = models.CharField(max_length=250)
    authors = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    summary = models.TextField()
    date =  models.CharField(max_length=50)
    year =  models.CharField(max_length=5)
    type = models.CharField(max_length=8,
                                      choices = event_type ,default='local')


    class Meta:
        """Meta definition for Events."""

        verbose_name = 'Events'
        verbose_name_plural = 'Events'
        ordering = ['-year']

    def __str__(self):
        """Unicode representation of Events."""
        return f'{self.paper} - {self.date}'


class FlagshipProject(models.Model):
    """Model definition for FlagshipProject."""

    # TODO: Define fields here
    title = models.CharField(max_length=250)
    description = models.TextField()

    class Meta:
        """Meta definition for FlagshipProject."""

        verbose_name = 'FlagshipProject'
        verbose_name_plural = 'FlagshipProjects'
        ordering = ['id']


    def __str__(self):
        """Unicode representation of FlagshipProject."""
        return self.title

class Publications(models.Model):
    """Model definition for Publications."""

    # TODO: Define fields here
    authors =  models.CharField( max_length=150)
    year = models.CharField( max_length=5)
    title =  models.CharField( max_length=250)
    journal = models.CharField( max_length=150)
    published = models.BooleanField()

    class Meta:
        """Meta definition for Publications."""

        verbose_name = 'Publications'
        verbose_name_plural = 'Publicationss'
        ordering = ['-year']


    def __str__(self):
        """Unicode representation of Publications."""
        return self.title

class ConferencePresentation(models.Model):
    """Model definition for ConferencePresentation."""

    # TODO: Define fields here
    authors = models.CharField( max_length=150)
    year = models.CharField( max_length=5)
    title = models.CharField( max_length=250)
    venue = models.CharField( max_length=250)


    class Meta:
        """Meta definition for ConferencePresentation."""

        verbose_name = 'ConferencePresentation'
        verbose_name_plural = 'ConferencePresentations'
        ordering = ['-year']


    def __str__(self):
        """Unicode representation of ConferencePresentation."""
        return f"{self.year} - {self.title[:20]}"
