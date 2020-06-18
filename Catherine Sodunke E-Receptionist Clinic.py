
import tkinter as tk
#E- Receptionist Clinic Project to check in patients and book appointments and analyse patients' observations e.t.c
#print("Welcome to e receptionist.")

#patient_hospital_number = input("What is your hospital number?  ")
#patient_DOB = int(input("What is your date of birth?  "))
#patient_name = input("What is your full name?  ")
#patient_address = str(input("Is your address correct please? y/n "))

#if patient_address == "y":
    #print("Continue")

#elif patient_address == "yes":
    #print("Continue")

#elif patient_address == "Yes":
    #print("Continue")

#else:
    #print("Put the right address in the address section")


#To check in with different Health Professionals:

#input ("Do you have appointment with hcp? y/n " )
#hcp = ["Midwife", "Nurse", "Dietitian", "Consultant", "Sonographer","Phlebotomist", "ACORN Team", "Group Practice Team", "Diabetic Midwife","Diabetic Nurse","Dietician"]
#is_checked= False
#while not is_checked:
   #for role in hcp:
    #if role == 'Sonographer':
        #check_in = input("Are you seeing the Sonographer? (y/n) ")
        #if check_in == "y":

            #is_checked = True
            #print('Please go to the screening room (room 7)')
            #break
        #else:
            #print("Please choose the Professional you are seeing today.")

    #elif role == 'Phlebotomist':
        #check_in = input("Are you seeing the Phlebotomist? (y/n) ")
        #if check_in == "y":

            #is_checked = True
            #print('Please take a ticket and sit in the main reception')
            #break
        #else:
            #print("Please choose the Professional you are seeing today.")

    #elif role == 'Dietitian':
        #check_in = input("Are you seeing the Dietitian? (y/n) ")
        #if check_in == "y":

            #is_checked = True
            #print('Please sit in the main reception waiting area.')
            #break
        #else:
            #print("Please choose the Professional you are seeing today.")

    #else:
        #check_in = input("Are you seeing the " + role + "? (y/n) ")
        #if check_in == "y":
            #is_checked = True
            #print("Please take a ticket and go to room 1a for observation.")
            #break

        #else:
            #print("Please choose the Professional you are seeing today.")
            #break

#E observation room to for observation

#print("Welcome to E observation room.")
#print("Please input your hospital number and take the printed sticker with your details.")
#print("Please read the e observation instructions on the wall beforehand.")
#print("Please take one urine bottle from the box for urine specimen and put the printed sticker on it.")

# This randomly decides whether the results were normal or not (Checking Vital Signs Results)

import random

#result_in = random.choice(["Abnormal", "Normal"])

#if result_in == "Abnormal":

            #print("HCP alerted about your observation results, please go to room 1b and sit, HCP would call you in soon.")

#else:
            #print("Your observation is normal, pls take your printed results and sit in the waiting area to be called in.")



#To book an appointment with hcp

#input("Do you want to book an appointment with hcp? y/n " )
#hcp = ["Midwife", "Nurse", "Dietitian", "Consultant", "Sonographer","Phlebotomist", "ACORN Team", "Group Practice Team", "Diabetic Midwife","Diabetic Nurse","Dietician"]
#is_booked= False
#while not is_booked:
   #for role in hcp:
       #book_in = input("Are you booking an appointment with the " + role + "? (y/n) ")
       #if book_in == "y":
           #is_booked = True
           #print("Please book the required appointment and take your printed appointment letter. See you again.")
           #break

       #else:
           #print("Thank you for using our services.")

#To cancel appointment with hcp


#hcp = ["Midwife", "Nurse", "Dietitian"," Consultant", "Sonographer","Phlebotomist", "ACORN Team", "Group Practice Team", "Diabetic Midwife","Diabetic Nurse","Dietician"]
#is_cancel = input("Do you want to cancel your appointment? ")
#if is_cancel == "y":
    #cancel_hcp = input("Please enter the HCP you would like to cancel an appointment with: ")
    #print("Your appointment has been cancelled with the " + cancel_hcp + ", " + "thank you for using our services, see you again" + ".")

