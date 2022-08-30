# NewsPortal

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

# апдейтим рейтинг авторов
# author1.update_rating()
# author2.update_rating()

# Вывод рейтинг Author с наибольшим рейтингом
# best_author = Author.objects.all().order_by('-rating').values('user', 'rating')[0]
# Author.objects.get(rating=best_author['rating'])

# Вывод статьи\новости с наибольшим рейтингом
# best_post = Post.objects.all().order_by('-rating').values('time_pub', 'author', 'rating', 'title', 'body')[0]
# the_post = Post.objects.get(rating=best_post['rating'])
# the_post

# best_post_comments = the_post.comment_set.all()
# best_post_comments
