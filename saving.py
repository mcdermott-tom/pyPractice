from os.path import exists

if __name__=='__main__':
    flExst = exists('savingDemo.txt')
    if not flExst:
        f = open('savingDemo.txt', 'x')
        f.write('0\nID\tName\tGPA\n')
        # f.close()

    students = []
    f=open('savingDemo.txt', 'r')
    n=(int(f.readline()))
    for i in range(n):
        students.append(i)
    # print(students[i] for i in students)
    choice=(input("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\nWelcome to our Singleton database! Would you like to:\n\nView Students and GPAs: (V)\nor\nCreate New Student (C)\n"))

    


    while(choice.lower()!=('v') and choice.lower()!=('c')):
        choice=input("Hrm, not a valid response... Type either V or C according to your choice.\n")

    if choice.lower() ==('c'):
        name=input('Enter student name:\n')
        gpa = input('Enter GPA:\n')
        w = open('savingDemo.txt', 'a')
        w.write('{0}\t{1}\t{2}'.format(n+1, name, gpa))
        print('Student saved!\nName: {0}'.format(name))
        n+=1

    if choice.lower()==('v'):
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nJust snooping today, eh? Fair enough, can't blame ya. Here are all of our student's recods. \nDon\'t do anything mischievious plz and thx :)\n\n")
        print('Students:\n',*[students[i] for i in students], sep='\t')
        if(len(students)<1):
            print("No students to display. :(\n\n")