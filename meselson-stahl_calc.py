#Meselson and Stahl Calculator

n = 2
no_cells = (float(input("Enter generation: ")))
total_cells = (n ** no_cells)
n_percentage = (n/total_cells)*100
n14_percentage = (100-n_percentage)

print("The", no_cells, "generation of semi-conservative DNA replication is", n14_percentage, "% N14-N-14 isotopes and",
      n_percentage, "% N15-N14 isotopes")

print("Would you like to see other feasible compositions?")
yes = ("yes")
no = ("no")
na = False
ans = input("Yes or No:")

new_cells = (float(no_cells+1))

if ans == yes:
    while new_cells < 1024:
        new_cells += 1
        total_newcells = (n ** new_cells)
        N_percentage = (n / total_newcells) * 100
        N14_percentage = (100 - N_percentage)
        print("The", new_cells, "generation of semi-conservative DNA replication is", N14_percentage,
              "% N14-N-14 isotopes and", N_percentage, "% N15-N14 isotopes")
    else:
        print("This generation has no significant traces of N15-N14 compounds left in the DNA sequence")

if ans == no:
    print("")
    na = True
