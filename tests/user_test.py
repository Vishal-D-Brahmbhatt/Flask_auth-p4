import logging
from app import config
from app import db
from app.db.models import User, Song
import os


# from faker import Faker

def test_adding_user(application):
    log = logging.getLogger("myApp")
    with application.app_context():
        assert db.session.query(User).count() == 0
        assert db.session.query(Song).count() == 0
        # showing how to add a record
        # create a record
        user = User('vishal@gmail.com', 'testtest')
        # add it to get ready to be committed
        db.session.add(user)
        # call the commit
        # db.session.commit()
        # assert that we now have a new user
        # assert db.session.query(User).count() == 1
        # finding one user record by email
        user = User.query.filter_by(email='vishal@gmail.com').first()
        log.info(user)
        # asserting that the user retrieved is correct
        assert user.email == 'vishal@gmail.com'
        # this is how you get a related record ready for insert
        user.songs = [Song("test", "smap", 1964, "Jazz"), Song("test2", "te", 1964, "Jazz")]
        # commit is what saves the songs
        db.session.commit()
        assert db.session.query(Song).count() == 2
        song1 = Song.query.filter_by(title='test').first()
        assert song1.title == "test"
        # changing the title of the song
        song1.title = "SuperSongTitle"
        # saving the new title of the song
        db.session.commit()
        song2 = Song.query.filter_by(title='SuperSongTitle').first()
        assert song2.title == "SuperSongTitle"
        # checking cascade delete
        db.session.delete(user)
        assert db.session.query(User).count() == 0
        assert db.session.query(Song).count() == 0


def test_uploading_files(application, client):
    log = logging.getLogger("myApp")
    with application.app_context():
        assert db.session.query(User).count() == 0
        assert db.session.query(Song).count() == 0

    # root = config.Config.BASE_DIR
    # Filecsv = '/music.csv'
    Flupload = config.Config.UPLOAD_FOLDER
    uploadFl = os.path.join(Flupload)
    uploadFile = os.path.join(uploadFl, '/music.csv')
    assert os.path.exists(uploadFl) is True

    resp = client.post('/songs/upload', data=uploadFile, follow_redirects=True)

    assert resp.status_code == 400
