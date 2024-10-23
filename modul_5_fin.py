import hashlib
import time
class User:                                             # Класс User представляет пользователя на платформе
    def __init__(self, nickname, password, age):                # Инициализатор класса User.
        self.nickname = nickname                        # Атрибут класса User: nickname(имя пользователя, строка)
        self.password = self.hash_password(password)    # Атрибут класса User: password(в хэшированном виде, число)
        self.age = age                                  # Атрибут класса User: age(возраст, число)
    def hash_password(self,password):                   # Функция хеширования пароля
        return hashlib.sha256(password.encode()).hexdigest()    #Хеширование пароля с использованием алгоритма SHA-256
    def __eq__(self, other):
        return self.nickname == other.nickname          #Переопределяем метод сравнения, чтобы проверять
                                                        # пользователя по имени пользователя
    def __str__(self):                                  # Функция строкового представления имени и возраста пользователя
        return f'{self.nickname}'                       # return f"User(nickname='{self.nickname}', age={self.age})"
class Video:
    def __init__(self,  title, duration, adult_mode=False): # Инициализатор класса Video
        self.title = title                              # Атрибут класса Video: title(заголовок, строка)
        self.duration = duration                        # Атрибут класса Video: duration(продолжительность, секунды)
        self.time_now = 0                               # Атрибут класса Video: time_now(секунда остановки (изначально 0))
                                                        # Текущее время просмотра видео
        self.adult_mode = adult_mode                    # Атрибут класса Video: adult_mode(ограничение по возрасту,
                                                        # bool (False по умолчанию))
    def __eq__(self, other):                            # Функция проверки видео по заголовку
        return self.title.lower() == other.title.lower()#Переопределяем метод сравнения, чтобы проверять видео по заголовку
    def __str__(self):                                  # Функция строкового представления параметров видео.
        return f"Video(title = '{self.title}' , duration={self.duration} , adult_mode={self.adult_mode}"  #Обратить внимание!
class UrTube:                                           # Класс UrTube представляет платформу и включает
                                                        # методы для взаимодействия с пользователями и видео
    def __init__(self):                                 # Инициализатор класса UrTube
        self.users = []                                 # Список зарегистрированных пользователей
        self.videos = []                                # Список доступных видео
        self.current_user = None                        # Текущий пользователь
    def log_in(self , nickname, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        for users in self.users:
            if users.nickname == nickname and users.password == hashed_password:
                self.current_user = users
                print(f'Пользователь {nickname} вошел в систему')
                return True
            print('Ошибка входа. Неверный логин или пароль')
            return False
        # Метод register, принимает три аргумента: nickname, password, age, и добавляет пользователя
        # в список, если пользователя не существует (с таким же nickname).
        # После регистрации, вход выполняется автоматически.
    def register(self, nickname, password, age):
        new_user = User(nickname , password , age)
        if new_user in self.users:
            print(f'Пользователь {nickname}уже существует')
        else:
            self.users.append(new_user)
            self.current_user = new_user
            print(f'Пользователь {nickname}успешно зарегистрирован и вошел в систему')
    def log_out(self):                         # Метод log_out используется для сброса текущего пользователя на None
        if self.current_user:
            print(f'Пользователь {self.current_user.nickname}вышел из системы')
        else:
            print('В системе нет активного пользователя')
        # Метод add, принимает неограниченное кол-во объектов класса Video и все добавляет в videos,
        # если с таким же названием видео ещё не существует.  В противном случае ничего не происходит
    def add(self , *videos):
        for video in videos:                    # Если с таким же названием видео ещё не существуе
            self.videos.append(video)           # Добавляет video в videos
            print(f'Видео "{video.title}"добавлено')
        else:
                print(f'Видео "{video.title}"уже существует')
    # Метод get_videos, принимает поисковое слово и возвращает список названий всех видео,
    # содержащих поисковое слово.
    # Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best' (не учитывать регистр)
    def get_videos(self, search_term):
        search_term_lower = search_term.lower()
        return [video.title for video in self.videos if search_term_lower in video.title.lower()]
    # Метод watch_video, принимает название фильма, если не находит точного совпадения(вплоть до пробела),
    # то ничего не воспроизводится, если же находит - ведётся отчёт в консоль на какой секунде ведётся
    # просмотр. После текущее время просмотра данного видео сбрасывается.
    def watch_video(self, title):
        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, покиньте страницу')
                return
            print(f"Начинается воспроизведение видео: {video.title}")
            for second in range(video.time_now , video.duration + 1):
                print(second , end='' , flush=True)
                time.sleep(1)                             # Имитируем просмотр по одной секунде
                print('Конец видео')
                video.time_now = 0                        # Сбрасываем время остановки после полного просмотра
                return
        print("Видео не найдено")
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')











