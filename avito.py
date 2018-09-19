#! /usr/bin/python3.5

# План
# 1. Сколько страниц
# 2. Сформировать список url на страницы выдачи
# 3.  Собрать данные


# #TODO
# Надо добавлять в БД и в файл
# проверять чтобы link был уникальным
# добавить возможность достать тел.
# достать картинку
# подробное описание
# работаем по принципу нашлась прокся, парсим пока не залочат, потом находим новую проксю
# Пересмотреть куда фоткнуть цикл для поиска прокси
# Сделать все классами

import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime, timedelta
import csv
from multiprocessing import Pool
from random import choice, uniform
from time import sleep
from os import environ

array_spec_words = ['suzuki', 'kawasaki', 'honda',
                    'yamaha', 'спорт', 'дорожник', 'нейкид', 'стрит-файтер']


template_task = "https://www.avito.ru/krasnodarskiy_kray/mototsikly_i_mototehnika/mototsikly?p="

months = ['Января',	'Февраля',	'Марта',	'Апреля',	'Мая',	'Июня',
          'Июля',	'Августа', 'Сентября',	'Октября',	'Ноября',	'Декабря']


class page_info:

	def __init__(self, link, usr_agent=None, proxy=None):
		self.link = link
		self.usr_agent = usr_agent
		self.proxy = proxy

	def get_html(self):
		r = requests.get(self.link, headers=self.usr_agent, proxies=self.proxy)
		self.text_page = r.text

	def get_last_page(self, html):
		html = self.text_page
		soup = BeautifulSoup(html, 'lxml')
		print(soup)
		last_page = soup.find('a', class_='pagination-page', text='Последняя')
		num_last_page = last_page.get('href')[-2:]
		return int(num_last_page)+1

# def write_csv(data):
# 	with open('main.csv', 'a', newline='') as f:
# 		writer = csv.writer(f, delimiter=';')
# 		writer.writerow((data['name'], data['price'], data['city'], data['time_publc'] ,data['link']))

# def normal_date(date):
# 	day = date.strftime('%d')
# 	month = months[ int(date.strftime('%m'))-1]
# 	return day + ' ' + month

# def dell_all_probel(text):
# 	return text.lstrip().rstrip()

# def get_page_date(html):
# 	soup = BeautifulSoup(html, 'lxml')
# 	# all_info = soup.find_all('div',class_='item_table-header')
# 	all_info = soup.find_all('div',class_='description item_table-description snippet-experiment-wrapper')
# 	# print('count_all_div', len(all_info))
# 	main_info = {}
# 	count = 0
# 	for inf in all_info:
# 		name = inf.find('a', class_='item-description-title-link').find('span').text.strip()
# 		link = inf.find('a', class_='item-description-title-link').get('href')
# 		price = inf.find('span', class_='price').get('content')
# 		city = inf.find('div', class_='data').find('p').text.strip()
# 		time_publc = inf.find('div', class_='js-item-date c-2').get('data-absolute-date')
# 		today = datetime.now().date()
# 		yesterday = today - timedelta(1)
# 		if re.findall('Сегодня', time_publc):
# 			time_publc = time_publc.replace('Сегодня', normal_date(today))
# 		elif re.findall('Вчера', time_publc):
# 			time_publc = time_publc.replace('Вчера', normal_date(yesterday))

# 		if price == '0':
# 			price = 'Цена не указана'
# 		for serch in array_spec_words:
# 			res = re.findall(serch.lower(), dell_all_probel(name.lower()))
# 			if res != []:
# 				main_info = {'name': dell_all_probel(name), 'price':dell_all_probel(price), 'city':dell_all_probel(city), 'time_publc':dell_all_probel(time_publc), 'link': dell_all_probel('https://www.avito.ru' + link)}
# 				write_csv(main_info)
# 				count +=1
# 				print(count)
# 			else:
# 				continue

# 	# try:
# 	# 	name = soup.find('a', class_='item-description-title-link').find('span').text.strip()
# 	# except:
# 	# 	name =''
# 	# print(main_info)

# def make_all(url, useragent=None, proxy=None):
# 	print('mk_all', url,useragent, proxy)
# 	html = get_html(url, useragent, proxy)
# 	get_page_date(html)

# def get_all_links_page(first_page, useragent=None, proxy=None):
# 	for_last_page = get_html(first_page, useragent, proxy)
# 	last_page = get_last_page(for_last_page)
# 	all_pages = []
# 	for i in range(1, last_page):
# 		# print('Страница №', i)
# 		url = template_task + str(i)
# 		all_pages.append(url)
# 	return all_pages


def main():
	home_dir = environ['HOME']
	# start = datetime.now()
	usr_agnts = open(home_dir + '/python_scripts/user_agents.txt').read().split('\n')
	proxys = open(home_dir + '/python_scripts/proxy_list.txt').read().split('\n')
	first_page = "https://www.avito.ru/krasnodarskiy_kray/mototsikly_i_mototehnika/mototsikly?p=1"
	for chanse in range(20):
		sleep(uniform(3,6))
		proxy = {'http': 'http://'+choice(proxys)}
		usr_agnt = {'User-Agent': choice(usr_agnts)}
		main_page = page_info(first_page, usr_agnt, proxy)
		html_text = main_page.get_html()
		last_page = main_page.get_last_page(html_text)
		print(chanse)
		#try:
			#main_page = page_info(first_page, usr_agnt, proxy)
			#html_text = main_page.get_html()
			#last_page = main_page.get_last_page(html_text)
			#print(last_page)
			#exit()
		#except:
			#continue

    # all_links_page = []
    # count = 0
  #while len(all_links_page) == 0:
     #	sleep(uniform(3,6))
    # 	proxy = {'http': 'http://'+choice(proxys)}
    # 	usr_agnt = {'User-Agent': choice(usr_agnts)}
    # 	try:
    # 		all_links_page = get_all_links_page(first_page)
    # 	except:
    # 		continue
    # 	all_links_page = get_all_links_page(first_page)
    # 	count += 1
    # 	print(count)
    # for task in range(1000):
    # 	sleep(uniform(3,6))
    # 	proxy = {'http': 'http://'+choice(proxys)}
    # 	usr_agnt = {'User-Agent': choice(usr_agnts)}
    # 	print(proxy, usr_agnt)
    # 	for num_list in all_links_page:
    # 		try:
    # 			make_all(num_list, usr_agnt, proxy)
    # 		except:
    # 			continue
    # 		make_all(num_list, usr_agnt, proxy)
    # end = datetime.now()
    # total = end - start
    # print(str(total))


if __name__ == "__main__":
    main()
