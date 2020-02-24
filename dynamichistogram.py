"""
g $$$$$$$$$$$$$$$$$$$$
f $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
t $$$$$$$$$$
o $$$$$$$$$$$$
"""


def histogram_maker(dictionary_of_sales):
	for company in dictionary_of_sales.keys():
		print(f"{company[0]} {dictionary_of_sales[company] * '$'}")

sales_Q1 = {
  'google': 20,
  'facebook': 25,
  'twitter': 10,
  'offline': 12,
}

sales_Q2 = {
  'google': 18,
  'facebook': 22,
  'twitter': 18,
	"amazon": 10,
  'offline': 13,
}

histogram_maker(sales_Q1)
print("--------------")
histogram_maker(sales_Q2)



# print('g ' + sales['google'] * '$')
# print('f ' + sales['facebook'] * '$')
# print('t ' + sales['twitter'] * '$')
# print('o ' + sales['offline'] * '$')
