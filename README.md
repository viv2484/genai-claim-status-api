# GenAI Claim Status API

## Prerequisite
  ### Install Required Tools
    # kubectl
    curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
    chmod +x kubectl
    sudo mv kubectl /usr/local/bin/

    # eksctl
    curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_Linux_amd64.tar.gz" | tar xz
    sudo mv eksctl /usr/local/bin/

    # terraform
    sudo yum install -y yum-utils
    sudo yum-config-manager --add-repo https://rpm.releases.hashicorp.com/AmazonLinux/hashicorp.repo
    sudo yum -y install terraform

    # Docker
    sudo yum update -y
    sudo yum install docker -y

## Architecture
- EKS on EC2
- API Gateway → EKS Service
- DynamoDB for claims
- S3 for notes
- Bedrock for summarization

## Endpoints
- GET /claims/{id}
- POST /claims/{id}/summarize

  ### Sample curl Tests
  - curl https://ghgedv4nr7.execute-api.us-east-1.amazonaws.com/dev/claims/CLM1001
  - curl -X POST https://ghgedv4nr7.execute-api.us-east-1.amazonaws.com/dev/claims/CLM1001/summarize

## Deployment
1. Terraform apply
2. kubectl apply -f k8s/
3. Push via Github Action wokflow

## Observability
CloudWatch logs enabled.





