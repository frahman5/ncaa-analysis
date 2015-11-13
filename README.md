# ncaa-analysis

### Naming Conventions for Teams

Let the four brackets be called A, B, C, D. 

## Round of 64 through Elite 8
A-x-..-z is the winner of the games played between x-..-z in conference A. e.g A-1 is the 1 seed in conference A.
A-1-16 is the winner of the game played between A-1 and A-16. A-1-16-8-9 is the winner of the games played between
A-1-16 and A-8-9. etc...

## Final four on
AW = Winner of A Bracket. BW = Winner of B Bracket. CW = Winner of C Bracket. DW = Winner of D Bracket. 
ABW = Winner between AW, BW. CDW = Winner between CW, DW. 
W = Overall Winner. 

## The teams participating in each of the 63 games are as follows:

Game | Teams
-----| -----
0    | (A-1, A-16)
1    | (A-8, A-9)
2    | (A-5, A-12)
3    | (A-4, A-13)
4    | (A-6, A-11)
5    | (A-3, A-14)
6    | (A-7, A-10)
7    | (A-2, A-15)
8    | (A-1-16, A-8-9)
9    | (A-5-12, A-4-13)
10   | (A-6-11, A-3-14)
11   | (A-7-10, A-2-15)
12   | (A-1-16-8-9, A-5-12-4-13)
13   | (A-6-11-3-14, A-7-10-2-15)
14   | (A-1-16-8-9-5-12-4-13, A-6-11-3-14-7-10-2-15)
15   | (B-1, B-16)
16   | (B-8, B-9)
17   | (B-5, B-12)
18   | (B-4, B-13)
19   | (B-6, B-11)
20   | (B-3, B-14)
21   | (B-7, B-10)
22   | (B-2, B-15)
23   | (B-1-16, B-8-9)
24   | (B-5-12, B-4-13)
25   | (B-6-11, B-3-14)
26   | (B-7-10, B-2-15)
27   | (B-1-16-8-9, B-5-12-4-13)
28   | (B-6-11-3-14, B-7-10-2-15)
29   | (B-1-16-8-9-5-12-4-13, B-6-11-3-14-7-10-2-15)
30   | (C-1, C-16)
31   | (C-8, C-9)
32   | (C-5, C-12)
33   | (C-4, C-13)
34   | (C-6, C-11)
35   | (C-3, C-14)
36   | (C-7, C-10)
37   | (C-2, C-15)
38   | (C-1-16, C-8-9)
39   | (C-5-12, C-4-13)
40   | (C-6-11, C-3-14)
41   | (C-7-10, C-2-15)
42   | (C-1-16-8-9, C-5-12-4-13)
43   | (C-6-11-3-14, C-7-10-2-15)
44   | (C-1-16-8-9-5-12-4-13, C-6-11-3-14-7-10-2-15)
45   | (D-1, D-16)
46   | (D-8, D-9)
47   | (D-5, D-12)
48   | (D-4, D-13)
49   | (D-6, D-11)
50   | (D-3, D-14)
51   | (D-7, D-10)
52   | (D-2, D-15)
53   | (D-1-16, D-8-9)
54   | (D-5-12, D-4-13)
55   | (D-6-11, D-3-14)
56   | (D-7-10, D-2-15)
57   | (D-1-16-8-9, D-5-12-4-13)
58   | (D-6-11-3-14, D-7-10-2-15)
59   | (D-1-16-8-9-5-12-4-13, D-6-11-3-14-7-10-2-15)
60   | (AW, BW)
61   | (CW, DW)
62   | (ABW, CDW)
------------------------------------------------------

### Bracket Conventions
Each bracket t is a length 63 tuple where t[x] is the index of the winner of the xth (zero-indexed) game of the NCAA tournament. 
For example, t[47] = 0 indicates that D-5 won the 47th game of a tournament. 
t[x] is either 0 or 1 for every x in between 0 and 62.
"""

## Sample bracket
sample = (0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 
          0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0)  
