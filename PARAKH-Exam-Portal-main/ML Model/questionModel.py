import joblib
from ML_Model import SkillLevelPredictor
import random
import time

#Load the pretrained model from the saved file
model_file = "skill_level_model.pkl"
loaded_predictor = SkillLevelPredictor()
loaded_predictor.load_model(model_file)


#better dict for question with classification -

beginner = {
    1: {
        'question': "Who was the founder of the Gupta dynasty?",
        'options': [
            "a) Chandragupta Maurya",
            "b) Samudragupta",
            "c) Ashoka",
            "d) Harsha",
        ],
        'correct_answer': "b) Samudragupta"
    },
    2: {
        'question': "The Rigveda, an ancient Indian text, is written in which language?",
        'options': [
            "a) Sanskrit",
            "b) Pali",
            "c) Prakrit",
            "d) Tamil",
        ],
        'correct_answer': "a) Sanskrit"
    },
    3: {
        'question': "Who was the author of the ancient Indian treatise on statecraft known as the 'Arthashastra'?",
        'options': [
            "a) Kalidasa",
            "b) Chanakya",
            "c) Valmiki",
            "d) Bhasa",
        ],
        'correct_answer': "b) Chanakya"
    },
    4: {
        'question': "The historic 'Dandi March' led by Mahatma Gandhi in 1930 was a protest against which British policy?",
        'options': [
            "a) Rowlatt Act",
            "b) Partition of Bengal",
            "c) Salt Tax",
            "d) Jallianwala Bagh Massacre",
        ],
        'correct_answer': "c) Salt Tax"
    },
    5: {
        'question': "Who was the first Indian woman to fly an aircraft solo?",
        'options': [
            "a) Rani Padmini",
            "b) Rani Lakshmibai",
            "c) Sarla Thakral",
            "d) Kalpana Chawla",
        ],
        'correct_answer': "c) Sarla Thakral"
    },
    6: {
        'question': "The 'Quit India Movement' was launched by Mahatma Gandhi in which year?",
        'options': [
            "a) 1932",
            "b) 1942",
            "c) 1947",
            "d) 1952",
        ],
        'correct_answer': "b) 1942"
    },
    7: {
        'question': "The famous caves of Ajanta and Ellora are primarily known for what?",
        'options': [
            "a) Buddhist Monasteries",
            "b) Hindu Temples",
            "c) Jain Shrines",
            "d) Rock-cut Sculptures and Paintings",
        ],
        'correct_answer': "d) Rock-cut Sculptures and Paintings"
    },
    8: {
        'question': "Who was the leader of the Jallianwala Bagh Massacre in Amritsar in 1919?",
        'options': [
            "a) Bhagat Singh",
            "b) Jawaharlal Nehru",
            "c) General Dyer",
            "d) Subhas Chandra Bose",
        ],
        'correct_answer': "c) General Dyer"
    },
    9: {
        'question': "The Harappan civilization is also known by which other name?",
        'options': [
            "a) Mesopotamian Civilization",
            "b) Indus Valley Civilization",
            "c) Mayan Civilization",
            "d) Egyptian Civilization",
        ],
        'correct_answer': "b) Indus Valley Civilization"
    },
    10: {
        'question': "Who was the founder of the Maurya dynasty?",
        'options': [
            "a) Ashoka",
            "b) Chandragupta Maurya",
            "c) Bindusara",
            "d) Bimbisara",
        ],
        'correct_answer': "b) Chandragupta Maurya"
    },
    11: {
        'question': "The battle of Panipat in 1526 led to the establishment of which dynasty in India?",
        'options': [
            "a) Mughal Dynasty",
            "b) Chola Dynasty",
            "c) Gupta Dynasty",
            "d) Vijayanagara Empire",
        ],
        'correct_answer': "a) Mughal Dynasty"
    },
    12: {
        'question': "Which Mughal Emperor is known for his architectural masterpiece, the Taj Mahal?",
        'options': [
            "a) Akbar",
            "b) Jahangir",
            "c) Aurangzeb",
            "d) Shah Jahan",
        ],
        'correct_answer': "d) Shah Jahan"
    },
    13: {
        'question': "Who was the author of the famous book 'Discovery of India'?",
        'options': [
            "a) Jawaharlal Nehru",
            "b) Mahatma Gandhi",
            "c) Rabindranath Tagore",
            "d) Subhas Chandra Bose",
        ],
        'correct_answer': "a) Jawaharlal Nehru"
    },
    14: {
        'question': "The term 'Swaraj' was popularized by which Indian leader during the freedom struggle?",
        'options': [
            "a) Sardar Vallabhbhai Patel",
            "b) Bal Gangadhar Tilak",
            "c) Jawaharlal Nehru",
            "d) Subhas Chandra Bose",
        ],
        'correct_answer': "b) Bal Gangadhar Tilak"
    },
    15: {
        'question': "Which event marked the beginning of the British East India Company's rule in India?",
        'options': [
            "a) Battle of Plassey",
            "b) Battle of Buxar",
            "c) Battle of Panipat",
            "d) Battle of Plakwah",
        ],
        'correct_answer': "a) Battle of Plassey"
    },
    16: {
        'question': "Who was the first woman President of the Indian National Congress?",
        'options': [
            "a) Sarojini Naidu",
            "b) Indira Gandhi",
            "c) Annie Besant",
            "d) Sucheta Kriplani",
        ],
        'correct_answer': "a) Sarojini Naidu"
    },
    17: {
        'question': "The Indian National Congress (INC) was founded in which year?",
        'options': [
            "a) 1885",
            "b) 1905",
            "c) 1947",
            "d) 1950",
        ],
        'correct_answer': "a) 1885"
    },
    18: {
        'question': "Who wrote the epic Sanskrit poem 'Ramayana'?",
        'options': [
            "a) Valmiki",
            "b) Tulsidas",
            "c) Vyasa",
            "d) Kalidasa",
        ],
        'correct_answer': "a) Valmiki"
    },
    19: {
        'question': "The historic 'Jallianwala Bagh Massacre' occurred in which city of Punjab?",
        'options': [
            "a) Lahore",
            "b) Amritsar",
            "c) Chandigarh",
            "d) Patiala",
        ],
        'correct_answer': "b) Amritsar"
    },
    20: {
        'question': "Who was the leader of the Indian National Army (INA) during World War II?",
        'options': [
            "a) Bhagat Singh",
            "b) Jawaharlal Nehru",
            "c) Subhas Chandra Bose",
            "d) Sardar Vallabhbhai Patel",
        ],
        'correct_answer': "c) Subhas Chandra Bose"
    },
    21: {
        'question': "Which Indian leader is known for his role in the Champaran Satyagraha against indigo planters?",
        'options': [
            "a) Mahatma Gandhi",
            "b) Jawaharlal Nehru",
            "c) Sardar Vallabhbhai Patel",
            "d) Rajendra Prasad",
        ],
        'correct_answer': "a) Mahatma Gandhi"
    },
    22: {
        'question': "The Battle of Plassey in 1757 established British control over which region of India?",
        'options': [
            "a) Bengal",
            "b) Punjab",
            "c) Maharashtra",
            "d) Tamil Nadu",
        ],
        'correct_answer': "a) Bengal"
    },
    23: {
        'question': "The Moplah Rebellion, which took place in the early 20th century, occurred in which Indian state?",
        'options': [
            "a) Kerala",
            "b) Tamil Nadu",
            "c) Andhra Pradesh",
            "d) Karnataka",
        ],
        'correct_answer': "a) Kerala"
    },
    24: {
        'question': "Who was the first Indian woman to become a pilot in the Indian Air Force (IAF)?",
        'options': [
            "a) Padmavathy Bandopadhyay",
            "b) Gunjan Saxena",
            "c) Avani Chaturvedi",
            "d) Sarla Thakral",
        ],
        'correct_answer': "d) Sarla Thakral"
    },
    25: {
        'question': "The famous Indian mathematician and astronomer Aryabhata was born in which ancient Indian kingdom?",
        'options': [
            "a) Magadha",
            "b) Kalinga",
            "c) Maurya",
            "d) Gupta",
        ],
        'correct_answer': "d) Gupta"
    },
}

