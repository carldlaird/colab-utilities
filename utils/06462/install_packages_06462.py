# This installation script implemented based on the notebook from Jeff Kantor
# see that notebook for more information, examples, and testing
# https://colab.research.google.com/github/jckantor/ND-Pyomo-Cookbook/blob/master/notebooks/01.02-Running-Pyomo-on-Google-Colab.ipynb#scrollTo=RlmSEN45glrk
# execute this script in your google colab with the following lines
# >>> !wget https://raw.githubusercontent.com/carldlaird/colab-utilities/main/utils/06462/install_packages_06462.py
# >>> import install_packages_06462

import os
os.system('apt-get install -y -qq glpk-utils')
os.system('apt-get install -y -qq coinor-cbc')
os.system('wget -N -q "https://ampl.com/dl/open/ipopt/ipopt-linux64.zip"')
os.system('unzip -o -q ipopt-linux64')
os.system('pip install pyomo')
import pyomo.common.fileutils as fileutils
fileutils.Executable.rehash()
fileutils.Executable('ipopt').set_path('/content/ipopt')
