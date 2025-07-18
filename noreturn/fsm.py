from statemachine import StateMachine, State, states


class TrafficLightMachine(StateMachine):
    green = State("Green", initial=True)
    yellow = State("Yellow", final=True)
    # red = State("Red")

    switch = green.to(yellow)

    on_enter_yellow = lambda self: print("yellow")  # callback

    # def on_enter_red(self):
    #     return print("red")  # callback

# event
TM = TrafficLightMachine()
print(TM.current_state)
TM.send("switch")
