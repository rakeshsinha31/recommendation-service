import jwt
import json
import numpy as np
import pandas as pd
from django.http import JsonResponse
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer


def important_features(dataset):
    data = dataset.copy()
    for _ in range(0, dataset.shape[0]):
        data[
            "imp"
        ] = f"{data['preferences']} {data['product_name']} {data['description']} {data['tags']}"
    return data


def recommend_ten(recon_list):
    first_ten = []
    count = 0
    for rec in recon_list:
        if count > 9:
            break
        count += 1
        first_ten.append(rec)
    return first_ten


def get_cosine_similarity(id, data):
    vec = TfidfVectorizer()
    vecs = vec.fit_transform(data["imp"].apply(lambda x: np.str_(x)))
    sim = cosine_similarity(vecs)
    item_id = data[data.user_id == id]["user_id"].values[0]
    scores = list(enumerate(sim[item_id]))
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
    sorted_scores = sorted_scores[1:]
    recons = [
        data[m[0] == data["user_id"]]["product_name"].values for m in sorted_scores
    ]
    first_ten = recommend_ten(recons)
    final_recommendetions = []
    for _, names in enumerate(first_ten):
        if names.size > 0:
            final_recommendetions.append(names)
    return final_recommendetions


def recommendations(request, user_id):
    token = request.headers.get("Authorization")

    if not token:
        return JsonResponse({"Error": "Missing Auth Token!"}, safe=False)
    try:
        jwt.decode(token, "secret", algorithms=["HS256"])
    except:
        return JsonResponse({"Error": "Invalid Token!"}, safe=False)

    dataset = pd.read_csv("/Users/rakeshsinha/Downloads/dataset.csv")

    """
    Call internal API to get the user transactions
    api_url = f"http://127.0.0.1:8000/api/get_dataset/{user_id}"
    response = requests.get(api_url)
    if response.status_code != 200:
        raise Exception
    dataset = response.json()
    """

    df = pd.DataFrame(dataset)
    data = important_features(df)
    recons = get_cosine_similarity(user_id, data)
    json_object = json.dumps([arr.tolist() for arr in recons])
    return JsonResponse(json_object, safe=False)
