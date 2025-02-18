% Base case: if the list is empty, there are no vowels.
count_vowels([], 0).

% Case when the head of the list is a vowel.
count_vowels([Head|Tail], Count) :-
    (Head == a; Head == e; Head == i; Head == o; Head == u),  % Check if the head is a vowel.
    count_vowels(Tail, TailCount),  % Recursive call for the tail of the list.
    Count is TailCount + 1.  % Increment the count.

% Case when the head of the list is not a vowel.
count_vowels([Head|Tail], Count) :-
    \+ (Head == a; Head == e; Head == i; Head == o; Head == u),  % Check if the head is not a vowel.
    count_vowels(Tail, Count).  % Recursive call without incrementing the count.