#To reschedule an appoint with hcp

#hcp = ["Midwife", "Nurse", "Dietitian"," Consultant", "Sonographer","Phlebotomist", "ACORN Team", "Group Practice Team", "Diabetic Midwife","Diabetic Nurse","Dietician"]
#is_reschedule = input("Do you want to reschedule your appointment? ")
#if is_reschedule == "y":
    #reschedule_hcp = input("Please enter the HCP you would like to reschedule your appointment with: ")
    #print("Your appointment has been rescheduled with the " + reschedule_hcp + ", " + "thank you for using our services, see you again" + ".")


def check_in():
    window2.destroy()
    global window3
    window3 = tk.Tk()
    tk.Label(window3,text="Patient details").grid(row=0)
    tk.Label(window3, text="Patient hospital number").grid(row=1)
    hospital_number=tk.Entry(window3)
    hospital_number.grid(row=1,column=1)
    tk.Label(window3, text="Date of birth").grid(row=2)
    date_of_birth = tk.Entry(window3)
    date_of_birth.grid(row=2, column=1)
    tk.Label(window3, text="Full name").grid(row=3)
    full_name = tk.Entry(window3)
    full_name.grid(row=3, column=1)
    tk.Label(window3, text="Type in your address?").grid(row=4)
    full_address = tk.Entry(window3)
    full_address.grid(row=4, column=1)
    Is_correct=tk.IntVar()
    check=tk.Checkbutton(window3,text="Is your address correct?", variable=Is_correct)
    check.grid(row=5)



    def check_in_confirmation(HCP):
        for label in window3.grid_slaves():
            if int(label.grid_info()["row"]) ==19:
                label.grid_forget()
        tk.Label(window3, text="  Checked in with the " + HCP + " ,thank you. ").grid(row=19)
        window3.mainloop()

    def check_in_with_dietician():
        for label in window3.grid_slaves():
            if int(label.grid_info()["row"]) == 19:
                label.grid_forget()
        tk.Label(window3, text="  Please sit in the waiting area,thank you. ").grid(row=19)
        window3.mainloop()

    def check_in_with_sonographer():
        for label in window3.grid_slaves():
            if int(label.grid_info()["row"]) ==19:
                label.grid_forget()
            tk.Label(window3, text="  Please go to the screening room 7.  ").grid(row=19)
            window3.mainloop()

    def check_in_with_Phlebotomist():
        for label in window3.grid_slaves():
            if int(label.grid_info()["row"]) == 19:
                label.grid_forget()
            tk.Label(window3, text="  Please take a ticket and sit in the main reception  ").grid(row=19)
            window3.mainloop()



    tk.Label(window3, text="  Check in with the Health Professional  ").grid(row=6)
    tk.Label(window3, text=" Choose the Health Professional you have an appointment with ").grid(row=7)
    button2 = tk.Button(window3, text="   Check in confirmed with Nurse  ",
    command=lambda: check_in_confirmation("Nurse"))
    button2.grid(row=8, column=0)
    button3 = tk.Button(window3, text="  Check in confirmed with Doctor ",
    command=lambda: check_in_confirmation("Doctor"))
    button3.grid(row=9, column=0)
    button4 = tk.Button(window3, text="  Check in confirmed with Phlebotomist   ",
    command= check_in_with_Phlebotomist)
    button4.grid(row=10, column=0)
    button5 = tk.Button(window3, text=" Check in confirmed with Midwife    ",
    command=lambda: check_in_confirmation("Midwife"))
    button5.grid(row=11, column=0)
    button6 = tk.Button(window3, text="    Check in with Dietician     ",
    command= check_in_with_dietician)
    button6.grid(row=12, column=0)
    button7 = tk.Button(window3, text="    Check in with Sonographer    ",
    command=check_in_with_sonographer)
    button7.grid(row=13, column=0)
    button8 = tk.Button(window3, text="    Check in with Consultant    ",
    command=lambda: check_in_confirmation("Consultant"))
    button8.grid(row=14, column=0)
    button9 = tk.Button(window3, text="  Check in with ACORN Team   ",
    command=lambda: check_in_confirmation("ACORN Team"))
    button9.grid(row=15, column=0)
    button10 = tk.Button(window3, text="  Check in with Group Practice ",
    command=lambda: check_in_confirmation("Group Practice"))
    button10.grid(row=16, column=0)
    button11 = tk.Button(window3, text="  Check in with Diabetic Midwife  ",
    command=lambda: check_in_confirmation("Diabetic Midwife"))
    button11.grid(row=17, column=0)
    button12 = tk.Button(window3, text="   Check in with Diabetic Nurse   ",
    command=lambda: check_in_confirmation("Diabetic Nurse"))
    button12.grid(row=18, column=0)


