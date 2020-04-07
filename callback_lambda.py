state = '0'

def update_state(new_state, instruction, validation):
    if validation(new_state):
        state = new_state
        print (instruction)
    else:
        print ("no valid state")

update_state('1', "move forward", lambda state : state in ['0', '2', '3'])

update_state('2', "move right", lambda state : state in ['2', '3'])

update_state('4', "collect", lambda state : state in ['0', '1', '3'])
