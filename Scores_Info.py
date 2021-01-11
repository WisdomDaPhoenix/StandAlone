#finding the largest and second largest of 7 numbers
largest = eval(input('Enter a score: '));
sec_largest = eval(input('Enter a lower score: '));
lowest = 0
flag = 0;
if sec_largest > largest:
   largest,sec_largest = sec_largest,largest;
agg_score = largest + sec_largest;
for i in range(5):
    num = eval(input('Enter other scores: '));
    agg_score = agg_score + num; 
    if num > largest:
       largest = num;
    if num > 100:
       flag = 1;
    elif num > sec_largest and num < largest:
       sec_largest = num;
    elif num > sec_largest:
       num,sec_largest = sec_largest,num
    if not (num > sec_largest):
        lowest = num;
                        
print('The lowest score is :', lowest)
print('The largest, second largest and average of the bunch of numbers are: ', largest, 'and', sec_largest, 'and', agg_score/10)
if flag == 1:
   print('One of the values is greater than 100, repeat the data entry exercise');
