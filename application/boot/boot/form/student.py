from boot.model.student import Student
from pweb_form_rest import fields, PWebForm


class StudentDetailsForm(PWebForm):

    class Meta:
        model = Student
        load_instance = True

    pictureUrl = fields.String()
    name = fields.String(required=True, error_messages={"required": "Please enter name"})
    email = fields.Email(required=True, error_messages={"required": "Please enter email"})
    address = fields.String(allow_none=True, type="textarea")
    fatherName = fields.String()
    motherName = fields.String()
    phoneNumber = fields.Integer(required=True, error_messages={"required": "Please enter phone number"})
    dateOfBirth = fields.Date(required=True, error_messages={"required": "Please enter date of birth"})



class StudentCreateForm(StudentDetailsForm):
    class Meta:
        model = Student
        load_instance = True

    password = fields.String(required=True, error_messages={"required": "Please enter password"}, type="password")


class StudentUpdateForm(StudentDetailsForm):
    class Meta:
        model = Student
        load_instance = True

    id = fields.Integer(required=True, error_messages={"required": "Please enter id"}, type="hidden", isLabel=False)

