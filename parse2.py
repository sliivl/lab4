import requests
from bs4 import BeautifulSoup
import fake_useragent
from random import randint

print("""
 #####    #####     ####     ####    ##        ####    #####   
 ##  ##   ##  ##   ##  ##   ##  ##   ##         ##     ##  ##  
 ##  ##   ##  ##   ##  ##   ##       ##         ##     ##  ##  
 #####    #####    ##  ##   ## ###   ##         ##     #####   
 ##       ####     ##  ##   ##  ##   ##         ##     ##  ##  
 ##       ## ##    ##  ##   ##  ##   ##         ##     ##  ##  
 ##       ##  ##    ####     ####    ######    ####    #####                                                              
""")


def parse_result(mainTag, mainClass, targetTag, targetClass = ''):
    check_block = soup.find(mainTag, mainClass)
    result_block = check_block.find_all(targetTag, targetClass)
    return result_block


user = fake_useragent.UserAgent().random
header = {"user-agent": user}
url = "https://proglib.io"
response = requests.get(url).text
soup = BeautifulSoup(response, 'lxml')

posts_names = parse_result('div', 'feed__items', 'h2', 'preview-card__title')
posts_content = parse_result('div', 'feed__items', 'div', 'preview-card__text')
posts = parse_result('div', 'feed__items', 'article', 'block preview-card')

random_index = randint(0, (len(posts_content)) - 1)

post_href = posts[random_index].find('a')

print(f"{posts_names[random_index].text.strip()}\n{posts_content[random_index].text.strip()} Ссылка - https://proglib.io{post_href.get('href')}")

input()

