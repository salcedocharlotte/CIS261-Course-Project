# Week 8 Rectangle Application - Charlotte Payan-Salcedo

from dataclasses import dataclass

@dataclass
class Rectangle:
    # Class representing a rectangle with height and width
    height: int
    width: int

    def getPerimeter(self):
        # Calculate and return the perimeter of the rectangle
        perimeter = 2 * self.height + 2 * self.width
        return perimeter

    def getArea(self):
        # Calculate and return the area of the rectangle
        area = self.height * self.width
        return area

    def getStr(self):
        # Generate and return a string representing the rectangle shape
        s = ""
        w = "*" * self.width + "\n"
        s += w
        for i in range(self.height - 2):
            s += "*" + " " * (self.width - 2) + "*\n"
        s += w
        return s

def main():
    # Main function to run the rectangle application
    print("Rectangle Calculator")
    print()

    again = "y"
    while again.lower() == "y":
        height = int(input("Height: "))
        width = int(input("Width: "))

        rectangle = Rectangle(height, width)
        print("Perimeter:", rectangle.getPerimeter())
        print("Area:", rectangle.getArea())
        print(rectangle.getStr())

        again = input("Continue? (y/n): ").lower()
        print()
    print("Bye!")

if __name__ == "__main__":
    main()
