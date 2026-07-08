# Project 02: Serverless URL Shortener on AWS

## 📖 Project Overview

This project demonstrates how to build a serverless URL shortener using AWS services.

Users will submit a long URL through an API endpoint, and the application will generate a short code, store the mapping in DynamoDB, and redirect users to the original URL when they visit the short link.

---

## 📌 Project Status

🚧 In Progress

---

## ☁️ AWS Services Used

| Service | Purpose |
|---------|---------|
| Amazon API Gateway | Expose HTTP endpoints |
| AWS Lambda | Run backend logic without servers |
| Amazon DynamoDB | Store short code and long URL mappings |
| AWS IAM | Manage permissions |
| Amazon CloudWatch | Logs and troubleshooting |

---

## 🏗️ Architecture

Architecture diagram will be added later.

---

## 🎯 Learning Objectives

- Build a serverless REST API
- Create AWS Lambda functions
- Store data in DynamoDB
- Configure IAM permissions
- Troubleshoot with CloudWatch Logs
- Document a serverless AWS project

---

## 🚀 Planned Endpoints

| Method | Path | Purpose |
|--------|------|---------|
| POST | `/shorten` | Create a short URL |
| GET | `/{code}` | Redirect to the original URL |

---

## 🧹 Cleanup

Cleanup instructions will be added after deployment testing.
