def drop_first_last(grades):
    first, *middle, last = grades
    avg = sum(middle) / len(middle)
    print(avg)

drop_first_last([87, 90, 78, 43, 21])
drop_first_last([87, 90, 78, 43, 21, 555, 44])