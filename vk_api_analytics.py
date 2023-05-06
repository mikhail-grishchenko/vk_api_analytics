import pandas as pd
import requests
import time
import random
import datetime
import re
from colorama import init, Fore, Back, Style
init(autoreset=True)


class Function():
    def __init__(self):
        self.token_friends = '' #token_friends
        self.user_id = #user_id
        self.version = 5.131
        self.group_id ='' #group_id
        self.owner_id = [] #owner_ids

    def get_offset(self):
        count = requests.get('https://api.vk.com/method/groups.getMembers', params={
                'group_id': self.group_id,
                'fields': 'city, last_seen',
                'access_token': self.token_friends,
                'v': self.version,
                'sort': 'city',
                'offset': 0,
            }).json()['response']['count']
        return count // 1000

    def get_users(self):
        self.city_list = [] #city_list
        self.city_list2 = [] #city_list2
        good_id_list = []
        response_list = []
        offset = 0
        max_offset = self.get_offset()
        while offset <= max_offset:
            response = requests.get('https://api.vk.com/method/groups.getMembers', params={
                'access_token': self.token_friends,
                'v': self.version,
                'group_id': self.group_id,
                'offset': offset*1000,
                'fields': 'domain, city, last_seen, sex',
              }).json()['response']
            offset += 1
            response_list += response['items']

        for city_title in self.city_list:
            for elem in response_list:
                try:
                    if elem['city']['title'] == city_title and elem['sex'] == 1 and elem['last_seen']['time'] > 1675238282:
                        good_id_list.append(elem['id'])
                except Exception as E:
                    print(E)
                    continue
        return good_id_list

    def save_data(self, data, filename):  # Функция сохранения базы в txt файле
        with open(filename, "w") as file:  # Открываем файл на запись
            # Записываем каждый id'шник в новой строке,
            # добавляя в начало "vk.com/id", а в конец перенос строки.
            for item in data:
                file.write(str(item) + "\n")

    def save_data_add(self, data, filename):  # Функция сохранения базы в txt файле
        with open(filename, "r+") as file:  # Открываем файл на запись  в режиме "чтение и обновление"
            for item in data:
                try:
                    file.seek(0, 2)
                    file.write(str(item) + "\n")
                except Exception as EE:
                    print(EE)
                    continue

    def enter_data(self, filename):  # Функция ввода базы из txt файла
        with open(filename) as file:  # Открываем файл на чтение
            b = []
            # Записываем каждую строчку файла в список,
            # убирая "vk.com/id" и "\n" с помощью среза.
            for line in file:
                # b.append(line[9:len(line) - 1])
                b.append(line[0:len(line) - 1])
            # print(1)
        return b


    def get_offset_getRequests(self):
        print(Style.BRIGHT + Back.GREEN + Fore.BLACK + 'some_function.\n')
        count_var = requests.get('https://api.vk.com/method/friends.getRequests', params={
                'access_token': self.token_friends,
                'v': self.version,
                'count': 1000,
                'offset': 0,
                'extended': 1,
                'need_mutual': 1,
                'out': 1,
            }).json()['response']['count']
        return count_var//1000


    def friends_getRequests(self):
        offset = 0
        max_offset = self.get_offset_getRequests()
        friends_getrequests_list = []
        friends_getrequests_id = []
        while offset <= max_offset:
            count_var = requests.get('https://api.vk.com/method/friends.getRequests', params={
                'access_token': self.token_friends,
                'v': self.version,
                'count': 1000,
                'offset': offset*1000,
                'extended': 1,
                'need_mutual': 1,
                'out': 1,
            }).json()['response']
            offset += 1
            friends_getrequests_list += count_var['items']
        for elem in friends_getrequests_list:
            friends_getrequests_id.append(elem['user_id'])
        return friends_getrequests_id

    def get_offset_friends_get(self):
        print(Style.BRIGHT + Back.GREEN + Fore.BLACK + 'some_function.\n')
        count_var = requests.get('https://api.vk.com/method/friends.get', params={
                'access_token': self.token_friends,
                'v': self.version,
                'count': 1000,
                'offset': 0,
                'extended': 1,
                'need_mutual': 1,
                'out': 1,
            }).json()['response']['count']
        return count_var//1000


    def friends_get(self):
        offset = 0
        max_offset = self.get_offset_friends_get()
        friends_get_list = []
        while offset <= max_offset:
            count_var = requests.get('https://api.vk.com/method/friends.get', params={
                'access_token': self.token_friends,
                'v': self.version,
                'count': 1000,
                'offset': offset*1000,
                'extended': 1,
                'need_mutual': 1,
                'out': 1,
            }).json()['response']
            offset += 1
            friends_get_list += count_var['items']
        return friends_get_list


    def get_offset_getSubscriptions(self):
        print(Style.BRIGHT + Back.GREEN + Fore.BLACK + 'some_function.\n')
        count_var = requests.get('https://api.vk.com/method/users.getSubscriptions', params={
                'access_token': self.token_friends,
                'user_id': self.user_id,
                'v': self.version,
                'count': 200,
                'offset': 0,
                'extended': 1,
            }).json()['response']['count']
        return count_var//200


    def users_getSubscriptions(self):
        offset = 0
        max_offset = self.get_offset_getSubscriptions()
        friends_get_list = []
        friends_get_id = []
        while offset <= max_offset:
            count_var = requests.get('https://api.vk.com/method/users.getSubscriptions', params={
                'access_token': self.token_friends,
                'user_id': self.user_id,
                'v': self.version,
                'count': 200,
                'offset': offset*200,
                'extended': 1,
            }).json()['response']
            offset += 1
            friends_get_list += count_var['items']
        for elem in friends_get_list:
            friends_get_id.append(elem['id'])
        return friends_get_id

    def wall_get(self, owner_id):
        wall_post = requests.get('https://api.vk.com/method/wall.get', params={
            'access_token': self.token_friends,
            'owner_id': owner_id,
            'v': self.version,
            'count': 10,
        }).json()['response']
        wall_text = []
        for elem in wall_post['items']:
            try:
                if elem['copy_history'][0]['text']:
                    wall_text.append(elem['copy_history'][0]['text'])
            except Exception as EE:
                print(EE)
            try:
                if elem['text']:
                    wall_text.append(elem['text'])
            except Exception as EE2:
                print(EE2)
                continue
        return wall_text

    def word_cleaner(self):
        post_text_list = []
        for elem in self.owner_id:
            try:
                post_text_list.extend(self.wall_get(elem))
                time.sleep(random.randint(2,3))
            except Exception as EE:
                print(EE)
                continue
        clean_text_list = []
        for elem2 in post_text_list:
            clean_text_list.extend(re.split('[:/ .!?_—="+*,\n-\n\n|#😄😋%°📌✔@❌🐞👏🍀👯💥🔥🏆🎁❤()]+', elem2.lower()))
        return clean_text_list

    def clean_post_word_list(self, owner_id):
        post_text_list = []
        try:
            post_text_list.extend(self.wall_get(owner_id))
            time.sleep(random.randint(2,3))
        except Exception as EE:
            print(EE)
        clean_text_list = []
        for elem2 in post_text_list:
            clean_text_list.extend(re.split('[:/ .!?_—="+*,\n-\n\n|#😄😋%°📌✔@❌🐞👏🍀👯💥🔥🏆🎁❤()]+', elem2.lower()))
        return clean_text_list


    def some_function(self):
        print(Style.BRIGHT + Back.GREEN + Fore.BLACK + 'some_function.\n')
        name_file = 'LOGS\log_' + str(datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')) + '.txt'
        self.save_data('', filename=name_file)
        data_id_new = self.enter_data(filename="data_id_new.txt")
        friends_get_id = self.enter_data(filename="friends_get_id.txt")
        friends_getRequests_id = self.enter_data(filename="friends_getRequests_id.txt")
        users_getSubscriptions = self.enter_data(filename="users_getSubscriptions.txt")
        black_list = self.enter_data(filename="black_list.txt")
        used_id_list = self.enter_data(filename="used_id_list.txt")
        some_user_id = self.enter_data(filename="some_user_id.txt")
        some_user_words = self.enter_data(filename="some_user_words.txt")
        num = 0
        num_max = random.randint(37, 39)
        print(Style.BRIGHT + Back.GREEN + Fore.BLACK + f'some_function{num_max}\n')
        some_function_exc = []
        some_function_fin = []
        try:
            for elem in data_id_new:
                if elem not in friends_get_id:
                    if elem not in friends_getRequests_id:
                        if elem not in users_getSubscriptions:
                            if elem not in black_list:
                                if elem not in used_id_list:
                                    if elem not in some_user_id:
                                        if num < num_max:
                                            word_list_elem = self.clean_post_word_list(elem)
                                            list_c = list(set(word_list_elem) & set(some_user_words))
                                            print(list_c)
                                            if len(list_c) > 5:
                                                self.save_data_add([elem], filename="some_user_id.txt")
                                                print(f"some_function {elem}.")
                                            else:
                                                some_function_id = []
                                                try:
                                                    time.sleep(random.randint(2, 7))
                                                    #Some function
                                                    print(Style.BRIGHT + Back.GREEN + Fore.BLACK + f"ID {elem} some_function\n")
                                                    some_function_id.extend([datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S'), elem])
                                                    self.save_data_add(some_function_id, filename=name_file)
                                                    self.save_data_add([elem], filename="used_id_list.txt")
                                                    time.sleep(random.randint(151, 187))
                                                    num += 1
                                                except Exception as E:
                                                    print(E)
                                                    some_function_id.extend([datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S'), E, elem])
                                                    self.save_data_add(some_function_id, filename=name_file)
                                                    self.save_data_add([elem], filename="used_id_list.txt")
                                                    continue
        except Exception as E:
            print(E)
            some_function_exc.extend([datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S'), E, elem])
            self.save_data_add(some_function_exc, filename=name_file)
            self.save_data_add([elem], filename="used_id_list.txt")

        some_function_fin.extend([datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S'), f"some_function {num}."])
        self.save_data_add(some_function_fin, filename=name_file)
        print(Style.BRIGHT + Back.GREEN + Fore.BLACK + f"some_function{num}.\n")


    def unique_filter (self):
        non_unique_list = self.enter_data(filename="data_id_new.txt")
        non_unique_list_df = pd.DataFrame(non_unique_list)
        return pd.unique(non_unique_list_df[0])



get_ids = Function()
get_ids.save_data(get_ids.friends_get(), filename="friends_get_id.txt")
get_ids.save_data(get_ids.friends_getRequests(), filename="friends_getRequests_id.txt")
get_ids.save_data(get_ids.users_getSubscriptions(), filename="users_getSubscriptions.txt")

time.sleep(random.randint(24, 35))

some_function = Function()
some_function.some_function()
input(Style.BRIGHT + Back.GREEN + Fore.BLACK + 'Нажмите любую клавишу для завершения программы...')
