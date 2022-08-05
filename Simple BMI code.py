#BMI stand for Body Mass Index
#BMI calculator using Python
#BMI=BMI = Weight(kg)/Height(m)^2
# Lets get start
#BMI stand for Body Mass Index

Weight = float(input("Enter weight in KG: "))
Height = float(input("Enter height in meter: "))
Height = Height*Height

#Now calculating BMI
BMI = Weight/Height
print("your Body Mass Index is here: ",BMI)
#Decition On BMI
if(BMI>0):
	if(BMI<=16):
		print("you are severely underweight.")
	elif(BMI<=18.5):
		print("you are underweight")   #Try to increase some
	elif(BMI>18.5 and BMI<=25):
		print("you are Healthy")  #Great job 
	elif(BMI>25 and BMI<=30):
		print("you are overweight")  #Try to decrease some      
	else: print("you are severely overweight")
else:("enter valid details")