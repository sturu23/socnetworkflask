
class Crud:


    def create(self,commit=None,**kwargs):
        for key,value in kwargs.items():
            setattr(self,key,value)

        if commit is not None:
            self.save()

    @classmethod
    def read(cls,id):
        return cls.query.all(id=id)


    def update(self,commit=None,**kwargs):
        for key,value in kwargs.items():
            setattr(self,key,value)
        if commit is not None:
            db.session.commit()


    def delete(self,commit=None):
        if commit is not None:
            db.session.delete(self)
            db.session.commit()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def find_by_email(self,email):
        email = self.query.filter_by(email=email).first()
        if email:
            return 'exists'
