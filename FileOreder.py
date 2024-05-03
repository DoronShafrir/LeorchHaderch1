import pandas as pd
import openpyxl





class Order:
    def __init__(self):
        self.gen = pd.read_csv("General2023C.csv", parse_dates=[0], encoding='iso-8859-8')

        self.Jan = pd.DataFrame(columns=self.gen.columns)
        self.Feb = pd.DataFrame(columns=self.gen.columns)
        self.Mar = pd.DataFrame(columns=self.gen.columns)
        self.Apr = pd.DataFrame(columns=self.gen.columns)
        self.May = pd.DataFrame(columns=self.gen.columns)
        self.Jun = pd.DataFrame(columns=self.gen.columns)
        self.Jul = pd.DataFrame(columns=self.gen.columns)
        self.Aug = pd.DataFrame(columns=self.gen.columns)
        self.Sep = pd.DataFrame(columns=self.gen.columns)
        self.Oct = pd.DataFrame(columns=self.gen.columns)
        self.Nov = pd.DataFrame(columns=self.gen.columns)
        self.Dec = pd.DataFrame(columns=self.gen.columns)

        # self.months = {
        #     1 : 'Jan',
        #     2 : self.Feb,
        #     3 : self.Mar,
        #     4 : self.Apr,
        #     5 : self.May,
        #     6 : self.Jun,
        #     7 : self.Jul,
        #     8 : self.Aug,
        #     9 : self.Sep,
        #     10 : self.Oct,
        #     11 : self.Nov,
        #     12 : self.Dec
        # }

    def seperate_lines(self):
        for i, r in self.gen.iterrows():
            month_number = r['תאריך'].month
            self.add_line(r, month_number )



    def add_line(self, line, month):
        if month == 1:
             # self.Jan = self.Jan.append(line, ignore_index=True)
            self.Jan = pd.concat([self.Jan, line])
            # print(self.Jan)
        # elif month == 2:
        #     self.Feb = self.Feb.append(line, ignore_index=True)
        # elif month == 3:
        #     self.Mar = self.Mar.append(line, ignore_index=True)
        # elif month == 4:
        #     self.Apr = self.Apr.append(line, ignore_index=True)
        # elif month == 5:
        #     self.May = self.May.append(line, ignore_index=True)
        # elif month == 6:
        #     self.Jun = self.Jun.append(line, ignore_index=True)
        # elif month == 7:
        #     self.Jul = self.Jul.append(line, ignore_index=True)
        # elif month == 8:
        #     self.Aug = self.Aug.append(line, ignore_index=True)
        # elif month == 8:
        #     self.Aug = self.Aug.append(line, ignore_index=True)
        # elif month == 9:
        #     self.Sep = self.Sep.append(line, ignore_index=True)
        # elif month == 10:
        #     self.Oct = self.Oct.append(line, ignore_index=True)
        # elif month == 11:
        #     self.Nov = self.Nov.append(line, ignore_index=True)
        # elif month == 12:
        #     self.Dec = self.Dec.append(line, ignore_index=True)

    def create_file(self):
        self.Jan.to_csv("Jan.csv", encoding='iso-8859-8')




if __name__ == "__main__":
    nava = Order()
    nava.seperate_lines()
    nava.create_file()