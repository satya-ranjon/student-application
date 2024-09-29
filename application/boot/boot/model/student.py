from pweb_orm import PwebModel, pweb_orm


class Student(PwebModel):
    pictureUrl = pweb_orm.Column("pictureUrl", pweb_orm.String())
    name = pweb_orm.Column("name", pweb_orm.String(150), nullable=False)
    email = pweb_orm.Column("email", pweb_orm.String(150), nullable=False)
    password = pweb_orm.Column("password", pweb_orm.String(250), nullable=False)
    address = pweb_orm.Column("address", pweb_orm.Text())
    fatherName = pweb_orm.Column("fatherName", pweb_orm.String(150))
    motherName = pweb_orm.Column("motherName", pweb_orm.String(150))
    phoneNumber = pweb_orm.Column("phoneNumber", pweb_orm.String(20))
    dateOfBirth = pweb_orm.Column("dateOfBirth", pweb_orm.Date())




    
    # phoneNumber = pweb_orm.Column("phoneNumber", pweb_orm.String(20), nullable=True)
    # enrollmentDate = pweb_orm.Column("enrollmentDate", pweb_orm.Date(), default=datetime.now)
    # gradeLevel = pweb_orm.Column("gradeLevel", pweb_orm.Integer(), nullable=False)
    # studentID = pweb_orm.Column("studentID", pweb_orm.String(20), unique=True, nullable=False)
    # emergencyContact = pweb_orm.Column("emergencyContact", pweb_orm.String(150), nullable=True)
    # medicalInfo = pweb_orm.Column("medicalInfo", pweb_orm.Text(), nullable=True)
    # isActive = pweb_orm.Column("isActive", pweb_orm.Boolean(), default=True)