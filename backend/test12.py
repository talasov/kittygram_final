import os
from dotenv import load_dotenv

# Загрузить переменные среды из файла .env
load_dotenv()

# Вывести значения переменных среды
print(os.environ.get('POSTGRES_USER'))
print(os.getenv('DB_NAME'))
