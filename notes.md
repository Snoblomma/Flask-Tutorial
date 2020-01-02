### Create database  
`db.create_all()`

### Querying 
`User.query.all()`  
`User.query.first()`  
`User.query.filter_by(username='Kate').first()`

### Adding to database
`post_1 = Post(title='Blog 1', content='First blog content', user_id=user.id)`
`db.session.add(post_1)`
`db.session.commit()`

### Delete database 
`db.drop_all()`