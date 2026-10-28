
variable "aws_region" {
  description = "AWS region for the DevOps project"
  type        = string
  default     = "ap-south-1"
}

variable "project_name" {
  description = "Name of the DevOps CI/CD project"
  type        = string
  default     = "aws-devops-cicd"
}
