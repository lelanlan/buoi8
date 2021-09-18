# Medium [1] Anagram Number:
#Viết hàm anagram_number() có đầu vào là một số nguyên và trả ra True nếu sau khi đảo ngược thứ tự các chữ số của số đó vẫn cho ta số ban đầu. Trả ra False nếu không giống.
def anagram_number(num):
    strnumber=str(num)
    str_reversenum = strnumber[::-1]
    reversenum = int(str_reversenum)
    if(num==reversenum):
        return True
    else:
        return False

print(anagram_number(1254))
print(anagram_number(121121))