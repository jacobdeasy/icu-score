"""
Abstract score module
"""
import pandas as pd

from mapping import *
from utils import read, variable_map


def score_picker(name):
	score_class = eval(name.capitalize())

	return score_class()


# class AbstractScore(object):
# 	"""docstring for AbstractScore"""
# 	def __init__(self, name):
# 		super(AbstractScore, self).__init__()
# 		self.dict = eval(name+'_dict')

# 	def tune(self):
# 		pass

# 	def predict(self):
# 		pass


# class Oasis(AbstractScore):
class Oasis(object):
	"""docstring for Oasis"""
	def __init__(self):
		super(Oasis, self).__init__()
		self.dict = oasis_dict

	def predict(self, file):
		var_scores = self.var_score(file)

		return sum(var_scores)

	def var_score(self, file):
		df = read(file)
		scores = []

		for var in ['temperature']:
			print(variable_map[var])
			print(self.dict[var]['bins'])
			print(self.dict[var]['labels'])
			# TO DO : fix non-unique mapping issue
			score = pd.cut(df[variable_map[var]],
						   bins=self.dict[var]['bins'],
						   labels=self.dict[var]['labels'])
			score = score.max()
			print(score)

		# for var in self.dict:
		# 	try:
		# 		score = pd.cut(df[variable_map[var]],
		# 					   bins=self.dict[var]['bins'],
		# 					   labels=self.dict[var]['labels'])
		# 	except:
		# 		print('Variable: "%s" not in dataframe' % var)
		# 		continue
			scores += [score]

		return scores
