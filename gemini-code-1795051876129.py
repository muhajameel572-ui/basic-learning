# ==========================================
# 1. PYTHON CURRICULUM (11 COMPLETE TOPICS)
# ==========================================
PYTHON_TOPICS = [
    {
        "title": "1. Introduction to Python",
        "level": "Beginner",
        "explanation": """
        Python is a high-level, interpreted, and general-purpose programming language created by Guido van Rossum in 1991.
        It emphasizes code readability with clean syntax using indentation rather than curly braces `{}`.
        Python is widely used in **Web Development, Data Science, Artificial Intelligence, Automation, and Scripting**.
        """,
        "code": '''# Your first Python program
print("Welcome to Smart Learning Master!")

# Basic arithmetic and comments
year = 2026
print(f"Learning Python in {year} is awesome!")''',
        "mcq": {
            "question": "Who created the Python programming language?",
            "options": ["Dennis Ritchie", "Guido van Rossum", "James Gosling", "Bjarne Stroustrup"],
            "answer": "Guido van Rossum",
            "explanation": "Guido van Rossum created Python and first released it in 1991."
        },
        "exercise": {
            "prompt": "Write a Python statement that prints 'Hello World' to the console.",
            "starter": "# Write your print statement below\n",
            "expected_substring": "print(",
            "solution": 'print("Hello World")'
        }
    },
    {
        "title": "2. Variables and Data Types",
        "level": "Beginner",
        "explanation": """
        Variables are containers for storing data values. Python is dynamically typed, meaning you don't need to declare variable types explicitly.
        **Core Data Types:**
        - `int`: Whole numbers (`10`, `-5`)
        - `float`: Decimal numbers (`3.14`, `99.9`)
        - `str`: Text enclosed in quotes (`"Python"`)
        - `bool`: Logical values (`True` or `False`)
        """,
        "code": '''student_name = "Sara"     # str
age = 20                  # int
gpa = 3.85                # float
is_enrolled = True        # bool

print(type(student_name), type(gpa))''',
        "mcq": {
            "question": "What is the output of `type(3.5)` in Python?",
            "options": ["<class 'int'>", "<class 'float'>", "<class 'str'>", "<class 'double'>"],
            "answer": "<class 'float'>",
            "explanation": "Numbers with decimal points are represented as `float` in Python."
        },
        "exercise": {
            "prompt": "Create a variable named `score` and assign it the integer value `100`, then print it.",
            "starter": "# Define score below\n",
            "expected_substring": "score",
            "solution": "score = 100\nprint(score)"
        }
    },
    {
        "title": "3. Operators",
        "level": "Beginner",
        "explanation": """
        Operators perform operations on variables and values:
        - **Arithmetic:** `+`, `-`, `*`, `/` (true division), `//` (floor division), `%` (modulus/remainder), `**` (exponentiation)
        - **Comparison:** `==`, `!=`, `>`, `<`, `>=`, `<=`
        - **Logical:** `and`, `or`, `not`
        """,
        "code": '''a, b = 15, 4
print("Division:", a / b)        # 3.75
print("Floor Division:", a // b) # 3
print("Remainder:", a % b)       # 3
print("Power:", 2 ** 3)          # 8''',
        "mcq": {
            "question": "Which operator calculates the remainder of a division in Python?",
            "options": ["//", "/", "%", "**"],
            "answer": "%",
            "explanation": "The modulus operator `%` returns the remainder after integer division."
        },
        "exercise": {
            "prompt": "Calculate 5 raised to the power of 3 using the exponentiation operator and print the result.",
            "starter": "# Calculate 5^3\n",
            "expected_substring": "**",
            "solution": "print(5 ** 3)"
        }
    },
    {
        "title": "4. If-Else Conditions",
        "level": "Beginner",
        "explanation": """
        Conditional statements allow your program to make decisions based on boolean conditions using `if`, `elif`, and `else`.
        Indentation (4 spaces) defines the block of code inside each condition.
        """,
        "code": '''marks = 82
if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
else:
    grade = "B"
print(f"Student Grade: {grade}")''',
        "mcq": {
            "question": "Which keyword is used in Python for 'else if'?",
            "options": ["elseif", "else if", "elif", "if else"],
            "answer": "elif",
            "explanation": "Python uses `elif` as a shorthand for 'else if'."
        },
        "exercise": {
            "prompt": "Write an `if` statement checking if `x = 10` is greater than `5`, and print 'Big'.",
            "starter": "x = 10\n",
            "expected_substring": "if",
            "solution": 'x = 10\nif x > 5:\n    print("Big")'
        }
    },
    {
        "title": "5. Loops (For & While)",
        "level": "Intermediate",
        "explanation": """
        Loops execute a block of code repeatedly:
        - **`for` loop:** Iterates over a sequence (list, string, or `range()`).
        - **`while` loop:** Repeats as long as a condition remains `True`.
        - **`break` & `continue`:** Control loop execution flow.
        """,
        "code": '''# For loop with range
for i in range(1, 6):
    print(f"Square of {i} is {i**2}")

# While loop
count = 3
while count > 0:
    print("Countdown:", count)
    count -= 1''',
        "mcq": {
            "question": "How many times will `for i in range(4):` execute?",
            "options": ["3", "4", "5", "Infinite"],
            "answer": "4",
            "explanation": "`range(4)` generates numbers 0, 1, 2, 3 — a total of 4 iterations."
        },
        "exercise": {
            "prompt": "Use a `for` loop with `range(3)` to print 'Python' three times.",
            "starter": "# Write loop here\n",
            "expected_substring": "for",
            "solution": 'for i in range(3):\n    print("Python")'
        }
    },
    {
        "title": "6. Functions",
        "level": "Intermediate",
        "explanation": """
        Functions are reusable blocks of code defined with the `def` keyword. They can accept parameters and send back results using `return`.
        """,
        "code": '''def calculate_area(radius, pi=3.14159):
    """Returns the area of a circle."""
    return pi * (radius ** 2)

print("Area:", round(calculate_area(5), 2))''',
        "mcq": {
            "question": "Which keyword is used to define a function in Python?",
            "options": ["function", "func", "def", "define"],
            "answer": "def",
            "explanation": "Functions in Python are declared using the `def` keyword."
        },
        "exercise": {
            "prompt": "Define a function named `add(a, b)` that returns the sum of `a` and `b`.",
            "starter": "# Define add function\n",
            "expected_substring": "def add",
            "solution": "def add(a, b):\n    return a + b\nprint(add(3, 4))"
        }
    },
    {
        "title": "7. Lists and Tuples",
        "level": "Intermediate",
        "explanation": """
        - **List (`[]`):** Ordered, **mutable** (changeable) collection of items.
        - **Tuple (`()`):** Ordered, **immutable** (unchangeable) collection of items, faster and safer for fixed data.
        """,
        "code": '''# List (Mutable)
languages = ["Python", "JavaScript", "C++"]
languages.append("Rust")
print("List:", languages)

# Tuple (Immutable)
coordinates = (24.8607, 67.0011)
print("Latitude:", coordinates[0])''',
        "mcq": {
            "question": "What is the main difference between a List and a Tuple?",
            "options": [
                "Lists are faster than tuples",
                "Lists are mutable, while Tuples are immutable",
                "Tuples can only hold integers",
                "Lists cannot contain duplicates"
            ],
            "answer": "Lists are mutable, while Tuples are immutable",
            "explanation": "You can modify, add, or remove items in a list, whereas tuples cannot be altered after creation."
        },
        "exercise": {
            "prompt": "Create a list `nums = [1, 2, 3]`, append `4` to it, and print `nums`.",
            "starter": "nums = [1, 2, 3]\n",
            "expected_substring": "append",
            "solution": "nums = [1, 2, 3]\nnums.append(4)\nprint(nums)"
        }
    },
    {
        "title": "8. Dictionaries and Sets",
        "level": "Intermediate",
        "explanation": """
        - **Dictionary (`{key: value}`):** Stores key-value pairs with fast O(1) lookup.
        - **Set (`{item1, item2}`):** Unordered collection of **unique** elements.
        """,
        "code": '''student = {"name": "Ali", "course": "Python", "score": 95}
print(student["name"])

unique_tags = {"ai", "python", "ai", "ml"}
print("Unique Tags:", unique_tags)  # {'ai', 'python', 'ml'}''',
        "mcq": {
            "question": "How do you safely access a key in a dictionary without raising a KeyError if it doesn't exist?",
            "options": ["dict.find()", "dict.get()", "dict.fetch()", "dict.lookup()"],
            "answer": "dict.get()",
            "explanation": "`dict.get('key', default)` returns `None` (or a default value) instead of throwing a KeyError."
        },
        "exercise": {
            "prompt": "Create a dictionary `car = {'brand': 'Toyota', 'year': 2024}` and print `car['brand']`.",
            "starter": "# Create dictionary\n",
            "expected_substring": "brand",
            "solution": "car = {'brand': 'Toyota', 'year': 2024}\nprint(car['brand'])"
        }
    },
    {
        "title": "9. Object-Oriented Programming (OOP)",
        "level": "Advanced",
        "explanation": """
        OOP organizes software design around **Classes** (blueprints) and **Objects** (instances).
        Key concepts include `__init__` constructors, `self`, **Encapsulation**, **Inheritance**, and **Polymorphism**.
        """,
        "code": '''class Student:
    def __init__(self, name, points=0):
        self.name = name
        self.points = points

    def earn_points(self, amount):
        self.points += amount
        return f"{self.name} now has {self.points} pts!"

s1 = Student("Zara", 100)
print(s1.earn_points(50))''',
        "mcq": {
            "question": "What is the purpose of the `__init__` method in a Python class?",
            "options": [
                "To delete an object",
                "To initialize object attributes when an instance is created",
                "To import external modules",
                "To create a static variable"
            ],
            "answer": "To initialize object attributes when an instance is created",
            "explanation": "`__init__` acts as the constructor in Python classes."
        },
        "exercise": {
            "prompt": "Create a class named `Dog` with a method `bark(self)` that prints 'Woof!'.",
            "starter": "# Define class Dog\n",
            "expected_substring": "class Dog",
            "solution": 'class Dog:\n    def bark(self):\n        print("Woof!")\nd = Dog()\nd.bark()'
        }
    },
    {
        "title": "10. File Handling",
        "level": "Advanced",
        "explanation": """
        Python uses the built-in `open()` function alongside the `with` context manager to safely read and write files without leaking resources.
        Modes: `'r'` (read), `'w'` (write/overwrite), `'a'` (append).
        """,
        "code": '''# Writing and reading using 'with' context manager
with open("notes.txt", "w") as file:
    file.write("Python File Handling is clean and safe!")

with open("notes.txt", "r") as file:
    content = file.read()
    print(content)''',
        "mcq": {
            "question": "Why is the `with open(...)` statement preferred when working with files?",
            "options": [
                "It automatically encrypts the file",
                "It automatically closes the file even if an exception occurs",
                "It makes files read-only",
                "It compresses file size"
            ],
            "answer": "It automatically closes the file even if an exception occurs",
            "explanation": "The `with` statement acts as a context manager that guarantees `file.close()` is called."
        },
        "exercise": {
            "prompt": "Write code using `with open('demo.txt', 'w') as f:` to write `'Hello'`.",
            "starter": "# File handling exercise\n",
            "expected_substring": "open(",
            "solution": "with open('demo.txt', 'w') as f:\n    f.write('Hello')"
        }
    },
    {
        "title": "11. Python Projects (Mini CLI Password Generator)",
        "level": "Advanced",
        "explanation": """
        Combining modules (`random`, `string`), functions, and list comprehensions lets you build practical real-world tools.
        Below is a complete secure password generator using Python's standard library.
        """,
        "code": '''import random
import string

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.choice(chars) for _ in range(length))

print("Generated Password:", generate_password(14))''',
        "mcq": {
            "question": "Which standard Python module provides `ascii_letters` and `digits`?",
            "options": ["text", "string", "char", "regex"],
            "answer": "string",
            "explanation": "The `string` module contains useful character constants like `string.ascii_letters`."
        },
        "exercise": {
            "prompt": "Import `random` and print a random integer between 1 and 10 using `random.randint(1, 10)`.",
            "starter": "import random\n",
            "expected_substring": "randint",
            "solution": "import random\nprint(random.randint(1, 10))"
        }
    }
]


