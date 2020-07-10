import os

images = 'C:\\VIT\\SET\\CODE\\darkflow-master\\new_model_data\\images'
a_list= 'C:\\VIT\\SET\\CODE\\darkflow-master\\new_model_data\\annotations'

images_list=os.listdir(images)
annot_list=os.listdir(a_list)

for img in images_list:
	img=img[:-4]
	if img+'.xml' not in annot_list:
		print(img+'.jpg')
		os.remove(images+'\\'+img+'.jpg')
	