import argparse
import pandas as pd
import sys

from score.score import Score


def parse_arguments(args_to_parse):
	"""Parse command line arguments"""
	description = 'Python implementation of ICU scores.'
	parser = argparse.ArgumentParser(description=description)

	# General options
	parser.add_argument('score_name', type=str,
						help='Name of the scoring system to use.')
	parser.add_argument('-o', '--out-dir', type=str,
						default='results',
						help='Directory to store results in.')
	parser.add_argument('-v', '--verbose', type=int,
						default=1,
						help='Level of verbosity.')

	# Score options
	parser.add_argument('-p', '--predict', type=bool,
						default=True,
						help='Whether to predict score per df.')
	args = parser.parse_args(args_to_parse)

	return args


def main(args):
	"""Main scoring function.

	Parameters
	----------
	args : argparse.Namespace
		Arguments
	"""

	# Initialise score class
	icu_score = Score(args.score_name)

	# Treat single files and directories the same
	if os.path.isdir(args.root):
		files = os.listdir(args.root)
	else
		files = [args.root]

	if args.predict:
		# Predict score
		predictions = []
		for file in files:
			prediction = icu_score.predict(file)
			predictions += [prediction]

			if args.verbose == 2:
				print(file, prediction)

		if args.verbose == 1:
			for i in range(max(len(root), 5)):
				print(root[i], predictions[i])

		# Save predictions
		if not os.path.exists(args.out_dir):
			os.makedirs(args.out_dir)
		prediction_df = pd.Dataframe(list(zip(root, predictions)),
					 				 columns=['Path', 'Score'])
		prediction_df.to_csv(index=None)


if __name__ == '__main__':
	args = parse_arguments(sys.argv[1:])
	main(args)
