import boto3

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
