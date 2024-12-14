from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Конфигурация подключения к базе данных
DATABASE_URL = "postgresql+psycopg://postgres:123123@127.0.0.1:5432/demoexamorm"

# Создание движка для взаимодействия с базой данных
engine = create_engine(DATABASE_URL)

# Базовый класс для моделей SQLAlchemy
Base = declarative_base()

# Конфигурация сессии
Session = sessionmaker(bind=engine)

# Создание экземпляра сессии
session = Session()

# Проверка соединения с базой данных
def test_connection():
    try:
        with engine.connect() as connection:
            print("Подключение к БД произошло успешно")
    except Exception as e:
        print(f"Ошибка подключения к БД: {e}")

# Вызов проверки
test_connection()
