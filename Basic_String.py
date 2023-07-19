astring = "hello world"
print(astring.index("o"))
print(astring[3:7:2])
print(astring[::-1])

s = "Hey there! what should this string be"
print("length of s = %d" % len(s))
print("the first a should occurrence of the letter a = %d" % s.index("a"))
print("the count of a is %d" % s.count("a"))

print("the fifth of char is %s" % s[0:5])
print("the last five char is %s" % s[-5:])

numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]
for number in numbers:
    if number == 237:
        numbers = [
            951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
            615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
            386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
            399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
            815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
            958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
            743, 527
        ]
        break
    else:
        print(number)

def list_benefits():
    return ["More organized code", "More readable code", "Easier code reuse"]

def build_sentence(benefit):
    return "%s is a benefit of function" % benefit

def name_of_benefit():
    list_benefit = list_benefits()
    for benefit in list_benefit:
        print(build_sentence(benefit))
name_of_benefit()