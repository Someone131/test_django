
class User:         # класс, содержащий информаци о пользователе
    def __init__(self, name, mail):
        self.name = name
        self.mail = mail


class Post(User):
    def __init__(self, title, date, text):
        self.title = title
        self.date = date    # впоследствии - текущая дата создания
        self.text = text
    pass


class Blog (Post):
    def __init__(self):
        super.__init__()
        self.news_feed = {}  # словарь с лентой новойстей, где ключ - тема, значение - текст
        self.subscribers = {}  # словарь с подписчиками, где где ключ - имя пользователя - подписчика,
        # значение - электронная почта подписчика
        self.subscribed = {}  # словарь с пользователями, на которые подписан, где где ключ - имя пользователя,
        # значение - электронная почта пользователя
        self.posts = {} # словарь с постами пользователя

    def send_message(self, message, user):  # метод - отправка сообщений пользователям
        pass

    def new_post(self, title, text):
        post=Post(title, text)
        self.posts.append(post)
        for user in self.subscribers.items():
            self.send_message(("User " + user.key + "aded new post: " + title + "/n" + text, user))

    def subscribe(self, user):  # метод - подписка на другого пользователя
        self.subscribed.append(user)
        pass

    def unsubscribe(self, user):  # метод - отписаться от другого пользователя
        self.subscribed.pop(user.key)
        pass