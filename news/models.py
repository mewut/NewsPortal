from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    ratingAuthor = models.SmallIntegerField(default=0)

    def update_rating(self):
        postRat = self.post_set.aggregate(postRating=sum('rating'))
        pRat = 0
        pRat += postRat.get('postRating')
        # суммарный рейтинг всех комментариев к статьям автора

        commentRat = self.authorUser.comment_set.aggregate(commentRating=Sum('rating'))
        cRat = 0
        cRat += commentRat.get('commentRating')
        # суммарный рейтинг всех комментариев автора

        self.ratingAuthor = pRat *3 + cRat
        self.save()
        # суммарный рейтинг каждой статьи автора умножается на 3


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    NEWS = 'NW'
    ARTICLE = 'AR'
    CATEGORY_CHOICES = (
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья')
    )
    categoryType = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=ARTICLE)
    dateCreation = models.DateTimeField(auto_now_add=True) # когда пост создадут, автоматически появится время создания
    postCategory = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=128)
    text = models.TextField() # не ограничиваем пользователя в символах, пусть пишет полотны текста
    rating = models.SmallIntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text[0:123] + '...'


class PostCategory(models.Model):
    postThrought = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoryThrought = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    dateCreation = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()


# python manage.py migrate
# python manage.py shell
# from news.models import * - все импортировали

# Теперь сделаем юзеров - Настю и Иру
# u1 = User.objects.create_user(username='Nastya')
# u2 = User.objects.create_user(username='Ira')

# Готово. Теперь создадим два объекта модели Author, связанные с пользователями
# Author.objects.create(authorUser=u1)
# Author.objects.create(authorUser=u2)

# Есть. Теперь нужно добавить 4 категории в модель Category
# Category.objects.create(name='IT')
# Category.objects.create(name='GAMES')
# Category.objects.create(name='CATS')
# Category.objects.create(name='DOGS')
# У меня будут IT, игры, котики и собачки. Почему бы и нет.

# Теперь создадим статьи:
# author = Author.objects.get(id=1)
# Post.objects.create(author=author, categoryType='NW', title='Helo world!', text='bla-bla') - это новость
# Post.objects.create(author=author, categoryType='AR', title='Cats', text='mew') - это статья
# Post.objects.create(author=author, categoryType='AR', title='Dogs', text='wof') - и вторая статья

# Добавим категории
# Post.objects.get(id=1).postCategory.add(Category.objects.get(id=1))
# Post.objects.get(id=1).postCategory.add(Category.objects.get(id=2))

# Создадим комментариb
# Comment.objects.create(commentPost=Post.objects.get(id=1), commentUser=Author.objects.get(id=1).authorUser, text='anytext')
# <Comment: Comment object (1)>
# >>> Comment.objects.create(commentPost=Post.objects.get(id=1), commentUser=Author.objects.get(id=1).authorUser, text='anytext')
# <Comment: Comment object (2)>
# >>> Comment.objects.create(commentPost=Post.objects.get(id=1), commentUser=Author.objects.get(id=1).authorUser, text='anytext')
# <Comment: Comment object (3)>
# >>> Comment.objects.create(commentPost=Post.objects.get(id=1), commentUser=Author.objects.get(id=1).authorUser, text='anytext')
# <Comment: Comment object (4)>

# Лайки и дислайки
# Comment.objects.get(id=1).like
# Comment.objects.get(id=1).dislike
# и можем проверить рейтинг вот так: Comment.objects.get(id=1).rating

# a = Author.objects.get(id=1)
# a.update_rating()
# a.ratingAuthor - посмотрим рейтинг

# for i in a:
# ...     i.ratingAuthor
# ...     i.ratingUser.username

# a = Author.objects.order_by('-ratingAuthor')[:1]
