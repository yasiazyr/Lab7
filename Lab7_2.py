import requests


def get_rickandmorty_character(character_name):

    URL = "https://rickandmortyapi.com/api/character"

    params = {
        'name': character_name
    }

    try:
        response = requests.get(URL, params=params, timeout=30)
        response.raise_for_status()

        data = response.json()
        characters = data['results']

        for character in characters:
            name = character['name']
            status = character['status']
            species = character['species']
            char_type = character['type'] if character['type'] else 'не указан'
            gender = character['gender']
            char_id = character['id']

            first_episode_url = character['episode'][0] if character['episode'] else None

            first_appearance = "неизвестно"
            if first_episode_url:
                try:
                    episode_response = requests.get(first_episode_url, timeout=10)
                    episode_response.raise_for_status()
                    episode_data = episode_response.json()
                    episode_name = episode_data['name']
                    episode_code = episode_data['episode']
                    first_appearance = f"{episode_code} - {episode_name}"
                except:
                    first_appearance = "информация временно недоступна"

            print(f"\n")
            print(f"Персонаж: {name}")
            print("-" * 35)
            print(f"ID: {char_id}")
            print(f"Статус: {status}")
            print(f"Вид: {species}")
            print(f"Тип: {char_type}")
            print(f"Пол: {gender}")
            print(f"Первое появление: {first_appearance}")

    except requests.exceptions.Timeout:
        print("Ошибка: Превышено время ожидания. Попробуйте снова.")
    except requests.exceptions.ConnectionError:
        print("Ошибка: Нет соединения с сервером.")
    except requests.exceptions.HTTPError as e:
        if response.status_code == 401:
            print("Ошибка: Неверный API ключ")
        else:
            print(f"Ошибка HTTP: {e}")
    except Exception as e:
        print(f"Ошибка: Персонаж '{character_name}' не найден")

print("Поиск информации о персонажах сериала Rick and Morty")
print("-" * 35)

character_name = input("Введите имя персонажа: ").strip()

if character_name:
    get_rickandmorty_character(character_name)
else:
    print("Ошибка: Вы не ввели имя персонажа")