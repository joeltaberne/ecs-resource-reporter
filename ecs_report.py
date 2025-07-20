import boto3
import json
import csv
from utils import write_to_file

def generate_report(cluster_name, output_format, file_path=None):
    client = boto3.client('ecs')
    response = client.list_services(cluster=cluster_name)
    services = response['serviceArns']

    report = []
    for service in services:
        service_details = client.describe_services(cluster=cluster_name, services=[service])
        tasks = service_details['services'][0]['deployments']
        report.append({
            "service": service,
            "tasks": tasks
        })

    if output_format == "json":
        if file_path:
            write_to_file(file_path, json.dumps(report, indent=4))
        else:
            print(json.dumps(report, indent=4))
    elif output_format == "csv":
        with open(file_path, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["service", "tasks"])
            writer.writeheader()
            for row in report:
                writer.writerow(row)