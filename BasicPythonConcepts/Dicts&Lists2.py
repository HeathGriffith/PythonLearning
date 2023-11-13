'''This task closely simulates operations you might perform using Boto3 in an AWS environment. 
It involves updating resource states, adding and removing resources, filtering based on specific criteria, and managing resource metadata. 
These operations are foundational for scripting and understanding the logic behind AWS infrastructure tasks in Python.'''

aws_resources = {
    "EC2": [
        {"name": "EC2_instance_1", "creation_date": "2021-08-15", "status": "running", "region": "us-east-1"},
        {"name": "EC2_instance_2", "creation_date": "2021-11-30", "status": "stopped", "region": "us-west-2"}
    ],
    "S3": [
        {"name": "data_bucket", "creation_date": "2020-05-20", "status": "active", "region": "eu-central-1"},
        {"name": "backup_bucket", "creation_date": "2021-09-12", "status": "active", "region": "ap-southeast-1"}
    ],
    "RDS": [
        {"name": "customer_db", "creation_date": "2021-07-07", "status": "available", "region": "us-east-1"},
        {"name": "inventory_db", "creation_date": "2021-10-21", "status": "modifying", "region": "eu-west-3"}
    ]
}

# (1) Update a Resource's Status: Change the status of EC2_instance_2 to "running".
aws_resources["EC2"][1]["status"] = "running"
# (2) Add a New Resource: Add a new EC2 instance named EC2_instance_3 with your choice of attributes.
aws_resources["EC2"].append({"name": "EC2_instance_3", "creation_date": "2021-11-30", "status": "stopped", "region": "us-west-2"})
# (3) Delete a Resource: Remove backup_bucket from the S3 resources.
del aws_resources["S3"][1]
# (4) List Resources in a Specific Region: Write a loop or a set of statements that lists all resources located in "us-east-1".

'''static, inferior solution:
for resource in aws_resources:
    if aws_resources[resource][0]["region"] == "us-east-1":
        print(aws_resources[resource][0]["name"])
    if aws_resources[resource][1]["region"] == "us-east-1":
        print(aws_resources[resource][1]["name"])'''

for resource_type in aws_resources:
    for resource in aws_resources[resource_type]:
        if resource["region"] == "us-east-1":
            print(resource["name"])


# (5) Modify a Resource's Region: Change the region of inventory_db in RDS to "us-east-1".
aws_resources["RDS"][1]["region"] = "us-east-1"

# (6) Print the Updated Resources: Display the entire aws_resources dictionary in a readable format to review the changes made.
print(aws_resources)

