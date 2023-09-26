import pymongo
url = "mongodb://mongoadmin:secret@127.0.0.1/admin"

class Persona:
	name: str
	surname: str

	def set_person(self,name,surname):
		self.name=name
		self.surname = surname


class DB:
	def save_to_database(self,persona):
	    connection = pymongo.MongoClient(url)
	    connection["testing"]["people"].insert_one(self.__dict__)




hector = Persona()
# Gestiona los datos
hector.set_person("Hector","Romero")
# Guarda en la base de datos
hector.save_to_database()


