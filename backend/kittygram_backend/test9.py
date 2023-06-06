import os

# Вывести значения переменных среды
print(os.environ.get('POSTGRES_USER'))
print(os.getenv('DB_NAME'))
