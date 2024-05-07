import pandas as pd
import openpyxl

class Order:
    def __init__(self):
        self.gen = pd.read_csv("General2023.csv", dayfirst=True, parse_dates=[0], encoding='iso-8859-8')
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

        self.months = [
            self.Jan, self.Feb, self.Mar,self.Apr, self.May, self.Jun, self.Jul, self.Aug, self.Sep, self.Oct, self.Nov, self.Dec]
        self.months_names = [
            'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    def seperate_lines(self):
        for i, line in self.gen.iterrows():
            month_number = line['תאריך'].month -1
            self.months[month_number] = pd.concat([self.months[month_number], line], ignore_index=True, axis=1)

    def sort_lines(self):
        for i in range(12):
            self.months[i] = self.months[i].transpose()
            if not self.months[i].empty:
                # self.months[i] = self.months[i].sort_values(by=self.months[i].iloc[:, 0])
                self.months[i] = self.months[i].sort_values(by=['סטטוס טיפול התקבל/לא התקבל/סיום'], ascending=False)
                self.months[i] = self.months[i].drop_duplicates(subset=['שם משפחה+ שם פרטי'], keep='first')
                
    def create_file(self):
        with pd.ExcelWriter('Year2023.xlsx') as writer:
            for i in range(12):
                self.months[i].to_excel(writer, sheet_name=self.months_names[i], index=False)


if __name__ == "__main__":
    nava = Order()
    nava.seperate_lines()
    nava.sort_lines()
    nava.create_file()


