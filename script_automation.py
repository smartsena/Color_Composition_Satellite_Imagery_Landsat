import os
import requests
import csv
import ast
import shutil
print("--","len(scene)","---->>>")


path_root = './'
# path_root = os.getcwd()
path_downlad = os.path.join(path_root, 'Download_scenes_v')
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


# from osgeo import gdal
import glob
import subprocess

# import subprocess
# from osgeo import gdal

dd = './Download_scenes_v/'
# dd = './Download_scenes/pasta_xpto2/'
for scene in unprocessed_scenes:
  satellite, colection, orbita, ponto = scene[:4], scene[35:37],scene[10:13],scene[13:16]
  path_scene = os.path.join(satellite, colection, orbita, ponto, scene)
  band4, band5, band6, mtl_scene, scene_composition  = dd + scene + '_B4.TIF', dd + scene + '_B5.TIF', dd + scene + '_B6.TIF', dd + scene + '_MTL.txt', os.path.join(path_scene, scene + '_R6G5B4.TIF')
  files_scene = [band4, band5, band6, mtl_scene,]
  print(band5+"Foi---------<<<<<<<<<<")
#   import pdb; pdb.set_trace()
  if os.path.exists(band4) and os.path.exists(band5) and os.path.exists(band6) and os.path.exists(mtl_scene):
    #se o diretório existe e se o scene_composition ainda não foi gerado
    os.makedirs(path_scene, exist_ok=True)
    if os.path.isdir(path_scene) and not os.path.exists(os.path.join(path_scene,os.path.split(scene_composition)[1])):
        cmd="gdal_merge.py -ot Float32 -of GTiff -separate -o " + scene_composition
        demList = [band6, band5, band4]
        subprocess.call(cmd.split()+demList)
        print("----------------------->>>>>>>>>>>>>>" + demList[1])
        # import pdb; pdb.set_trace()
        for file_scene in files_scene:
          #cria a pasta
          if not os.path.exists(os.path.join(path_scene,os.path.split(file_scene)[1])):
            #move o arquivo
            # shutil.move('./Download_scenes/pasta_xpto2/', './LC08x/foi/foiDeNovo')
            shutil.copy(os.path.join(dd,os.path.split(file_scene)[1]), path_scene)
