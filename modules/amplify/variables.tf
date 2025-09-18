variable "app_name" {
  type = string
}

variable "repository_url" {
  type        = string
  description = "Git repository URL for the Amplify app"
  default     = ""
}