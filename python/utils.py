# --------------------------------
# utils.py
# This script will make an API call to Betteromics to pull data.
# Date Created: 10-10-2023
# © 2023 Betteromics Inc.
# --------------------------------

import json

import pandas as pd
import requests


def create_dataframe_from_query(query: str) -> pd.DataFrame:
    """
    Args:
        query (str): a SQL statement to filter the data.

    Returns:
        dataframe (pd.DataFrame): data pulled from Betteromics API
    """
    query_request = {"sql_text": query}

    # Make the API request
    data_api_response = requests.post(
        url=f"{BETTEROMICS_API_URL}/get_query_data",
        headers={"accept": "application/json", "sub": user_sub, "token": access_token},
        json=query_request,
    )
    # Checking for errors
    if data_api_response.status_code != 200:
        error_response = data_api_response.json()
        if "detail" in error_response and "message" in error_response["detail"]:
            error_message = error_response["detail"]["message"]
            print(f"Error encountered: {error_message}")
            if "Invalid signature" in error_message:
                print(f"You need to re-authenticate and generate a new token\nNavigate to {BETTEROMICS_URL} and log in")
        raise Exception(error_response)

    # Get the AWS S3 location where the CSV data file is located
    data_s3_url = data_api_response.json()["download_url"]
    return pd.read_csv(data_s3_url)


# --------------------------------
# URLs for authentication token
# We will be using Betteromics URL: https://public-demo.betteromics.com
# We will be using Betteromics API URL: https://api.public-demo.betteromics.com/api
# --------------------------------
BETTEROMICS_URL = "https://public-demo.betteromics.com"
BETTEROMICS_API_URL = "https://api.public-demo.betteromics.com/api"  # used to make API calls

print(f"We will be using Betteromics URL: {BETTEROMICS_URL}")
print(f"We will be using Betteromics API URL: {BETTEROMICS_API_URL}")
print(
    f"Please log into {BETTEROMICS_URL} through your web browser!\nTHIS STEP IS MANDATORY.\nYou do not have to keep the"
    " tab open afterwards."
)

# --------------------------------
# Generate an API auth token
# Copy the full text (Ctrl+a, Ctrl+c) seen in the browser; Paste the text (token) into the input field below that is shown when the cell is run
# --------------------------------

# shows URL that provides authentication token, using that token, it authenticates the user
auth_session_json = input(
    f"Navigate to {BETTEROMICS_URL}/api/session and copy/paste the text from your browser here and press enter: "
)

try:
    auth_session = json.loads(auth_session_json)
    user_sub = auth_session["userSub"]
    access_token = auth_session["accessToken"]
    print(f"You are identified as: {user_sub}")
except json.JSONDecodeError:
    print(
        "The text you pasted is not valid JSON,"
        "please try running this cell again.\n"
        f"Be sure to copy ALL text from {BETTEROMICS_URL}/api/session"
    )
