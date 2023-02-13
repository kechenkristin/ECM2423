### E1
```prolog

```


?- eat(X, honey), eat(X, salmons).  
X = bears.

```prolog
foodchain(X, Y) :- eat(X, Y).
foodchain(X, Y) :- 
	eat(X, Z),
        foodchain(Z, Y).     
```


```
?- foodchain(rats, X).
false.

?- foodchain(X, worms).
X = salmons ;
X = bears ;
false.
```

