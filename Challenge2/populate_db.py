import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from table_def import Album, Artist
 
engine = create_engine('sqlite:///mymusic.db', echo=True)
 
# create a Session
Session = sessionmaker(bind=engine)
session = Session()
 
# Create an artist
new_artist = Artist("Newsboys")
new_artist.albums = [Album("Live Love A ", 
                          "Rap",
                           "ASAP Rocky", "CD")]
 
# add more albums
more_albums = [Album("I am not a human being",
                     "Rap",
                     "Lil Wayne", "CD"),
               Album("Title and Registration", 
                     "Country",
                     "Death Cab for Cutie", "CD"),
               Album("Curtain Call: The Hits",
                     "Country",
                     "Eminem", "CD")]
new_artist.albums.extend(more_albums)
 
# Add the record to the session object
session.add(new_artist)
# commit the record the database
session.commit()
 
# Add several artists
session.add_all([
    Artist("Eminem"),
    Artist("Lil Wayne"),
    Artist("Dave Matthews Band")
    ])
session.commit()
