#1.	Filtrowanie: Wykorzystaj funkcję filter() oraz wyrażenie lambda, aby stworzyć nową listę zawierającą tylko te urządzenia, których status to "online".
#2.	Sortowanie: Wykorzystaj funkcję sorted() na przefiltrowanej liście, aby uporządkować urządzenia według zużycia procesora (cpu_usage) w kolejności malejącej.
#3.	Wyświetlanie: Wypisz wynikową listę w konsoli.
# Format: {"host": nazwa, "status": stan, "cpu_usage": %, "uptime_dni": dni}
#Poprawna odpowiedź:
#{'host': 'Router_D', 'status': 'online', 'cpu_usage': 92, 'uptime_dni': 15}
#{'host': 'Router_A', 'status': 'online', 'cpu_usage': 85, 'uptime_dni': 120}
#{'host': 'Router_C', 'status': 'online', 'cpu_usage': 40, 'uptime_dni': 350}
#{'host': 'Router_E', 'status': 'online', 'cpu_usage': 15, 'uptime_dni': 200}
urzadzenia = [
    {"host": "Router_A", "status": "online", "cpu_usage": 85, "uptime_dni": 120},
    {"host": "Router_B", "status": "offline", "cpu_usage": 0, "uptime_dni": 0},
    {"host": "Router_C", "status": "online", "cpu_usage": 40, "uptime_dni": 350},
    {"host": "Router_D", "status": "online", "cpu_usage": 92, "uptime_dni": 15},
    {"host": "Router_E", "status": "online", "cpu_usage": 15, "uptime_dni": 200}
]
