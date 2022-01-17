import os
os.system('apt-get install -y -qq glpk-utils')
os.system('apt-get install -y -qq coinor-cbc')
os.system('wget -N -q "https://ampl.com/dl/open/ipopt/ipopt-linux64.zip"')
os.system('unzip -o -q ipopt-linux64')
os.system('pip install pyomo')
import pyomo.common.fileutils as fileutils
fileutils.Executable.rehash()
fileutils.Executable('ipopt').set_path('/content/ipopt')
