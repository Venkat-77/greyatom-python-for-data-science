# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
path
filepath = path
bank = pd.read_csv(filepath) 
print(bank.head())
categorical_var  = bank.select_dtypes(include = 'object')
print("="*50)
print(categorical_var)
print("="*50)
numerical_var  = bank.select_dtypes(include = 'number')
print("="*50)
print(numerical_var) 



# code starts here






# code ends here


# --------------
# code starts here
import numpy as np
import pandas as pd
from scipy.stats import mode 
path
filepath = path
bank = pd.read_csv(filepath) 
banks = bank.drop('Loan_ID',axis=1)
banks = pd.DataFrame(banks)
print(banks.head())
print(banks.isnull().sum())
bank_mode = banks.mode()
print("="*50)
for column in banks.columns:
    banks[column].fillna(banks[column].mode()[0], inplace=True)
print("="*50)
print(banks.head(10))


# --------------
# Code starts here
import numpy as np
import pandas as pd
from scipy.stats import mode 
path
filepath = path
bank = pd.read_csv(filepath) 
banks = bank.drop('Loan_ID',axis=1)
banks = pd.DataFrame(banks)
print(banks.head())
print(banks.isnull().sum())
bank_mode = banks.mode()
print("="*50)
for column in banks.columns:
    banks[column].fillna(banks[column].mode()[0], inplace=True)
print("="*50)
print(banks.head(10))
avg_loan_amount = banks.pivot_table(index=['Gender','Married','Self_Employed'],values='LoanAmount',aggfunc='mean')
print("="*50)
print(avg_loan_amount)



# code ends here



# --------------
# code starts here

# code for loan aprroved for self employed
loan_approved_se = banks.loc[(banks["Self_Employed"]=="Yes")  & (banks["Loan_Status"]=="Y"), ["Loan_Status"]].count()
print(loan_approved_se)

# code for loan approved for non self employed
loan_approved_nse = banks.loc[(banks["Self_Employed"]=="No")  & (banks["Loan_Status"]=="Y"), ["Loan_Status"]].count()
print(loan_approved_nse)

# percentage of loan approved for self employed
percentage_se = (loan_approved_se * 100 / 614)
percentage_se=percentage_se[0]
# print percentage of loan approved for self employed
print(percentage_se)

#percentage of loan for non self employed
percentage_nse = (loan_approved_nse * 100 / 614)
percentage_nse=percentage_nse[0]
#print percentage of loan for non self employed
print (percentage_nse)

# code ends here


# --------------
# code starts here


# loan amount term 

loan_term = banks['Loan_Amount_Term'].apply(lambda x: int(x)/12 )


big_loan_term=len(loan_term[loan_term>=25])

print(big_loan_term)

# code ends here


# --------------
# code starts here
import numpy as np
import pandas as pd
from scipy.stats import mode 
path
filepath = path
bank = pd.read_csv(filepath) 
banks = bank.drop('Loan_ID',axis=1)
loan_groupby = banks.groupby('Loan_Status')['ApplicantIncome', 'Credit_History']
print(loan_groupby)
mean_values = banks.groupby('Loan_Status')['ApplicantIncome', 'Credit_History'].agg(np.mean)
print(mean_values)


# code ends here