def appointment_confirmed(HCP):
    for label in window4.grid_slaves():
        if int(label.grid_info()["row"]) == 13:
            label.grid_forget()
    tk.Label(window4, text="Appointment confirmed with the " + HCP + " ,thank you see you again.").grid(row=13)
    window4.mainloop()

def book_appointment():

    window2.destroy()
    global window4
    window4 = tk.Tk()
    tk.Label(window4, text="Booking appointment with Health Professional").grid(row=0)
    tk.Label(window4, text="Choose the Health Professional you want to book appointment with").grid(row=1)
    button2 = tk.Button(window4,text=" Book appointment with Nurse",
    command =lambda: appointment_confirmed("Nurse"))
    button2.grid(row=2, column=0)
    button3 = tk.Button(window4, text=" Book appointment with Doctor",
    command=lambda: appointment_confirmed("Doctor"))
    button3.grid(row=3, column=0)
    button4 = tk.Button(window4, text=" Book appointment with Phlebotomist",
    command=lambda: appointment_confirmed("Phlebotomist"))
    button4.grid(row=4, column=0)
    button5 = tk.Button(window4, text=" Book appointment with Midwife",
    command=lambda: appointment_confirmed("Midwife"))
    button5.grid(row=5, column=0)
    button6 = tk.Button(window4, text=" Book appointment with Dietician",
    command=lambda: appointment_confirmed("Dietician"))
    button6.grid(row=6, column=0)
    button7 = tk.Button(window4, text=" Book appointment with Sonographer",
    command=lambda: appointment_confirmed("Sonographer"))
    button7.grid(row=7, column=0)
    button8 = tk.Button(window4, text=" Book appointment with Consultant",
    command=lambda: appointment_confirmed("Consultant"))
    button8.grid(row=8, column=0)
    button9 = tk.Button(window4, text=" Book appointment with ACORN Team",
    command=lambda: appointment_confirmed("ACORN Team"))
    button9.grid(row=9, column=0)
    button10 = tk.Button(window4, text=" Book appointment with Group Practice",
    command=lambda: appointment_confirmed("Group Practice"))
    button10.grid(row=10, column=0)
    button11 = tk.Button(window4, text=" Book appointment with Diabetic Midwife",
    command=lambda: appointment_confirmed("Diabetic Midwife"))
    button11.grid(row=11, column=0)
    button12 = tk.Button(window4, text=" Book appointment with Diabetic Nurse",
    command=lambda: appointment_confirmed("Diabetic Nurse"))
    button12.grid(row=12, column=0)




