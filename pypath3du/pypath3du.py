import flopy
import numpy as np
import os
from flopy.mbase import BaseModel
from flopy.pakbase import Package


class Modpath3du(BaseModel):
	"""
	Mod-Path3DU base class
	"""

	def __init__(self, modelname='modpath3DUtest',primfile_ext='prim3du',
                 version='modpath3du', exe_name='mp3du.exe', modflowmodel=None,
                 dis_file=None, dis_unit=87, head_file=None, budget_file=None,
                 model_ws=None, external_path=None, verbose=False,
                 load=True, listunit=7):
		"""
		Model constructor
		"""

		BaseModel.__init__(self, modelname, primfile_ext, exe_name, model_ws=model_ws)

		self.version_type(version)
		self.set_version(version)

		self.__mf = modflowmodel
		self.lst = 3