def lambda_handler(event, context):
    print("Lambda3 event:", event)
    # Example logic: just return a success message
    return {
        "statusCode": 200,
        "message": "Lambda3 processed successfully"
    }