def cancel_appt():
    def cancenllation_confirmed(HCP):
        for label in window5.grid_slaves():
            if int(label.grid_info()["row"]) == 13:
                label.grid_forget()
        tk.Label(window5, text=" Appointment cancellation confirmed with the " + HCP + " ,thank you see you again.").grid(row=13)
        window5.mainloop()

    #window2.destroy()
    global window5
    window5 = tk.Tk()
    tk.Label(window5, text=" Appointment cancellation with Health Professional").grid(row=0)
    tk.Label(window5, text="Choose the Health Professional you want to cancel appointment with").grid(row=1)
    button2 = tk.Button(window5,text="  Cancel appointment with Nurse  ",
    command =lambda: cancenllation_confirmed("Nurse"))
    button2.grid(row=2, column=0)
    button3 = tk.Button(window5, text="  Cancel appointment with Doctor ",
    command=lambda: cancenllation_confirmed("Doctor"))
    button3.grid(row=3, column=0)
    button4 = tk.Button(window5, text=" Cancel appointment with Phlebotomist",
    command=lambda: cancenllation_confirmed("Phlebotomist"))
    button4.grid(row=4, column=0)
    button5 = tk.Button(window5, text="  Cancel appointment with Midwife  ",
    command=lambda: cancenllation_confirmed("Midwife"))
    button5.grid(row=5, column=0)
    button6 = tk.Button(window5, text=" Cancel appointment with Dietician",
    command=lambda: cancenllation_confirmed("Dietician"))
    button6.grid(row=6, column=0)
    button7 = tk.Button(window5, text=" Cancel appointment with Sonographer",
    command=lambda: cancenllation_confirmed("Sonographer"))
    button7.grid(row=7, column=0)
    button8 = tk.Button(window5, text=" Cancel appointment with Consultant",
    command=lambda: cancenllation_confirmed("Consultant"))
    button8.grid(row=8, column=0)
    button9 = tk.Button(window5, text=" Cancel appointment with ACORN Team",
    command=lambda: cancenllation_confirmed("ACORN Team"))
    button9.grid(row=9, column=0)
    button10 = tk.Button(window5, text=" Cancel appointment with Group Practice",
    command=lambda: cancenllation_confirmed("Group Practice"))
    button10.grid(row=10, column=0)
    button11 = tk.Button(window5, text=" Cancel appointment with Diabetic Midwife",
    command=lambda: cancenllation_confirmed("Diabetic Midwife"))
    button11.grid(row=11, column=0)
    button12 = tk.Button(window5, text=" Cancel appointment with Diabetic Nurse",
    command=lambda: cancenllation_confirmed("Diabetic Nurse"))
    button12.grid(row=12, column=0)






def reschedule_appt():
        def rescheduled_appointment_confirmed(HCP):
            for label in window6.grid_slaves():
                if int(label.grid_info()["row"]) == 13:
                    label.grid_forget()

            tk.Label(window6, text=" Rescheduled appointment confirmed with the " + HCP + " ,thank you see you again.  ").grid (row=13)
            window6.mainloop()

        # window2.destroy()
        global window6
        window6 = tk.Tk()
        tk.Label(window6, text="  Appointment rescheduled with Health Professional ").grid(row=0)
        tk.Label(window6, text="Choose the Health Professional you want to reschedule appointment with").grid(row=1)
        button2 = tk.Button(window6, text="  Reschedule appointment with Nurse ",
        command=lambda: rescheduled_appointment_confirmed("Nurse"))
        button2.grid(row=2, column=0)
        button3 = tk.Button(window6, text="  Reschedule appointment with Doctor ",
        command=lambda: rescheduled_appointment_confirmed("Doctor"))
        button3.grid(row=3, column=0)
        button4 = tk.Button(window6, text=" Reschedule appointment with Phlebotomist",
        command=lambda: rescheduled_appointment_confirmed("Phlebotomist"))
        button4.grid(row=4, column=0)
        button5 = tk.Button(window6, text=" Reschedule appointment with Midwife",
        command=lambda:rescheduled_appointment_confirmed("Midwife"))
        button5.grid(row=5, column=0)
        button6 = tk.Button(window6, text="  Reschedule appointment with Dietician ",
        command=lambda: rescheduled_appointment_confirmed("Dietician"))
        button6.grid(row=6, column=0)
        button7 = tk.Button(window6, text=" Reschedule appointment with Sonographer",
        command=lambda: rescheduled_appointment_confirmed("Sonographer"))
        button7.grid(row=7, column=0)
        button8 = tk.Button(window6, text=" Reschedule appointment with Consultant",
        command=lambda: rescheduled_appointment_confirmed("Consultant"))
        button8.grid(row=8, column=0)
        button9 = tk.Button(window6, text=" Reschedule appointment with ACORN Team",
        command=lambda: rescheduled_appointment_confirmed("ACORN Team"))
        button9.grid(row=9, column=0)
        button10 = tk.Button(window6, text=" Reschedule appointment with Group Practice",
        command=lambda: rescheduled_appointment_confirmed("Group Practice"))
        button10.grid(row=10, column=0)
        button11 = tk.Button(window6, text=" Reschedule appointment with Diabetic Midwife",
        command=lambda: rescheduled_appointment_confirmed("Diabetic Midwife"))
        button11.grid(row=11, column=0)
        button12 = tk.Button(window6, text=" Reschedule appointment with Diabetic Nurse",
        command=lambda: rescheduled_appointment_confirmed("Diabetic Nurse"))
        button12.grid(row=12, column=0)


