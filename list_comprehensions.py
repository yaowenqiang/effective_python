matrix = [[1,2,3], [4,5,6], [7,8,9]]
flat = [x for row in matrix for x in row]
print(flat)

squared = [[x ** 2 for x in row] for row in matrix]
print(squared)


three_matrix = [
    [
        [
            1,2,3,
        ],
        [
            4,5,6,
        ]
    ],
    [
        [
            7,8,9,
        ],
        [
            10,11,12,
        ]
    ]
]

flat3 = [x for sublist1 in three_matrix
         for sublist2 in sublist1
         for x in sublist2
         ]

print(flat3)


flat_list = []

for sublist1 in three_matrix:
    for sublist2 in sublist1:
        flat_list.extend(sublist2)

print(flat_list)


b = [x for x in flat_list if x > 4 and x % 2 ==0]
c = [x for x in flat_list if x > 4 if x % 2 ==0]
print(b)
print(c)


filtered_matrix = [[x for x in row if x % 3 == 0]
                   for row in matrix if sum(row) >= 10
                   ]

print(filtered_matrix)



c = list(range(100))
d = [x for x in c if x % 2 == 0 if x % 3 == 0]
print(d)