# ==========================================
# 2. TYPING TEST PARAGRAPHS
# ==========================================
TYPING_PARAGRAPHS = [
    "Artificial intelligence and machine learning are transforming modern software development. By mastering Python programming and problem solving, students can build intelligent applications that automate complex workflows and analyze massive datasets efficiently.",
    "Consistent daily practice is the secret to mastering both touch typing and software engineering. Focus on accuracy first before pushing for raw speed, keep your posture upright, and let muscle memory guide your fingers across the home row keys.",
    "Karachi is the largest city in Pakistan and serves as its premier industrial and financial hub. Located along the Arabian Sea coastline, it connects global trade routes while fostering a rapidly growing community of technology startups and young developers.",
    "Clean code always looks like it was written by someone who cares. Meaningful variable names, modular functions, proper error handling, and clear documentation turn fragile scripts into reliable production systems that teams can maintain for years.",
    "The universe is vast and filled with billions of galaxies, each containing countless stars and planetary systems. Modern space telescopes allow astronomers to peer billions of years back in time, uncovering the origins of cosmic structures."
]


# ==========================================
# 3. GENERAL KNOWLEDGE (GK) QUESTION BANK
#    (104 Curated Questions across 8 Categories)
# ==========================================
GK_QUESTIONS = [
    # --- WORLD KNOWLEDGE (13) ---
    {"cat": "World Knowledge", "diff": "Easy", "q": "Which is the largest ocean on Earth?", "opts": ["Atlantic Ocean", "Indian Ocean", "Pacific Ocean", "Arctic Ocean"], "ans": "Pacific Ocean", "exp": "The Pacific Ocean covers more than 30% of Earth's surface."},
    {"cat": "World Knowledge", "diff": "Easy", "q": "How many continents are there in the world?", "opts": ["5", "6", "7", "8"], "ans": "7", "exp": "The 7 continents are Asia, Africa, North America, South America, Antarctica, Europe, and Australia."},
    {"cat": "World Knowledge", "diff": "Easy", "q": "Which country is known as the Land of the Rising Sun?", "opts": ["China", "South Korea", "Japan", "Thailand"], "ans": "Japan", "exp": "Japan is called Nippon, meaning 'origin of the sun'."},
    {"cat": "World Knowledge", "diff": "Easy", "q": "What is the currency of the United Kingdom?", "opts": ["Euro", "Dollar", "Pound Sterling", "Franc"], "ans": "Pound Sterling", "exp": "The British Pound Sterling (£) is the official currency of the UK."},
    {"cat": "World Knowledge", "diff": "Medium", "q": "Where is the headquarters of the United Nations located?", "opts": ["Geneva", "New York City", "Vienna", "Paris"], "ans": "New York City", "exp": "The UN headquarters has been in Manhattan, New York City since 1952."},
    {"cat": "World Knowledge", "diff": "Medium", "q": "Which country has the largest population in the world?", "opts": ["China", "India", "United States", "Indonesia"], "ans": "India", "exp": "India surpassed China as the world's most populous nation."},
    {"cat": "World Knowledge", "diff": "Medium", "q": "Which language has the most native speakers globally?", "opts": ["English", "Spanish", "Mandarin Chinese", "Hindi"], "ans": "Mandarin Chinese", "exp": "Mandarin Chinese has over 900 million native speakers."},
    {"cat": "World Knowledge", "diff": "Medium", "q": "What is the capital city of Canada?", "opts": ["Toronto", "Vancouver", "Ottawa", "Montreal"], "ans": "Ottawa", "exp": "Ottawa is the federal capital of Canada."},
    {"cat": "World Knowledge", "diff": "Medium", "q": "Which international organization awards the Nobel Prizes?", "opts": ["UNESCO", "Swedish & Norwegian Committees", "World Bank", "Red Cross"], "ans": "Swedish & Norwegian Committees", "exp": "Nobel Prizes are awarded annually by Swedish and Norwegian institutions."},
    {"cat": "World Knowledge", "diff": "Hard", "q": "Which country has the most time zones in the world?", "opts": ["Russia", "United States", "France", "China"], "ans": "France", "exp": "Counting overseas territories, France spans 12 time zones."},
    {"cat": "World Knowledge", "diff": "Hard", "q": "What is the oldest continuously inhabited city in the world?", "opts": ["Athens", "Damascus", "Rome", "Cairo"], "ans": "Damascus", "exp": "Damascus, Syria has been continuously inhabited for over 11,000 years."},
    {"cat": "World Knowledge", "diff": "Hard", "q": "Which Nordic country is NOT a member of the European Union?", "opts": ["Sweden", "Finland", "Norway", "Denmark"], "ans": "Norway", "exp": "Norway is in the EEA/Schengen Area but not an EU member state."},
    {"cat": "World Knowledge", "diff": "Hard", "q": "What is the official currency of Switzerland?", "opts": ["Euro", "Swiss Franc", "Krona", "Mark"], "ans": "Swiss Franc", "exp": "Switzerland uses the Swiss Franc (CHF)."},

    # --- SCIENCE (13) ---
    {"cat": "Science", "diff": "Easy", "q": "What is the chemical symbol for Water?", "opts": ["H2O", "CO2", "O2", "NaCl"], "ans": "H2O", "exp": "Each water molecule has two hydrogen atoms and one oxygen atom."},
    {"cat": "Science", "diff": "Easy", "q": "Which planet is known as the Red Planet?", "opts": ["Venus", "Mars", "Jupiter", "Saturn"], "ans": "Mars", "exp": "Iron oxide (rust) on Mars' surface gives it a reddish appearance."},
    {"cat": "Science", "diff": "Easy", "q": "What gas do plants absorb from the atmosphere during photosynthesis?", "opts": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"], "ans": "Carbon Dioxide", "exp": "Plants convert CO2 and water into glucose and oxygen using sunlight."},
    {"cat": "Science", "diff": "Easy", "q": "What is the center of an atom called?", "opts": ["Electron", "Nucleus", "Orbit", "Molecule"], "ans": "Nucleus", "exp": "The nucleus contains protons and neutrons at the center of an atom."},
    {"cat": "Science", "diff": "Medium", "q": "What is the speed of light in a vacuum (approx.)?", "opts": ["300,000 km/s", "150,000 km/s", "30,000 km/s", "3,000 km/s"], "ans": "300,000 km/s", "exp": "Light travels at 299,792 kilometers per second in a vacuum."},
    {"cat": "Science", "diff": "Medium", "q": "Which organ in the human body produces insulin?", "opts": ["Liver", "Kidney", "Pancreas", "Stomach"], "ans": "Pancreas", "exp": "Beta cells in the pancreas secrete insulin to regulate blood sugar."},
    {"cat": "Science", "diff": "Medium", "q": "What is the hardest natural substance on Earth?", "opts": ["Gold", "Iron", "Diamond", "Quartz"], "ans": "Diamond", "exp": "Diamond ranks 10 on the Mohs scale of mineral hardness."},
    {"cat": "Science", "diff": "Medium", "q": "Which vitamin is synthesized when human skin is exposed to sunlight?", "opts": ["Vitamin A", "Vitamin B12", "Vitamin C", "Vitamin D"], "ans": "Vitamin D", "exp": "UVB rays trigger Vitamin D synthesis in the skin."},
    {"cat": "Science", "diff": "Medium", "q": "What is the chemical symbol for Gold?", "opts": ["Go", "Gd", "Au", "Ag"], "ans": "Au", "exp": "Au comes from the Latin word for gold, 'Aurum'."},
    {"cat": "Science", "diff": "Hard", "q": "Which subatomic particle has no electric charge?", "opts": ["Proton", "Electron", "Neutron", "Positron"], "ans": "Neutron", "exp": "Neutrons are electrically neutral particles found in atomic nuclei."},
    {"cat": "Science", "diff": "Hard", "q": "What is the powerhouse of the cell?", "opts": ["Ribosome", "Mitochondria", "Golgi Body", "Lysosome"], "ans": "Mitochondria", "exp": "Mitochondria generate most of the cell's ATP energy."},
    {"cat": "Science", "diff": "Hard", "q": "What is the pH value of pure neutral water at 25°C?", "opts": ["5", "7", "8", "10"], "ans": "7", "exp": "A pH of 7 is chemically neutral."},
    {"cat": "Science", "diff": "Hard", "q": "Who proposed the theory of General Relativity?", "opts": ["Isaac Newton", "Albert Einstein", "Niels Bohr", "Galileo Galilei"], "ans": "Albert Einstein", "exp": "Albert Einstein published General Relativity in 1915."},

    # --- HISTORY (13) ---
    {"cat": "History", "diff": "Easy", "q": "Who was the first person to walk on the Moon?", "opts": ["Buzz Aldrin", "Yuri Gagarin", "Neil Armstrong", "Michael Collins"], "ans": "Neil Armstrong", "exp": "Neil Armstrong stepped onto the Moon on July 20, 1969."},
    {"cat": "History", "diff": "Easy", "q": "In which year did World War II end?", "opts": ["1942", "1945", "1948", "1950"], "ans": "1945", "exp": "World War II ended in 1945 following the surrenders of Germany and Japan."},
    {"cat": "History", "diff": "Easy", "q": "Which ancient civilization built the pyramids at Giza?", "opts": ["Romans", "Greeks", "Egyptians", "Mayans"], "ans": "Egyptians", "exp": "The Giza pyramids were built during Egypt's Old Kingdom."},
    {"cat": "History", "diff": "Easy", "q": "Who invented the telephone?", "opts": ["Thomas Edison", "Alexander Graham Bell", "Nikola Tesla", "Guglielmo Marconi"], "ans": "Alexander Graham Bell", "exp": "Bell was awarded the first US patent for the telephone in 1876."},
    {"cat": "History", "diff": "Medium", "q": "In which year did the Berlin Wall fall?", "opts": ["1985", "1987", "1989", "1991"], "ans": "1989", "exp": "The Berlin Wall fell on November 9, 1989."},
    {"cat": "History", "diff": "Medium", "q": "Who was the first human to journey into outer space?", "opts": ["Neil Armstrong", "Yuri Gagarin", "John Glenn", "Alan Shepard"], "ans": "Yuri Gagarin", "exp": "Soviet cosmonaut Yuri Gagarin orbited Earth on April 12, 1961."},
    {"cat": "History", "diff": "Medium", "q": "The Industrial Revolution began in which country?", "opts": ["Germany", "United States", "Great Britain", "France"], "ans": "Great Britain", "exp": "The Industrial Revolution started in Great Britain in the late 18th century."},
    {"cat": "History", "diff": "Medium", "q": "Who painted the Mona Lisa?", "opts": ["Michelangelo", "Leonardo da Vinci", "Raphael", "Vincent van Gogh"], "ans": "Leonardo da Vinci", "exp": "Leonardo da Vinci painted the Mona Lisa during the Italian Renaissance."},
    {"cat": "History", "diff": "Hard", "q": "Which empire was ruled by Suleiman the Magnificent?", "opts": ["Mughal Empire", "Ottoman Empire", "Roman Empire", "Persian Empire"], "ans": "Ottoman Empire", "exp": "Suleiman reigned over the Ottoman Empire from 1520 to 1566."},
    {"cat": "History", "diff": "Hard", "q": "In what year was the Magna Carta signed?", "opts": ["1066", "1215", "1492", "1776"], "ans": "1215", "exp": "King John of England sealed the Magna Carta in June 1215."},
    {"cat": "History", "diff": "Hard", "q": "Who was the founder of the Mughal Empire in South Asia?", "opts": ["Akbar", "Babur", "Humayun", "Shah Jahan"], "ans": "Babur", "exp": "Babur founded the Mughal Empire in 1526 after the First Battle of Panipat."},
    {"cat": "History", "diff": "Hard", "q": "Which ancient city was buried by the eruption of Mount Vesuvius in 79 AD?", "opts": ["Sparta", "Pompeii", "Carthage", "Troy"], "ans": "Pompeii", "exp": "Pompeii was preserved under volcanic ash from Mount Vesuvius."},
    {"cat": "History", "diff": "Medium", "q": "Which ship sank in the North Atlantic in April 1912?", "opts": ["Lusitania", "Britannic", "RMS Titanic", "Olympic"], "ans": "RMS Titanic", "exp": "The RMS Titanic sank on April 15, 1912 after hitting an iceberg."},

    # --- GEOGRAPHY (13) ---
    {"cat": "Geography", "diff": "Easy", "q": "Which is the longest river in the world?", "opts": ["Amazon River", "Nile River", "Yangtze River", "Mississippi River"], "ans": "Nile River", "exp": "The Nile River in Africa stretches roughly 6,650 km."},
    {"cat": "Geography", "diff": "Easy", "q": "What is the highest mountain peak in the world?", "opts": ["K2", "Kangchenjunga", "Mount Everest", "Makalu"], "ans": "Mount Everest", "exp": "Mount Everest stands at 8,848.86 meters above sea level."},
    {"cat": "Geography", "diff": "Easy", "q": "Which is the largest desert in the world?", "opts": ["Sahara Desert", "Arabian Desert", "Gobi Desert", "Antarctic Desert"], "ans": "Antarctic Desert", "exp": "Antarctica is technically the largest cold desert on Earth; Sahara is the largest hot desert."},
    {"cat": "Geography", "diff": "Easy", "q": "Which continent is the Sahara Desert located in?", "opts": ["Asia", "Africa", "Australia", "South America"], "ans": "Africa", "exp": "The Sahara covers much of North Africa."},
    {"cat": "Geography", "diff": "Medium", "q": "Which strait separates Asia and North America?", "opts": ["Strait of Gibraltar", "Bering Strait", "Strait of Malacca", "Bosporus Strait"], "ans": "