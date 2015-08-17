from __future__ import unicode_literals, division

import IPython
import warnings
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt

class Notebook(object):
	"""Utiliy Library when using Jupyter Notebooks"""
	def __init__(self):
		super(ClassName, self).__init__()
		print 'hello'
		# Notebook Options
		# %matplotlib inline
		warnings.filterwarnings('ignore')
		np.set_printoptions(suppress=True)
		global mart
		mart = 'hll'

		try :
		    if(__IPYTHON__) :
		        # get_ipython().magic(u'cd ~/')
		        # get_ipython().magic(u'load_ext autosave')
		        get_ipython().magic(u'matplotlib inline')
		except NameError :
		    print 'errror'

		# Import Global modules
		import_modules()

	def set_matplotlib_styles(self, **kwargs):
		self.matplotlib_styles.update(kwargs)

	def import_modules(self):
		print 'hello'
		np == __import__('numpy')


	matplotlib_styles = {
		'axes.labelsize': 17,
		'axes.titlesize': 16,
		'figure.figsize': [18, 8],
		'grid.linewidth': 1.6,
		'legend.fontsize': 17,
		'lines.linewidth': 2,
		'lines.markeredgewidth': 0.0,
		'lines.markersize': 11,
		'patch.linewidth': 0.5,
		'xtick.labelsize': 16,
		'xtick.major.pad': 20,
		'xtick.major.width': 2,
		'xtick.minor.width': 1,
		'ytick.labelsize': 16.0,
		'ytick.major.pad': 20,
		'ytick.major.width': 2,
		'ytick.minor.width': 1
	}
	
# 	wide_c = dict(c, **{'figure.figsize':[20,8]})

# # Source Data
# id = '1GnTfMdu9LATsemrfHrnWepsVo-H6oma8AZPXgC7RU1k'
# url = 'https://docs.google.com/spreadsheets/d/' + id + '/export?format=csv&id'
# r = requests.get(url)
# df = pd.read_csv(StringIO(r.content), parse_dates=[u'Timestamp'])

# # Episode
# episode = lambda x : x - 1
# episode_no = episode(4)
# episode_list = df['Episode'].unique()
# episode_title = episode_list[episode_no]

# # Awards
# awards = ['Wit','Jockey','Bloodshed','Style','Support']
# award_votes = [a[:2]+str(n) for a in awards for n in range(1,4)]
# awards_points = [32,16,8]
# multiplier = [0.125,0,25,0.5,1,2,4,8]

# # Players
# id = '1DIVq4s9U_nfY3cHcknGjeV3iGpfW_zxUx-bjFNm4Ebo'
# url = 'https://docs.google.com/spreadsheets/d/' + id + '/export?format=csv&id'
# r = requests.get(url)
# bids = pd.read_csv(StringIO(r.content), parse_dates=[u'Timestamp'])

# # Merge in Names
# voting_records = df.merge(bids[['Name','Email Address']])

# # Data Cleaning
# voting_records.columns = ['Timestamp'] + award_votes + ['Email','Episode','Name']
# voting_records = voting_records[['Episode','Name'] + award_votes + ['Email','Timestamp']]

# # Utility Functions
# def table(df,replace_match="",replace_str=""):
#     return IPython.display.display(HTML(df.to_html().replace('<table border="1" class="dataframe">','<table class="table table-striped table-hover">').replace(replace_match,replace_str)))

# # HTML Functions
# h1 = lambda x : prnt(HTML('''<h1 style="text-align:center">'''+ x +'''</h1>'''))
# h2 = lambda x: prnt(HTML('''<h2 style="text-align:center">'''+ x +'''</h2>'''))
# h2_success = lambda x: prnt(HTML('''<h2 style="text-align:center" class="alert alert-success">'''+ x +'''</h2>'''))

# h3_danger = lambda x: prnt(HTML('''<h3 style="text-align:center" class="alert alert-danger">'''+ x +'''</h3>'''))
# h3_info = lambda x: prnt(HTML('''<h3 style="text-align:center" class="alert alert-info">'''+ x +'''</h3>'''))
# h3_warning = lambda x: prnt(HTML('''<h3 style="text-align:center" class="alert alert-warning">'''+ x +'''</h3>'''))

# h3 = lambda x : prnt(HTML('''<h3 style="text-align:center">'''+ x +'''</h3>'''))
# p  = lambda x : prnt(HTML('''<p class="text_cell_render">'''+ x +'''</p>'''))

# md_wrap = lambda s, m, e: reduce(lambda x, y: x + "".join(y), zip(s.split(m), ['<'+e+'>','</'+e+'>'] * int(len(s)/2)), "")[:-3] if (m in s) else s
# md_b = lambda s : md_wrap(s,'**','b')
# md_i = lambda s :  md_wrap(s,'_','i')

# md = lambda s : md_i(md_b(s))

# def ul(lis):
#     lis = ['''<div class="panel panel-default"><div class="panel-body">''' + md(li) + '''</div></div>''' for li in lis]
#     prnt(HTML("".join(lis)))