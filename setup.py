import sys
from cx_Freeze import setup, Executable

import os.path
import numpy
import tkinter
import cv2
import tensorflow.contrib.framework.python.ops.gen_variable_ops
import tensorflow.contrib.layers.python.layers.utils
import tensorflow.contrib.quantize.python.quant_ops
import tensorflow.contrib.timeseries.python.timeseries.model_utils
import tensorflow.contrib.timeseries.python.timeseries.input_pipeline
import tensorflow.contrib.timeseries.python.timeseries.saved_model_utils
import tensorflow.contrib.timeseries.python.timeseries.model
import tensorflow.contrib.timeseries.python.timeseries.math_utils
import tensorflow.contrib.timeseries.python.timeseries.ar_model
import tensorflow.contrib.timeseries.python.timeseries.estimators
import tensorflow.contrib.timeseries.python.timeseries.feature_keys
import tensorflow.contrib.timeseries.python.timeseries.head
import tensorflow.contrib.timeseries.python.timeseries.state_management
import tensorflow.contrib.timeseries.python.timeseries.test_utils

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os","tkinter","numpy","cv2"],
					 "includes":['tensorflow.contrib.framework.python.ops.gen_variable_ops',
								 'tensorflow.contrib.layers.python.layers.utils',
								 'tensorflow.contrib.timeseries.python.timeseries.model_utils',
								 'tensorflow.contrib.timeseries.python.timeseries.input_pipeline',
								 'tensorflow.contrib.timeseries.python.timeseries.saved_model_utils',
								 'tensorflow.contrib.quantize.python.quant_ops',
								 'tensorflow.contrib.timeseries.python.timeseries.model',
								 'tensorflow.contrib.timeseries.python.timeseries.math_utils',
								'tensorflow.contrib.timeseries.python.timeseries.ar_model',
								'tensorflow.contrib.timeseries.python.timeseries.estimators',
								'tensorflow.contrib.timeseries.python.timeseries.feature_keys',
								'tensorflow.contrib.timeseries.python.timeseries.head',
								'tensorflow.contrib.timeseries.python.timeseries.state_management',
								'tensorflow.contrib.timeseries.python.timeseries.test_utils'],
					"include_files": ["retrain.py", "test.py","config.py","instructions.txt"],
					'include_msvcr': True,}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
	base = "Console"
    #base = "Win32GUI"

setup(  name = "Marine Animal Image Classifier",
        version = "0.1",
        description = "Marine Animal Image Classifier",
        options = {
			"build_exe": build_exe_options
		},
        executables = [Executable("MarineAnimalImageClassifierGUI.py", base=base)])