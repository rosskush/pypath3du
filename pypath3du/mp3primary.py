import flopy 
import os
import numpy as np
from flopy.pakbase import Package




class Primary():
	def __init__(self,file_nam, gsf_file,model_ws,thread_ct=3,flow_model_type='modflow',gsf_type='GSF_V.1.1.0'):
		# 'modflow'
		flow_model_type = flow_model_type.upper()
		self.fn_path = os.path.join(model_ws,file_nam)
		self.flow_model_type = flow_model_type.upper()
		self.gsf_file = gsf_file
		self.gsf_type=gsf_type
		self.thread_ct = thread_ct


	def pathline(self,name,init_stepsize,strt_shpfile,cellid_attr,time_attr,zloc_attr,
		direction='Forward', capture_radius=1., sim_end_time=None,track_to_termination=True, 
		dispersion=False,retardation=False):

		direction = direction.upper()


	def write_file(self):
		"""
		Write the package file
		Returns
		-------
		None
		"""
		# item numbers and CamelCase variable names correspond to Modpath 6 documentation
		# nrow, ncol, nlay, nper = self.parent.mf.nrow_ncol_nlay_nper

		f_prim = open(self.fn_path, 'w')
		f_prim.write('{\n\t"FLOW_MODEL_TYPE" : {\n')


		f_prim.write(f'\t\t"{self.flow_model_type}": ' + '{\n')
		f_prim.write('\t\t\t "GSF_FILE" : {\n')
		f_prim.write('\t\t\t\t "TYPE" : ' + f'"{self.gsf_type}"\n')

		f_prim.write('\t\t\t\t "FILE_NAME" : ' + f'"{self.gsf_file}"\n')

		f_prim.write('\t\t\t},\n')

		f_prim.write('\t\t\t"OUTPUT_PRECISION" : ' + f'"SINGLE",\n')
		f_prim.write('\t\t\t"IFACE" : ' + '[ {"WEL" : 0}, {"CHD" : 7}],\n')
		f_prim.write(f'\t\t\t"THREAD_COUNT" : {self.thread_ct}\n')



		f_prim.close()

prim = Primary('Primary.json','mp3du.gsf',model_ws='')

pathline = prim.write_file()


