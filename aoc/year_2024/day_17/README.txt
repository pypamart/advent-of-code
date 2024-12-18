0 |->2,4 -> B = A % 8
1 |  1,6 -> B = B ^ 6
2 |  7,5 -> C = A // 2 ** B
3 |  4,4 -> B = B ^ C
4 |  1,7 -> B = B ^ 7 -> XOR sur les 3 derniers digits
5 |  0,3 -> A = A // 3 ** 2 = A // 9
6 |  5,5 -> Affiche Registre B modulo 8 [2,4,1,6,7,5,4,4,1,7,0,3,5,5,3,0]
7 |--3,0 -> A == 0
 

# 0
7 | B = valeur
6 | B = 8 * x  + X
5 | A = A * 9 + [0, 1, 2, 3, 4, 5, 6, 7, 8]
4 | B = 7 ^ B
3 | B = C ^ B
2 |
1 | B = 6 ^ B
0 | A =
 
7 |  
6 |
5 |
4 | B = a*8 + 7 - X
3 |
 

1[0] 1
1010[3,0] 10 = 3*3 + 1
1010111[5,3,0] 87 = 15.4*5 + 3*3 + 1
1010111001[5,5,3,0]
1010111001001[3,5,5,3,0] 5577
1010111001001000[0,3,5,5,3,0] 44616 et 44619
1010111001001000010 [7,0,3,5,5,3,0] 356930 et 356957
1010111001001000010000 [1,7,0,3,5,5,3,0] 2855440 et 2855446 et 2 et 855661 et 2855662 et 2855663
1010111001001000010000100[4,1,7,0,3,5,5,3,0]
22843524
22843525
22845288
22845296
22845298
22845304
22845306
[4,4,1,7,0,3,5,5,3,0]
182748196
182762304
182762308
182762309
182762372
182762373
182762435
182762436
182762437
182762451
[5,4,4,1,7,0,3,5,5,3,0]
 
0 001
1
2
3 010 001
4
5 111 001
6
7
8
 

Search candidate for [0]
Matched: 1
001
Search candidate for [3, 0]
Matched: 10
001010
Search candidate for [5, 3, 0]
Matched: 87
001010111
Search candidate for [5, 5, 3, 0]
Matched: 697
001010111001
Search candidate for [3, 5, 5, 3, 0]
Matched: 5577
001010111001001
Search candidate for [0, 3, 5, 5, 3, 0]
Matched: 44616
001010111001001000
Search candidate for [7, 0, 3, 5, 5, 3, 0]
Matched: 356930
001010111001001000010
Search candidate for [1, 7, 0, 3, 5, 5, 3, 0]
Matched: 2855440
001010111001001000010000
Search candidate for [4, 1, 7, 0, 3, 5, 5, 3, 0]
Matched: 22843524
001010111001001000010000100
Search candidate for [4, 4, 1, 7, 0, 3, 5, 5, 3, 0]
Matched: 182748196
001010111001001000010000100100
Search candidate for [5, 4, 4, 1, 7, 0, 3, 5, 5, 3, 0]
Matched: 1461985568
001010111001001000010000100100000
Search candidate for [7, 5, 4, 4, 1, 7, 0, 3, 5, 5, 3, 0]
Search candidate for [6, 7, 5, 4, 4, 1, 7, 0, 3, 5, 5, 3, 0]
Search candidate for [1, 6, 7, 5, 4, 4, 1, 7, 0, 3, 5, 5, 3, 0]
Search candidate for [4, 1, 6, 7, 5, 4, 4, 1, 7, 0, 3, 5, 5, 3, 0]
Search candidate for [2, 4, 1, 6, 7, 5, 4, 4, 1, 7, 0, 3, 5, 5, 3, 0]
(venv) (2024 )



Search candidate for [0]
Matched: 1
1
Search candidate for [3, 0]
Matched: 10
12
Search candidate for [5, 3, 0]
Matched: 87
127
Search candidate for [5, 5, 3, 0]
Matched: 697
1271
Search candidate for [3, 5, 5, 3, 0]
Matched: 5577
12711
Search candidate for [0, 3, 5, 5, 3, 0]
Matched: 44616
127110
Search candidate for [7, 0, 3, 5, 5, 3, 0]
Matched: 356930
1271102
Search candidate for [1, 7, 0, 3, 5, 5, 3, 0]
Matched: 2855440
12711020
Search candidate for [4, 1, 7, 0, 3, 5, 5, 3, 0]
Matched: 22843524
127110204
Search candidate for [4, 4, 1, 7, 0, 3, 5, 5, 3, 0]
Matched: 182748196
1271102044
Search candidate for [5, 4, 4, 1, 7, 0, 3, 5, 5, 3, 0]
Matched: 1461985568
12711020440
Search candidate for [7, 5, 4, 4, 1, 7, 0, 3, 5, 5, 3, 0]
Search candidate for [6, 7, 5, 4, 4, 1, 7, 0, 3, 5, 5, 3, 0]
Search candidate for [1, 6, 7, 5, 4, 4, 1, 7, 0, 3, 5, 5, 3, 0]
Search candidate for [4, 1, 6, 7, 5, 4, 4, 1, 7, 0, 3, 5, 5, 3, 0]
Search candidate for [2, 4, 1, 6, 7, 5, 4, 4, 1, 7, 0, 3, 5, 5, 3, 0]