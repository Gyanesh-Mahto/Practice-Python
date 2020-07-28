l1=['ZERO','ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE','TEN', 'ELEVEN', 'TWELVE', 'THIRTEEN', 'FOURTEEN', 'FIFTEEN', 'SIXTEEN', 'SEVENTEEN', 'EIGHTEEN', 'NINTEEN']
l2=['TWENTY', 'THIRTY', 'FOURTY', 'FIFTY', 'SIXTY', 'SEVENTY', 'EIGHTY', 'NINTY']
l3=['ONE HUNDRED', 'TWO HUNDRED', 'THREE HUNDRED', 'FOUR HUNDRED', 'FIVE HUNDRED', 'SIX HUNDRED', 'SEVEN HUNDRED', 'EIGHT HUNDRED', 'NINE HUNDRED']

num=int(input('Please enter any number between 0 to 999: '))
if num>=0 and num<=19:
    print('{}'.format(l1[num]))
elif num>19 and num<=99:
    temp=num
    num_1=temp%10
    if num_1==0:
        temp=temp//10
        num_2=temp%10    
        print('{}'.format(l2[num_2-2]))
    else:
        temp=temp//10
        num_2=temp%10
        print('{} {}'.format(l2[num_2-2], l1[num_1]))
elif num>99 and num<=999:
    temp=num
    num_1=temp%10
    temp=temp//10
    num_2=temp%10
    temp=temp//10
    num_3=temp
    if num_1==0 and num_2==0:
        print(l3[num_3-1])
    elif num_2==0:
        print('{} {}'.format(l3[num_3-1], l1[num_1]))
    else:
        print('{} and {} {}'.format(l3[num_3-1],l2[num_2-2], l1[num_1]))
            
else:
    print('Please enter number between 0 to 999')
