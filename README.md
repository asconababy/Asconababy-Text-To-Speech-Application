# Text-to-Speech Application
![IaC](https://img.shields.io/badge/IaC-Terraform-7B42BC?style=for-the-badge&logo=terraform)
![Cloud](https://img.shields.io/badge/Cloud-AWS-232F3E?style=for-the-badge&logo=amazonaws)
![Text-to-Speech](https://img.shields.io/badge/Text--to--Speech-API-4B5563?style=for-the-badge)
![Amazon Polly](https://img.shields.io/badge/Amazon%20Polly-TTS-F9A03C?style=for-the-badge&logo=amazon)
![AWS Lambda](https://img.shields.io/badge/AWS%20Lambda-Serverless-F58536?style=for-the-badge&logo=awslambda)
![API Gateway](https://img.shields.io/badge/API%20Gateway-Rest%20API-6B7280?style=for-the-badge&logo=amazonaws)
![Amplify](https://img.shields.io/badge/AWS%20Amplify-Frontend-F59E0B?style=for-the-badge&logo=awsamplify)

A serverless text-to-speech application built with AWS services and Terraform infrastructure as code.
This project combines the power of AWS Lambda, API Gateway, S3, and Amplify to deliver a modern, full-stack solution.

## Architecture

<img width="757" height="558" alt="Screenshot (177)" src="https://github.com/user-attachments/assets/77fe4e3d-2f76-4427-ad13-95bdebd37802" />

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
  

## Screenshots


UI Welcome Page
<img width="1366" height="688" alt="Screenshot (164)" src="https://github.com/user-attachments/assets/43ef43d3-d6ea-48ba-8b58-f4f915293c88" />



UI In Process
<img width="1366" height="656" alt="Screenshot (167)" src="https://github.com/user-attachments/assets/15390407-1819-4c15-8f28-412dd1264e5f" />



API Gateway
<img width="1366" height="647" alt="Screenshot (171)" src="https://github.com/user-attachments/assets/b5ebdebe-c206-44ab-a42f-29f29614fabb" />



Amplify Deployment 
<img width="1366" height="641" alt="Screenshot (168)" src="https://github.com/user-attachments/assets/6b75777d-d5ee-464e-8e6f-54f3e38e73fd" />



CloudWatch Logs
<img width="1366" height="641" alt="Screenshot (173)" src="https://github.com/user-attachments/assets/b1fd4ff4-d73e-4731-9324-05d553a50b62" />



Lambda Function
<img width="1366" height="645" alt="Screenshot (170)" src="https://github.com/user-attachments/assets/1008cb31-5cd8-46bc-ac19-0a1ec4e8e73f" />



Terraform Apply Output
<img width="1366" height="716" alt="Screenshot (176)" src="https://github.com/user-attachments/assets/5c45de5d-1cea-43b5-b081-294e1f586a9b" />



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
