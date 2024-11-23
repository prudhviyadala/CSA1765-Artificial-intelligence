% Facts
likes(john, pizza).
likes(mary, sushi).

% Rule
eats_out(X) :- likes(X, _).

% Backward chaining process
% Check if the goal can be satisfied
backward_chaining(Goal) :-
    call(Goal), !. % Use call/1 to execute the goal
