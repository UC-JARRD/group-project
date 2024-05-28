# Authorization Server - Data Contract
1. Token:
access_token (str): The access token generated during authentication.
token_type (str): The type of token, typically "bearer".
2. TokenData:
username (str, optional): The username associated with the token data. It can be None.
4. User:
username (str): The username of the user.
email (str, optional): The email address of the user. It can be None.
full_name (str, optional): The full name of the user. It can be None.
disabled (bool, optional): Indicates whether the user is disabled. It can be None.
4. UserInDB:
Inherits from User.
hashed_password (str): The hashed password of the user stored in the database.

# Endpoints:
1. POST /token:
Request Body: OAuth2PasswordRequestForm
Response Body: Token
Description: Endpoint for user login. Validates credentials, generates an access token, and returns it. Uses the OAuth2PasswordRequestForm model for form data.
2. GET /users/me/:
Request Headers: Authorization token
Response Body: User
Description: Endpoint to get the current user’s details.
3. GET /users/me/items:
Request Headers: Authorization token
Response Body: List of items
Description: Endpoint to get items owned by the current user.

# Notes:
- The Token model represents the structure of the access token returned during login.
- The TokenData model represents additional token data, such as the username associated with the token.
- The User model represents the structure of user data.
- The UserInDB model extends User and includes additional data stored in the database, such as the hashed password.
- Endpoints /users/me/ and /users/me/items require a valid authorization token in the request headers to access user-specific data.

Ensure to specify the database for user authentication and retrieval.