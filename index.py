#script to stop running EC2 instances based on tag values 
import boto3
client=boto3.client('ec2')
def lambda_handler(event, context):
    response=client.describe_instances(Filters=[{'Name': 'tag:stop', 'Values': ['yes']}, 
                                                {'Name': 'instance-state-name','Values': ['running']}])
    for reservation in response["Reservations"]:
	    for instance in reservation["Instances"]:
	        #if instance['State'] == "running":
		    #print(instance["InstanceId"] + "stopping")
		    id=[instance["InstanceId"]]
            client.stop_instances(InstanceIds=id)
            print(instance["InstanceId"] + "stopped")
    return("Completed")