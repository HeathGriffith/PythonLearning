
import boto3
'''
def create_bucket():
    client = boto3.client('s3')
    response = client.create_bucket(
        Bucket='kwargs-practice-bucket', 
        CreateBucketConfiguration={'LocationConstraint': 'us-east-1'}
    )
    print(response)

def main():
    create_bucket()

if __name__ == "__main__":
    main()
'''


def create_bucket(**kwargs):
    client = boto3.client('s3')
    response = client.create_bucket(**kwargs)
    print(response)

kwargs = {
    'Bucket': 'kwargs-practice-bucket83', 
    'CreateBucketConfiguration':{'LocationConstraint': 'us-west-2'}
    }

def main():
    create_bucket(**kwargs)

if __name__ == "__main__":
    main()