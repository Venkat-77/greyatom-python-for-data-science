# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
path
data = pd.read_csv(path)
loan_status = data['Loan_Status'].value_counts()
#loan_status = pd.DataFrame(loan_status)
print(loan_status)
plt.figure(figsize=[14,8])
plt.xlabel("Loan Status YES/NO")
plt.ylabel("Number")
plt.title("Loan Status")
plt.bar(loan_status.index,loan_status)
plt.show()





#Code starts here


# --------------
#Code starts here
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
path
data = pd.read_csv(path)
property_and_loan = data.groupby(['Property_Area','Loan_Status'])
property_and_loan = property_and_loan.size().unstack()
property_and_loan.plot(kind='bar', stacked=False, figsize=(15,10))
# Label X-axes and Y-axes
plt.xlabel('Property Area')
plt.ylabel('Loan Status')
# Rotate X-axes labels
plt.xticks(rotation=45)
# Display plot
plt.show()











# --------------
#Code starts here
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
path
data = pd.read_csv(path)
education_and_loan = property_and_loan = data.groupby(['Education','Loan_Status'])
education_and_loan = property_and_loan.size().unstack()
education_and_loan.plot(kind='bar', stacked=False, figsize=(15,10))
# Label X-axes and Y-axes
plt.xlabel('Education Status')
plt.ylabel('Loan Status')
# Rotate X-axes labels
plt.xticks(rotation=45)
# Display plot
plt.show()




# --------------
#Code starts here
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
path
data = pd.read_csv(path)
graduate = data[data['Education'] == 'Graduate']
print(graduate.head())
not_graduate = data[data['Education'] == 'Not Graduate']
print(not_graduate)
graduate['LoanAmount'].plot(kind='density', label='Graduate')
plt.show()
not_graduate['LoanAmount'].plot(kind='density', label='Not Graduate')
plt.show()









#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
fig, (ax_1, ax_2,ax_3) = plt.subplots(3,1, figsize=(20,10))
path
data = pd.read_csv(path)
ax_1.scatter(data['ApplicantIncome'],data["LoanAmount"])
ax_1.set_title("Applicant Income")
ax_2.scatter(data['CoapplicantIncome'],data["LoanAmount"])
ax_2.set_title("Coapplicant Income")

data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']
ax_3.scatter(data['TotalIncome'],data["LoanAmount"])
ax_3.set_title("Total Income")



