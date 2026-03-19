import boto3

ses = boto3.client('ses', region_name='ap-south-1')

def handler(event, context):
    print("Success Flow:", event)

    ses.send_email(
        Source='ryuzakilevi6@gmail.com',
        Destination={'ToAddresses': ['ryuzakilevi6@gmail.com']},
        Message={
            'Subject': {'Data': 'SUCCESS: File Uploaded ✅'},
            'Body': {
                'Text': {
                    'Data': f"File processed successfully\n\nEvent: {event}"
                }
            }
        }
    )

    return {"status": "success email sent"}