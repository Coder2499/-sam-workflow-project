# 🚀 AWS SAM Event-Driven Workflow Project

## 📌 Project Overview

This project demonstrates a **fully automated event-driven serverless workflow** built using AWS services.

Whenever a file is uploaded to an S3 bucket, the system automatically triggers a workflow that processes the event and sends an email notification.

---

## 🧠 Architecture Flow

```
S3 Upload 
   ↓
EventBridge Rule
   ↓
Step Function (Orchestration)
   ↓
Lambda1 (Reads config from SSM)
   ↓
Choice State (Decision Making)
   ↓
Lambda2 (Success) / Lambda3 (Failure)
   ↓
SES Email Notification
```

---

## ⚙️ Services Used

* AWS SAM (Infrastructure as Code)
* AWS S3 (Storage & Trigger)
* Amazon EventBridge (Event Routing)
* AWS Step Functions (Workflow Orchestration)
* AWS Lambda (Compute)
* AWS Systems Manager (SSM Parameter Store)
* Amazon SES (Email Notification)

---

## 🪣 S3 Bucket

* Acts as the **entry point of the system**
* File upload triggers an event
* EventBridge integration enabled for real-time event flow

---

## ⚡ EventBridge

* Captures **S3 Object Created events**
* Filters relevant events
* Passes structured input to Step Function using Input Transformer

---

## 🔄 Step Function

* Controls the entire workflow
* Executes tasks in sequence
* Includes:

  * Lambda invocation
  * Conditional branching (Choice State)

---

## 🧪 Lambda Functions

### 🔹 Lambda1 (Core Logic)

* Reads configuration from SSM Parameter Store
* Decides execution path dynamically
* Returns:

  * `"type": "success"` → Lambda2
  * `"type": "fail"` → Lambda3

---

### 🔹 Lambda2 (Success Handler)

* Triggered when execution is successful
* Sends email using SES
* Notifies successful processing

---

### 🔹 Lambda3 (Failure Handler)

* Triggered on failure or mismatch condition
* Sends failure notification email

---

## 🧠 SSM Parameter Store

* Stores dynamic configuration (`my-config`)
* Used to control workflow behavior without code changes

Example:

* Value = `A` → Success flow
* Value ≠ `A` → Failure flow

---

## 📧 SES (Simple Email Service)

* Used for sending email notifications
* Requires verified email addresses
* Sends:

  * Success email (Lambda2)
  * Failure email (Lambda3)

---

## 🔐 IAM Roles & Permissions

* Step Function → Invoke Lambda
* Lambda → Read SSM + Send Email via SES
* EventBridge → Start Step Function

Ensures secure and controlled access between services.

---

## 🚀 Deployment Steps

```bash
sam build
sam deploy --guided
```

---

## 🧪 How to Test

1. Upload a file to the S3 bucket
2. EventBridge triggers Step Function
3. Lambda1 reads config from SSM
4. Based on condition:

   * Success → Lambda2 → Email sent
   * Failure → Lambda3 → Email sent

---

## 💡 Key Concepts Demonstrated

* Event-Driven Architecture
* Serverless Computing
* Loose Coupling using EventBridge
* Workflow Orchestration using Step Functions
* Dynamic Configuration using SSM
* Automated Notifications using SES

---

## 🧨 Real-World Use Case

This architecture can be used for:

* File processing pipelines
* Data validation workflows
* Automated notifications systems
* Serverless backend automation

---

## 🎯 Conclusion

This project showcases a **scalable, loosely coupled, event-driven serverless architecture** that is widely used in real-world cloud applications.

---

## 👨‍💻 Author

* Built using AWS SAM
* Designed for learning, projects, and interview preparation
