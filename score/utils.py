import pandas as pd


def read(file_name):
	extension = file_name[-3:]
	if extension == 'psv':
		sep = '|'
	elif extension == 'tsv':
		sep = '\t'
	else:
		sep = ','

	return pd.read_csv(file_name, sep=sep)


# variable_map = {
# 	'temperature': ['Temp', 'temp', 'TEMPERATURE']
# }

variable_map = {
	'temperature': 'Temp'
}
