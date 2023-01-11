#! usr/bin/env python3
import html

def main():
    # trivia dictionary

    trivia= {
         "category": "Entertainment: Film",
         "type": "multiple",
         "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
         "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
         "incorrect_answers": [
             "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
             "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
             "&quot;Round up the usual suspects.&quot;"
            ]
         }
    question = trivia['question']
    correct_answer = trivia['correct_answer']
    wrong_answer_1 = trivia['incorrect_answers'][0]
    wrong_answer_2 = trivia['incorrect_answers'][1]
    wrong_answer_3 = trivia['incorrect_answers'][2]
    print(html.unescape(question  + '\nA)' + correct_answer  + '\nB)' + wrong_answer_1  + '\nC)' + wrong_answer_2  + '\nD)' + wrong_answer_2))
    answer = input()
    if answer.lower() =='a':
        print("Correct!")
    else:
        print("Incorrect!")
main()

