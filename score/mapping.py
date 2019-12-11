import numpy as np


oasis_dict = {
	'admission_type': {
		'bins': ['ELECTIVE', 'EMERGENCY', 'URGENT'],
		'labels': [0, 6, 6]
		# 'type': 
	},
	'age': {
		'bins': [-1, 24, 53, 77, 89, 200],
		'labels': [0, 3, 6, 9, 7]
		# 'type':
	},
	'glasgow_coma_scale_total': {
		'bins': [-1, 7, 13, 14, 15],
		'labels': [10, 4, 3, 0]
		# 'type':
	},
	'heart_rate': {
		'bins': [-1, 32, 88, 106, 125, 300],
		'labels': [4, 0, 1, 3, 6]
		# 'type':
	},
	'mean_blood_pressure': {
		'bins': [-1, 20.65, 51.0, 61.33, 143.44, 350],
		'labels': [4, 3, 2, 0, 3]
		# 'type':
	},
	'prelos': {
		'bins': [-0.01, 0.17, 4.95, 24.0, 311.8, 3650.0],
		'labels': [5, 3, 0, 2, 1]
		# 'type':
	},
	'respiratory_rate': {
		'bins': [-1, 5, 12, 22, 29, 43, 200],
		'labels': [10, 1, 0, 1, 6, 9]
		# 'type':
	},
	'temperature': {
		'bins': [-1, 33.22, 35.93, 36.39, 36.89, 39.88, 80.0],
		'labels': [3, 4, 2, 0, 2, 6],
		# 'type':
	},
	'urine_output': {
		'bins': [-1, 671.09, 1427, 2544.14, 6896.8, 20000],
		'labels': [10, 5, 1, 0, 8]
		# 'type':
	},
	'ventilated': {
		'bins': [1],
		'labels': [9]
		# 'type':
	}
}


# saps2_dict = {
# 	'admission_type': {
# 		'bins': ['ELECTIVE', 'EMERGENCY', 'URGENT'],
# 		'labels': [0, 6, 6],
# 		'type':
# 	},
# 	'age': {
# 		'bins': [-1, 40.0, 60.0, 70.0, 75.0, 80.0, 200],
# 		'labels': [0, 7, 12, 15, 16, 18],
# 		'type':
# 	},
# 	'bicarbonate': {
# 		'bins': [-1, 24, 53, 77, 89, 200],
# 		'labels': [0, 3, 6, 9, 7],
# 		'type':
# 	},
# 	'bilirubin': {
# 		'bins': [-1, 4.0, 6.0, 40.0],
# 		'labels': [0, 4, 9],
# 		'type':
# 	},
# 	'blood_urea_nitrogen': {
# 		'bins': [-1, 28.0, 84.0, 200.0],
# 		'labels': [0, 6, 10],
# 		'type':
# 	},
# 	'glasgow_coma_scale_total': {
# 		'bins': [-1, 5, 8, 10, 13, 15],
# 		'labels': [26, 13, 7, 5, 0],
# 		'type':
# 	},
# 	'heart_rate': {
# 		'bins': [-1, 40.0, 70.0, 120.0, 160.0, 300.0],
# 		'labels': [11, 2, 0, 4, 7],
# 		'type':
# 	},
# 	'icd9': {
# 		'bins': ,
# 		'labels': ,
# 		'type':
# 	},
# 	'potassium': {
# 		'bins': [-1, 3.0, 5.0, 50.0],
# 		'labels': [3, 0, 3],
# 		'type':
# 	},
# 	'sodium': {
# 		'bins': [-1, 125.0, 145.0, 300.0],
# 		'labels': [5, 0, 1],
# 		'type':
# 	},
# 	'systolic_blood_pressure': {
# 		'bins': [-1, 70.0, 100.0, 200.0, 500.0],
# 		'labels': [13, 5, 0, 2],
# 		'type':
# 	},
# 	'temperature': {
# 		'bins': [-1, 39.0, np.inf],
# 		'labels': [0, 3],
# 		'type':
# 	},
# 	'urine_output': {
# 		'bins': [-1, 500, 1000, np.inf],
# 		'labels': [11, 4, 0],
# 		'type':
# 	},
# 	'ventilated': {
# 		'bins': [-1, 100, 200, np.inf],
# 		'labels': [11, 9, 6],
# 		'type':
# 	},
# 	'white_blood_cell_count': {
# 		'bins': [-1, 1.0, 20.0, 200.0],
# 		'labels': [12, 0, 3],
# 		'type':
# 	}
# }


# apache2_dict = {
# 	'label1': {
# 		'bins': [],
# 		'labels': [],
# 		'type':
# 	}
# }
