"""
Flask financial calculation code
"""
import pylab
import types
import math
import copy
import matplotlib.pyplot as plt 

def _dict2lists(data):
    """
    Convert a dictionary into a list of keys and values, sorted by
    key.  

    Arguments:
    data -- dictionary

    Returns:
    A tuple of two lists: the first is the keys, the second is the values
    """
    xvals = data.keys()
    xvals.sort()
    yvals = []
    for x in xvals:
        yvals.append(data[x])
    return xvals, yvals





class Mortgage():
	def __init__(self, rate_percentage, number_of_years, principal_amount):
		self.r = rate_percentage
		self.n = number_of_years 
		self.p = principal_amount 

	def monthly_payment(self):

		"""
		This is a method for calculating the monthly payment for a home 
		mortgage given the rate percentage, number of years, and principal amount
		"""
		if (self.r==0):
			
			#print ("If the interest rate percentage is zero, then the monthly payment is simply the principal divided by the total number of months")
			return (self.p)/(self.n*12)
		else:
			numerator = ((self.r/1200.0)*self.p)
			denominator = (1-(1+(self.r/1200))**-(self.n*12))
			#(1-(1+pow((self.r/1200.0),-(self.n*12))))
			if (1-(1+(self.r/1200))**-(self.n*12))==0:
				return 0
			final = numerator/denominator
			return round(final,2)

	def total_interest_paid(self):
		total_payment = self.monthly_payment()*self.n*12-self.p
		return total_payment
	

def graph_mortgage_times(rate_percentage, number_of_years, principal_amount):
	"""
	This function creates a credit payment object with given APR, Balance, and monthly payment.
	It then procees to create a dictionary where each value is the payment incremented and the corresponding value
	is the time in months to payoff the balance given the key payment. Therefore, you should see a 
	decrease in time to payoff the balance as the monthly payment increases.
	"""
	
	empty_dict = {}
	
	for i in range(1,10):
		new_time = Mortgage(rate_percentage, i*number_of_years, principal_amount)
		empty_dict[i*number_of_years] = new_time.total_interest_paid()

	keys = empty_dict.keys()
	keys.sort()
	print 'number of years  total interest paid'
	for key in keys:
		for key2 in empty_dict.keys():
			if (key==key2):
				print (str(key)+"               $"+str(empty_dict[key]))
	A=_dict2lists(empty_dict)
	plt.plot(A[0],A[1])
	plt.xlabel('number of years paying interest')
	plt.ylabel('total interest paid (dollars)')
	return plt



#A = Mortgage(6.5,200000,30)
#print A.total_interest_paid()

#graph_mortgage_times(6.5,30,200000)



class Credit_Card_Payment():

	def __init__(self, APR_percentage, Balance, Monthly_payment):

		self.a = APR_percentage
		self.b = Balance
		self.p = Monthly_payment

	def payoff_time(self):
		"""
		This is a method which returns the time it takes to payoff an input credit card balance with 
		an input APR percentage and an input monthly payment

		https://www.vcalc.com/wiki/KurtHeckman/Credit+Card+Equation
		"""
		units = 'months'
		percent = self.a/100.0
		if (((1+(self.b/self.p)*(1-(1+(percent/365))**30))) or (1+(percent/365.0))) < 0: #if required to take log a negative,
		#return not feasible
			return 0


		numerator = math.log((1+(self.b/self.p)*(1-(1+(percent/365))**30)))
		denominator = math.log(1+(percent/365.0))


		result = ((-1.0/30)*(numerator/denominator))

		if (units.lower() == 'years'):
			return round(result*0.0833,2)
		elif (units.lower() == 'months'):
			return round(result,2)
		elif (units.lower() == 'weeks'):
			return round(result*4.345,2)
		elif (units.lower() == 'days'):
			return round(result*30.417,2)
		else:
			return "Select only years, months, weeks, or days"
	
	

def graph_credit_payoff_times(APR, Balance, monthly_payment):
	"""
	This function creates a credit payment object with given APR, Balance, and monthly payment.
	It then procees to create a dictionary where each value is the payment incremented and the corresponding value
	is the time in months to payoff the balance given the key payment. Therefore, you should see a 
	decrease in time to payoff the balance as the monthly payment increases.
	"""
	
	empty_dict = {}
	
	for i in range(1,10):
		new_time = Credit_Card_Payment(APR, Balance, i*monthly_payment)
		empty_dict[i*monthly_payment] = new_time.payoff_time()

	keys = empty_dict.keys()
	keys.sort()
	print 'monthly payment  payoff time (months)'
	for key in keys:
		for key2 in empty_dict.keys():
			if (key==key2):
				print (str(key)+"               $"+str(empty_dict[key]))
	A=_dict2lists(empty_dict)
	plt.plot(A[0],A[1])
	plt.xlabel('monthly payment amount (dollars)')
	plt.ylabel('payoff time (months)')
	return plt

A = Credit_Card_Payment(3,1000, 800)
#print A.payoff_time('months')
#print A.payoff_time('months')
#graph_credit_payoff_times(4,10000,100)



def calculate_APR(i,q):
	"""
	This function calculates the APR
	i = yearly interest rate
	q = how many times i is compounded per year
	"""
	r = (1+(i/(q*1.0)))**q-1

	return r

#print calculate_APR(2,3)

def calculate_interest_rate_from_APR(r,q):

	i = q*(((1+r)**(1/(q*1.0)))-1)

	return i

#print calculate_interest_rate_from_APR(2,3)