def check_vital_observation():
    def get_results():
        result_in = random.choice(["Abnormal", "Normal"])

        if result_in == "Abnormal":

            tk.Label(window7, text=" HCP alerted about your observation results, please go to room 1b and sit, HCP would call you in soon.").grid(row=6)
        else:
            tk.Label(window7,text="   Your observation is normal, pls take your printed results and sit in the waiting area to be called in.    ").grid(row=6)
        window7.mainloop()
    global window7
    window7 = tk.Tk()
    tk.Label(window7, text= "Welcome to E observation room.").grid(row=1)



    tk.Label(window7, text="Please input your hospital number and take the printed sticker with your details.").grid(row=2)



    tk.Label(window7, text="Please read the e observation instructions on the wall beforehand.").grid(row=3)



    tk.Label(window7, text="Please take one urine bottle from the box for urine specimen and put the printed sticker on it.").grid(row=4)

    button1 = tk.Button(window7, text="Check vital signs results" ,
    command=get_results)
    button1.grid(row=5)
    window7.mainloop()



def Homepage():
    window.destroy()
    global window2
    window2 = tk.Tk()

    button1 = tk.Button(window2,
       text=" Check in with Health Professional",
       width=40,
       height=5,
       background="Blue",
       foreground="White", command=check_in
                        )
    button1.grid(row=1, column=0)


    button2 = tk.Button(window2,
        text=" Book appt with Health Professional",
        width=40,
        height=5,
        background="Blue",
        foreground="White", command=book_appointment
                       )
    button2.grid(row=2, column=0)




    button3 = tk.Button(window2,
        text=" Cancel appt with Health Professional",
        width=40,
        height=5,
        background="Blue",
        foreground="White", command=cancel_appt
                       )

    button3.grid(row=3, column=0)


    button4 = tk.Button(window2,
        text=" Reschedule appt with Health Professional",
        width=40,
        height=5,
        background="Blue",
        foreground="White", command=reschedule_appt)
    button4.grid(row=4, column=0)


    button5 = tk.Button(window2,
        text=" Vital observation with Health Professional",
        width=40,
        height=5,
        background="Blue",
        foreground="White", command=check_vital_observation
                       )
    button5.grid(row=5, column=0)



    window2.mainloop()
window = tk.Tk()
greeting = tk.Label(window,text="Welcome to e Receptionist @ Cathy Health Services")
greeting.grid(row=0)
label = tk.Label(window,
    text="Motto: Excellent Services",
    fg="white",
    bg="blue",
    width=25,
    height=15
                 )
label.grid(row=1)

button = tk.Button(window,
    text=" Welcome, start here",
    width=30,
    height=5,
    background="Blue",
    foreground="White", command = Homepage
)
button.grid(row=2)
window.mainloop()























