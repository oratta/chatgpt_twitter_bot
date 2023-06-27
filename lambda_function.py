import json
import main
def lambda_handler(event, context):
    # TODO implement
    text = main.main()
    return {
        'statusCode': 200,
        'body': json.dumps(text)
    }
