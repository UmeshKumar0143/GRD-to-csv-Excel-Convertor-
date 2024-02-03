import imdlib as imd

start_yr = 2021

end_yr = 2021 
variable = 'tmax'

file_format = 'yearwise' 

file_dir = 'D:\SDE\PROGRAMS\PYTHON\Project -01\imd_data'

data = imd.open_data(variable, start_yr, end_yr,'yearwise', file_dir) 

if variable == 'tmax' or variable == 'tmin':
    grid_size = 1 
    y_count = 31
    x_count = 31 
    x = 67.5 
    y = 7.5 


data
data.shape
np_array = data.data

years_no = (end_yr - start_yr) + 1


day = 0
for yr in range(0,years_no):
    f = open("D:\SDE\PROGRAMS\PYTHON\Project -01\imd_data\Converted Data\Tempratures"+str(start_yr+yr)+"_"+str(variable)+".csv",'w') 

    if ((start_yr+yr) % 4 == 0) and ((start_yr+yr) % 100 != 0):  

        days = 366
        count = yr + days
    elif ((start_yr+yr) % 4 == 0) and ((start_yr+yr) % 100 == 0) and ((start_yr+yr) % 400 == 0):
        days = 366
        count = yr + days
    else:
        days = 365
        count = yr + days

    day = day + days

    f.write("X,Y,")
    for d in range(0, days):
        f.write(str(d+1))
        f.write(",")
    f.write("\n")

    for j in range(0, y_count):

        for i in range(0, x_count):

            f.write(str((i * grid_size) + x))
            f.write(",")
            f.write(str((j * grid_size) + y))
            f.write(",")
            time = 0
            for k in range(day-days, day):

                val = np_array[k,i,j]
                if val == 99.9000015258789 or val == -999:
                    f.write(str(-9999))
                    f.write(",")
                else:
                    f.write(str(val))
                    f.write(",")


            f.write("\n")
    print("File for " + str(start_yr + yr) + "_" + str(variable) + " is saved")
print("CSV conversion successful !")

