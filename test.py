from channel import Channel

my_obj = Channel(0)

my_obj.welcome_text("Code is Working")

dat = my_obj.data_import('Salary_Data.csv')

my_obj.save_data(dat)

my_obj.load_data()

my_obj.table('x-axis', 'y-axis')

my_obj.graph_it(0, 1)