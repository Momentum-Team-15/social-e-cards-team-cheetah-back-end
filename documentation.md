# E-Card API

This application is an API built with Django REST Framework (DRF) that lets users track E-Cards that they want to create, share, or favorite -- kind of like any social media. Cards are listed with important information like title, user,font, and whether it is marked as “Published”.

# Link to Production Application
https://ecard-web-service.onrender.com/

**All requests, except registration and log in, require authentication**.

## Required Headers

Requests to endpoints requiring authentication should set the `Authorization` header to `Token <token>`, where `<token>` is the token received in the login response.

POST requests with a body should set the `Content-Type` header to `application/json`.

Documentation starts here: __________________________________________________________________

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

# Social E-Card Endpoints 

Base Url for all endpoints: 
<BASE_URL> : https://ecard-web-service.onrender.com/

## User Authentication

### Register a new user:

#### request:
Username and password are required fields. Email is optional.
Token should not be entered or enabled.

POST  <BASE_URL>/auth/users/

```json
{
  "username": "baby_yoda",
  "password": "grogu"
}
```

#### response:
201 Created

```json
{
  "email": "",
  "username": "baby_yoda",
  "id": 6
}
```

### Log In:

#### request:
Username and password are required fields.

POST  <BASE_URL>/auth/token/login/

```json
{
  "username": "testusername",
  "password": "testpassword"
}
```

### response:
```json
{
  "auth_token": "c312049c7f034a3d1b52eabc2040b46e094ff34c"
}
```

### Log out

#### request:

Authentication Required.
Must be logged in.

POST  <BASE_URL>/auth/token/login/


#### response:
```json
"No body returned for response"
```

### Search for User, Tag, and Cards (Note this is NOT REQUIRED)

This searches for user by their username and name. For tag this searches by there type ("WEDDING","BIRTHDAY","CHRISTMAS", etc..), note for tags to show up th search has to be capitalized. For Cards it searches based on the title of the card. 

Note that the name of the form has to be 'q' for search to work.

#### request:
```txt
GET  <BASE_URL>/search-all/
```
```txt
Query
name = q
value = WEDDING (what is submitted by form)
```

#### response:
```json
{
	"Card": [
		{
			"id": 10,
			"title": "WEDDING",
			"user": 2,
			"border_style": "SOLID",
			"border_color": "BLACK",
			"font_family": "UBUNTO",
			"font_color": "BLACK",
			"text_alignment": "LEFT",
			"outer_msg": "blabla",
			"inner_msg": "yes sir",
			"created_at": "2022-11-20T19:26:26.739390Z",
			"updated_at": "2022-11-20T19:26:26.739408Z",
			"published": false
		}
	],
	"Tag": [
		{
			"id": 3,
			"type": "WEDDING",
			"tag": [
				6,
				8
			]
		}
	],
	"User": [
		{
			"id": 4,
			"name": null,
			"bio": "The greatest test v2",
			"username": "WEDDING",
			"email": ""
		}
	]
}
```

### List all cards of Logged In User:

#### request:
Authentication required.

GET  <BASE_URL>/cards/user/

#### response:
```json
[
	{
		"id": 11,
		"title": "Card 5",
		"user": "admin",
		"border_style": "SOLID",
		"border_color": "BLACK",
		"font_family": "ARIAL",
		"font_color": "BLACK",
		"text_alignment": "LEFT",
		"outer_msg": "Outer Message 5",
		"inner_msg": "Inner Message 5",
		"created_at": "2022-11-30T00:47:02.016961Z",
		"updated_at": "2022-11-30T00:47:33.613417Z",
		"published": true,
		"background_color": "WHITE"
	},
	{
		"id": 12,
		"title": "Card 6",
		"user": "admin",
		"border_style": "DOTTED",
		"border_color": "BLACK",
		"font_family": "UBUNTO",
		"font_color": "BLACK",
		"text_alignment": "LEFT",
		"outer_msg": "Outer Message 6",
		"inner_msg": "Inner Message 6",
		"created_at": "2022-11-30T00:47:24.316047Z",
		"updated_at": "2022-11-30T00:47:24.316067Z",
		"published": true,
		"background_color": "WHITE"
	}
]
```

### List all Cards for logged in user and all published cards:

#### request:
Requires authentication.

GET  <BASE_URL>/cards/

