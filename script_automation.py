import os
import requests
import csv
import ast
import shutil
# from osgeo import gdal
# import glob
import subprocess
print("--","len(scene)","---->>>")
print(os.getcwd())

class ColorCompositonLC08:

    def __init__(self) -> None:
        self.path_root = './'
        self.path_download = os.path.join(self.path_root, 'Download_scenes_v')
        # self.path_download = os.path.join(self.path_root, 'Download_scenes/pasta_xpto2/')
        self.path_scenes = os.path.join(self.path_root, 'LC08')

        print("--1-->>> path_root " + self.path_root)
        print("--2-->>> path_download " + self.path_download)
        print("--3-->>> path_scenes " + self.path_scenes)


    def list_downloaded_files(self):
        #lista os arquivos
        path_temp = os.getcwd()
        os.chdir(self.path_download)
        list_all_files= list(filter(os.path.isfile, os.listdir()))
        os.chdir(path_temp)
        print("--4-->>>  ")
        print(list_all_files)
        # import pdb; pdb.set_trace()

        return list_all_files


    def list_unprocessed_scenes(self):
        unprocessed_scenes = []
        list_all_files = self.list_downloaded_files()
        [unprocessed_scenes.append(x[0:40]) for x in list_all_files if x[0:40] not in unprocessed_scenes]
        print("--5-->>>  " + str(len(unprocessed_scenes)))
        print(unprocessed_scenes)

        return unprocessed_scenes


    def create_catalog (self):
        unprocessed_scenes= self.list_unprocessed_scenes()
        # import pdb; pdb.set_trace()
        for scene in unprocessed_scenes:
          satellite, colection, orbita, ponto, ano = scene[:4], scene[35:37],scene[10:13],scene[13:16],scene[17:21]
          path_scene = os.path.join(satellite, colection, orbita, ponto, scene)
          band4, band5, band6, mtl_scene, scene_composition  =os.path.join(self.path_download, scene + '_B4.TIF'), os.path.join(self.path_download, scene + '_B5.TIF'), os.path.join(self.path_download, scene + '_B6.TIF'), os.path.join(self.path_download, scene + '_MTL.txt'), os.path.join(path_scene, scene + '_R6G5B4.TIF')
          files_scene = [band4, band5, band6, mtl_scene,]
          print(band5+"--6--Foi-----<<<<<<<<<<")
          print(os.path.exists(band5))
          if os.path.exists(band4) and os.path.exists(band5) and os.path.exists(band6) and os.path.exists(mtl_scene):
            #cria a pasta
            os.makedirs(path_scene, exist_ok=True)
            #se o diretório existe e se o scene_composition ainda não foi gerado
            if os.path.isdir(path_scene) and not os.path.exists(os.path.join(path_scene,os.path.split(scene_composition)[1])):
                cmd="gdal_merge.py -ot Float32 -of GTiff -separate -o " + scene_composition
                demList = [band6, band5, band4]
                subprocess.call(cmd.split()+demList)
                print("----------------------->>>>>>>>>>>>>>" + demList[1])
                for file_scene in files_scene:
                  if not os.path.exists(os.path.join(path_scene,os.path.split(file_scene)[1])):
                    #move o arquivo
                    # shutil.move('./Download_scenes/pasta_xpto2/', './LC08x/foi/foiDeNovo')
                    shutil.copy(os.path.join(self.path_download,os.path.split(file_scene)[1]), path_scene)


instance = ColorCompositonLC08()
instance.create_catalog()
