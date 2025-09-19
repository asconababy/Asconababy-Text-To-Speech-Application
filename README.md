# Text-to-Speech Application
![IaC](https://img.shields.io/badge/IaC-Terraform-7B42BC?style=for-the-badge&logo=terraform)
![Cloud](https://img.shields.io/badge/Cloud-AWS-232F3E?style=for-the-badge&logo=amazonaws)
![Text-to-Speech](https://img.shields.io/badge/Text--to--Speech-API-4B5563?style=for-the-badge)
![Amazon Polly](https://img.shields.io/badge/Amazon%20Polly-TTS-F9A03C?style=for-the-badge&logo=amazon)
![AWS Lambda](https://img.shields.io/badge/AWS%20Lambda-Serverless-F58536?style=for-the-badge&logo=awslambda)
![API Gateway](https://img.shields.io/badge/API%20Gateway-Rest%20API-6B7280?style=for-the-badge&logo=amazonaws)
![Amplify](https://img.shields.io/badge/AWS%20Amplify-Frontend-F59E0B?style=for-the-badge&logo=awsamplify)

A serverless text-to-speech application built with AWS services and Terraform infrastructure as code.

## Architecture

- **Frontend**: Static web application hosted on AWS Amplify
- **Backend**: AWS Lambda function with Amazon Polly integration
- **API**: AWS API Gateway for REST endpoints
- **Storage**: Amazon S3 for audio file storage
- **Infrastructure**: Terraform modules for automated deployment

## Features

- Convert text to speech using Amazon Polly
- Multiple voice options and languages
- Audio file generation and storage
- Responsive web interface
- Serverless architecture

## Prerequisites

- AWS CLI configured with appropriate credentials
- Terraform >= 1.0
- Node.js (for Lambda functions)

## Deployment

1. Clone the repository:
```bash
git clone https://github.com/asconababy/Asconababy-Text-To-Speech-Application.git
cd Asconababy-Text-To-Speech-Application
```

2. Initialize Terraform:
```bash
terraform init
```

3. Deploy infrastructure:
```bash
terraform plan
terraform apply
```

## Project Structure

```
├── frontend/           # Web application files
├── lambda/            # Lambda function code
├── modules/           # Terraform modules
│   ├── amplify/       # AWS Amplify configuration
│   ├── api_gateway/   # API Gateway setup
│   ├── iam/          # IAM roles and policies
│   ├── lambda/       # Lambda function deployment
│   └── s3/           # S3 bucket configuration
├── main.tf           # Main Terraform configuration
└── outputs.tf        # Terraform outputs
```

## Usage

1. Access the web application via the Amplify URL
2. Enter text in the input field
3. Select voice and language options
4. Click "Convert to Speech" to generate audio
5. Download or play the generated audio file

## AWS Services Used

- Amazon Polly (Text-to-Speech)
- AWS Lambda (Serverless compute)
- Amazon S3 (Storage)
- AWS API Gateway (REST API)
- AWS Amplify (Frontend hosting)
- AWS IAM (Security and permissions)

## License

This project is licensed under the MIT License.
