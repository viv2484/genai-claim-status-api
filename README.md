# GenAI Claim Status API

## Architecture
- EKS on EC2
- API Gateway → EKS Service
- DynamoDB for claims
- S3 for notes
- Bedrock for summarization

## Endpoints
- GET /claims/{id}
- POST /claims/{id}/summarize

## Deployment
1. Terraform apply
2. kubectl apply -f k8s/
3. Push via Github Action wokflow

## Observability
CloudWatch logs enabled.




