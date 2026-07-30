terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

# 1. Network Core
resource "aws_vpc" "logistics_vpc" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  tags = { Name = "Logistics-Production-VPC" }
}

resource "aws_subnet" "public_subnet" {
  vpc_id                  = aws_vpc.logistics_vpc.id
  cidr_block              = "10.0.1.0/24"
  map_public_ip_on_launch = true
  tags = { Name = "Public-Subnet-01" }
}

# 2. Storage & Database Layers
resource "aws_s3_bucket" "logistics_storage" {
  bucket_prefix = "uop-logistics-stream-data-"
  force_destroy = true
}

resource "aws_dynamodb_table" "inventory_metrics" {
  name         = "LogisticsInventoryMetrics"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "timestamp"

  attribute {
    name = "timestamp"
    type = "S"
  }
}

# 3. Fixed Security IAM Role (Using Heredoc Syntax to prevent Windows string corruption)
resource "aws_iam_role" "lambda_execution_role" {
  name = "logistics_lambda_execution_role"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "://amazonaws.com"
      },
      "Effect": "Allow"
    }
  ]
}
EOF
}

resource "aws_iam_role_policy_attachment" "lambda_logs" {
  role       = aws_iam_role.lambda_execution_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

# 4. Automatically Zip Your Local Python Code
data "archive_file" "lambda_zip" {
  type        = "zip"
  source_file = "lambda_stream.py"
  output_path = "lambda_function_payload.zip"
}

# 5. Deploy the Serverless AWS Lambda Function
resource "aws_lambda_function" "logistics_stream_lambda" {
  filename      = data.archive_file.lambda_zip.output_path
  function_name = "LogisticsStreamProcessor"
  role          = aws_iam_role.lambda_execution_role.arn
  handler       = "lambda_stream.lambda_handler"
  runtime       = "python3.11"

  source_code_hash = data.archive_file.lambda_zip.output_base64sha256

  environment {
    variables = {
      DYNAMODB_TABLE = aws_dynamodb_table.inventory_metrics.name
      S3_BUCKET      = aws_s3_bucket.logistics_storage.id
    }
  }
}
