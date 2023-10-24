import os
import requests
import csv
import ast
import shutil
print("--","len(scene)","---->>>")


path_root = './'
# path_root = os.getcwd()
path_downlad = os.path.join(path_root, 'Download_scenes')
path_scenes = os.path.join(path_root, 'LC08')



#lista os arquivos
path_temp = os.getcwd()
os.chdir(path_downlad)
list_all_files= list(filter(os.path.isfile, os.listdir()))
os.chdir(path_temp)



unprocessed_scenes = []
[unprocessed_scenes.append(x[0:40]) for x in list_all_files if x[0:40] not in unprocessed_scenes]
print(unprocessed_scenes)
len(unprocessed_scenes)




import subprocess
from osgeo import gdal

dd = './Download_scenes/pasta_xpto2/'
for scene in unprocessed_scenes:
  satellite, colection, orbita, ponto = scene[:4], scene[35:37],scene[10:13],scene[13:16]
  path_scene = os.path.join(satellite, colection, orbita, ponto, scene)
  band4, band5, band6, mtl_scene  = dd + scene + '_B4.TIF', dd + scene + '_B5.TIF', dd + scene + '_B6.TIF', dd + scene + '_MTL.txt'
  files_scene = [band4, band5, band6, mtl_scene,]
  # import pdb; pdb.set_trace()
  if os.path.exists(band4) and os.path.exists(band5) and os.path.exists(band6) and os.path.exists(mtl_scene):
    for file_scene in files_scene:
      #cria a pasta
      os.makedirs(path_scene, exist_ok=True)
      if os.path.isdir(path_scene) and not os.path.exists(os.path.join(path_scene,os.path.split(file_scene)[1])):
        #move o arquivo
        # shutil.move('./Download_scenes/pasta_xpto2/', './LC08x/foi/foiDeNovo')
        shutil.copy(os.path.join(dd,os.path.split(file_scene)[1]), path_scene)
