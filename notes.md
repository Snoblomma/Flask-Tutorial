### Import db
`from flaskblog import db`

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

### Tree of dependencies
`pipdeptree`

### Environment vars
`set "SECRET_KEY=really secret don't tell anyone"`

Then to check if it's really set:  
`echo %SECRET_KEY%`