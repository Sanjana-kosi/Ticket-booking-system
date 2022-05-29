source1={1:"Austin", 2:"Houston", 3:"garland",4:"Paris",5:"Dallas", 6:"forth worth", 7:"salt lake city", 8:"miami", 9:"Frisco", 10:"Allen" }
dest={11:"New York", 12:"Houston", 13:"Los angeles",14:"Paris", 15:"Dallas", 16:"Chicago", 17:"salt lake city", 18:"miami", 19:"Pheonix", 20:"San diego"}
dis1={"Austin to New York":300, "Austin to Houston":400, "Austin to Los angeles":700, "Austin to Paris":500, "Austin to Dallas":400, "Austin to Chicago":700, "Austin to Salt lake city":900, "Austin to miami":200, "Austin to Pheonix":900, "Austin to San diego":500,"Houston to New York":400, "Houston to Austin":200, "Houston to Los angeles":700, "Houston to Paris":800, "Houston to Dallas":200, "Houston to Chicago":500, "Houston to Salt lake city":900, "Houston to miami":800, "Houston to Pheonix":300, "Houston to San diego":400, "garland to New york":500, "garland to Houston":500, "garland to Los angeles":600, "garland to Paris":400, "garland to Dallas":400, "garland to Chicago":600, "garland to Salt lake city":300, "garland to miami":200, "garland to Pheonix":800, "garland to San diego":700, " Paris to New york":300, "Paris to Houston":500, "Paris to Los angeles":300, "Paris to Austin":700, "Paris to Dallas":600, "Paris to Chicago":300, "Paris to Salt lake city":800, "Paris to miami":400, "Paris to Pheonix":700, "Paris to San diego":500, }
fareflight=60
faretrain=50
farebus=45 
x=int(input("please choose a source. type 1 for Austin, 2 for Hosuton, 3 for garland, 4 for Paris, 5 for Dallas, 6 for forth worth, 7 for salt lake city, 8 for miami, 9 for Frisco, 10 for Allen:  "))
truez=1 # varibale that controls the loop
while truez==1:
    sourcecity=source1[x] # takes the source form dictionary
    z= int(input(" please choose a destination. type 1 for exit, type 11 for new york, 12 for houston, 13 for los Angeles, 14 for Paris, 15 for Dallas, 16 for Chicago, 17 for salt lake city, 18 for miami, 19 for Pheonix, 20 for san diego: "))
    destcity=dest[z]
    y=sourcecity+ " to "+ destcity  # adds both cities 
    a=dis1[y]
    service= int(input(" please choose a travel option, type 1 for plane, 2 for train, 3 for bus:  "))
    if service==1:
        price=a*fareflight
        print(" your total fare is: ", price)
    elif service==2:
        price=a*faretrain
        print(" your total fare is: ", price)
    elif service==3:
        price=a*farebus
        print(" your total fare is: ", price)
    name=input(" enter your name: ")
    number=input("enter your number: ")
    truez=input("exit from this type 1: ")
    print(" thanks for booking with us")