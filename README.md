# NLP-to-SQL

## Introduction
Using OpenAi state of the art text-davinci-003 model to generate SQL queries from natural language.
This is meant for people with no SQL knowledge to be able to query a database using natural language.

## Requirements
`
pip install -r requirements.txt
`
## Installation
1. Clone the repository
2. Install the requirements
3. Run the main.py file

## Usage
1. Use your own database or use the one provided in the repository
2. You need an OPENAI API key saved as an environment variable called OPENAI_API_KEY

## Example
1. Input: "Show me all the employees that work in the IT department"
2. Output: "SELECT * FROM employees WHERE department = 'IT'"

## Limitations
1. The model is not perfect and will not work for all queries

## Author

Dhruv Sahu


