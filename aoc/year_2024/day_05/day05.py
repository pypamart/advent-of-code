from collections import defaultdict

ORDERS = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13"""

UPDATES = """75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

ORDERS2 = """61|98
25|32
25|15
98|88
98|77
98|34
32|34
32|13
32|75
32|91
87|13
87|26
87|39
87|75
87|27
26|46
26|13
26|75
26|29
26|93
26|53
22|39
22|42
22|76
22|46
22|98
22|24
22|37
76|74
76|79
76|39
76|11
76|15
76|42
76|36
76|69
77|85
77|99
77|34
77|94
77|43
77|59
77|56
77|22
77|29
79|94
79|26
79|29
79|32
79|85
79|98
79|88
79|34
79|61
79|99
58|69
58|32
58|98
58|79
58|11
58|77
58|59
58|43
58|15
58|35
58|74
96|51
96|46
96|11
96|72
96|98
96|66
96|62
96|15
96|42
96|43
96|69
96|37
74|32
74|99
74|72
74|43
74|51
74|88
74|61
74|79
74|35
74|56
74|59
74|34
74|69
27|15
27|37
27|98
27|96
27|39
27|79
27|61
27|25
27|66
27|36
27|91
27|77
27|62
27|56
39|79
39|56
39|15
39|36
39|77
39|58
39|73
39|69
39|66
39|98
39|99
39|42
39|74
39|61
39|47
12|22
12|15
12|62
12|66
12|76
12|69
12|39
12|91
12|61
12|58
12|46
12|79
12|37
12|25
12|74
12|24
43|13
43|35
43|88
43|24
43|75
43|53
43|72
43|27
43|64
43|93
43|85
43|87
43|94
43|59
43|92
43|84
43|12
15|61
15|87
15|32
15|79
15|77
15|35
15|29
15|11
15|26
15|59
15|51
15|85
15|34
15|92
15|98
15|64
15|99
15|37
46|42
46|61
46|51
46|64
46|66
46|79
46|36
46|59
46|58
46|11
46|98
46|15
46|43
46|77
46|69
46|35
46|72
46|56
46|73
35|53
35|75
35|39
35|12
35|76
35|96
35|47
35|84
35|88
35|24
35|94
35|27
35|26
35|91
35|34
35|64
35|92
35|93
35|87
35|29
99|32
99|92
99|22
99|12
99|24
99|94
99|26
99|96
99|87
99|88
99|91
99|34
99|27
99|29
99|76
99|13
99|53
99|75
99|85
99|93
99|84
88|93
88|41
88|27
88|75
88|62
88|76
88|39
88|25
88|24
88|47
88|96
88|94
88|46
88|12
88|91
88|13
88|34
88|87
88|29
88|26
88|85
88|84
69|77
69|92
69|11
69|79
69|99
69|34
69|98
69|51
69|88
69|15
69|56
69|87
69|35
69|26
69|61
69|42
69|72
69|64
69|37
69|59
69|85
69|43
69|32
91|73
91|37
91|96
91|47
91|11
91|58
91|62
91|74
91|15
91|79
91|69
91|39
91|42
91|43
91|77
91|66
91|46
91|41
91|61
91|98
91|51
91|25
91|56
91|36
64|94
64|22
64|91
64|39
64|34
64|84
64|27
64|47
64|13
64|93
64|25
64|75
64|88
64|96
64|12
64|92
64|53
64|41
64|24
64|87
64|76
64|26
64|29
64|85
41|61
41|37
41|42
41|47
41|69
41|79
41|51
41|56
41|72
41|66
41|62
41|15
41|11
41|58
41|46
41|73
41|99
41|98
41|77
41|43
41|25
41|36
41|39
41|74
93|13
93|47
93|58
93|66
93|74
93|79
93|24
93|96
93|15
93|84
93|76
93|27
93|22
93|69
93|62
93|12
93|41
93|25
93|46
93|75
93|53
93|36
93|39
93|91
84|46
84|39
84|61
84|36
84|41
84|76
84|96
84|13
84|58
84|47
84|37
84|66
84|22
84|62
84|15
84|74
84|25
84|42
84|79
84|24
84|53
84|69
84|27
84|91
29|74
29|76
29|41
29|27
29|22
29|25
29|53
29|96
29|24
29|91
29|12
29|66
29|75
29|47
29|69
29|36
29|39
29|84
29|62
29|94
29|13
29|58
29|46
29|93
53|96
53|42
53|36
53|51
53|41
53|15
53|61
53|69
53|27
53|79
53|66
53|73
53|39
53|37
53|77
53|46
53|98
53|11
53|25
53|91
53|62
53|47
53|74
53|58
51|85
51|92
51|11
51|13
51|73
51|75
51|88
51|26
51|59
51|12
51|99
51|94
51|34
51|72
51|56
51|77
51|93
51|87
51|35
51|84
51|64
51|32
51|29
51|43
11|75
11|12
11|59
11|99
11|35
11|22
11|13
11|85
11|77
11|73
11|94
11|43
11|84
11|29
11|87
11|92
11|34
11|93
11|32
11|64
11|56
11|72
11|26
11|88
94|76
94|12
94|84
94|15
94|62
94|93
94|24
94|39
94|25
94|53
94|58
94|91
94|27
94|66
94|41
94|36
94|46
94|47
94|74
94|22
94|69
94|75
94|13
94|96
34|26
34|47
34|24
34|93
34|13
34|66
34|96
34|12
34|76
34|85
34|22
34|27
34|39
34|25
34|94
34|87
34|41
34|46
34|29
34|53
34|75
34|62
34|91
34|84
59|26
59|88
59|32
59|41
59|27
59|96
59|94
59|13
59|84
59|53
59|12
59|34
59|35
59|22
59|92
59|29
59|91
59|64
59|75
59|76
59|87
59|24
59|93
59|85
75|66
75|39
75|46
75|15
75|37
75|47
75|96
75|22
75|25
75|62
75|13
75|69
75|12
75|24
75|41
75|53
75|74
75|84
75|76
75|58
75|36
75|27
75|79
75|91
72|93
72|92
72|26
72|24
72|53
72|35
72|84
72|29
72|85
72|94
72|76
72|91
72|27
72|59
72|13
72|87
72|64
72|34
72|75
72|99
72|22
72|88
72|32
72|12
36|69
36|79
36|37
36|58
36|59
36|92
36|56
36|61
36|64
36|73
36|88
36|11
36|98
36|51
36|99
36|72
36|15
36|34
36|35
36|32
36|77
36|43
36|42
36|74
42|93
42|29
42|34
42|51
42|73
42|11
42|32
42|35
42|99
42|56
42|43
42|88
42|92
42|85
42|59
42|64
42|87
42|77
42|75
42|12
42|94
42|26
42|72
42|98
13|53
13|62
13|66
13|41
13|24
13|58
13|79
13|25
13|69
13|27
13|42
13|61
13|39
13|91
13|15
13|37
13|96
13|76
13|47
13|74
13|98
13|22
13|36
13|46
37|43
37|56
37|98
37|64
37|72
37|77
37|88
37|59
37|87
37|34
37|73
37|85
37|94
37|92
37|29
37|99
37|35
37|51
37|11
37|26
37|32
37|42
37|93
37|61
56|92
56|35
56|72
56|34
56|12
56|64
56|59
56|87
56|88
56|76
56|93
56|29
56|43
56|94
56|26
56|22
56|32
56|53
56|24
56|75
56|85
56|99
56|84
56|13
24|27
24|91
24|51
24|41
24|46
24|25
24|11
24|62
24|58
24|66
24|15
24|36
24|96
24|39
24|79
24|53
24|74
24|61
24|47
24|98
24|73
24|37
24|69
24|42
92|27
92|76
92|46
92|26
92|75
92|84
92|87
92|96
92|91
92|13
92|34
92|88
92|39
92|22
92|85
92|29
92|24
92|94
92|47
92|41
92|25
92|53
92|12
92|93
73|35
73|72
73|12
73|32
73|13
73|34
73|99
73|76
73|88
73|56
73|94
73|77
73|84
73|29
73|75
73|87
73|26
73|93
73|59
73|92
73|43
73|64
73|85
73|22
62|32
62|35
62|11
62|51
62|61
62|98
62|73
62|43
62|56
62|59
62|15
62|92
62|66
62|58
62|36
62|74
62|64
62|69
62|99
62|42
62|37
62|77
62|79
62|72
85|13
85|94
85|53
85|39
85|93
85|96
85|75
85|87
85|62
85|12
85|66
85|26
85|76
85|29
85|27
85|91
85|41
85|25
85|22
85|36
85|84
85|24
85|47
85|46
47|15
47|51
47|61
47|73
47|37
47|98
47|43
47|32
47|58
47|46
47|11
47|79
47|99
47|74
47|42
47|56
47|62
47|66
47|25
47|69
47|59
47|72
47|77
47|36
66|69
66|99
66|35
66|32
66|61
66|98
66|15
66|74
66|56
66|43
66|79
66|37
66|72
66|77
66|51
66|88
66|59
66|92
66|36
66|73
66|64
66|58
66|42
66|11
61|29
61|64
61|43
61|72
61|88
61|93
61|42
61|75
61|77
61|56
61|59
61|73
61|34
61|94
61|92
61|32
61|85
61|51
61|99
61|87
61|11
61|35
61|26
25|58
25|59
25|74
25|43
25|51
25|56
25|79
25|69
25|61
25|66
25|99
25|36
25|11
25|73
25|46
25|77
25|98
25|72
25|42
25|35
25|37
25|62
98|35
98|99
98|64
98|93
98|84
98|87
98|32
98|92
98|72
98|43
98|85
98|11
98|26
98|12
98|51
98|73
98|29
98|94
98|59
98|75
98|56
32|93
32|87
32|84
32|53
32|92
32|64
32|76
32|26
32|12
32|41
32|22
32|96
32|39
32|85
32|27
32|94
32|35
32|24
32|88
32|29
87|47
87|29
87|93
87|36
87|41
87|12
87|24
87|46
87|58
87|53
87|84
87|66
87|76
87|25
87|96
87|22
87|91
87|94
87|62
26|91
26|62
26|66
26|24
26|84
26|74
26|27
26|58
26|22
26|39
26|12
26|76
26|41
26|36
26|94
26|47
26|96
26|25
22|53
22|61
22|58
22|74
22|25
22|66
22|47
22|41
22|96
22|36
22|51
22|15
22|62
22|69
22|79
22|91
22|27
76|37
76|53
76|58
76|66
76|51
76|41
76|24
76|91
76|62
76|61
76|27
76|96
76|98
76|46
76|25
76|47
77|64
77|87
77|92
77|26
77|84
77|76
77|12
77|32
77|75
77|24
77|72
77|88
77|35
77|13
77|93
79|59
79|42
79|64
79|35
79|43
79|87
79|51
79|73
79|37
79|72
79|77
79|11
79|92
79|56
58|34
58|64
58|42
58|72
58|51
58|92
58|56
58|61
58|73
58|99
58|37
58|88
58|85
96|74
96|39
96|73
96|47
96|79
96|25
96|61
96|77
96|41
96|36
96|56
96|58
74|42
74|15
74|98
74|73
74|37
74|64
74|87
74|85
74|11
74|77
74|92
27|47
27|41
27|51
27|11
27|46
27|69
27|42
27|73
27|74
27|58
39|43
39|25
39|51
39|72
39|46
39|11
39|59
39|62
39|37
12|47
12|41
12|36
12|27
12|96
12|84
12|13
12|53
43|29
43|26
43|32
43|99
43|22
43|34
43|76
15|56
15|88
15|42
15|72
15|73
15|43
46|99
46|32
46|74
46|62
46|37
35|85
35|22
35|13
35|41
99|35
99|59
99|64
88|22
88|53
69|73"""

