resource "aws_amplify_app" "this" {
  name     = var.app_name
  platform = "WEB_COMPUTE"

  build_spec = <<-EOT
    version: 1
    frontend:
      phases:
        preBuild:
          commands:
            - echo "Starting build process"
        build:
          commands:
            - echo "No build step needed"
      artifacts:
        baseDirectory: frontend
        files:
          - 'index.html'
          - 'favicon.ico'
      cache:
        paths: []
  EOT

  tags = {
    Project = "TextToSpeech"
  }
}

resource "aws_amplify_branch" "main" {
  app_id      = aws_amplify_app.this.id
  branch_name = "main"
  stage       = "PRODUCTION"
}