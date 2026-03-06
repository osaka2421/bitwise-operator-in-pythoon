##strings and operation 
str1= "hii osaka \n c , c++"#3 \n for next line 
print(str1)
str2= "hii a \t z"## use for tab \t
print(str2)
## opeartion 
# concatenation
print(str1 + str2)
print(len(str1+str2))# len is fuction use to calu the length of the string not just chara also empty space 
# indexing means postion of chara we can have the position of particular chara even empty spec
str3 = "saransh clg"
print(str3[0])
#slicing
# negative index
# slicing means divding the index i part it also inlucles the empty part 
str4= "dic mic"
print(str4[3:7])
print(str4[-0:-2])       # reverse index
##fuctionin string 
# end with : privde the ending word of string
str="i am studying python from github"
print(str.endswith("hub"))

# funtion 2 capitlize use to capital the frist word of the strins
print(str.capitalize())
str = print(str.capitalize())


# replace use to replace the value in string to new val
print(str.replace("a","O"))

# find use to find th index of search val
print(str.find("a"))

# count use to cout the word or chara from the string
print(str.count("h"))


# take a name from input and print its len
str6 =input("enter your name:")

print(len(str6))

# count th $
str7= " i am the $programmer of $python"
print(str7.count("$"))

