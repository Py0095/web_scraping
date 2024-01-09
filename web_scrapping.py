import requests
from bs4 import BeautifulSoup as bs

response = requests.get('https://pnh.gouv.ht/')


if response.status_code == 200:
    print('tout bagay ok!!!')
    # parsePage = bs(response.content,'lxml')
    #li jere erreur tou men pa pi byn ke htmm5lib lan
    parsePage = bs(response.content,'html.parser')
    #li jere erreur html yo li pi lan 
    # parsePage = bs(response.content,'html5lib')
    # print(parsePage.h1)
    # print(parsePage.form.h1)
    # btn = parsePage.find('button',{'class':'btn'})
    # print(btn)
    # links = parsePage.find('body')
    # print(links.get_text())
    # for  link in links:
    #     print(link.string)

    print(parsePage.select('div h1'))
elif response.status_code == 404:
    print('page la pa egziste!!!')
else:
    print('bagay yo pa bon!!!')