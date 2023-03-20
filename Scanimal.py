user_input = input("Do you want to use the scanner? (yes/no) ")
#The user will type yes or no. If "yes," the camera will open for the scanning process.
#openCV has been installed in Pycharm allowing it to be accessed for the camera module.

#If the user inouts "no," they will be prompted to manually enter information.
if user_input.lower() == "yes":
    import camera_module

    video = camera_module.cv2.VideoCapture(0)

    while True:
        ret, frame = video.read()
        camera_module.cv2.imshow("Scan", frame)
        if camera_module.cv2.waitKey(1) & 0xFF == ord('a'):
            break
    video.release()
    camera_module.cv2.destroyAllWindows()

#Below is the where the user will be directed to if they enter "no"
elif user_input.lower() == "no":
    weight = float(input("Enter your dog's weight in pounds: "))
    breed = input("Enter your dog's breed: ")

    if breed.lower() == "chihuahua":
        food = weight * 0.02
        exercise = "30 minutes of moderate exercise per day"
    elif breed.lower() == "labrador retriever":
        food = weight * 0.03
        exercise = "1 hour of intense exercise per day"
    elif breed.lower() == "german shepherd":
        food = weight * 0.04
        exercise = "1.5 hours of intense exercise per day"
    elif breed.lower() == "poodle":
        food = weight * 0.025
        exercise = "45 minutes of moderate exercise per day"
    elif breed.lower() == "boxer":
        food = weight * 0.035
        exercise = "1 hour of intense exercise per day"
    elif breed.lower() == "beagle":
        food = weight * 0.025
        exercise = "45 minutes of moderate exercise per day"
    elif breed.lower() == "siberian husky":
        food = weight * 0.035
        exercise = "1.5 hours of intense exercise per day"
    elif breed.lower() == "golden retriever":
        food = weight * 0.03
        exercise = "1 hour of moderate exercise per day"
        Grooming = "Should be brushed several times a week to avoid mats"
    elif breed.lower() == "dachshund":
        food = weight * 0.025
        exercise = "30 minutes of moderate exercise per day"
    elif breed.lower() == "rottweiler":
        food = weight * 0.045
        exercise = "1 hour of intense exercise per day"
    elif breed.lower() == "pug":
        food = weight * 0.02
        exercise = "30 minutes of moderate exercise per day"
    elif breed.lower() == "great dane":
        food = weight * 0.06
        exercise = "2 hours of moderate exercise per day"
    elif breed.lower() == "bulldog":
        food = weight * 0.025
        exercise = "45 minutes of moderate exercise per day"
    elif breed.lower() == "border collie":
        food = weight * 0.03
        exercise = "1.5 hours of intense exercise per day"
    elif breed.lower() == "dalmatian":
        food = weight * 0.03
        exercise = "1 hour of intense exercise per day"
    elif breed.lower() == "doberman pinscher":
        food = weight * 0.04
        exercise = "1 hour of intense exercise per day"
    elif breed.lower() == "great pyrenees":
        food = weight * 0.045
        exercise = "1 hour of moderate exercise per day"
    elif breed.lower() == "jack russell terrier":
        food = weight * 0.02
        exercise = "45 minutes of intense exercise per day"
    elif breed.lower() == "newfoundland":
        food = weight * 0.05
        exercise = "1 hour of moderate exercise per day"
    elif breed.lower() == "shih tzu":
        food = weight * 0.025
        exercise = "30 minutes of moderate exercise per day"
    else:
        print("We do not have information on the recommended food and exercise for that breed.")
        food = None
        exercise = None
#The information below will be displayed for each breed.
    if food:
        print("For a", breed, "that weighs", weight, "pounds, the recommended daily food intake is", food,
              "cups a day, and the recommended amount of exercise is", exercise)
