# --------------
# Importing header files
import numpy as np
path

# Path of the file has been stored in variable called 'path'

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
data_file = path # path for the file
data=np.genfromtxt(data_file, delimiter=",", skip_header=1)
print("\nData: \n\n", data)
print("\nType of data: \n\n", type(data))
census = np.concatenate((data, new_record), axis=0)
print(census)

#Code starts here



# --------------
#Code starts here
path
age = np.zeros((1001,), dtype=int)
age = census[:, 0]

max_age = np.max(age)
min_age = np.min(age)
age_mean = np.mean(age)
age_std = np.std(age)
print(max_age)
print(min_age)
print(age_mean)
print(age_std)





# --------------
#Code starts here
import numpy as np
path
data_file = path # path for the file
data=np.genfromtxt(data_file, delimiter=",", skip_header=1)
ra= []
race = np.array(ra)
x = census.shape[0]
race_0=census[census[:,2]==0]
race_1=census[census[:,2]==1]
race_2=census[census[:,2]==2]
race_3=census[census[:,2]==3]
race_4=census[census[:,2]==4]
len_0 = race_0.shape[0]
print(len_0)
len_1 = race_1.shape[0]
print(len_1)
len_2 = race_2.shape[0]
print(len_2)
len_3 = race_3.shape[0]
print(len_3)
len_4 = race_4.shape[0]
print(len_4)
print(len(race_0))
minority_race = 3
print(minority_race)





# --------------
#Code starts here
working_ho = []
working_hours = np.array(working_ho)
senior_citizens = census[census[:,0]>60]
#print(senior_citizens)
working_hours = senior_citizens[:,6]
print(working_hours)
senior_citizens_len = len(working_hours)
print(senior_citizens_len)
working_hours_sum = np.sum(working_hours) 
avg_working_hours = working_hours_sum/senior_citizens_len
print(avg_working_hours)


# --------------
#Code starts here
hi = []
lo = []
high = np.array(hi)
low = np.array(lo)
high = census[census[:,1]>10]
low = census[census[:,1]<=10]
avg_pay_high = np.mean((high[:,7]))
print(avg_pay_high)
avg_pay_low = np.mean((low[:,7]))
print(avg_pay_low)


