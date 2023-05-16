import time

from New_Proj.checker_price import CheckerPrice
from New_Proj.send_mail import SendMail
from reader import ReaderCsv
from open_url import OpenUrl


reader = ReaderCsv('file.csv')
reader.file_list()
reader.get_url_list()
open = OpenUrl()
open.navigate_to_urls1()
model_dict = open.navigate_to_urls1()
reader.write_data(model_dict)
checker = CheckerPrice("output.csv", reader, open)
change_models = checker.compare_prices(model_dict)
print(change_models)
sender_email = None
sender_password = None
receiver_email = None
email_sender = SendMail(sender_email, sender_password, receiver_email)
email_sender.send_discount_email(change_models)







time.sleep(30)