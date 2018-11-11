from flask import Flask, request, render_template
import formulas
import retirementCalc

app = Flask(__name__)

logged_in = True # Change this depending on whether the user is logged in (for later)
@app.route('/')
def index():
    return render_template('home.html',login = logged_in)

@app.route('/start')
def start():
    return render_template('start.html',login = logged_in)

@app.route('/retirement')
def retirement():
    return render_template('retirement.html',login = logged_in)

@app.route('/retirement', methods=['POST'])
def retirement_post():
    current_age = int(request.form['current_age'])
    years_left = int(request.form['years_left'])
    monthly_contribution = float(request.form['monthly_contribution'])
    total = float(request.form['total'])
    rate = float(request.form['rate'])
    retirementResult = \
        retirementCalc.Retire401K(current_age, years_left, monthly_contribution, total, rate).calc_401()

    return render_template('retirement_results.html', retirementResult=retirementResult)


@app.route('/mortgage')
def mortgage():
    return render_template('mortgage.html',login = logged_in)

@app.route('/mortgage', methods=['POST'])
# hello
def mortgage_post():
    rate_percentage = float(request.form['rate_percentage'])
    number_of_years = float(request.form['number_of_years'])
    principal_amount = float(request.form['principal_amount'])

    userMortgage= formulas.Mortgage(rate_percentage,number_of_years,principal_amount)
    userMonthly_Payment = int(userMortgage.monthly_payment())
    userTotal_Interest_Paid = int(userMortgage.total_interest_paid())

    A = formulas.graph_mortgage_times(rate_percentage, number_of_years, principal_amount)
    A.show()

    return render_template('mortgage_result.html', userMonthly_Payment=userMonthly_Payment,
                                                    userTotal_Interest_Paid=userTotal_Interest_Paid)


@app.route('/credit_payment')
def creditpayment():
    return render_template('credit_payment.html',login = logged_in)

@app.route('/credit_payment', methods=['POST'])
def creditpayment_post():
    apr_percentage = float(request.form['apr_percentage'])
    balance = float(request.form['balance'])
    monthly_payment = float(request.form['monthly_payment'])
    payment = formulas.Credit_Card_Payment(apr_percentage,balance,monthly_payment)
    payofftime = int(payment.payoff_time())

    A = formulas.graph_credit_payoff_times(apr_percentage, balance, monthly_payment)
    A.show()

    return render_template('creditpayment_result.html',payofftime=payofftime)

if __name__ == '__main__':
    app.run(debug=True)
