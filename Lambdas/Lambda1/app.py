import boto3

ssm = boto3.client("ssm")

def lambda_handler(event, context):
    print("Lambda1 event:", event)
    try:
        response = ssm.get_parameter(Name="my-config")
        value = response["Parameter"]["Value"]
        return {
            "statusCode": 200,
            "ssm_value": value
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "error": str(e)
        }