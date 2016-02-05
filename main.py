from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def simpleProbability(train_df, name, val):
	total = len(train_df[train_df[name] == val])
	train_df[name + 'Rate'] = (train_df[name] == val) & (train_df['Survived'] == 1)
	t_pclass = len(train_df[train_df[name + 'Rate'] == True])
	print('rate ' + name + ' ' + str(val) + '\t' + str(t_pclass/total))


def main():
	train_df = pd.read_csv('train.csv', index_col='PassengerId')
	# Structure of df
	# PassengerId, Survived, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked
	# survival        Survival
	#                 (0 = No; 1 = Yes)
	# pclass          Passenger Class
	#                 (1 = 1st; 2 = 2nd; 3 = 3rd)
	# name            Name
	# sex             Sex
	# age             Age
	# sibsp           Number of Siblings/Spouses Aboard
	# parch           Number of Parents/Children Aboard
	# ticket          Ticket Number
	# fare            Passenger Fare
	# cabin           Cabin
	# embarked        Port of Embarkation
	#                 (C = Cherbourg; Q = Queenstown; S = Southampton)
	# likely to have little to do with final model
	# 	- ticket
	# 	- fare

	# Affect of individulal variables on survival rate

	# pclass
	simpleProbability(train_df, 'Pclass', 1)
	simpleProbability(train_df, 'Pclass', 2)
	simpleProbability(train_df, 'Pclass', 3)

	# Sex
	simpleProbability(train_df, 'Sex', 'male')
	simpleProbability(train_df, 'Sex', 'female')

	#print(train_df)

if __name__ == '__main__':
	main()