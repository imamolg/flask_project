from flaskProject.flaskProject import db
from flaskProject.models import BlogPosts,User


#insert 
# db.session.add(BlogPosts("signal","I\'am signal."))
# db.session.add(BlogPosts("ara","I\'am ara."))
# db.session.add(BlogPosts("UC","I\'am UC."))
# db.session.add(BlogPosts("aucland","I\'am aucland."))
# db.session.add(BlogPosts("christchurch","I\'am churstchurch."))
# db.session.add(BlogPosts("quenstown","I\'am quenstown."))
db.session.add(User("chetan","chetan.baadkar@email","password"))


# commit the changes
db.session.commit()
