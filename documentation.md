# E-Card API

This application is an API built with Django REST Framework (DRF) that lets users track E-Cards that they want to create, share, or favorite -- kind of like any social media. Cards are listed with important information like title, user,font, and whether it is marked as “Published”.

**All requests, except registration and log in, require authentication**.

## Required Headers

Requests to endpoints requiring authentication should set the `Authorization` header to `Token <token>`, where `<token>` is the token received in the login response.

POST requests with a body should set the `Content-Type` header to `application/json`.

Documentation starts here: __________________________________________________________________

## Register a new user

### request

Username and password are required.

```
POST <BASE_URL>/auth/users/

{
  "username": "baby_yoda",
  "password": "grogu"
}
```

### response

```
201 Created

{
  "email": "",
  "username": "baby_yoda",
  "id": 6
}

```

## Log In

### request

```
POST <BASE_URL>/auth/token/login/

{
  "username": "testusername",
  "password": "testpassword"
}
```

### response

```json
{
  "auth_token": "c312049c7f034a3d1b52eabc2040b46e094ff34c"
}
```


## A search for User, Tag, and Cards (Note this is NOT REQUIRED)

This searches for user by their username and name. For tag this searches by there type ("WEDDING","BIRTHDAY","CHRISTMAS", etc..), note for tags to show up th search has to be capitalized. For Cards it searches based on the title of the card. 

Note that the name of the form has to be 'q' for search to work.

### request

```txt
GET <BASE_URL>/search-all/
```
```txt
Query
name = q
value = WEDDING (what is submitted by form)
```

### response

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

## List all Cards for particular user
Requires authentication.
### request
```txt
GET <BASE_URL>/cards/user/
```
### response
```json
[
    {
        "id": 2,
        "title": "Test",
        "user": 1,
        "border_style": "DOTTED",
        "border_color": "BLUE",
        "font_family": "RALEWAY",
        "font_color": "BLACK",
        "text_alignment": "CENTER",
        "outer_msg": "asdasd",
        "inner_msg": "adasdasd",
        "created_at": "2022-11-17T12:32:33.657292Z",
        "updated_at": "2022-11-17T12:32:33.657327Z",
        "published": false
    },
    {
        "id": 3,
        "title": "Test2",
        "user": 1,
        "border_style": "DOTTED",
        "border_color": "BLACK",
        "font_family": "MERRIWEATHER",
        "font_color": "BLACK",
        "text_alignment": "RIGHT",
        "outer_msg": "asdasdsad",
        "inner_msg": "sasdadsasadsa",
        "created_at": "2022-11-17T12:32:47.668606Z",
        "updated_at": "2022-11-17T12:32:47.668642Z",
        "published": true
    }
]
```

## List all Cards for particular user and all published

Requires authentication.

### request

```txt
GET <BASE_URL>/cards/
```

### response

```json
[
	{
		"id": 2,
		"title": "Test",
		"user": 1,
		"border_style": "DOTTED",
		"border_color": "BLUE",
		"font_family": "RALEWAY",
		"font_color": "BLACK",
		"text_alignment": "CENTER",
		"outer_msg": "asdasd",
		"inner_msg": "adasdasd",
		"created_at": "2022-11-17T12:32:33.657292Z",
		"updated_at": "2022-11-17T12:32:33.657327Z",
		"published": false
	},
	{
		"id": 3,
		"title": "Test2",
		"user": 4,
		"border_style": "DOTTED",
		"border_color": "BLACK",
		"font_family": "MERRIWEATHER",
		"font_color": "BLACK",
		"text_alignment": "RIGHT",
		"outer_msg": "asdasdsad",
		"inner_msg": "sasdadsasadsa",
		"created_at": "2022-11-17T12:32:47.668606Z",
		"updated_at": "2022-11-17T12:32:47.668642Z",
		"published": true
    }
]
```
## Add a Card

Requires authentication.

### request

```txt
POST <BASE_URL>/cards/
```
```json
{
	"title": "example",
	"border_style": "SOLID",
	"font_family": "UBUNTO",
	"text_alignment": "LEFT",
	"outer_msg": "blabla",
	"inner_msg": "yes sir"
}
```

### response

```json

{
	"id": 7,
	"title": "example",
	"user": 1,
	"border_style": "SOLID",
	"border_color": "BLACK",
	"font_family": "UBUNTO",
	"font_color": "BLACK",
	"text_alignment": "LEFT",
	"outer_msg": "blabla",
	"inner_msg": "yes sir",
	"created_at": "2022-11-17T18:13:32.950733Z",
	"updated_at": "2022-11-17T18:13:32.950747Z",
	"published": false
}

```