UPDATES2 = """92,88,34,85,87,26,29,94,93,75,12,84,13,22,76,24,53,27,91,41,39,47,25
84,13,22,76,27,91,39,47,46,58,74,79,61
62,47,41,22,75,96,93,25,24,66,76,36,94,84,53,13,29,74,39,27,12
51,77,99,32,35,34,26,93,84
75,36,13,58,74,93,22,84,24
56,36,42,64,79,98,92,32,77,69,43,59,66,11,99
98,56,72,35,92,88,87,26,94
87,76,75,12,13,72,59,43,35,85,88,32,64,93,77,26,34,92,22,84,94,56,29
96,41,47,12,94,39,29,24,66,91,84,76,27,36,93,22,46,13,75,53,58,26,25
27,32,91,87,59,94,24,99,85,29,12,64,75,92,13,22,53,93,35,88,34
87,26,29,94,75,12,84,13,22,76,53,91,96,41,39,25,46,66,36
13,27,24,22,53,59,34,72,88,99,35,29,92
69,35,74,61,15,98,32,79,88,85,11
94,91,88,13,12,53,64,47,24,29,39
29,94,46,75,12,27,62,36,84,41,26
32,35,64,92,88,34,85,87,26,29,94,93,75,12,84,13,22,76,24,53,27,96,41
79,37,61,42,98,51,11,73,77,56,72,99,59,32,35,64,92,88,34,85,87,26,29
77,56,99,59,32,35,64,92,88,34,85,87,26,29,75,12,84,13,76
73,43,72,59,32,35,64,92,34,85,93,75,12,84,13
91,25,15,66,24,47,58,69,37,46,62,41,76,79,96,74,53,98,27,61,42,36,22
35,64,92,85,87,26,94,93,75,12,84,22,76,53,39
75,74,24,22,58,79,62,47,96
53,36,27,84,93,66,46,13,25,47,62,41,87,91,39,22,75
79,37,61,42,98,51,11,73,56,43,72,99,59,32,35,64,92,88,34,85,87,26,29
74,69,15,79,37,61,42,98,51,11,73,77,56,72,99,59,35,64,92,88,85
96,39,46,94,22,29,76,88,47,41,27,13,25,34,12,85,26,93,91
79,98,64,85,26
47,25,46,62,66,58,69,15,79,37,61,42,98,11,56,43,72,99,59
91,41,39,47,62,74,15,79,42,51,11,73,56
64,98,72,99,61,56,32,92,35,34,42,74,73,69,59,11,58,37,43
98,11,43,72,99,32,88,34,26
56,32,58,11,73,15,42,37,64,61,66,35,74,99,92,79,36,69,98,43,77
94,93,87,75,84,53,85,27,12
37,51,35,64,34
22,76,24,27,91,96,41,46,62,66,69
39,25,15,79,37,56,43
59,32,35,64,92,88,34,85,87,29,94,93,75,12,84,13,22,76,24,53,27,91,96
42,98,51,11,73,77,56,43,72,99,59,32,35,64,92,88,85,87,26,29,94,93,75
64,92,88,34,85,87,29,93,12,84,13,22,24,53,27,91,96
25,46,62,66,36,58,74,69,15,79,37,61,42,98,51,11,73,77,56,43,72,99,32
88,75,96,41,76,85,53
87,34,25,46,84,96,29,91,93,47,12,62,26,76,27,94,75,85,13,41,24
84,91,47,66,69,79,61
22,76,24,53,27,91,96,41,39,25,46,62,66,36,58,74,69,15,37,61,98
27,96,41,39,47,25,46,66,36,58,74,69,15,79,37,61,42,98,11,73,77
76,84,46,47,91,41,12,39,79,53,15,37,96,24,69
47,62,66,74,15,61,42,77,59
41,53,51,36,91,62,37,39,69,73,61,74,27,58,42,66,79,47,25,11,46
56,43,72,99,59,32,35,64,92,34,85,87,26,29,94,93,12,84,13,76,24
25,62,58,74,69,15,61,42,51,77,43,72,99,59,32
73,58,98,62,25,69,15,61,43,66,77,47,96,46,36
22,76,24,27,91,96,41,39,25,46,62,36,74,69,79,37,61
22,76,24,53,27,91,96,39,25,46,62,66,36,74,15,79,37,61,42
37,15,77,79,51,39,61,27,47,98,91,66,25,74,62
87,26,29,94,27,41,47,25,46
77,87,73,42,43,56,29,34,59,37,35,94,51
84,36,93,46,69,12,53
64,87,35,15,69,42,88
75,26,76,84,64,94,59,88,12,92,27,53,93,35,32
88,87,29,84,13,22,24,27,41,39,46
76,24,27,91,96,41,39,47,25,46,66,36,58,74,69,15,37,61,42,98,51
12,13,22,53,27,91,96,47,25,62,66,36,58,74,69,15,37
69,79,37,42,51,11,73,77,99,59,32,34,87
13,22,76,24,53,27,91,96,41,39,47,25,46,66,36,58,74,69,15,79,37,61,42
64,93,34,29,92,61,99
13,91,84,75,41,26,94,87,27,88,64,24,29,53,76,85,34
26,93,77,88,34,75,22,43,32,73,59,87,92,35,99
47,41,74,93,46,12,53,94,69,76,62,22,36
29,53,24,64,43,34,12
42,98,51,32,35,11,56,69,64,77,73,92,72,79,99,59,88,15,61,85,43
12,62,91,46,93,39,96,58,76,53,25,69,36,13,15,66,27
47,46,66,58,74,69,15,37,61,98,51,11,73,77,43,99,59
76,53,96,41,25,66,58,74,79,42,51
47,66,58,74,37,11,73
85,29,94,13,46,62,66
24,53,36,58,15,37,11
51,39,98,58,69,11,43,56,15,72,79,37,46,25,74,36,61,62,77,99,42,66,47
27,41,26,39,75,34,88,29,85,24,94,35,64,84,96,91,53,92,87
53,27,91,47,46,58,74,15,79,61,42,98,73
37,42,98,51,73,77,56,43,72,99,59,32,35,64,88,34,85,87,26,29,94
64,85,94,93,12,76,91,41,47
51,11,73,77,56,43,99,59,35,64,92,34,85,87,94,93,75,12,84
74,25,27,62,22,41,84,12,36,96,39,29,91,76,24,94,46
64,34,59,35,11,99,51,84,12
84,76,27,39,69
61,79,73,56,87,37,85,32,99
94,72,76,32,24,93,43
76,24,53,27,91,96,41,39,47,25,46,62,66,36,58,74,69,15,79,37,61,98,51
22,41,88,24,87,64,92,47,12
25,77,96,41,42,69,74
43,72,99,59,32,35,92,88,87,26,29,94,12
25,66,74,69,79,98,51,73,56,43,72,99,32
24,58,94,47,22,66,76,41,53,75,27,39,36,46,96,84,62,29,91
15,46,99,72,79,36,39,37,56,66,77
59,64,32,87,93,77,75,99,85,51,12,88,72,92,34,98,43
24,11,66,58,39,53,61,41,47
77,43,72,99,59,64,92,88,85,87,26,29,94,93,75,12,84,13,22
47,62,66,36,58,74,69,79,37,56,72,99,59
15,64,88,87,99,92,98,85,34,69,79,77,61,72,59,51,11,35,56
84,13,22,76,24,53,41,39,47,25,46,66,36,58,74,69,79,37,61
64,92,88,85,53,96,41
94,87,12,56,59,99,11,93,88,75,13,72,77
64,92,29,93,59,87,34,91,26,12,84,94,88,24,76,75,27,35,53,22,96,32,13
87,26,29,93,75,12,84,13,76,24,53,27,91,96,41,39,47,46,62,66,36
85,98,43,61,77,34,29,59,11,35,72,99,73,93,32,51,42
37,61,51,73,77,43,72,99,64,92,88,34,94
87,12,93,46,84,62,25,13,96,66,39,94,36,24,22
69,58,24,61,47,66,22,74,25,46,96,41,62,91,37,98,27,79,36,53,39,15,42
74,53,96,93,13,91,46,84,25,75,58,12,39
84,43,53,64,85,26,12,72,92
29,85,77,34,51,93,61,42,92
73,77,43,72,59,32,35,64,88,34,87,93,12,13,22
36,79,37,42,51,72,88
84,13,22,76,24,53,27,25,46,62,66,36,58,15,79,37,61
79,37,61,42,98,51,11,77,56,43,59,32,35,64,92,88,34,85,87,26,29
39,47,25,62,66,79,61,42,98,51,11,73,77,43,99
42,77,51,79,59,99,61,36,11,64,66,58,56,73,43,62,35,72,32,15,37
25,12,39,53,47
15,51,58,42,37,56,72,35,92,98,43,59,99,74,36,32,61,77,79
29,61,59,11,43,51,42,64,26,32,93
34,94,13,53,91,25,62
37,51,87,92,35,56,64,34,72,29,61,26,73,88,43
22,93,76,13,35,72,12,64,94,87,88,26,59,85,27,32,75,92,99,53,29
59,74,61,77,35,98,79,34,37,58,56
39,36,53,62,27
61,35,73,59,92
85,87,26,93,75,12,84,22,76,24,41,25,66
62,15,73,58,74,37,43,56,41,79,42,51,66,11,47,69,98,36,46,77,96
77,56,72,99,32,35,87,29,94,93,75,84,76
46,66,36,58,69,15,79,37,42,98,51,11,73,77,56,43,72,99,59,32,35
91,96,41,25,46,62,66,36,58,74,69,15,79,61,42,98,51,11,56
85,26,94,84,24,53,66
51,79,42,37,59,58,61,47,72,99,36,73,98,43,69
92,87,26,29,75,84,22,76,24,39,25
25,74,15,37,73
72,77,73,61,59,35,69,43,56,66,92,42,79
27,91,96,41,39,47,25,46,62,66,36,58,74,69,15,79,37,98,51,11,73
66,79,42,98,43,72,99,59,32
59,32,87,29,94,84,13,22,76,53,27
42,98,51,11,73,77,56,43,72,59,32,35,64,92,88,34,85,87,26,29,94,93,75
79,37,61,98,51,73,77,56,43,72,99,59,32,35,64,92,88,34,85,87,26
11,56,72,32,35,92,85,26,93,75,12
22,29,13,56,24,88,92
92,88,87,29,94,75,22,76,24,96,25
26,12,87,35,41,32,84,75,76,64,93,85,22
64,88,94,13,22,76,27,91,41
75,22,76,53,41,39,25,36,79
35,64,88,87,26,29,93,75,84,13,22,91,96
84,13,22,53,91,47,46,62,58,74,79,37,61
91,96,25,46,66,36,69,79,37,77,56
75,13,22,96,39,47,74,69,79
79,11,73,77,56,59,34,85,87,26,29
87,26,29,94,93,75,12,13,22,76,24,53,27,91,96,41,39,47,25,46,62,66,36
56,43,72,99,59,88,34,85,87,26,29,94,12
15,79,42,98,11,73,77,56,99,35,92,34,85,87,26
32,36,58,73,69,51,74,59,61,56,98,35,66,11,37,15,42,46,79,43,62
76,24,53,27,96,41,47,25,46,62,66,36,58,74,69,15,79,61,42,98,51
53,47,25,74,15,61,73
98,15,11,37,72,61,66,36,79,56,74,59,51,64,35,69,99
39,25,62,36,15,79,42,98,11,73,43,72,99
76,13,87,22,29
27,29,84,24,93,76,66,74,46,62,39,94,91
99,88,34,94,13,22,91
98,73,99,64,92,85,12
64,34,29,75,96,41,47
12,22,76,53,96,39,47,66,74,69,37
75,12,76,53,91,39,47,66,36,15,79
26,29,93,12,84,13,22,76,24,96,41,47,25,46,62,36,58
27,58,37,77,46,39,25,11,15,69,41,51,98
93,75,12,22,76,27,91,96,41,39,47,25,46,62,66,36,74,69,15
24,53,27,41,47,74,69,79,11
37,42,11,99,85
42,98,11,73,77,56,43,72,99,59,32,35,64,92,88,34,85,87,26,29,94,93,75
99,62,66,72,79,61,11,74,58,42,69,39,36,37,98,46,51,73,56,15,25
75,12,13,41,39,66,69
27,22,75,26,29,91,94,85,62,41,93
98,61,37,77,42,32,11,34,87,85,79,73,88,43,59,56,69,15,35
72,35,26,94,12
47,56,62,15,98,39,79,42,41,77,46,69,43,51,36,37,61,72,74
98,32,69,61,99,64,77,34,42,56,79,43,74,15,35,92,11,58,37
13,34,91,39,12,84,24,29,53,76,88,25,27,93,75,22,92,26,94
42,51,11,73,77,56,43,99,59,32,35,64,92,88,34,85,87,26,29,94,75
27,91,39,46,58,74,69,15,79,61,42
74,15,37,51,11,73,99,59,35
88,32,37,87,15,61,98,85,26,11,92,64,43
76,27,91,58,79
88,99,98,56,61,74,15,43,36,72,92
37,61,98,11,99,35,64,92,87,29,94
73,77,56,43,64,92,85
27,29,96,76,75,87,39,88,91,24,47,64,34
42,51,64,87,29,93,75
85,87,93,99,35,72,42,51,32,73,29,26,98,88,64,34,59,11,75,94,92
75,12,13,22,76,24,27,91,41,47,66,36,58,74,15
88,34,85,87,26,29,94,93,75,12,84,13,76,24,53,27,91,96,41,39,47,25,46
12,87,46,22,53,91,88
74,79,37,42,51,11,73,77,56,43,72,99,35,64,85
15,56,77,37,88,64,35,51,11,32,72,34,73,43,59,42,69,79,99,74,98
84,13,24,53,91,25,46,66,69,37,61
35,87,84,12,13,88,77,93,72,43,32,92,29,73,34,22,94,85,26
99,74,69,34,58,35,56,42,15,64,61,88,98,77,43
77,56,43,72,59,32,92,34,85,87,26,29,93,75,84,13,76
87,51,72,11,73,37,34,15,42,85,99,77,35"""


