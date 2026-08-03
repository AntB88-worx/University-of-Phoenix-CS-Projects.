# Phase 2: Serverless Logistics Architecture & Cloud IaC ☁️

This sub-project demonstrates cloud engineering literacy by converting local streaming components into an automated, serverless AWS pipeline using Infrastructure as Code (IaC).

## 🛠️ Architecture & Objectives

*   **Infrastructure as Code (IaC)**: Authored robust HashiCorp Configuration Language (HCL) templates (`main.tf`) to programmatically deploy isolated network topologies (AWS VPC & Subnets) instantly via terminal.
*   **Serverless Processing**: Adapted traditional continuous-loop scripts into a native, event-driven AWS Lambda Function handler architecture (`lambda_stream.py`) equipped with secure URL verification filters.
*   **Cloud Storage & NoSQL**: Configured delivery infrastructure to route operational telemetry events into an Amazon S3 storage bucket and low-latency Amazon DynamoDB database table layers.
*   **Identity & Access Security**: Implemented strict, least-privilege AWS IAM Execution Roles using explicit resource policies to allow secure Lambda cross-service actions.
*   **Live Analytics Stream**: Integrated an interactive Streamlit monitoring dashboard (`dashboard.py`) to actively scan DynamoDB and render rolling real-time metric visualizations.

## 🚀 Automated Deployment

Provision the complete network, storage, database, and execution layer using a single automated lifecycle loop:

```bash
# 1. Initialize the working directory and upgrade AWS provider modules
terraform init -upgrade

# 2. Generate and review the execution plan to verify architecture metrics
terraform plan

# 3. Deploy the automated serverless data pipeline safely to AWS
terraform apply -auto-approve
```

To run your visualization dashboard locally once your infrastructure is active:

```bash
streamlit run dashboard.py
```

To prevent long-term billing or active cloud resource consumption, tear down the environment safely with:

```bash
terraform destroy -auto-approve
```
