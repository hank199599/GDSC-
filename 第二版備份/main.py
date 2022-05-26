

def handleWebhook(request):

    import json
    from random import choice

    f = open('meals.json')
    meals_dict = json.load(f)

    req = request.get_json()

    responseText = ""
    intent = req["queryResult"]["intent"]["displayName"]

    if intent == "Default Welcome Intent":
        responseText = "來自Cloud Function的誠摯歡迎"
    elif intent == "Default Fallback Intent":
        fallbacks = ["再講一次可以嗎?","對不起，我不清楚你所表達的意思","試著換個方式問看看吧","我剛剛恍神了，再說一次好嗎?"]
        responseText = choice(fallbacks)
    elif intent == "輸出想到的美食":
        types = req["queryResult"]["parameters"]["input"]
        if types in ["午餐","晚餐"]:
            types = "午晚餐"

        if types in list(meals_dict.keys()):
            results = choice(meals_dict[types])
            responseText = f" 「{results}」如何呢? "
        else:
            fallbacks = ["我當機了，讓我再想一下","再幫我撐十秒","等待靈感降落中..."]
            responseText = choice(fallbacks)

    # You can also use the google.cloud.dialogflowcx_v3.types.WebhookRequest protos instead of manually writing the json object
    res = {"fulfillmentMessages": [{"text": {"text": [responseText]}}]}

    return res