# ----------------------------------------------------------------------
# Composição colorida/empilhamento das bandas
# ----------------------------------------------------------------------

from osgeo import gdal
import glob
import subprocess

cmd="gdal_merge.py -ot Float32 -of GTiff -separate -o LC08/01/006/063/LC08_L1GT_006063_20191016_20191016_01_RT/LC08_L1GT_222061_20230222_20230301_02_T2_B6B5B4.TIF"

demList = ["./Download_scenes_v/LC08_L1GT_222061_20230222_20230301_02_T2_B4.TIF","./Download_scenes_v/LC08_L1GT_222061_20230222_20230301_02_T2_B5.TIF","./Download_scenes_v/LC08_L1GT_222061_20230222_20230301_02_T2_B6.TIF"]
subprocess.call(cmd.split()+demList)

