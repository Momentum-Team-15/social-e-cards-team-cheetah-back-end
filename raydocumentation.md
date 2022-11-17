## List all comments

### request

Username and password are required.

```
GET <BASE_URL>/comments

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
GET <BASE_URL>/comments/1

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
GET <BASE_URL>/friends

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
GET <BASE_URL>/friends/6

```

### response

```json
200 OK

{
	"id": 6,
	"user": 2
}


## List all favorites

### request

Username and password are required.

```
GET <BASE_URL>/favorites

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
GET <BASE_URL>/favorites/2

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
