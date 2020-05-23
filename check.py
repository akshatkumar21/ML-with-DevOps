file = open('/mlops/Main_Build.py','r')
key = file.read()				

if 'keras' or 'tensorflow' in key:		
	if 'Conv2D' or 'Convolution' or 'Dense' in key:				
		print('CNNcode')
	else:
		print('not a CNNcode')
else:
	print('Not Deep Learning')