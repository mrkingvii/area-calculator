print("=========================================================")
print("Select function")
print("A. Find the perimeter")
print("B. Find the area")

choice = input("Please select what you want to do: ")
print("=========================================================")

if choice == "A":
    print("Select shape")
    print("A. Triangle △")
    print("B. Square ⃞")
    print("C. Rectangle ▭")
    print("D. Trapezoid ⏢")
    print("E. Circle ◯")

    choice_p = input("Please select what shape you want to find the perimeter: ")
    print("=========================================================")

    if choice_p == "A":
        print("Please input the lengths of the sides of the triangle")
        l_tri1 = float(input("Length 1: "))
        l_tri2 = float(input("Length 2: "))
        l_tri3 = float(input("Length 3: "))
        P_Tri = l_tri1 + l_tri2 + l_tri3
        print("=========================================================")
        print(f"△ The perimeter of your triangle is {P_Tri} △")
        print("=========================================================")
    elif choice_p == "B":
        print("Please input the length of the sides of the square")
        l_sq1 = float(input("Length of the square: "))
        P_sq = l_sq1 * 4
        print("=========================================================")
        print(f"⃞ The perimeter of your square is {P_sq} ⃞")
        print("=========================================================")
    elif choice_p == "C":
        print("Please input the lengths of the sides of the Rectangle")
        l_rec1 = float(input("Length of the rectangle: "))
        l_rec2 = float(input("Height of the rectangle: "))
        P_rec = 2 * (l_rec2 + l_rec1)
        print("=========================================================")
        print(f"▭ The perimeter of your rectangle is {P_rec} ▭")
        print("=========================================================")
    elif choice_p == "D":
        print("Please input the lengths of the sides of the Trapezoid")
        l_trp1 = float(input("Length 1: "))
        l_trp2 = float(input("Length 2: "))
        l_trp3 = float(input("Length 3: "))
        l_trp4 = float(input("Length 4: "))
        P_Trp = l_trp1 + l_trp2 + l_trp3 + l_trp4
        print("=========================================================")
        print(f"⏢ The perimeter of your Trapezoid is {P_Trp} ⏢")
        print("=========================================================")
    elif choice_p == "E":
        print("please input the radius of the Circle")
        r_circ = float(input("radius of the Circle: "))
        p_circ = 2 * (22 / 7) * r_circ
        print("=========================================================")
        print(f"◯ The perimeter of your Circle is {p_circ} ◯")
        print("=========================================================")
    else:
        print("Invalid shape choice.")
elif choice == "B":
    print("Select shape")
    print("A. Triangle △")
    print("B. Square ⃞")
    print("C. Rectangle ▭")
    print("D. Trapezoid ⏢")
    print("E. Circle ◯")

    choice_a = input("Please select what shape you want to find the area: ")
    print("=========================================================")

    if choice_a == "A":
        print("Please input the height and the base value of your triangle")
        a_tri_c = float(input("base length of the triangle: "))
        a_tri_h = float(input("height of the triangle: "))
        a_tri = (1 / 2) * a_tri_c * a_tri_h
        print("=========================================================")
        print(f"△ area of the triangle is {a_tri} △")
        print("=========================================================")
    elif choice_a == "B":
        print("Please input the length of the sides of the square")
        a_sq_l = float(input("Length : "))
        a_sq = a_sq_l ** 2
        print("=========================================================")
        print(f"⃞ area of the square is {a_sq} ⃞")
        print("=========================================================")
    elif choice_a == "C":
        print("Please input length and height of the rectangle")
        a_rec_l = float(input("length of the rectangle: "))
        a_rec_h = float(input("height of the rectangle: "))
        a_rec = a_rec_h * a_rec_l
        print("=========================================================")
        print(f"▭ area of the rectangle is {a_rec} ▭")
        print("=========================================================")
    elif choice_a == "D":
        print("Please enter length of the base 1, base 2 and the height")
        a_trp_a = float(input("Length of the base 1: "))
        a_trp_b = float(input("Length of the base 2: "))
        a_trp_h = float(input("Height of the Trapezoid: "))
        a_trp = ((a_trp_a + a_trp_b) / 2) * a_trp_h
        print("=========================================================")
        print(f"⏢ area of the Trapezoid is {a_trp} ⏢")
        print("=========================================================")
    elif choice_a == "E":
        print("Please enter the radius of the Circle")
        a_crc_r = float(input("Radius of the Circle:"))
        a_crc = (22 / 7) * a_crc_r ** 2
        print("=========================================================")
        print(f"◯ the area of the Circle is {a_crc} ◯")
        print("=========================================================")
    else:
        print("Invalid shape choice.")
else:
    print("Invalid function choice.")
