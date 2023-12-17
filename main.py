import time

"""
  ______              _             _ _           _
 |  ____|            | |   /\      | (_)         | |
 | |__ ___   ___ __ _| |  /  \   __| |_ _   _ ___| |_
 |  __/ _ \ / __/ _` | | / /\ \ / _` | | | | / __| __|
 | | | (_) | (_| (_| | |/ ____ | (_| | | |_| \__ | |_
 |_|  \___/ \___\__,_|_/_/    \_\__,_| |\__,_|___/\__|
                                    _/ |
                                   |__/


----------------Created by $auce & Our Good Ole Friend, ChatGPT--------------------------------


COMING SOON... Maybe? - GUI! Having issues with Tkinter at the moment but I'm working on finding a fix.
                                                                                                    """

checkFlag = True


def ACS():  # "Arbitrary Check Sequence" Restarts program x seconds after entering query.
    print("Restarting")
    time.sleep(1.5)
    main()


# Calculation for focal length after crop factor
def calculate_effective_focal_length(original_focal_length, crop_factor):
    effective_focal_length = original_focal_length * crop_factor
    checkFlag = False
    return effective_focal_length


# Captures input and returns results in the console
def main():
    try:
        original_focal_length = float(input("Enter the ORIGINAL FOCAL LENGTH of the lens (example: 50mm = 50): "))
        crop_factor = float(input("Enter the crop factor(example: 1.5x = 1.5): "))

        if original_focal_length <= 0 or crop_factor <= 0:
            print("Please enter valid positive values for focal length and crop factor.")
        else:
            effective_focal_length = calculate_effective_focal_length(original_focal_length, crop_factor)
            print(f"The adjusted focal length after crop factor is: {effective_focal_length} mm")
            ACS()  # Calls the check sequence to restart the program


    except ValueError:
        print("Invalid input. Please enter ONLY numeric values.")
        ACS()  # Calls the check sequence to restart the programs


if __name__ == "__main__":
    main()
