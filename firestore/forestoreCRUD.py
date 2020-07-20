import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Insert object
class City():
    def __init__(self, name, state, country, capital=False, population=0,
                 regions=[]):
        self.name = name
        self.state = state
        self.country = country
        self.capital = capital
        self.population = population
        self.regions = regions

    @staticmethod
    def from_dict(source):
        pass

    def to_dict(self):
        return {
            'name' : self.name,
            'state' : self.state,
            'country' : self.country,
            'capital' : self.capital,
            'population' : self.population,
            'regions' : self.regions
        }

    def __repr__(self):
        return(
            u'City(name={}, country={}, population={}, capital={}, regions={})'
            .format(self.name, self.country, self.population, self.capital,
                    self.regions))

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

    # 割とプロジェクトごとに実装は異なる感じっぽい
    def sample_query(self):
        doc_ref = self.collection(u'cities')
        doc_ref.where(u'population', u'<', 100000)
        doc_ref.where(u'state', u'==', u'CA')

        return doc_ref.stream()

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


    collection = u'cities'
    data = City(u'San Francisco', u'CA', u'USA', False, 860000, [u'west_coast', u'norcal']).to_dict()
    firebase_crud.add(collection, u'SF', data)

    data = City(u'Los Angeles', u'CA', u'USA', False, 3900000, [u'west_coast', u'socal']).to_dict()
    firebase_crud.add(collection, u'LA', data)    

    # query version
    docs = firebase_crud.sample_query()
    for doc in docs:
        print(u'{} => {}'.format(doc.id, doc.to_dict()))
