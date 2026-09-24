#include <stdio.h>
#include <stdlib.h>

#define MAX_LINE_LENGTH 100
#define MAX_NUMBERS_PER_ROW 10

int main() 
{
    FILE *inputFile, *below60File, *above60File;
    char line[MAX_LINE_LENGTH];
    int totalNumbers = 0, below60Count = 0, above60Count = 0;
    float grade;
    
    inputFile = fopen("numbers.txt", "r");
    if (inputFile == NULL)
    {
        printf("Error opening numbers.txt\n");
        return 1;
    }
    
    below60File = fopen("below60.txt", "w");
    if (below60File == NULL)
    {
        printf("Error opening below60.txt\n");
        fclose(inputFile);
        return 1;
    }
    
    above60File = fopen("above60.txt", "w");
    if (above60File == NULL)
    {
        printf("Error opening above60.txt\n");
        fclose(inputFile);
        fclose(below60File);
        return 1;
    }

    // Read and process the input file
    while (fgets(line, MAX_LINE_LENGTH, inputFile) != NULL)
    {
        if (sscanf(line, "number%d : %f", &totalNumbers, &grade) == 2)
        {
            if (grade <= 60.00)
            {
                fprintf(below60File, "%.2f ", grade);
                below60Count++;
                if (below60Count % MAX_NUMBERS_PER_ROW == 0)
                {
                    fprintf(below60File, "\n");
                }
            } 
            else
            {
                fprintf(above60File, "%.2f ", grade);
                above60Count++;
                if (above60Count % MAX_NUMBERS_PER_ROW == 0)
                {
                    fprintf(above60File, "\n");
                }
            }
            totalNumbers++;
        }
    }
    
    fclose(inputFile);
    fclose(below60File);
    fclose(above60File);
    
    // Print the summary
    printf("numbers.txt contains: %d numbers\n", totalNumbers);
    printf("above60.txt contains: %d numbers\n", above60Count);
    printf("below60.txt contains: %d numbers\n", below60Count);
    
    return 0;
}
