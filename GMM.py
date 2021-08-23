class Gym:
    superuser = {"admin": "admin"}
    members = {}
    regimens = {}


class WorkoutRegimen:
    def __init__(self, *week_workouts, bmi=None):
        if bmi:
            if bmi < 18.5:
                workouts = ["Chest", "Biceps", "Rest", "Back", "Triceps", "Rest", "Rest"]
            elif bmi < 25:
                workouts = ["Chest", "Biceps", "Cardio/Abs", "Back", "Triceps", "Legs", "Rest"]
            elif bmi < 30:
                workouts = ["Chest", "Biceps", "Cardio/Abs", "Back", "Triceps", "Legs", "Cardio"]
            else:
                workouts = ["Chest", "Biceps", "Cardio", "Back", "Triceps", "Cardio", "Cardio"]
        else:
            workouts = list(week_workouts)

        self.mon, self.tue, self.wed, self.thu, self.fri, self.sat, self.sun = workouts

    def view_regimen(self):
        print("------ Workout Regimen ------")
        print(f"Mon: {self.mon}  Tue: {self.tue}  Wed: {self.wed}", end="  ")
        print(f"Thu: {self.thu}  Fri: {self.fri}  Sat: {self.sat}  Sun: {self.sun}")


class Member:
    def __init__(self, full_name, age, gender, mobile_no, email, bmi, membership_duration):
        self.full_name = full_name
        self.age = age
        self.gender = gender
        self.mobile_no = mobile_no
        self.email = email
        self.bmi = bmi
        self.membership_duration = membership_duration
        self.workout_regimen = WorkoutRegimen(bmi=self.bmi)

    def view_profile(self):
        print("------ Member Profile -----")
        print("Full Name:", self.full_name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Mobile Number:", self.mobile_no)
        print("Email:", self.email)
        print("BMI:", self.bmi)
        print("Membership Duration:", self.membership_duration, "months")

    def view_workout_regimen(self):
        self.workout_regimen.view_regimen()


class SuperUser:
    def create_member(self, *member_details):
        new_member = Member(*member_details)
        if new_member.mobile_no in Gym.members:
            print("Creating member failed.")
            print("Member with same contact number already exists.")
            return
        Gym.members[new_member.mobile_no] = new_member
        print("Member created successfully.")

    def view_member(self, mobile_no):
        if mobile_no not in Gym.members:
            print("No member with the given mobile number is available")
            return
        member = Gym.members[mobile_no]
        member.view_profile()
        member.view_workout_regimen()

    def update_member(self, mobile_no, *member_details):
        if mobile_no not in Gym.members:
            print("Update member failed.")
            print("No member with the given mobile number is available")
            return
        updated_member = Member(*member_details)
        if mobile_no == updated_member.mobile_no:
            Gym.members[mobile_no] = updated_member
        else:
            Gym.members[updated_member.mobile_no] = updated_member
            del Gym.members[mobile_no]
        print("Member updated successfully.")

    def delete_member(self, mobile_no):
        if mobile_no not in Gym.members:
            print("No member with the given mobile number is available")
            return
        del Gym.members[mobile_no]
        print("Deleted member successfully.")

    def create_regimen(self, *regimen):
        regimen_id = max(Gym.regimens.keys()) + 1 if len(Gym.regimens) else 0
        Gym.regimens[regimen_id] = WorkoutRegimen(*regimen)
        print("Regimen created successfully with regimen id:", regimen_id)

    def view_regimen(self, regimen_id):
        if regimen_id not in Gym.regimens:
            print("Regimen with given id is not available")
            return
        Gym.regimens[regimen_id].view_regimen()

    def update_regimen(self, regimen_id, *regimen):
        if regimen_id not in Gym.regimens:
            print("Update regimen failed.")
            print("Regimen with given id is not available")
            return
        Gym.regimens[regimen_id] = WorkoutRegimen(*regimen)
        print("Regimen updated successfully.")

    def delete_regimen(self, regimen_id):
        if regimen_id not in Gym.regimens:
            print("Delete regimen failed.")
            print("Regimen with given id is not available")
            return
        del Gym.regimens[regimen_id]
        print("Regimen deleted successfully.")


def main():
    print("+-----------------------------+")
    print("|  GYM MEMBERSHIP MANAGEMENT  |")
    print("+-----------------------------+")

    while True:
        print("\nLogin as")
        print("1. SuperUser  2. Member  3. Exit")
        user_choice = int(input("Enter your choice: "))
        print()
        if user_choice == 1:
            username = input("Username: ")
            password = input("Password: ")
            if username in Gym.superuser and password == Gym.superuser[username]:
                print("Logged in successfully!")
                superuser = SuperUser()
                handle_superuser_operations(superuser)
            else:
                print("Login Failed! Invalid credentials.")
        elif user_choice == 2:
            mobile_no = input("Mobile Number: ")
            if mobile_no in Gym.members:
                member = Gym.members[mobile_no]
                print("Logged in successfully!")
                print("Welcome", member.full_name)
                handle_member_operations(member)
            else:
                print("Login Failed! Invalid credentials.")
        elif user_choice == 3:
            print("Exited. Have a great Day!")
            break
        else:
            print("Invalid choice")


def handle_superuser_operations(superuser: SuperUser):
    while True:
        print("\n1. Create Member  2. View Member  3. Update Member  4. Delete Member")
        print("5. Create Regimen  6. View Regimen  7. Update Regimen  8. Delete Regimen")
        print("9. Logout")
        choice = int(input("Enter your choice: "))
        print()
        if choice == 1:
            print("To create a member, please enter the following details")
            full_name = input("Full Name: ").title()
            age = int(input("Age: "))
            gender = input("Gender: ")
            mobile_no = input("Mobile Number: ")
            email = input("Email: ")
            bmi = float(input("BMI: "))
            membership_duration = int(input("Membership Duration (months): "))
            superuser.create_member(full_name, age, gender, mobile_no, email, bmi, membership_duration)
        elif choice == 2:
            print("To view a member, please enter their")
            mobile_no = input("Mobile Number: ")
            superuser.view_member(mobile_no)
        elif choice == 3:
            print("To update a member, please enter the")
            mobile_no = input("Mobile Number: ")
            if mobile_no not in Gym.members:
                print("Update member failed.")
                print("No member with the given mobile number is available")
            else:
                print("Member exists! Please enter the following details to update")
                member = Gym.members[mobile_no]
                full_name = input("Full Name: ")
                age = input("Age: ")
                gender = input("Gender: ")
                mobile_no = input("Mobile Number: ")
                email = input("Email: ")
                bmi = input("BMI: ")

                print("Current Membership:", member.membership_duration, "months")
                print("1. Extend Membership  2. Revoke Membership  3. No Update")
                mem_choice = int(input("Enter your choice: "))
                if mem_choice == 1:
                    ext_mem_dur = int(input("Extend membership by (months): "))
                    membership_duration = member.membership_duration + ext_mem_dur
                elif mem_choice == 2:
                    membership_duration = 0
                else:
                    membership_duration = member.membership_duration

                # Defaults to previous value if update value is empty
                full_name = full_name.title() if full_name.strip() else member.full_name
                age = int(age) if age.strip() else member.age
                gender = gender if gender.strip() else member.gender
                mobile_no = mobile_no if mobile_no.strip() else member.mobile_no
                email = email if email.strip() else member.email
                bmi = float(bmi) if bmi.strip() else member.bmi

                member_details = (full_name, age, gender, mobile_no, email, bmi, membership_duration)
                superuser.update_member(member.mobile_no, *member_details)
        elif choice == 4:
            print("To delete a member, please enter their")
            mobile_no = input("Mobile Number: ")
            superuser.delete_member(mobile_no)
        elif choice == 5:
            print("To create a regimen, please enter the following details")
            mon = input("Mon: ").title()
            tue = input("Tue: ").title()
            wed = input("Wed: ").title()
            thu = input("Thu: ").title()
            fri = input("Fri: ").title()
            sat = input("Sat: ").title()
            sun = input("Sun: ").title()
            superuser.create_regimen(mon, tue, wed, thu, fri, sat, sun)
        elif choice == 6:
            print("To view a regimen, please enter the")
            regimen_id = int(input("Regimen id: "))
            superuser.view_regimen(regimen_id)
        elif choice == 7:
            print("To update a regimen, please enter the following details")
            regimen_id = int(input("Regimen id: "))
            if regimen_id not in Gym.regimens:
                print("Regimen with given id is not available")
            else:
                regimen = Gym.regimens[regimen_id]
                mon = input("Mon: ").title()
                tue = input("Tue: ").title()
                wed = input("Wed: ").title()
                thu = input("Thu: ").title()
                fri = input("Fri: ").title()
                sat = input("Sat: ").title()
                sun = input("Sun: ").title()

                # Defaults to previous value if update value is empty
                mon = mon if mon.strip() else regimen.mon
                tue = tue if tue.strip() else regimen.tue
                wed = wed if wed.strip() else regimen.wed
                thu = thu if thu.strip() else regimen.thu
                fri = fri if fri.strip() else regimen.fri
                sat = sat if sat.strip() else regimen.sat
                sun = sun if sun.strip() else regimen.sun

                superuser.update_regimen(regimen_id, mon, tue, wed, thu, fri, sat, sun)
        elif choice == 8:
            print("To delete a regimen, please enter the")
            regimen_id = int(input("Regimen id: "))
            superuser.delete_regimen(regimen_id)
        elif choice == 9:
            print("Logged out successfully!")
            break
        else:
            print("Invalid choice")


def handle_member_operations(member: Member):
    while True:
        print("\n1. My Regimen  2. My Profile  3. Logout")
        choice = int(input("Enter your choice: "))
        print()
        if choice == 1:
            member.view_workout_regimen()
        elif choice == 2:
            member.view_profile()
        elif choice == 3:
            print("Logged out successfully!")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
