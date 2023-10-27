
import os
import requests
import csv
import ast


# error_images=[["LC08_L1GT_222061_20230222_20230301_02_T2_B4.TIF","LC08_L1GT_222061_20230222_20230301_02_T2_B5.TIF","LC08_L1GT_222061_20230222_20230301_02_T2_B6.TIF"],["xxxxxLC08_L1GT_222061_20230222_20230301_02_T2_B4.TIF","xxxxxLC08_L1GT_222061_20230222_20230301_02_T2_B5.TIF","xxxxLC08_L1GT_222061_20230222_20230301_02_T2_B6.TIF"]]
error_images2=[["LC08_L1GT","222061_20230222_20230301_02_T2_B4.TIF"],["LC08_L1GT","LC08_L1GT_222061_20230222_20230301_02_T2_B5.TIF"],["LC08_L1GT","LC08_L1GT_222061_20230222_20230301_02_T2_B6.TIF"],["LC08_L1GT","xxxxxLC08_L1GT_222061_20230222_20230301_02_T2_B4.TIF"],["LC_L1GT","xxxxxLC08_L1GT_222061_20230222_20230301_02_T2_B5.TIF"],["LC08_L1GT","xxxxLC08_L1GT_222061_20230222_20230301_02_T2_B6.TIF"]]
#Repositório para salvar os arquivos gerados
path_save_files = "/home/lucasalves/workspace/Pessoal_Projetos/x/Color_Composition_Satellite_Imagery_Landsat" #"caminho_do_destino"
# os.makefile("errors_images_20230306.csv", exist_ok=True)
file= "/home/lucasalves/workspace/Pessoal_Projetos/x/Color_Composition_Satellite_Imagery_Landsat/errors_images_20230306.csv"


print(os.getcwd())

if os.path.isdir(path_save_files):
	print("Foi---0----->>>>")
	with open(os.path.join(path_save_files,"errors_images_20230306.csv"), 'w', newline='') as f:
		print("Foi---1----->>>>")
		writer = csv.writer(f)
		writer.writerows(error_images2)
# 	with open(os.path.join(path_save_files,"catalog_images.csv"), 'w', newline='') as f:
# 		print("Foi---2----->>>>")
# 		writer = csv.writer(f)
# 		writer.writerows(catalog_metadata)
# 	with open(os.path.join(path_save_files,"error_scnes.csv"), 'w', newline='') as f:
# 		print("Foi---3----->>>>")
# 		writer = csv.writer(f)
# 		writer.writerows(error_scnes)
# else:
	print(path_save_files, " não é um repositório válido.")



# with open(os.path.join(path_save_files,"errors_images_20230306.csv"), 'w', newline='') as f: writer = csv.writer(f); writer.writerows(error_images2)




