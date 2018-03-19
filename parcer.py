fromhtml.parser importHTMLParser
fromurllib.request importurlopen

classMyHTMLParser(HTMLParser):
    def__init__(self, site_name, *args, **kwargs):
        # список ссылок
        self.links =[]
        # имя сайта
        self.site_name =site_name
        # вызываем __init__ родителя
        super().__init__(*args, **kwargs)
        # при инициализации "скармливаем" парсеру содержимое страницы
        self.feed(self.read_site_content())
        # записываем список ссылок в файл
        self.write_to_file()


	  defhandle_starttag(self, tag, attrs):
     # проверяем является ли тэг тэгом ссылки
     iftag =='a':
         # находим аттрибут адреса ссылки
         forattr inattrs:
             ifattr[0] =='href':
                 # проверяем эту ссылку методом validate() (мы его еще напишем)
                 ifnotself.validate(attr[0]):
                     # вставляем адрес в список ссылок
                          self.links.append(attr[1])
defvalidate(self, link):
     """ Функция проверяет стоит ли добавлять ссылку в список адресов. 
     В список адресов стоит добавлять если ссылка:
          1) Еще не в списке ссылок
          2) Не вызывает javascript-код
          3) Не ведет к какой-либо метке. (Не содержит #) 
      """
      returnlink inself.links or'#'inlink or'javascript:'inlink
defread_site_content(self):
    returnstr(urlopen(self.site_name).read())
   # открываем файл
     f =open('links.txt', 'w')
     # записываем отсортированный список ссылок, каждая с новой строки
     f.write('\n'.join(sorted(self.links)))
     # закрываем файл
     f.close()
