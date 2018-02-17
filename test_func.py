def get_vat(price, vat_rate):
	price = float (price)
	if price < 0:
		price = price*(-1)
	vat = price / 100 * vat_rate
	price_no_vat = price - vat
	print (price_no_vat)

price1 = '1.5'
vat_rate1 = 18
get_vat(price1, vat_rate1)


def get_summ (one, two, delimeter = ' '):
	summ = str(one) + str(delimeter) + str (two)
	return summ.upper()


print(get_summ ('Hello', 'word'))