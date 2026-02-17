resource "aws_dynamodb_table" "claims" {
  name         = "claims-table"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "claimId"

  attribute {
    name = "claimId"
    type = "S"
  }
}
