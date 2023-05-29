from flask import Flask,request,render_template
import pickle 
import pandas as pd

credit = Flask(__name__)

@credit.route('/')
def fun1():
    return render_template('credit_score.html')

@credit.route('/predict',methods=['post'])
def fun2():
    name = request.form['name']
    age = request.form['age']
    annual_income = request.form['annual_income']
    salary = request.form['salary']
    no_of_acc = request.form['no_of_acc']
    no_of_cc = request.form['no_of_cc']
    int_rate = request.form['int_rate']
    tfl = request.form['tfl']
    dfdd = request.form['dfdd']
    nfdp = request.form['nfdp']
    ccl = request.form['ccl']
    nfci = request.form['nfci']
    cm = request.form['cm']
    ob = request.form['ob']
    cha = request.form['cha']

    mymodel = pickle.load(open('credit_score.pkl', 'rb'))
    values = [[age,annual_income,salary,no_of_acc,no_of_cc,int_rate,tfl,dfdd,nfdp,ccl,nfci,cm,ob,cha]]
    df = pd.DataFrame(data=values,columns=['Age','Annual_Income','Monthly_Inhand_Salary','Num_Bank_Accounts','Num_Credit_Card','Interest_Rate','Type_of_Loan','Delay_from_due_date','Num_of_Delayed_Payment','Changed_Credit_Limit','Num_Credit_Inquiries','Credit_Mix','Outstanding_Debt','Credit_History_Age'])

    score = mymodel.predict(df)[0]
    return "{}'s credit score is {}".format(name, score)

if __name__=='__main__':
    credit.run(debug=True)