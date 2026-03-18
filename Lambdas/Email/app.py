import boto3

ses = boto3.client("ses")

def lambda_handler(event, context):
    try:
        response = ses.send_email(
            Source="ryuzakilevi6@gmail.com",  # your verified sender
            Destination={
                "ToAddresses": ["ryuzakilevi6@gmail.com"]  # recipient
            },
            Message={
                "Subject": {
                    "Data": "Step Function Notification"
                },
                "Body": {
                    "Text": {
                        "Data": f"Workflow finished. Event: {event}"
                    }
                }
            }
        )
        print("SES response:", response)
        return {"statusCode": 200, "body": "Email sent successfully"}
    except Exception as e:
        print("Error sending email:", e)
        return {"statusCode": 500, "error": str(e)}