def check_if_good_order_update(update, orders_before, orders_after):
    nb_pages = len(update)
    for i in range(nb_pages):
        # After check
        # is_after_checked = True if set(update_pages_sequence[i + 1:]).intersection(set(update_pages_sequence)) == set(update_pages_sequence[i + 1:]) else False
        # if i < nb_pages:
        #     for value in update[i+1:]:
        #         is_good_order = value in orders_after[update[i]]

        #         if not is_good_order:
        #             return False

        # Ci dessus ne sert à rien                
        # # Before check
        for value in update[:i]:
            is_good_order = value in orders_before[update[i]]
                
            if not is_good_order:
                return False
        
    return True


def reorder(update, orders_before, orders_after):
    list = [update[0]]
    for new_value in update[1:]:
        # Il faudrait en fait faire une classe
        index_to_insert = 0
        for i, value in enumerate(list):
            if value in orders_before[new_value]:
                index_to_insert = i + 1
            else:
                break
        list.insert(index_to_insert, new_value)

    # print("Before:", update)
    # print("After: ", list)
    # print(list[len(list)//2])
    return list[len(list)//2] 

# Pour la deuxième partie le bubble sort aurait pu fonctionné, c'est ce qu'ont fait les camarades


        




if __name__ == "__main__":
    orders_before = defaultdict(list)
    orders_after = defaultdict(list)

    for order in ORDERS2.split("\n"):
        pages = order.split("|")
        orders_before[int(pages[1])].append(int(pages[0]))
        orders_after[int(pages[0])].append(int(pages[1]))

    count = 0
    count2 = 0
    for line in UPDATES2.split("\n"):
        update = [int(number) for number in line.split(",")]
        is_good_order_update = check_if_good_order_update(update, orders_before, orders_after)
        # print(update, is_good_order_update)

        if is_good_order_update:
            count += update[len(update)//2]

        else:
            count2 += reorder(update, orders_before, orders_after)
            # new_update = reorder(update, orders_before, orders_after)
            # count2 += new_update[len(new_update)//2]

    print(count)
    print(count2)
        
            
# On pourrait aussi reconstruire le livre