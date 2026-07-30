# Phase 2: Serverless Logistics Architecture & Cloud IaC ☁️

This sub-project demonstrates cloud engineering literacy by converting local streaming components into an automated, serverless AWS pipeline using Infrastructure as Code (IaC).

### 🛠️ Architecture & Objectives
* **Infrastructure as Code (IaC):** Authored modular HashiCorp Configuration Language (HCL) templates (`main.tf`) to programmatically deploy isolated multi-tiered networks (AWS VPC & Subnets) instantly via terminal.
* **Serverless Processing:** Adapted traditional continuous-loop scripts into a native event-driven AWS Lambda Function handler architecture (`lambda_stream.py`).
* **Cloud Storage & NoSQL:** Configured delivery infrastructure to route operational telemetry events into an Amazon S3 storage bucket and telemetry records into a low-latency Amazon DynamoDB database table.
* **Identity & Access Security:** Implemented native structural Trust Policy Documents (`data.aws_iam_policy_document`) to adhere to strict cloud privileges.

### 🚀 Automated Deployment
Provision the complete network, storage, database, and execution layer using a single automated lifecycle loop:
```bash
terraform init -upgrade
terraform apply --auto-approve
```

To prevent long-term billing or active cloud resource consumption, tear down the environment safely with:
```bash
terraform destroy --auto-approve
```