#### response:
```json
[
	{
		"id": 1,
		"title": "The first card made",
		"user": "Corey",
		"border_style": "DOTTED",
		"border_color": "BLACK",
		"font_family": "ARIAL",
		"font_color": "BLACK",
		"text_alignment": "LEFT",
		"outer_msg": "The first card ever made",
		"inner_msg": "Inner message",
		"created_at": "2022-11-29T20:27:12.992621Z",
		"updated_at": "2022-11-29T23:55:39.865951Z",
		"published": true,
		"background_color": "WHITE"
	},
	{
		"id": 5,
		"title": "This is Taylors Card",
		"user": "Taylor",
		"border_style": "GROOVE",
		"border_color": "BLACK",
		"font_family": "RALEWAY",
		"font_color": "BLACK",
		"text_alignment": "LEFT",
		"outer_msg": "This is a test",
		"inner_msg": "Taylor's test that is.",
		"created_at": "2022-11-29T20:36:08.105769Z",
		"updated_at": "2022-11-29T23:56:35.954497Z",
		"published": true,
		"background_color": "WHITE"
	},
	{
		"id": 11,
		"title": "Card 5",
		"user": "admin",
		"border_style": "SOLID",
		"border_color": "BLACK",
		"font_family": "ARIAL",
		"font_color": "BLACK",
		"text_alignment": "LEFT",
		"outer_msg": "Outer Message 5",
		"inner_msg": "Inner Message 5",
		"created_at": "2022-11-30T00:47:02.016961Z",
		"updated_at": "2022-11-30T00:47:33.613417Z",
		"published": true,
		"background_color": "WHITE"
	}
]	
```
### Add a Card:

#### request:
Requires authentication.
Title, border_style, font_family, text_alignment, outer_msg, & inner_msg are required fields.
Background_color, border_color, font_color, published will be set to default if not manually set.

POST  <BASE_URL>/cards/user/

```json
{
	"title": "Bday Card",
	"border_style": "SOLID",
	"font_family": "UBUNTO",
	"text_alignment": "CENTER",
	"outer_msg": "Happy Birthday!",
	"inner_msg": "It's your bday!"
}
```

#### response:
```json
{
	"id": 14,
	"title": "Bday Card",
	"user": "admin",
	"border_style": "SOLID",
	"border_color": "BLACK",
	"font_family": "UBUNTO",
	"font_color": "BLACK",
	"text_alignment": "CENTER",
	"outer_msg": "Happy Birthday!",
	"inner_msg": "It's your bday!",
	"created_at": "2022-11-30T01:00:36.903553Z",
	"updated_at": "2022-11-30T01:00:36.903573Z",
	"published": false,
	"background_color": "WHITE"
}
```

### Delete a Card:

### request:
Requires authentication.

DELETE <BASE_URL>/cards/<int:id>

#### response:
```json
"No body returned for response"
```

### Card detail page:

#### request:
Requires authentication.

GET  <BASE_URL>/cards/<int:pk>

#### response:
```json
{
	"id": 1,
	"title": "The first card made",
	"user": "Corey",
	"border_style": "DOTTED",
	"border_color": "BLACK",
	"font_family": "ARIAL",
	"font_color": "BLACK",
	"text_alignment": "LEFT",
	"outer_msg": "The first card ever made",
	"inner_msg": "Inner message",
	"created_at": "2022-11-29T20:27:12.992621Z",
	"updated_at": "2022-11-29T23:55:39.865951Z",
	"published": true,
	"background_color": "WHITE"
}
```

## Search of user profiles:

searches for users based on username and name of users.

Note name of form needs to be q for search to work

#### request:
```txt
GET  <BASE_URL>/profile/search/
```
```txt
Query
name = q
value = test
```

#### response:
```json
[
	{
		"id": 2,
		"name": null,
		"bio": null,
		"username": "test",
		"email": ""
	}
]
```

### List Logged In User Profile:

#### request
Requires authentication.

GET  <BASE_URL>/profile/

### response
```json
[
	{
		"id": 11,
		"name": null,
		"bio": null,
		"username": "admin",
		"email": "",
		"avatar": null,
		"cards": [
			11,
			12,
			14
		],
		"comments": []
	}
]
```
_________not working/redundant (only works with /me, not pk)__________________
### See profile of other Users:

#### request:
Requires authentication.

GET  <BASE_URL>profile/<int:id>/

#### response:
```json

	{
		"id": 1,
		"name": null,
		"bio": "The greatest example ever",
		"username": "admin",
		"email": ""
	}

```
_______________________________________________________________________

### Update Logged In User's profile:

#### request:
Requires authentication. 
Username is required.

PUT  <BASE_URL>/profile/me/

```json
{
	"username": "ray",
	"name": "Ray",
	"bio": "this is my bio",
	"email": "email@myemail.com"
}
```

### response
```json
{
	"id": 11,
	"name": "Ray",
	"bio": "this is my bio",
	"username": "ray",
	"email": "email@myemail.com",
	"avatar": null,
	"cards": [
		11,
		12,
		14
	],
	"comments": []
}
```

### To delete Logged In User's profile:

#### request:
Requires authentication. 
Be aware the user should then be forced to sign in.  
NOTE THAT username is required in order to update other attributes

DELETE  <BASE_URL>/profile/me/

#### response:
```json
"No body returned for response"
```

### Details for a tags:

#### request:
GET  <BASE_URL>/tags/


#### response:
```json
[
	{
		"id": 1,
		"type": "BIRTHDAY",
		"tag": [
			5
		]
	}
]
```

