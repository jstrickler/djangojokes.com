from django.db import models
from django.urls import reverse
from django.conf import settings
from common.utils.text import unique_slug

class Tag(models.Model):
    tag = models.CharField(max_length=50)
    slug = models.SlugField(
        max_length=50, unique=True, null=False, editable=False,
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('jokes:tags', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.tag

# Create your models here.
class Joke(models.Model):
    """
    Joke: A single joke

    A hilarious joke, stored as a question and an answer. Be prepared for
    belly laughts and guffaws. 
    """
    question = models.TextField(max_length=256, help_text="The first part of the joke")
    answer = models.TextField(max_length=100, blank=True, help_text="The second part of the joke")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # riddles = models.ForeignKey('Riddle')

    slug = models.SlugField(
        max_length=50, unique=True, editable=False,
        null=False
    )

    @property
    def num_votes(self):
        return self.jokevotes.count()
    
    @property
    def num_likes(self):
        return self.jokevotes.filter(vote=1).count()

    @property
    def num_dislikes(self):
        return self.jokevotes.filter(vote=-1).count()


    category = models.ForeignKey(
        'Category', 
        on_delete=models.PROTECT,
        related_name="jokes",
    )

    tags = models.ManyToManyField(
        'tag',
    )                  

    # def to_speech(self):
    #     """
    #     Let the user listen to the joke. 
    #     """
    #     pass  # say joke out loud

    def save(self, *args, **kwargs):
        """
        Save record to database. Extends builtin .save() and creates
        the slug field for a joke. 
        """
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))  # Joke??
        super().save(*args, **kwargs) # 


    class Meta:
        db_table = 'jokes'
#        ordering = ['question', 'answer']
        ordering = ['-updated']

    def get_absolute_url(self):
        """
        Create a URL using the joke's slug field. 

        :return _type: A string representing the URL for one joke. 
        """
        return reverse('jokes:detail', args=[str(self.slug)])

    def __str__(self):
        return self.question

class Category(models.Model):
    category = models.CharField(max_length=50)
    slug = models.SlugField(
        max_length=50, unique=True, null=False, editable=False
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('jokes:category', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))
        super().save(*args, **kwargs)

    class Meta:
        # verbose_name = "???"  if needed
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category
    
class JokeVote(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='jokevotes'
    )
    joke = models.ForeignKey(
        Joke, on_delete=models.CASCADE,
        related_name='jokevotes'
    )
    vote = models.SmallIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'joke'], name='one_vote_per_user_per_joke'
            )
        ]