from django.db import models


# The Author model stores information about the authors of the news articles.
class Author(models.Model):
    # The first_name field is a CharField which will store the author's first name.
    # max_length=50 means the field can hold up to 50 characters.
    first_name = models.CharField(max_length=50)

    # The last_name field is a CharField which will store the author's last name.
    # Similar to first_name, it can hold up to 50 characters.
    last_name = models.CharField(max_length=50)

    # The bio field is a TextField, which is used for storing longer text about the author.
    # This field will contain a short biography of the author.
    bio = models.TextField()

    # The photo field is an ImageField that allows uploading and storing an author's photo.
    # The image will be saved to the 'media/authors/' directory.
    # blank=True and null=True mean the photo field is optional.
    photo = models.ImageField(upload_to='authors/', blank=True, null=True)

    # The __str__ method defines how the Author object is represented as a string.
    # In this case, it will return the author's full name (first name + last name).
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# The News model stores information about individual news articles.
class News(models.Model):
    # The title field is a CharField that stores the title of the news article.
    # It can hold up to 200 characters.
    title = models.CharField(max_length=200)

    # The author field establishes a relationship between the News and Author models.
    # It is a ForeignKey, meaning each news article is linked to one author.
    # on_delete=models.CASCADE means that if the author is deleted, all their related news articles
    # will also be deleted.
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    # The pub_date field is a DateField that stores the publication date of the news article.
    # It stores only the date (without time) when the article was published.
    pub_date = models.DateField()

    # The content field is a TextField, which is used for storing the full text of the news article.
    content = models.TextField()

    # The image field is an ImageField that allows uploading and storing an image related to the news article.
    # The image will be saved in the 'media/news/' directory.
    # blank=True and null=True mean the image field is optional.
    image = models.ImageField(upload_to='news/', blank=True, null=True)

    # The __str__ method defines how the News object is represented as a string.
    # In this case, it returns the title of the news article.
    def __str__(self):
        return self.title