intermediate = {
    1: {
        'question': "The historic city of Fatehpur Sikri, known for its Mughal architecture, is located in which Indian state?",
        'options': [
            "a) Uttar Pradesh",
            "b) Rajasthan",
            "c) Madhya Pradesh",
            "d) Punjab",
        ],
        'correct_answer': "a) Uttar Pradesh"
    },
    2: {
        'question': "Who was the first woman Prime Minister of India?",
        'options': [
            "a) Sushma Swaraj",
            "b) Indira Gandhi",
            "c) Sonia Gandhi",
            "d) Mayawati",
        ],
        'correct_answer': "b) Indira Gandhi"
    },
    3: {
        'question': "The Indian Constitution was adopted on which date?",
        'options': [
            "a) January 26, 1947",
            "b) August 15, 1947",
            "c) January 26, 1950",
            "d) August 15, 1950",
        ],
        'correct_answer': "c) January 26, 1950"
    },
    4: {
        'question': "The famous Kailasa Temple, carved out of a single rock, is located in which cave complex?",
        'options': [
            "a) Ajanta Caves",
            "b) Ellora Caves",
            "c) Elephanta Caves",
            "d) Karla Caves",
        ],
        'correct_answer': "b) Ellora Caves"
    },
    5: {
        'question': "Which Indian leader is often referred to as the 'Lion of Punjab'?",
        'options': [
            "a) Bhagat Singh",
            "b) Lala Lajpat Rai",
            "c) Bal Gangadhar Tilak",
            "d) Subhas Chandra Bose",
        ],
        'correct_answer': "b) Lala Lajpat Rai"
    },
    6: {
        'question': "The 'Battle of Haldighati' in 1576 was fought between which two historical figures?",
        'options': [
            "a) Rana Sanga and Akbar",
            "b) Maharana Pratap and Akbar",
            "c) Babur and Ibrahim Lodhi",
            "d) Sher Shah Suri and Humayun",
        ],
        'correct_answer': "b) Maharana Pratap and Akbar"
    },
    7: {
        'question': "Who was the Governor-General of India during the Indian Rebellion of 1857?",
        'options': [
            "a) Lord Dalhousie",
            "b) Lord Canning",
            "c) Lord Curzon",
            "d) Lord Wellesley",
        ],
        'correct_answer': "b) Lord Canning"
    },
    8: {
        'question': "The 'Quit India Movement' was launched by Mahatma Gandhi in which year?",
        'options': [
            "a) 1932",
            "b) 1942",
            "c) 1947",
            "d) 1952",
        ],
        'correct_answer': "b) 1942"
    },
    9: {
        'question': "The famous 'Kumbh Mela' is a major pilgrimage and festival celebrated primarily in which Indian state?",
        'options': [
            "a) Uttar Pradesh",
            "b) Bihar",
            "c) Madhya Pradesh",
            "d) Rajasthan",
        ],
        'correct_answer': "a) Uttar Pradesh"
    },

    10: {
        'question': "Who was the first Sikh Guru?",
        'options': [
            "a) Guru Nanak Dev Ji",
            "b) Guru Angad Dev Ji",
            "c) Guru Amar Das Ji",
            "d) Guru Ram Das Ji",
        ],
        'correct_answer': "a) Guru Nanak Dev Ji"
    },
    11: {
        'question': "Which Mughal Emperor is known for his policy of religious tolerance and his support for the arts and culture?",
        'options': [
            "a) Akbar",
            "b) Babur",
            "c) Jahangir",
            "d) Aurangzeb",
        ],
        'correct_answer': "a) Akbar"
    },
    12: {
        'question': "The famous rock-cut temples of Mahabalipuram are located in which Indian state?",
        'options': [
            "a) Tamil Nadu",
            "b) Karnataka",
            "c) Andhra Pradesh",
            "d) Kerala",
        ],
        'correct_answer': "a) Tamil Nadu"
    },
    13: {
        'question': "The ancient city of Varanasi is situated on the banks of which river?",
        'options': [
            "a) Yamuna River",
            "b) Godavari River",
            "c) Ganges River",
            "d) Brahmaputra River",
        ],
        'correct_answer': "c) Ganges River"
    },
    14: {
        'question': "Who was the author of the book 'Anandmath,' which includes the song 'Vande Mataram'?",
        'options': [
            "a) Rabindranath Tagore",
            "b) Bankim Chandra Chattopadhyay",
            "c) Swami Vivekananda",
            "d) Subhas Chandra Bose",
        ],
        'correct_answer': "b) Bankim Chandra Chattopadhyay"
    },

    15: {
        'question': "Which famous Indian physicist is known for his work on the theory of black holes and the 'Hawking radiation'?",
        'options': [
            "a) C.V. Raman",
            "b) S.N. Bose",
            "c) Satyendra Nath Bose",
            "d) Stephen Hawking",
        ],
        'correct_answer': "d) Stephen Hawking"
    },


}



