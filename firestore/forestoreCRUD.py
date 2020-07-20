import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


class Firestore_CRUD():
    self.db = None;

    def __init__(self, project_id):
        self.db = self.init_project(project_id)

    def init_project(self, project_id):
        # Use the application default credentials
        cred = credentials.ApplicationDefault()
        firebase_admin.initialize_app(cred, {
        'projectId': project_id,
        })

        return firestore.client()


    def add(self, collection , document, data):
        doc_ref = self.db.collection(collection).document(document)
        doc_ref.set(data)

    def get(self, collection):
        users_ref = self.db.collection(collection)
        docs = users_ref.stream()
        return docs

if __name__ == '__main__':
    firebase_crud = Firestore_CRUD('projectId')
    data = {
        u'key' : u'value'
    }
    collection = u'user'
    document = u'name'

    # add
    firebase_crud.add(collection, document, data)

    # get
    docs = firebase_crud.get(collection)
    for doc in docs:
        print(u'{} => {}'.format(doc.id, doc.to_dict()))

    # query version
    
    