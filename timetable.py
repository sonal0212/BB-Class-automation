from classes_link import class_links
# TIME-TABLE
Time1 = (9, 40)
Time2 = (10, 30)
Time3 = (11, 20)
Time4 = (12, 10)
Time5 = (13, 00)
Time6 = (13, 50)
Time7 = (14, 40)
Time8 = (15, 30)
time_table = {
    "Monday": [

        (class_links.get("computer_networks"), *Time1),
        (class_links.get("project_1"), *Time2),
        (class_links.get("software_eng"), *Time3),
        (class_links.get("microprocessor_and_interfacing_lab"), *Time5),
        (class_links.get("microprocessor_and_interfacing_lab"), *Time6),
        (class_links.get("probability_and_statistics"), *Time7),
        (class_links.get("microprocessor_and_interfacing"), *Time8)

    ],
    "Tuesday": [

        (class_links.get("probability_and_statistics"), *Time1),
        (class_links.get("soft_skill"), *Time2),
        (class_links.get("soft_skill"), *Time3),
        (class_links.get("principles_of_ai"), *Time4),
        (class_links.get("probability_and_statistics"), *Time6)
],
    "Wednesday": [

        (class_links.get("life_skill_and_mentoring"), *Time1),
        (class_links.get("python_lab"), *Time2),
        (class_links.get("python_lab"), *Time3),
        (class_links.get("computer_networks_lab"), *Time5),
        (class_links.get("computer_networks_lab"), *Time6),
        (class_links.get("software_eng"), *Time7),
        (class_links.get("computer_networks"), *Time8),
        ("https://cuchd.blackboard.com/ultra/courses/_54190_1/outline", 18, 16)
    ],
    "Thursday": [

        (class_links.get("principles_of_ai"), *Time1),
        (class_links.get("python_lab"), *Time2),
        (class_links.get("python_lab"), *Time3),
        (class_links.get("microprocessor_and_interfacing"), *Time4),
        (class_links.get("data_structure_and_algo"), *Time6),
        (class_links.get("software_eng"), *Time7),
        (class_links.get("probability_and_statistics"), *Time8),
    ],
    "Friday": [

        (class_links.get("microprocessor_and_interfacing"), *Time1),
        (class_links.get("software_eng_lab"), *Time2),
        (class_links.get("software_eng_lab"), *Time3),
        (class_links.get("computer_networks"), *Time5),
        (class_links.get("principles_of_ai"), *Time6)
    ]
}