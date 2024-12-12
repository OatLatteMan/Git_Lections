# page_generator.py
import json

a_element = """
        <a href="{url}">
            <h2>{title}</h2>
            <img src="{img}" alt="{title}">
        </a>
"""

def gen_list():
    with open('Git_lections/Lekce_08_05.12.24/scraped_data.json', encoding='utf-8') as file:
        data = json.load(file)

        result = ''

        for item in data:
            link = a_element.format(
                url = item['url'],
                title = item['title'],
                img = item['img'],
            )
            result += link
        return result



def save_list():
    list_html = gen_list()
    with open('Git_Lections/Lekce_09_10.12.24/list.html', mode='r', encoding='utf-8') as file:
        html = file.read()
        html = html.replace('<!-- HTML -->', list_html)

    with open('Git_Lections/Lekce_09_10.12.24/list2.html', mode='w', encoding='utf-8') as file:
        file.write(html)

save_list()
