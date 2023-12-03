#include <stdio.h>
#include <stdlib.h>
#include <string.h>





int findFirstAndLastDigit(char* s)
{
    int len = strlen(s);
    int res1;
    int res2;
    char* buffer = (char*)malloc(1000*sizeof(char));
    int j = 0;
    for(int i = 0; i < len; i++)
    {        
        if(s[i] >= '0' && s[i] <= '9')
        {
            if (j == 0){
                res1 = s[i] - '0';
                res2 = s[i] - '0';
                printf("%d",res1);
                j=1;
            }else{
                res2 = s[i] - '0';
                printf("%d",res2);
            }             
        }
    }
    int c = res1*10 + res2;
    printf(" -- %d\n",c);
    return c;
}

int main()
{
    FILE *f;
    char* c = (char*)malloc(1000*sizeof(char));
    f=fopen("day1/input1.txt","rt");
    int x;
    int sum = 0;
    while((fgets(c,1000,f))!=NULL){
        x = findFirstAndLastDigit(c);
        sum += x;
    }
    printf("%d",sum);
    fclose(f);
    return 0; 
}