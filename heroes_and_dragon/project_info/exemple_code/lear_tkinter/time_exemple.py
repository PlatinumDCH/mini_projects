from datetime import datetime

now = datetime.now()
min = now.minute
sec = now.second
print(f'{min}:{sec}')