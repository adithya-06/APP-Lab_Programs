from automata.fa.dfa import DFA # DFA which does not accept any input
dfa = DFA(
    states={'q0', 'q1', 'q2','q3'}, input_symbols={'0', '1'}, 
    transitions={
        'q0': {'0': 'q3', '1': 'q1'},
        'q1': {'0': 'q2', '1': 'q3'},
        'q2': {'0': 'q3', '1': 'q1'},
        'q3': {'0': 'q3', '1': 'q3'},
    },
    initial_state='q0',final_states={'q1','q2'}
)
for i in range(1,8):
    num = input("Enter the string:")
    if(dfa.accepts_input(num)):
        print("Accepted")
    else:
        print("Rejected")
