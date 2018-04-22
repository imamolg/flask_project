from flaskProject.flaskProject import db
from flaskProject.models import BlogPosts

BlogPosts.__table__.drop(engine)

# create the data base and db table
db.create_all()

#insert 
db.session.add(BlogPosts("Good","I\'am good."))
db.session.add(BlogPosts("Well","I\'am well."))
db.session.add(BlogPosts("Test","I\'am Test."))

# commit the changes
db.session.commit()
