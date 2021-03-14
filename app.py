import math

c = int(input("Choose a method:\n1. LOC based estimation\n2. FP based estimation\n3. COCOMO II\n"))

if c == 1:
    print("Work in progress")
elif c == 2:
    inp = int(input("\nNo. of User Inputs: "))
    out = int(input("No. of User Outputs: "))
    inq = int(input("No. of User Inqueries: "))
    maf = int(input("No. of User Files: "))
    inf = int(input("No. of External Interfaces: "))
    
    
    print("\nParameter           Weighting Factors\n"
          "                    Simple  Average  Complex\n"
          "User Input          3       4        6\n"
          "User Output         4       5        7\n"
          "User Inquries       3       4        6\n"
          "Files               7       10       15\n"
          "External interfaces 5       7        10\n")
    w_inp = int(input("Weighting factor for User Inputs: "))
    w_out = int(input("Weighting factor for User Outputs: "))
    w_inq = int(input("Weighting factor for User Inquries: "))
    w_maf = int(input("Weighting factor for User Files: "))
    w_inf = int(input("Weighting factor for External Interfaces: "))
    
    
    print("\nGeneral system characteristics on a scale of 0-5\n"
          "0 = No Influence\n" 
          "1 = Incidental\n"
          "2 = Moderate\n"
          "3 = Average\n"
          "4 = Significant\n"
          "5 = Essential\n")
    print("Enter general system characteristics for 14 questions: ")
    gsc1 = int(input("\nBackup and recovery: "))
    gsc2 = int(input("Data communication: "))
    gsc3 = int(input("Distributed processing functions: "))
    gsc4 = int(input("Is performance critical?: "))
    gsc5 = int(input("Existing operating environment: "))
    gsc6 = int(input("On-line data entry: "))
    gsc7 = int(input("Input transaction built over multiple screens: "))
    gsc8 = int(input("Master files updated on-line: "))
    gsc9 = int(input("Complexity of inputs, outputs, files, inquiries: "))
    gsc10 = int(input("Complexity of processing: "))
    gsc11 = int(input("Code design for re-use: "))
    gsc12 = int(input("Are conversion/installation included in design?: "))
    gsc13 = int(input("Multiple installations: "))
    gsc14 = int(input("Application designed to facilitate change by the user: "))
    
    
    count_total = ((inp*w_inp)+(out*w_out)+(inq*w_inq)+(maf*w_maf)+(inf*w_inf))
    di = gsc1+gsc2+gsc3+gsc4+gsc5+gsc6+gsc7+gsc8+gsc9+gsc10+gsc11+gsc12+gsc13+gsc14
    tcf = 0.65+(0.01*di)
    fp = count_total*tcf
    
    print("\nCount total/UFP: ",count_total)
    print("\nDI or VAF or Fi or TDI: ",di)
    print("\nTCF: ",tcf)
    print("\nFunctional Point - FP = ",math.ceil(fp))

    
elif c == 3:
    print("Work in progress")
    