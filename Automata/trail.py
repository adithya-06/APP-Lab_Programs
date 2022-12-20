from automata.fa.dfa import DFA 
dfa = DFA(
    states={'q0', 'q1', 'q2','q3'},
    input_symbols={'a', 'b'},
    transitions={
        'q0': {'a': 'q1', 'b': 'q0'},
        'q1': {'a': 'q2', 'b': 'q0'},
        'q2': {'a': 'q2', 'b': 'q3'},
        'q3': {'a': 'q1', 'b': 'q0'},
    },
    initial_state='q0', final_states={'q3'}
)
for i in range(1,6):
    num = input("Enter the string :")
    if(dfa.accepts_input(num)):
        print("Accepted")
    else:
        print("Rejected")
