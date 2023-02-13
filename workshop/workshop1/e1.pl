mammals(rats).
mammals(bears).
fish(salmons).
eat(bears, honey).
eat(bears, salmons).
eat(salmons, worms).

foodchain(X, Y) :- eat(X, Y).
foodchain(X, Y) :- 
	eat(X, Z),
	foodchain(Z, Y).
