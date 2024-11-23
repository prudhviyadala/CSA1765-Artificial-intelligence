% Facts
likes(john, pizza).
likes(mary, sushi).

% Rule
eats_out(X) :- likes(X, _).

% Forward chaining process
forward_chaining :-
    % Collect all facts
    findall(X, likes(X, _), People),
    % Apply the rule to each person
    forall(member(Person, People), (eats_out(Person), assert(fact(eats_out(Person))))).

% Query to list all facts
list_facts :-
    fact(Fact),
    write(Fact), nl,
    fail.
list_facts.