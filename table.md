# URLS
| URL	| Description | Possible request |
| -----|-----|-----| 
| BASE_URL/auth/users/| register a new user | POST |
| BASE_URL/auth/token/login/ | log in | POST |
| BASE_URL/auth/token/logout/ | log out | POST |
| BASE_URL/search-all/ | (optional)A search for user, tag, and Cards | GET |
| BASE_URL/cards/user/ | show all card for user logged in | GET, POST |
| BASE_URL/cards/ | Show all cards that are published and all cards user has created | GET |
| BASE_URL/cards/int:pk/ | Looks at card detail | GET, PUT, PATCH, DELETE |
| BASE_URL/profile/search/ | (optional) searches for users based on username and name of user | GET|
| BASE_URL/profile/ | list logged in user profile | GET |
| BASE_URL/profile/int:pk/ | detail of logged in user profile | GET, PUT, DELETE |
| BASE_URL/tags/ | gives tag information | GET, POST |
| BASE_URL/tags/int:pk/ | editing indiv tag to remove cards from being tagged | GET, PUT |
| BASE_URL/comments/ | List all comments | GET, POST |
| BASE_URL/comments/int:pk/ | list comment detail page | GET, PUT, DELETE |
| BASE_URL/friends/ | list all friends | GET, POST |
| BASE_URL/friends/int:pk/ | Friends detail page | GET, DELETE |
| BASE_URL/favorites/ | list all favorite cards | GET, POST |
| BASE_URL/favorites/int:pk/ | detail about favorited item | GET, DELETE |