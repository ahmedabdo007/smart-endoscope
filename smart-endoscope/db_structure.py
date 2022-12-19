from peewee import *

db=MySQLDatabase('endscop', user='root', password='root',
                         host='localhost', port=3306)



class specialization(Model):
    name = CharField()

    class Meta:
        database = db

gender_chioces=(
    (1,'Male'),
    (2,'Female')
)


class patient(Model):
    name = CharField()
    age = IntegerField(null=True)
    gender = CharField(null=True,choices=gender_chioces) 
    sergarydate = DateField()
    address = CharField(null=True)
    phone = CharField(null=True)
    

    class Meta:
        database = db
    
class doctor(Model):
    name = CharField()
    address = CharField(null=True)
    phone = CharField(null=True)
    specialization = ForeignKeyField(specialization,backref="specialization",unique=True)

    class Meta:
        database = db

class admin(Model):
    name = CharField()
    national_id = IntegerField(null=True,unique=True)
    phone = CharField(null=True)
    email = CharField(null=True,unique=True)

    class Meta:
        database = db

db.connect()
db.create_tables([ specialization , patient , doctor , admin])