advanced = {

    1: {
        'question': "Who is considered the 'Father of Indian Space Program'?",
        'options': [
            "a) Dr. A.P.J. Abdul Kalam",
            "b) Dr. Vikram Sarabhai",
            "c) Dr. Homi J. Bhabha",
            "d) Dr. Satish Dhawan",
        ],
        'correct_answer': "b) Dr. Vikram Sarabhai"
    },
    2: {
        'question': "The famous 'Khajuraho Group of Monuments' is known for its intricately carved temples and is located in which Indian state?",
        'options': [
            "a) Rajasthan",
            "b) Madhya Pradesh",
            "c) Uttar Pradesh",
            "d) Karnataka",
        ],
        'correct_answer': "b) Madhya Pradesh"
    },
    3: {
        'question': "Who was the first Indian to win an individual Olympic gold medal?",
        'options': [
            "a) Milkha Singh",
            "b) Abhinav Bindra",
            "c) P.T. Usha",
            "d) Sushil Kumar",
        ],
        'correct_answer': "b) Abhinav Bindra"
    },
    4: {
        'question': "The ancient university of Nalanda, a renowned center of learning, was located in which present-day Indian state?",
        'options': [
            "a) Bihar",
            "b) Uttar Pradesh",
            "c) Madhya Pradesh",
            "d) West Bengal",
        ],
        'correct_answer': "a) Bihar"
    },


    5: {
        'question': "Who was the first woman to climb Mount Everest from India?",
        'options': [
            "a) Bachendri Pal",
            "b) Arunima Sinha",
            "c) Santosh Yadav",
            "d) Premlata Agarwal",
        ],
        'correct_answer': "a) Bachendri Pal"
    },
    6: {
        'question': "The Indian Constitution was adopted on which date?",
        'options': [
            "a) January 26, 1947",
            "b) August 15, 1947",
            "c) January 26, 1950",
            "d) August 15, 1950",
        ],
        'correct_answer': "c) January 26, 1950"
    },


    7: {
        'question': "Who was the first woman President of India?",
        'options': [
            "a) Pratibha Patil",
            "b) Indira Gandhi",
            "c) Sonia Gandhi",
            "d) Sarojini Naidu",
        ],
        'correct_answer': "a) Pratibha Patil"
    },


}




