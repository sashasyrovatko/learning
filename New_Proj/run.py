import time
from reader import ReaderCsv
from open_url import OpenUrl
from bot import Bot


reader = ReaderCsv('file.csv')
reader.file_list()
reader.get_url_list()
open = OpenUrl()
open.navigate_to_urls1()
open.navigate_to_all_pages()
model_list = open.navigate_to_urls1()
reader.write_data(model_list)
# open.navigate_to_urls2(reader.get_url_list())


time.sleep(30)