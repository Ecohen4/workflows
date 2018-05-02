import pandas as pd
import boto3

# connect to s3
s3 = boto3.resource('s3')

# get data from s3
data_endpoint = "https://s3.amazonaws.com/galvanize-denver-platte/puppies.csv"
df = pd.read_csv(data_endpoint)

# compute something on your ec2 instance
df['puppies_per_capita'] = df.puppies / df.people
df.to_csv('data/puppies_per_capita.csv', index=False)
print( 'puppies!' )
print( df.head() )

# write results back to s3
with open('data/puppies_per_capita.csv', 'rb') as data:
	s3.Bucket('galvanize-denver-platte').put_object(Key='puppy_rates.csv', Body=data)
	# or equivalently
	# s3.Object('galvanize-denver-platte', 'puppy_rates.csv').put(Body=data)

