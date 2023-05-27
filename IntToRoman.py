def intToRoman(num):
    m = ["", "M","MM", "MMM", "MMMM"]
    c = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC","DCCC","CM"]
    x = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
    i = ["", "I","II","III","IV","V","VI","VII","VIII","IX"]
    
    thousands = m[num//1000]
    hundreds = c[(num%1000)//100]
    tens = x[(num%100)//10]
    ones = i[num%10]
    ans = (thousands+hundreds+tens+ones)
    print(ans)

intToRoman(5)
intToRoman(4137)
intToRoman(123)
