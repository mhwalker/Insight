import hashlib

api_key='6bd1a01c8bfafc91299636a8cfeabdc1'
api_secret='961a58beef5c05381882dc27417e10bc'
pf_url='http://api.petfinder.com/'

def formSecret(arguments):
    mash=api_secret+arguments
    m = hashlib.md5()
    m.update(mash)
    return m.hexdigest()

def formRequest(action,arguments):
    return pf_url+action+"?"+arguments

def cleanPhotoList(photos):
    newPhotos = []
    for photo in photos:
        if photo["size"] == 'x':
            newPhotos.append(photo)
    return newPhotos