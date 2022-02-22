from classes_link import class_links
# TIME-TABLE
class1 = (9, 40)
class2 = (10, 30)
class3 = (11, 20)
class4 = (12, 10)
class5 = (13, 00)
class6 = (13, 50)
class7 = (14, 40)
class8 = (15, 30)
time_table = {
    "Monday": [

        (class_links.get("computer_networks"), *class1),
        (class_links.get("project_1"), *class2),
        (class_links.get("software_eng"), *class3),
        (class_links.get("microprocessor_and_interfacing_lab"), *class5),
        (class_links.get("microprocessor_and_interfacing_lab"), *class6),
        (class_links.get("probability_and_statistics"), *class7),
        (class_links.get("microprocessor_and_interfacing"), *class8)

    ],
    "Tuesday": [

        (class_links.get("probability_and_statistics"), *class1),
        (class_links.get("soft_skill"), *class2),
        (class_links.get("soft_skill"), *class3),
        (class_links.get("principles_of_ai"), *class4),
        (class_links.get("probability_and_statistics"), *class6)
    ],
    "Wednesday": [

        (class_links.get("life_skill_and_mentoring"), *class1),
        (class_links.get("python_lab"), *class2),
        (class_links.get("python_lab"), *class3),
        (class_links.get("computer_networks_lab"), *class5),
        (class_links.get("computer_networks_lab"), *class6),
        (class_links.get("software_eng"), *class7),
        (class_links.get("computer_networks"), *class8)
    ],
    "Thursday": [

        (class_links.get("principles_of_ai"), *class1),
        (class_links.get("python_lab"), *class2),
        (class_links.get("python_lab"), *class3),
        (class_links.get("microprocessor_and_interfacing"), *class4),
        (class_links.get("data_structure_and_algo"), *class6),
        (class_links.get("software_eng"), *class7),
        (class_links.get("probability_and_statistics"), *class8),
    ],
    "Friday": [

        (class_links.get("microprocessor_and_interfacing"), *class1),
        (class_links.get("software_eng_lab"), *class2),
        (class_links.get("software_eng_lab"), *class3),
        (class_links.get("computer_networks"), *class5),
        (class_links.get("principles_of_ai"), *class6)
    ]
}