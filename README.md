
# EMS Project

Small project to manage the employees of an organisation.


## Features

- User Register, Login, Logout
- Employee Management (CRUD)
- Leave Mangement (Create, Read)
- Feature level permissions (Admin only, User Only)


## To Do

(__For Admin__)
- Login API
- Employee Mangement
    - Employees List API
        - Functionalities: search, sort. (__Pending__)
        - Show: Employee id, Employee Name, contact, Email, Designation, Reporting to, Work location. (__Completed__) 
    - Employee Details API (__Completed__)
    - Employee Create API (__Completed__)
        - Fields: Employee Name, Email, Contact Number, Emergency Contact Number, Address, Postion, DOB, Martial status, Blood Group,Job Title, work Location, Date of Joining(use pipe for a particular format), Reporting to, Linked In link, Profile pic.
    - Employee Edit API (__Completed__)
        - Fields: Employee Name, Email, Contact Number, Emergency Contact Number, Address, Postion, DOB, Martial status, Blood Group,Job Title, work Location, Date of Joining(use pipe for a particular format), Reporting to, Linked In link, Profile pic.
    - Employee Delete API (__Completed__)
- Leave Management
    - List API to list all employees leave request.
        - Fiters: to list all approved leaves, to list pending approval leaves. (__Pending__)
        - Fields: Employee Name, Apply date, Nature of leave, first day, last day, number of days. (__Completed__)
        - API to approve and reject leave request from employees. (__Pending__)
(__For Employees__)
- Leave application page
    - API to list leaves of current employee
        - Show: Apply date, Nature of leave, first day, last day, number of days.
		- Functionalities: search, sort.
    - Leave application request API:
        - Fields: Apply date(auto populate), Nature of leave, first day, last day, number of days.
- Logout API
