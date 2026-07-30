# 1. Tell Terraform to connect to your AWS Account
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1" # Deploys directly to the N. Virginia data centers
}

# 2. Automatically build your custom virtual cloud network (VPC)
resource "aws_vpc" "logistics_vpc" {
  cidr_block           = "10.0.0.0/16" # Your isolated cloud network space
  enable_dns_hostnames = true

  tags = {
    Name        = "Logistics-Production-VPC"
    Environment = "DevOps-Portfolio"
  }
}

# 3. Create a public entry subnet inside your virtual network
resource "aws_subnet" "public_subnet" {
  vpc_id                  = aws_vpc.logistics_vpc.id
  cidr_block              = "10.0.1.0/24"
  map_public_ip_on_launch = true

  tags = {
    Name = "Public-Subnet-01"
  }
}
