ip = "192.168.3.1"
separation_1 = ip.split('.')
separation_2 = [bin(int(i))[2:].zfill(8) for i in separation_1 ]
print("{:10}{:10}{:10}{:10} \n{:10}{:10}{:10}{:10}".format(separation_1[0], separation_1[1], separation_1[2], separation_1[-1], separation_2[0], separation_2[1], separation_2[2], separation_2[-1]))