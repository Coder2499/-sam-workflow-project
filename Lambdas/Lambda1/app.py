import boto3

ssm = boto3.client('ssm')

def handler(event, context):
    print("Event:", event)

    try:
        param = ssm.get_parameter(Name="my-config", WithDecryption=True)
        value = param['Parameter']['Value']

        return {
            "type": "success",
            "config": value,
            "input": event
        }
    except Exception as e:
        return {
            "type": "fail",
            "error": str(e),
            "input": event
        }