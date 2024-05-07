import pandas as pd
import openpyxl





class Order1:
    def __init__(self):
        self.gen = pd.read_csv("General2023.csv", parse_dates=[0], dayfirst=True,  encoding='iso-8859-8')
        self.gen['תאריך'] = self.gen['תאריך'].dt.date

        self.Jan = pd.DataFrame()
        self.Feb = pd.DataFrame()
        self.Mar = pd.DataFrame()
        self.Apr = pd.DataFrame()
        self.May = pd.DataFrame()
        self.Jun = pd.DataFrame()
        self.Jul = pd.DataFrame()
        self.Aug = pd.DataFrame()
        self.Sep = pd.DataFrame()
        self.Oct = pd.DataFrame()
        self.Nov = pd.DataFrame()
        self.Dec = pd.DataFrame()

        self.months = [self.Jan, self.Feb, self.Mar, self.Apr, self.May, self.Jun, self.Jul, self.Aug, self.Sep, self.Oct, self.Nov, self.Dec ]


    # def seperate_lines(self):
    #     for i, line in self.gen.iterrows():
    #         month_number = line['תאריך'].month
    #         line = pd.DataFrame(line, index=self.gen.columns)
    #         self.months[month_number - 1] = pd.concat([self.months[month_number - 1], line], axis=1)
    #         print(self.months[month_number].info)

            # self.add_line(r, month_number )

    def seperate_lines(self):
        temp_month = pd.DataFrame()
        for i, line in self.gen.iterrows():
            month_number = line['תאריך'].month
            if self.months[month_number - 1] is None:
                self.months[month_number - 1] = pd.DataFrame(columns=self.gen.columns)
            self.months[month_number - 1] = pd.concat([self.months[month_number - 1], pd.DataFrame(line).T], ignore_index=True, axis = 1)
            # temp_month = self.months[month_number - 1]
            # temp_month = pd.concat([temp_month, pd.DataFrame(line)], ignore_index=True, axis=1)
            # self.months[1] = pd.concat([self.months[1], temp_month], ignore_index=True, axis = 0)


    # def add_line(self, line, month):
    #
    #     if month == 1:
    #         self.Jan = pd.concat([self.Jan, line],axis = 1)
    #     elif month == 2:
    #         self.Feb = pd.concat([self.Feb, line],axis = 1)
    #     elif month == 3:
    #         self.Mar = pd.concat([self.Mar, line],axis = 1)
    #     elif month == 4:
    #         self.Apr = pd.concat([self.Apr, line],axis = 1)
    #     elif month == 5:
    #         self.May = pd.concat([self.May, line],axis = 1)
    #     elif month == 6:
    #         self.Jun = pd.concat([self.Jun, line],axis = 1)
    #     elif month == 7:
    #         self.Jul = pd.concat([self.Jul, line],axis = 1)
    #     elif month == 8:
    #         self.Aug = pd.concat([self.Aug, line],axis = 1)
    #     elif month == 9:
    #         self.Sep = pd.concat([self.Sep, line],axis = 1)
    #     elif month == 10:
    #         self.Oct = pd.concat([self.Oct, line],axis = 1)
    #     elif month == 11:
    #         self.Nov = pd.concat([self.Nov, line],axis = 1)
    #     elif month == 12:
    #         self.Dec = pd.concat([self.Dec, line],axis = 1)

    def add_line(self, line, month):
        for i in range(12):
            if month == i:
                self.months[i-1] = pd.concat([self.months[i-1], line],axis = 1)

    def create_file(self):
        self.Jan = self.Jan.transpose()
        # self.Jan.to_csv("Jan.csv", encoding='iso-8859-8', index=False)
        self.Feb = self.Feb.transpose()
        # self.Feb.to_csv("Feb.csv", encoding='iso-8859-8', index=False)
        self.Mar = self.Mar.transpose()
        # self.Mar.to_csv("Mar.csv",  index=False)
        self.Apr = self.Apr.transpose()
        # self.Apr.to_csv("Apr.csv", encoding='iso-8859-8', index=False)
        self.May = self.May.transpose()
        # self.May.to_csv("May.csv", encoding='iso-8859-8', index=False)
        self.Jun = self.Jun.transpose()
        # self.Jun.to_csv("Jun.csv", encoding='iso-8859-8', index=False)
        self.Jul = self.Jul.transpose()
        # self.Jul.to_csv("Jul.csv", encoding='iso-8859-8', index=False)
        self.Aug = self.Aug.transpose()
        # self.Aug.to_csv("Aug.csv", encoding='iso-8859-8', index=False)
        self.Sep = self.Sep.transpose()
        # self.Sep.to_csv("Sep.csv", encoding='iso-8859-8', index=False)
        self.Oct = self.Oct.transpose()
        # self.Oct.to_csv("Oct.csv", encoding='iso-8859-8', index=False)
        self.Nov = self.Nov.transpose()
        # self.Nov.to_csv("Nov.csv", encoding='iso-8859-8', index=False)
        self.Dec = self.Dec.transpose()
        # self.Dec.to_csv("Dec.csv", encoding='iso-8859-8', index=False)
        with pd.ExcelWriter('Year2023.xlsx') as writer:
            self.Jan.to_excel(writer,sheet_name='Jan',index=False)
            self.Feb.to_excel(writer,sheet_name='Feb',index=False)
            self.Mar.to_excel(writer,sheet_name='Mar',index=False)
            self.Apr.to_excel(writer,sheet_name='Apr',index=False)
            self.May.to_excel(writer,sheet_name='May',index=False)
            self.Jun.to_excel(writer,sheet_name='Jun',index=False)
            self.Jul.to_excel(writer,sheet_name='Jul',index=False)
            self.Aug.to_excel(writer,sheet_name='Aug',index=False)
            self.Sep.to_excel(writer,sheet_name='Sep',index=False)
            self.Oct.to_excel(writer,sheet_name='Oct',index=False)
            self.Nov.to_excel(writer,sheet_name='Nov',index=False)
            self.Dec.to_excel(writer,sheet_name='Dec',index=False)

if __name__ == "__main__":
    nava = Order()
    nava.seperate_lines()
    nava.create_file()