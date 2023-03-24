import time


def startup_function():
    welcome_function()
    set_constraints()
    generate_plumbing_systems()
    generate_electrical_systems()
    generate_hvac_systems()
    generate_lighting_systems()
    generate_fire_protection_systems()
    generate_security_systems()
    generate_communication_systems()
    generate_special_systems()
    generate_output()


def welcome_function():
    print("Welcome to the neighborhood generator!")
    print("Generation starting now! \n\n")


def set_constraints():
    # set constraints for the project
    print("Setting constraints...")
    time.sleep(0.5)


def generate_plumbing_systems():
    # generate plumbing systems for the project
    print("Generating plumbing systems...")
    time.sleep(0.5)


def generate_electrical_systems():
    # generate electrical systems for the project
    print("Generating electrical systems...")
    time.sleep(0.5)


def generate_hvac_systems():
    # generate HVAC systems for the project
    print("Generating HVAC systems...")
    time.sleep(0.5)


def generate_lighting_systems():
    # generate lighting systems for the project
    print("Generating lighting systems...")
    time.sleep(0.5)


def generate_fire_protection_systems():
    # generate fire protection systems for the project
    print("Generating fire protection systems...")
    time.sleep(0.5)


def generate_security_systems():
    # generate security systems for the project
    print("Generating security systems...")
    time.sleep(0.5)


def generate_communication_systems():
    # generate communication systems for the project
    print("Generating communication systems...")
    time.sleep(0.5)


def generate_special_systems():
    # generate special systems for the project
    print("Generating special systems...")
    time.sleep(0.5)


def generate_output():
    # generate output for the project
    print("Generating output...")
    print("\n")
    print("Done! Here is your city: \n")
    with open("ascii_city_alfr_2021/village1.txt", "r") as f:
        print(f.read())

    time.sleep(0.5)


startup_function()
