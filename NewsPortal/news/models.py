from django.contrib.auth.models import User
from django.db import models


class Author(models.Model):
    objects_author_user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField()


    def update_rating(self):
        pass



class Category(models.Model):
    category_name = models.CharField(max_length=255, unique=True)



class Post(models.Model):
    ARTICLE = 'article'
    NEWS = 'news'
    POST_TYPE_CHOICES = [
        (ARTICLE, 'Статья'),
        (NEWS, 'Новость')
    ]

    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # связь «один ко многим» с моделью Author;
    post_type = models.CharField(max_length=10, choices=POST_TYPE_CHOICES)  # поле с выбором — «статья» или «новость»;
    time_on = models.DateTimeField(auto_now_add=True)  # автоматически добавляемая дата и время создания;
    category = models.ManyToManyField(Category, through='PostCategory')  # связь «многие ко многим» с моделью Category (с дополнительной моделью PostCategory);
    article_title = models.CharField(max_length=255)  # заголовок статьи/новости;
    article_text = models.TextField()  # текст статьи/новости;
    article_rating = models.IntegerField(default=0)  # рейтинг статьи/новости.
    rating_comment = models.IntegerField(default=0)  # рейтинг комментария.


    def like(self):
        self.rating_comment +=1
        self.save()

    def dislike(self):
        self.rating_comment -=1
        self.save()


    def preview(self):
        preview_lenght = 124
        if len(self.article_text) <= preview_lenght:
            return self.article_text
        else:
            return self.article_text[:preview_lenght].rstrip() + '...'




class Comment(models.Model):
    '''Под каждой новостью/статьёй можно оставлять комментарии,
    поэтому необходимо организовать их способ хранения тоже.
    Модель будет иметь следующие поля: '''
      # связь «один ко многим» с моделью Post;
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # связь «один ко многим» с моделью Post;
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # связь «один ко многим» со встроенной моделью User (комментарии может оставить любой пользователь, необязательно автор);
    text_comment = models.TextField()  # текст комментария;
    time_create_comment = models.DateTimeField(auto_now_add=True)  # дата и время создания комментария;
    rating_comment = models.IntegerField(default=0)  # рейтинг комментария.

    '''Модель Comment
    Под каждой новостью/статьёй можно оставлять комментарии, поэтому необходимо организовать их способ хранения тоже.
    Модель будет иметь следующие поля:
    связь «один ко многим» с моделью Post;
    связь «один ко многим» со встроенной моделью User (комментарии может оставить любой пользователь, необязательно автор);
    текст комментария;
    дата и время создания комментария;
    рейтинг комментария.'''
    def like(self):
        self.rating_comment +=1
        self.save()

    def dislike(self):
        self.rating_comment -=1
        self.save()



class PostCategory(models.Model):
    ''' Промежуточная модель для связи «многие ко многим»: '''
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # связь «один ко многим» с моделью Post;
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # связь «один ко многим» с моделью Category.





