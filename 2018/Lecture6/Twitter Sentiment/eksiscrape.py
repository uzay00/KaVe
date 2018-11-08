from lxml import html
from requests import get, RequestException
from user_agent import generate_user_agent

url = 'https://eksisozluk.com/mustafa-kemal-ataturk--34712'
ua = generate_user_agent(device_type="desktop", os=('linux', 'mac'))

def get_content(url):
    try:
        res = get(url, headers={'User-Agent': ua})
        status = res.status_code
        if status == 200:
            return res.content
        else:
            print(status)
    except RequestException as ex:
        print('Request Error!')
        print(ex)
    except KeyboardInterrupt:
        print('The request is interrupted!')

def get_entries(url, num_fetch):
    entries = []
    page = 1

    while len(entries) < num_fetch:
        html_element = html.document_fromstring(get_content(url + '?p=' + str(page)))
        entries.extend(entry.text_content().strip() for entry in html_element.xpath('.//div[@class="content"]') if len(entries) < num_fetch)
        page += 1

    return entries

entries = get_entries(url, 20)
for i, entry in enumerate(entries):
    print('Entry %d: %s' % (i+1, entry))