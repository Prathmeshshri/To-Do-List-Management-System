print('To Do List Mannagement System')

tasks = []

def add_task():
    title = input('Enter task title - ')

    if title == '':
        print('Task Title Cannot be empty')
        return

    description = input('Enter Description - ')

    print('\nPriority :')
    print('1. High')
    print('2. Medium')
    print('3. Low')

    choice = input('Enter Choice - ')

    if choice == '1':
        priority = 'High'
    elif choice == '2':
        priority = 'Medium'
    elif choice == '3':
        priority = 'Low'    
    else:
        priority = 'Medium'
        print('Invalid Choice. Medium Priority Selected. ')

    print('\nCategory :')
    print('1. College')
    print('2. Personal')
    print('3. Work')

    choice = input('Enter Choice - ')

    if choice == '1':
        category = 'College'
    elif choice == '2':
        category = 'Personal'
    elif choice == '3':
        category = 'Work'
    else:
        category = 'Other'

    task = {
        'title': title,
        'description': description,
        'priority': priority,
        'category': category,
        'status': 'Pending'
    }

    tasks.append(task)

    print('Task added successfully!')


def view_task():
    print('\n====ALL TASK====')

    if len(tasks) == 0:
        print('No tasks available')
        return

    for i in range(len(tasks)):
        print('\nTask', i + 1)
        print('Title: ', tasks[i]['title'])
        print('Description: ', tasks[i]['description'])
        print('Priority: ', tasks[i]['priority'])
        print('Category: ', tasks[i]['category'])
        print('Status: ', tasks[i]['status'])
        print('-------------------------')

def pending_task():
    print('\n====PENDING TASKS====')

    found = False

    for i in range(len(tasks)):
        if tasks[i]['status'] == 'Pending':
            found = True
            print('\nTask', i + 1)
            print('Title:', tasks[i]['title'])
            print('Priority:', tasks[i]['priority'])
            print('Category:', tasks[i]['category'])

        if found == False:
         print('No pending tasks')

def completed_task():
    print('\n==== COMPLETED TASKS ====')

    found = False

    for i in range(len(tasks)):
        if tasks[i]['status'] == 'Completed':
            found = True
            print('\nTask', i + 1)
            print('Title:', tasks[i]['title'])
            print('Priority:', tasks[i]['priority'])
            print('Category:', tasks[i]['category'])

        found == False
        print('No completed tasks')


def search_task():
    print('\n====SEARCH TASK====')

    search = input('Enter task title - ')
    found = False

    for i in range(len(tasks)):
        if search.lower() in tasks[i]['title'].lower():
           found = True
           print('\nTask', i + 1)
           print('Title:', tasks[i]['title'])
           print('Description:', tasks[i]['description'])
           print('Priority:', tasks[i]['priority'])
           print('Category:', tasks[i]['category'])
           print('Status:', tasks[i]['status'])
           
    if found == False:
        print('Take not found')
        

def update_task():
    print('\n==== UPDATE TASK ====')

    if len(tasks) == 0:
        print('No task available')
        return

    view_task()

    try:
        number = int(input('\nEnter task number: '))

        if number < 1 or number > len(tasks):
            print('Invalid task number')
            return

        index = number - 1

        print('\n1. Update Title')
        print('2. Update Description')
        print('3. Update Priority')

        choice = input('Enter Choice - ')

        if choice == '1':
            new_title = input('Enter new title - ')
            tasks[index]['title'] = new_title
            print('Title update')

        elif choice == '2':
            new_description = input('Enter new description - ')
            tasks[index]['description'] = new_description
            print('Description updated')

        elif choice == '3':
            print('1. High')
            print('2. Medium')
            print('3. Low')

            priority = input('Enter choice - ')

            if priority == '1':
                tasks[index]['priority'] = 'High'
            elif priority == '2':
                tasks[index]['priority'] = 'Medium'
            elif priority == '3':
                tasks[index]['priority'] = 'Low'
            else:
                print('Invalid choice')
                return

            print('Priority updated')

        else:
             print('Invalid choice')

    except ValueError:
         print('Please enter a number')



def complete_task():
    print('\n===== COMPLETE TASK =====')

    if len(tasks) == 0:
        print('No tasks available')
        return

    view_task()

    try:
        number = int(input('\nEnter task number '))

        if number < 1 or number > len(tasks):
            print('Invalid task number')
            return

        index = number - 1

        tasks[index]['status'] = 'Completed'

        print('Task marked as completed!')

    except ValueError:
        print('Please enter a number')


def delete_task():
    print('\n==== DELETE TASK ====')

    if len(tasks) == 0:
        print('No tasks available')
        return

    view_task()

    try:
        number = int(input('\nEnter task number - '))

        if number < 1 or number > len(tasks):
            print('Invalid task number ')
            return

        index = number - 1

        confirmation = input(
            'Are you sure? (yes/no): '
        )

        if confirmation.lower() == 'yes':
            tasks.pop(index)
            print('Task deleted successfully')
        else:
            print('Task was not deleted')

    except ValueError:
        print('Please enter a number')


def statistics():
    print('\n===== TASK STATISTICS =====')

    total = len(tasks)
    completed = 0
    pending = 0

    for task in tasks:
        if task['status'] == 'Completed':
            completed = completed + 1
        else:
            pending = pending + 1

    print('Total Tasks -', total)
    print('Completed Tasks -', completed)
    print('Pending Tasks -', pending)

    if total > 0:
        percentage = (completed / total) * 100
        print('Completion :', percentage, '%')
    else:
        print('Completion: 0%')


while True:

    print('\n========================')
    print('     TO-DO LIST MANAGER')
    print('=========================')
    print('1. Add Task')
    print('2. View All Task')
    print('3. View Pending Tasks')
    print('4. View Completed Tasks')
    print('5. Search Task')
    print('6. Update Task')
    print('7. Complete Task')
    print('8. Delete Task')
    print('9. Task Statistics')
    print('10. Exit')
    print('===========================')

    choice = input('Enter your choice - ')

    if choice == '1':
        add_task()

    elif choice == '2':
        view_task()

    elif choice == '3':
        pending_task()

    elif choice == '4':
        completed_task()

    elif choice == '5':
        search_task()

    elif choice == '6':
        update_task()

    elif choice == '7':
        complete_task()

    elif choice == '8':
        delete_task()

    elif choice == '9':
        statistics()

    elif choice == '10':
        print('\nThank you for using To-Do List Manager!')
        break

    else:
        print('Invalid choice. Please try again')
        
