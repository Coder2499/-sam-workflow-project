def lambda_handler(event, context):
    print("Lambda2 event:", event)
    # Example logic: just return a success message
    return {
        "statusCode": 200,
        "message": "Lambda2 processed successfully"
    }