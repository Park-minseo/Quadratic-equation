import math

a=float(input("x²의 계수를 입력하세요: "))
b = float(input("x의 계수를 입력해주세요: "))
c = float(input("상수항의 계수를 입력해주세요: "))
근1 = 근2 = 0
판별식 = b ** 2 - 4 * a * c

def 근의공식1(a, b, c):
    근1= (b*-1) + math.sqrt(판별식) / 2*a
    return 근1
def 근의공식2(a, b, c):
    근2= (b*-1) - math.sqrt(판별식) / 2*a
    return 근2

if 판별식 >= 0:
    근1=근의공식1(a,b,c)
    근2=근의공식2(a,b,c)
    if a==1:
        if b==1:
            if 판별식 == 0:
                print("x²+x{0:+}=0의 근은 {1}".format(c, 근1))
            else:
                print("x²+x{0:+}=0의 근은 {1}, {2}".format(c, 근1,근2))
        else:
            if 판별식 == 0:
                print("x²{0:+}x{1:+}=0의 근은 {2}".format(b,c, 근1))
            else:
                print("x²{0:+}x{1:+}=0의 근은 {2}, {3}".format(b,c, 근1,근2))
    else:
        if b==1:
            if 판별식 == 0:
                print("{0}x²+x{1:+}=0의 근은 {2}".format(a,c,근1))
            else:
                print("{0}x²+x{1:+}=0의 근은 {2}, {3}".format(a,c,근1,근2))
        else:
            if 판별식 == 0:
                print("{0}x²{1:+}x{2:+}=0의 근은 {3}".format(a,b,c, 근1))
            else:
                print("{0}x²{1:+}x{2:+}=0의 근은 {3}. {4}".format(a,b,c, 근1,근2))
elif b ** 2 -4 * a* c < 0:
    print("허근은 해당 프로그램에서 지원되지 않습니다.")


