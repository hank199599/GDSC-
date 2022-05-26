def handleWebhook(request):

    req = request.get_json()

    responseText = ""
    intent = req["queryResult"]["intent"]["displayName"]

    if intent == "Default Welcome Intent":
        responseText = "Hello from a GCP Webhook"
    elif intent == "Default Fallback Intent":
        responseText = "再講一次可以嗎?"
    else:
        responseText = f"沒有定義這個Intent 「{intent}」 在 fulfillment的回應呦!"

    # You can also use the google.cloud.dialogflowcx_v3.types.WebhookRequest protos instead of manually writing the json object
    res = {"fulfillmentMessages": [{"text": {"text": [responseText]}}]}

    return res