class Result:
    def calculate(self, m1, m2, m3=0):
        total = m1 + m2 + m3

        if m3 == 0:
            average = total / 2
        else:
            average = total / 3

        print("Total Marks:", total)
        print("Average:", average)


# Creating object
r = Result()

# Two subjects
print("Two Subjects:")
r.calculate(80, 90)

# Three subjects
print("Three Subjects:")
r.calculate(80, 90, 70)