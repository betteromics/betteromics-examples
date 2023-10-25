## --------------------------------
## utils.R
## This script will make an API call to Betteromics to pull data.
## Date Created: 10-10-2023
## © 2023 Betteromics Inc.
## --------------------------------

# required packages 
if(!require(httr)){
  install.packages("httr")
  library(httr)
}

if(!require(jsonlite)){
  install.packages("jsonlite")
  library(jsonlite)
}

if(!require(readr)){
  install.packages("readr")
  library(readr)
}

## --------------------------------
## URLs for authentication token
## We will be using Betteromics URL: https://public-demo.betteromics.com
## We will be using Betteromics API URL: https://api.public-demo.betteromics.com/api
## --------------------------------

BETTEROMICS_URL <- "https://public-demo.betteromics.com"
BETTEROMICS_API_URL <- "https://api.public-demo.betteromics.com/api" # used to make API calls

cat(sprintf("We will be using Betteromics URL: %s\n", BETTEROMICS_URL))
cat(sprintf("We will be using Betteromics API URL: %s\n", BETTEROMICS_API_URL))

cat(
  sprintf(
    "Please log into %s through your web browser!\nTHIS STEP IS MANDATORY.\nYou do not have to keep the tab open afterwards.",
    BETTEROMICS_URL
  ))

## --------------------------------
## Generate an API auth token
## Copy the full text (Ctrl+a, Ctrl+c) seen in the browser; Paste the text (token) into the input field below that is shown when the cell is run
## --------------------------------

# shows URL that provides authentication token, using that token, it authenticates the user
auth_session_json <- readline(prompt = paste0("Navigate to ", BETTEROMICS_URL, "/api/session and copy/paste the text from your browser here: "))

auth_session <- jsonlite::fromJSON(auth_session_json)

if (!is.null(auth_session$userSub) && !is.null(auth_session$accessToken)) {
  user_sub <- auth_session$userSub
  access_token <- auth_session$accessToken
  cat(sprintf("You are identified as: %s\n", user_sub))
} else {
  cat("The text you pasted is not valid JSON, please try running this code again.\n",
      sprintf("Be sure to copy ALL text from %s/api/session\n", BETTEROMICS_URL)) 
}

## --------------------------------
## Query Data
## This API call is used to pull back data from Betteromics using a SQL statement to filter the data.
## 1. Ensure you are authenticated & have generated an auth token (see above)
## 2. `create_dataframe_from_query` will pull your specified fields defined in a SQL query
## 3. Result will be returned as a dataframe
## --------------------------------
headers <- c(
  "accept" = "application/json",
  "sub" = user_sub,
  "token" = access_token
)

create_dataframe_from_query <- function (query) {
  # Define the query and request JSON
  query_request <- list(sql_text = query)

  # Make the API request
  data_api_response <- POST(
    url = paste0(BETTEROMICS_API_URL, "/get_query_data"),
    body = query_request,
    encode = "json",
    add_headers(.headers=headers)
  )
  
  if (data_api_response$status == 200) {
    # Get the AWS S3 location where the CSV data file is located
    data_s3_url <- content(data_api_response, "parsed")$download_url
    # Read the CSV data into a data frame
    dataframe <- read_csv(data_s3_url, show_col_types = FALSE)
    return(dataframe)
    
  } else {
    cat("Error encountered:", http_status(data_api_response)$reason, "\n")
  }
}