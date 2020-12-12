def nth_num(arr)
    if(arr.length()<3)
        return 0
    end

    puts arr[2]
    arr.shift(3)
    return nth_num(arr)
    


end

nth_num([1, 2, 3, 4, 5, 6, 7, 8, 9])

#prints the third element of an array
#slice off the first three elements of the array
#recursively repeat