/* 
a. Use Prolog structures to represent simple geometric shapes:
- point - two numbers representing X and Y coordinates
- seg - a line defined by two points
- triangle - defined by three points
*/

point(X, Y) :- number(X), number(Y).

seg(X1, Y1, X2, Y2) :- 
	point(X1, Y1), point(X2, Y2).

triangle(X1, Y1, X2, Y2, X3, Y3) :- 
	point(X1, Y1),
	point(X2, Y2),
	point(X3, Y3).

/*
b. Given the two families of triangles below, find their intersection:
- family 1: all triangles with corners 1 and 3 in (1,1) and (2,3), and corner 2 anywhere
- family 2: all triangles with corner 1 anywhere, and corners 2 and 3 on the vertical lines
X=4, and X=2
*/

% c. Define rules for vertical and horizontal segments
