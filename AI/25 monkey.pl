% Initial state
initial_state(on_ground).

% Actions and their effects
action(on_ground, push_box, box_under_banana).
action(box_under_banana, climb, on_box).
action(on_box, reach, banana_reached).

% Plan generation
plan(State, [], State).
plan(State1, [Action | Rest], Goal) :-
    action(State1, Action, State2),
    plan(State2, Rest, Goal).
