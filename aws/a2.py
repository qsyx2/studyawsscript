#!/usr/bin/python
# -*- coding: utf-8 -*-

import boto3

ec2 = boto3.resource('ec2')
vpc = ec2.Vpc('vpc-df5df2ba')
route_table = ec2.RouteTable('rtb-d629a8b3')
client = boto3.client('ec2')
#route_table_iterator = vpc.route_tables.all()
#list(ec2.RouteTable)
instances = ec2.instances.filter(
    Filters=[{'Name': 'subnet-id', 'Values': ['subnet-cd28b7a8']}])
for instance in instances:
    natid = instance.id
print natid

response = client.replace_route(
    DryRun=False,
    RouteTableId='rtb-d629a8b3',
    DestinationCidrBlock='0.0.0.0/0',
    InstanceId= natid,
)

response
