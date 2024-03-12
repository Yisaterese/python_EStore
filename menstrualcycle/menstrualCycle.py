from datetime import datetime
import sys

class MenstrualCycle:

    current_time = datetime.now()

    def welcome_message(self):
        print("""Hi welcome to Female lulu menstrual tracking application, thank you for choosing us.
            """)

    def get_user_name(self):
        user_name = str(input("What is your?. "))
        print("Hello  " + user_name)

    def get_user_age(self):
        user_age = int(input("How old?. "))
        average_menstrual_age = 12

        if user_age < average_menstrual_age:
            print("""
             Hello! This app is designed for users who have started menstruating and may contain sensitive content related to menstrual health.
             If you're under 12 years of age and have questions, consider talking to a trusted adult or healthcare provider for guidance. Take care!
                    """)

            response = str(input("Would you like to continue with the app? enter yes/no"))
            if response.casefold() == "yes":
                print("""
                    Hello welcome to Female Lulu Menstrual cycle tracking app!.
                    Track and monitor your menstrual cycle with ease.
                    Get insights, predictions, and helpful reminders.
                    Let's get started!""")

            elif response.casefold() == "no":
                print("Goodbye, thank you for choosing us.")
                sys.exit()


def display_menstrual_information():
    print("""
             What is menstruation?
             Menstruation is one part of a woman's cycle when the lining of the uterus (endometrium) is shed.
             This occurs throughout a woman's reproductive life. With each monthly cycle, the endometrium prepares itself to nourish a fetus.
             Increased levels of estrogen and progesterone help thicken its walls.
             If fertilization does not occur, the endometrium, along with blood and mucus from the vagina and cervix make up the menstrual flow that leaves the body through the vagina during the period.

             When does menstruation start?
             On average, a young woman in the world has her first menstrual period at about age 12.
             This is generally 2 to 3 years after her breasts start to grow. This is also soon after she notices pubic and underarm hair.

             Stress, strenuous exercise, and diet can affect when a girl first has her period.
             The American College of Obstetricians and Gynecologists recommends that a young woman consult her healthcare provider if she has not started to menstruate by the age of 15, or if she has not begun to develop breast buds, pubic hair, or underarm hair by the age of 13.

             What is ovulation?
             Ovulation is a phase of the female menstrual cycle that involves the release of an egg (ovum) from one of the ovaries.
             It generally occurs about two weeks before the start of the menstrual period.
                """)
    print("""

        """)


def calculate_menstrual_cycle():

    last_day_of_flow = int(input("When was the last day of your menstrual flow?"))
    last_flow_month = int(input("What moth did you experience your last flow?."))
    year_of_last_flow = int(input("What year was that the last flow?."))
    menstrual_cycle_length = int(input("What is your menstrual cycle length?."))

    days_of_month = datetime.monthrange(year_of_last_flow,last_flow_month)


    valid_answer = True
    while valid_answer:
        if last_day_of_flow < days and last_day_of_flow > days:
            for days in range(1,days_of_month + 1):
                print("Enter a valid date")

    next_flow = days_of_month[0] + menstrual_cycle_length
    window_period = last_day_of_flow + 13
    print(f"Your next menstrual flow is: {next_flow}")
    print(f"Your window is: {window_period }")

    response = int(input("do you wish to see your subsequent mestrual predictions?"))
    if response.casefold() == "yes":

        average_subsequent_period = 0
        sum = 0

        sumof_average_daysof_period = int(input("Enter your avergae days of flow for prediction."))

        for index in range(1, sumof_average_daysof_period):
            sumof_average_daysof_period = int(input())
            sum += sumof_average_daysof_period
            average_subsequent_period = sum / index

        print(f"Your average subsequent menstrual prediction is:{average_subsequent_period}",)






