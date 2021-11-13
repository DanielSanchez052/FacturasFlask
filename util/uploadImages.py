import os
import uuid
from werkzeug.utils import secure_filename 
import config

def uploadImage(file):
    if file.filename == '': return 'NAN'

    if file : #and allowed_file(file.filename)
        filename = secure_filename(uuid.uuid4().hex+file.filename)
        file.save(os.path.join(config.Config.UPLOAD_FOLDER,filename))
        return filename