def main():
    u = input("Are you a new user? \n 1. y \n 2. n \n")
    if u == 'y':
        new_user = True
    else:
        new_user = False

    if new_user:
        level = 'beginner'
    else:
        level = current_level

    print("Let's Start - \n")
    advCount = 0
    intermCount = 0
    beginCount = 0
    total_time = 0  
    total_questions = 5  

    for i in range(1,total_questions+1):
        

        print("Q",i,"-",end=" ")
        if level == 'advanced':
            n = len(advanced)
            num = random.randint(1, 7)
            print(advanced[num]['question'], '\n')
            print(advanced[num]['options'], '\n')
            ans = input("Enter answer option:  \t")
            print("\n")
            if ans == advanced[num]['correct_answer'][0]:
                correctness = 1
                advCount += 1
            else:
                correctness = 0
        elif level == 'beginner':
            n = len(beginner)
            num = random.randint(1, 25)
            print(beginner[num]['question'], '\n')
            print(beginner[num]['options'], '\n')
            ans = input("Enter answer option:  \t")
            print("\n")
            if ans == beginner[num]['correct_answer'][0]:
                correctness = 1
                beginCount += 1
            else:
                correctness = 0
        elif level == 'intermediate':
            n = len(intermediate)
            num = random.randint(1, 15)
            print(intermediate[num]['question'], '\n')
            print(intermediate[num]['options'], '\n')
            ans = input("Enter answer option: \t")
            print("\n")
            if ans == intermediate[num]['correct_answer'][0]:
                correctness = 1
                intermCount += 1
            else:
                correctness = 0


        new_level = level
        new_correctness = correctness

        predicted_level = loaded_predictor.predict(new_level, new_correctness)
        level = predicted_level
        print(level,"\n")
        

    print("\n")
    print("REPORT - \n")
    print("Advanced questions answered correctly: ", advCount, "\n")
    print("Intermediate questions answered correctly: ", intermCount, "\n")
    print("Easy questions answered correctly: ", beginCount, "\n")

    percentage_correct = (advCount + intermCount + beginCount) / (total_questions) * 100
    print(f"Percentage of correct answers: {percentage_correct:.2f}%")
    print("\n")

if __name__ == "__main__":
    main()