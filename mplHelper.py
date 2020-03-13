import matplotlib.pyplot as plt

class mplHelper:
	"""
	Silly little helper to set nice things about matplotlib plots so I don't have to type it every time.
	"""
	@classmethod
	def initializeMpl(cls):
		params = {'text.usetex': False, 'mathtext.fontset': 'dejavusans','font.size':14}
		plt.rcParams.update(params)  

	@classmethod
	def mySave(cls,flName):
		plt.savefig(flName,dpi=500,bbox_inches='tight')

	@classmethod
	def hist1D(cls,thing,bins,range,weights,normed=True,save='histPlot'):
		"""
		@param thing:
		@param bins:
		@param range:
		@param weights:
		@param normed:
		@param save: String that, if empty, will just plot the figure, meaning you can plot more than one.
		"""
		import numpy as np
		xx,yy = np.histogram(thing,bins=bins,range=range,weights=weights,density=normed)
		xx = 0.5*(xx[1:]+xx[:-1])
		plt.plot(xx,yy,'k')
		if save:
			mplHelper.mySave(save)