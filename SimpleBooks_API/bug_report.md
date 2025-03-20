## Testcase
- ID
- Titlu (verify that..., check that...)
- optional:
  - summary, description
  - Preconditions ()
    - login 
    - credentials
    - token 
    - environment 
    - compatibility testing
  - Steps to reproduce
    - list actions in application
  - Expected results
    - One or more checks, at least one
  - Post conditions
    - At the end of the test


## Bug
- ID
- Titlu (error description)
- optional:
  - summary, description
  - Preconditions ()
    - login
    - credentials
    - token 
    - environment 
    - compatibility testing
  - Steps to reproduce
    - list actions in application
  - Actual results
    - The behaviour of the application based on the user action 
  - Expected results
    - One or more checks, at least one
  - Post conditions
    - At the end of the test


## Bug
- ID
- Titlu (error description)
- optional:
  - summary, description
  - Preconditions ()
    - login
    - credentials
    - token 
    - environment 
    - compatibility testing
  - Steps to reproduce
    - list actions in application
  - Actual results
    - The behaviour of the application based on the user action 
  - Expected results
    - One or more checks, at least one
  - Post conditions
    - At the end of the test

## Title: Unexpected response for get all books endpoint when using limit parameter equal to zero
 - Steps to reproduce
   - use get method for endpoint "https://simple-books-api.glitch.me/books?type=&limit=0"
   - verify the response status code 
   - verify the response json body
 - Actual result
   - the received response status code is 200
   - the json response returns a list with all available books
 - Expected result
   - the received response status code to be 400
   - the json response contains an object with error key "Invalid value for query parameter 'limit'. Must be greater than 1."
 