## Look at cards details

Requires authentication. 

### request

```txt
GET <BASE_URL>/cards/<int:pk>/
```

### response
```json
{
	"id": 7,
	"title": "example",
	"user": 1,
	"border_style": "SOLID",
	"border_color": "BLACK",
	"font_family": "UBUNTO",
	"font_color": "BLACK",
	"text_alignment": "LEFT",
	"outer_msg": "blabla",
	"inner_msg": "yes sir",
	"created_at": "2022-11-17T18:13:32.950733Z",
	"updated_at": "2022-11-17T18:13:32.950747Z",
	"published": false
}
```

## Search of user profiles

searches for users based on username and name of users.

Note name of form needs to be q for search to work

### request

```txt
GET <BASE_URL>/profile/search/
```
```txt
Query
name = q
value = test
```

### response

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

## List user profile

Requires authentication.

### request

```txt
GET <BASE_URL>/profile/
```


### response

```json
[
	{
		"id": 1,
		"name": null,
		"bio": "The greatest example ever",
		"username": "admin",
		"email": ""
	}
]
```

## To look at info in a user profile

Requires authentication.

### request

```txt
GET <BASE_URL>profile/<int:id>/
```

### response

```json

	{
		"id": 1,
		"name": null,
		"bio": "The greatest example ever",
		"username": "admin",
		"email": ""
	}

```

## To update a user profile

Requires authentication. NOTE THAT username is required in order to update other attributes

### request

```txt
PUT <BASE_URL>/profile/<int:id>
```
```json
{
	"id": 1,
	"name": null,
	"bio": "The greatest test",
	"username": "admin",
	"email": ""
}
```

### response

```json
[
	{
		"id": 1,
		"name": null,
		"bio": "The greatest test",
		"username": "admin",
		"email": ""
	}
]
```

## To delete a user profile

Requires authentication. Be aware the user should then be forced to sign in.  NOTE THAT username is required in order to update other attributes

### request

```txt
DELETE <BASE_URL>/profile/<int:id>
```
```json
{
	"username": "admin",
}
```

### response

```json
[

]
```

## Details for a tags

### request

```txt
GET <BASE_URL>/tags/
```

### response

```json
[
	{
		"id": 2,
		"type": "BIRTHDAY",
		"tag": [
			6
		]
	}
]
```

## Adding a tag
Note that in [] should be id number of card

### request

```txt
POST <BASE_URL>/tags/
```
```json
{
	"tag": [6]
}
```
### response

```json
[
	{
		"id": 2,
		"type": "BIRTHDAY",
		"tag": [
			6
		]
	}
]
```

## getting indiv tag

### request

```txt
GET <BASE_URL>/tags/<int:id>/
```
### response

```json
{
	"id": 3,
	"type": null,
	"tag": [
		6
	]
}
```

## Editing indiv tag

### request

```txt
PUT <BASE_URL>/tags/<int:id>/
```
```json
{
	"tag": [6, 8]
}
```

### response

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

## List all comments

### request

Username and password are required.

```
GET <BASE_URL>/comments/

```

### response

```json
200 OK

[
	{
		"id": 3,
		"card": 3,
		"comment": "This is a comment by user on Ray's bday card!",
		"commentor": 2
	},
	{
		"id": 2,
		"card": 3,
		"comment": "This is a comment on Ray's Birthday card by admin!",
		"commentor": 1
	},
	{
		"id": 1,
		"card": 1,
		"comment": "This is a comment by admin on Autumn 2022 card!",
		"commentor": 1
	}
]

```

## Comment detail page

### request

Username and password are required.

```
GET <BASE_URL>/comments/1/

```

### response

```json
200 OK

{
	"id": 1,
	"card": 1,
	"comment": "This is a comment by admin on Autumn 2022 card!",
	"commentor": 1
}

```

## List all Friends

### request

Username and password are required.

```
GET <BASE_URL>/friends/

```

### response

```json
200 OK

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

## Friends detail page

### request

Username and password are required.

```
GET <BASE_URL>/friends/6/

```

### response

```json
200 OK

{
	"id": 6,
	"user": 2
}
```

## List all favorites

### request

Username and password are required.

```
GET <BASE_URL>/favorites/

```

### response

```json
200 OK

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

## Favorite detail page

### request

Username and password are required.

```
GET <BASE_URL>/favorites/2/

```

### response

```json
200 OK

{
	"id": 2,
	"card": 2,
	"user": 1,
	"created_at": "2022-11-17T19:16:30.587099Z"
}

```
