import random

class player:
    def __init__(self, name):
        self.name = name
        self.rows = {
        "row 1": [0, 0, 0],
        "row 2": [0, 0, 0],
        "row 3": [0, 0, 0]
        }
        
    
    def print_rows(self):
        for row in self.rows:
            print(f"{row}: {self.rows[row]}")
        return

    def roll(self):
        die = random.randint(1,6)
        return die
  
    
    def assign(self, die_value=1):
        empty_rows =[]
        for row in self.rows:
            for die in self.rows[row]:
                if die == 0:
                    empty_rows.append(row)
                    break
        while True:
            print("")
            self.print_rows()
            print("")
            selected_row = input(f'Which row would you like to place the die in? ({empty_rows})').strip().lower()
            print(selected_row)

            if selected_row in empty_rows:
                for i in range(len(self.rows[selected_row])):
                    if self.rows[selected_row][i] == 0:
                        print(f"Index {i}")
                        self.rows[selected_row][i] = die_value
                        print(self.rows[selected_row])
                        return  # Exit the loop once a valid row is found and die is assigned
            else:
                print("Incorrect row selected, please try again.")

                         
test = player("Test")
test.assign()
test.print_rows()