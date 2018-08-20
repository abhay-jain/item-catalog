from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Items, Base, User

engine = create_engine('sqlite:///itemcatalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine


DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create dummy user
User1 = User(name="Abhay Jain", email="abhayj72@gmail.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# Items for Category Soccer
category1 = Category(user_id=1, name="Soccer")
session.add(category1)
session.commit()

item1 = Items(user_id=1, name="Shinguards", category=category1
	, description="A shin guard or shin pad is a piece of equipment worn on the front of a player's shin to protect them from injury. These are commonly used in sports including association football, baseball, ice hockey, field hockey, lacrosse, cricket, and other sports.")

item2 = Items(user_id=1, name="Jersey", category=category1
	, description="a knitted garment with long sleeves, worn over the upper body.")

item3 = Items(user_id=1, name="Soccer Cleats", category=category1
	, description="Football boots, called cleats or soccer shoes in North America, are an item of footwear worn when playing football. Those designed for grass pitches have studs on the outsole to aid grip.")

session.add(item1)
session.commit()
session.add(item2)
session.commit()
session.add(item3)
session.commit()


#Items for Category Basketball
category2 = Category(user_id=1, name="Basketball")
session.add(category2)
session.commit()

item1 = Items(user_id=1, name="Backboard", category=category2
	, description="The backboard is the rectangular board that is placed behind the rim. It helps give better rebound to the ball.")

item2 = Items(user_id=1, name="Jersey", category=category2
	, description="The T-shirt")

item3 = Items(user_id=1, name="Shoes", category=category2
	, description="One needs specialized shoes when playing basketball.")

session.add(item1)
session.commit()
session.add(item2)
session.commit()
session.add(item3)
session.commit()



#Items for Category Baseball
category3 = Category(user_id=1, name="Baseball")
session.add(category3)
session.commit()

item1 = Items(user_id=1, name="Gloves", category=category3
	, description="One of the first things you'll need is a baseball glove")

item2 = Items(user_id=1, name="Bat", category=category3
	, description="Baseball bat is the next thing you need")

item3 = Items(user_id=1, name="Base ball", category=category3
	, description="Ball is the one with which you play")

session.add(item1)
session.commit()
session.add(item2)
session.commit()
session.add(item3)
session.commit()



#Items for Category Frisbee
category4 = Category(user_id=1, name="Frisbee")
session.add(category4)
session.commit()


item1 = Items(user_id=1, name="Frisbee", category=category4
	, description="the frisbee itself")

session.add(item1)
session.commit()

#Items for Category Snowboarding
category5 = Category(user_id=1, name="Snowboarding")
session.add(category5)
session.commit()

item1 = Items(user_id=1, name="Snowboard", category=category5
	, description="The board used in Snowboarding")


session.add(item1)
session.commit()


#Items for Category Hockey
category6 = Category(user_id=1, name="Hockey")
session.add(category6)
session.commit()

item1 = Items(user_id=1, name="Hockey stick", category=category6
	, description="The stick used in hockey to play the game")

item2 = Items(user_id=1, name="Ball", category=category6
	, description="The ball used in the game")


session.add(item1)
session.commit()
session.add(item2)
session.commit()
