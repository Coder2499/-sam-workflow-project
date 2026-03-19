import boto3

ses = boto3.client('ses', region_name='ap-south-1')

def handler(event, context):
    print("Failure Flow:", event)

    ses.send_email(
        Source='ryuzakilevi6@gmail.com',
        Destination={'ToAddresses': ['ryuzakilevi6@gmail.com']},
        Message={
            'Subject': {'Data': 'FAILED: File Processing ❌'},
            'Body': {
                'Text': {
                    'Data': f"Something went wrong\n\nEvent: {event}"
                }
            }
        }
    )

    return {"status": "failure email sent"}