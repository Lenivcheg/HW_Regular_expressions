# import re

import csv


contact_list_right = []
with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

for item in contacts_list:
    correct_name = ' '.join(item[:3]).split(' ')

    res = [correct_name[0], correct_name[1], correct_name[2], item[3], item[4], item[5], item[6]]

    contact_list_right.append(res)


# with open("phonebook.csv", "w", encoding="utf-8") as f:
#   datawriter = csv.writer(f, delimiter=',')
#   # Вместо contacts_list подставьте свой список
#   datawriter.writerows(contact_list_right)