### Adding a tag

#### request:
Authentication Required.
Tag is a reguired field.
Note that in [] should be id number of card.

POST  <BASE_URL>/tags/

```json
{
	"tag": [6]
}
```
#### response:
```json
[
	{
		"id": 2,
		"type": "null",
		"tag": [
			6
		]
	}
]
```

### Get an Individual Tag:

#### request:
GET  <BASE_URL>/tags/<int:id>/

#### response:
```json
{
	"id": 1,
	"type": "BIRTHDAY",
	"tag": [
		5
	]
}
```

### Editing an Individual Tag:

### request:
PUT  <BASE_URL>/tags/<int:id>/

```json
{
	"tag": [6, 8]
}
```

#### response:
```json
{
	"id": 3,
	"type": null,
	"tag": [
		6,
        8
	]
}
```

### List all comments:

#### request:
Username and password are required.

GET  <BASE_URL>/comments/


#### response:
200 OK
```json
[
	{
		"id": 1,
		"card": 1,
		"comment": "Test comment",
		"commentor": "Taylor"
	},
	{
		"id": 2,
		"card": 5,
		"comment": "this is a comment on Taylor's card by admin",
		"commentor": "admin"
	},
	{
		"id": 3,
		"card": 2,
		"comment": "this is a comment on test card by admin",
		"commentor": "admin"
	}
]
```

### Comment detail page:

#### request:
Authenitcation Required.

GET  <BASE_URL>/comments/<int:id>/

#### response:
200 OK
```json
{
	"id": 1,
	"card": 1,
	"comment": "Test comment",
	"commentor": "Taylor"
}
```

### Add a Comment:

#### request:
Authenitcation Required.
Card and Comment are required fields.

POST  <BASE_URL>/comments/

```json
{
	"card": 1,
	"comment": "This is a comment!"
}
```

#### response:
200 OK
```json
{
	"id": 4,
	"card": 1,
	"comment": "This is a comment!",
	"commentor": "ray"
}
```
### Delete a Comment:

#### request:
Authenitcation Required.

DELETE  <BASE_URL>/comments/<int:id>/

#### response:
200 OK
```json
"No body returned for response"
```

### List all Friends:

#### request:
Authentication Required.

GET  <BASE_URL>/friends/

#### response:
200 OK
```json
[
	{
		"id": 6,
		"user": 2
	},
	{
		"id": 9,
		"user": 3
	}
]
```

### Friends detail page:

#### request:
Authentication Required

GET  <BASE_URL>/friends/<int:id>/

#### response:
200 OK
```json

{
	"id": 6,
	"user": 2
}
```

### Add a Friend:

#### request:
Authentication Required

POST  <BASE_URL>/friends/

```json
{
	"current_user": 1,
	"friend": 4
}
```

#### response:
201 CREATED
```json
{
	"id": 8,
	"current_user": 1,
	"friend": 4
}
```

### Delete a Friend:

#### request:
Authentication Required.
ID is the id of the friendship.

DELETE  <BASE_URL>/friends/<int:id>/

#### response:
```json
"No body returned for response"
```

### List all favorites:

#### request:
Username and password are required.

GET  <BASE_URL>/favorites/

#### response:
200 OK
```json
[
	{
		"id": 1,
		"card": 1,
		"user": 1,
		"created_at": "2022-11-17T18:50:20.189108Z"
	},
	{
		"id": 2,
		"card": 2,
		"user": 1,
		"created_at": "2022-11-17T19:16:30.587099Z"
	}
]
```

### Favorite detail page:

#### request:
Authentication Required.

GET  <BASE_URL>/favorites/int:id/

#### response:
200 OK
```json
{
	"id": 2,
	"card": 2,
	"user": 1,
	"created_at": "2022-11-17T19:16:30.587099Z"
}
```
### Add a Favorite:

#### request:
Authentication Required

POST  <BASE_URL>/favorites/

```json
{
	"current_user": 1,
	"friend": 4
}
```

#### response:
201 CREATED
```json
{
	"id": 8,
	"current_user": 1,
	"friend": 4
}
```

### Delete a Favorite:

#### request:
Authentication Required

DELETE  <BASE_URL>/favorites/<int:id>/

#### response:
```json
"No body returned for response"
```

### Upload/Edit an Avatar Image:

#### request:
Authentication Required.

PATCH  <BASE_URL>/auth/users/me/avatar/

- 'Binary File' should be selected in first drop down > choose file to upload.
- Headers:
| Content-Type	| image/jpeg |
| Content-Disposition| attachment; nameofyourfile.jpeg |

#### response:
200 OK
```json
{
	"id": 1,
	"name": "ray",
	"bio": "this is my bio!",
	"username": "admin",
	"email": "email@email.com",
	"avatar": "https://cheetahbucket2.s3.amazonaws.com/user_avatars/1hector_hQZnOAR.jpeg"
}
```
