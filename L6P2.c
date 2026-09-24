#include <stdio.h>
#include <stdlib.h>

// Function to check if a character is printable ASCII
int isPrintableASCII(char c)
{
    return (c >= 0x20 && c <= 0x7E);
}

// Function to print the file summary
void printSummary(unsigned char *data, int length)
{
    if (length < 4)
    {
        printf("Insufficient data to determine the magic number.\n");
        return;
    }

    // Print the magic number
    printf("Magic Number: 0x%02X%02X%02X%02X\n", data[3], data[2], data[1], data[0]);

    // Calculate the percentage of printable ASCII characters
    int printableCount = 0;
    for (int i = 0; i < length; i++)
    {
        if (isPrintableASCII(data[i]))
        {
            printableCount++;
        }
    }

    double printablePercentage = (double)printableCount / length * 100;

    // Determine the type of file
    if (printablePercentage >= 75.0)
    {
        printf("This file is definitely a text file: >= 75%% ASCII\n");
    }
    else if (printablePercentage >= 25.0)
    {
        printf("This file is probably a text file: between 25 and 74%% ASCII\n");
    }
    else
    {
        printf("This file is definitely a binary file: < 25%% ASCII\n");
    }
}

int main()
{
    char filename[50];
    printf("Enter the name of the file to open: ");
    scanf("%s", filename);

    FILE *file = fopen(filename, "rb");
    if (!file)
    {
        perror("Error opening file");
        return EXIT_FAILURE;
    }

    // Buffer to store the file contents
    unsigned char buffer[16];
    size_t bytesRead;
    int offset = 0;
    int totalBytes = 0;
    unsigned char firstFourBytes[4] = {0};

    printf("===========================================================================\n");
    printf("|offset |          Hexadecimal Data                       |Character Format|\n");
    printf("===========================================================================\n");

    while ((bytesRead = fread(buffer, 1, sizeof(buffer), file)) > 0)
    {
        // Store the first four bytes for summary
        if (totalBytes < 4)
        {
            for (int i = 0; i < bytesRead && totalBytes < 4; i++, totalBytes++)
            {
                firstFourBytes[totalBytes] = buffer[i];
            }
        }
        totalBytes += bytesRead;

        // Print the offset
        printf("|%06X|", offset);

        // Print the hexadecimal data and character format
        for (size_t i = 0; i < bytesRead; i++)
        {
            if (i == 8) printf(" ");
            printf("%02X ", buffer[i]);
        }

        // Fill the remaining space if less than 16 bytes read
        for (size_t i = bytesRead; i < 16; i++)
        {
            if (i == 8) printf(" ");
            printf("   ");
        }
        printf("|");

        // Print the character format
        for (size_t i = 0; i < bytesRead; i++)
        {
            char ch = buffer[i];
            printf("%c", (ch >= 0x20 && ch <= 0x7E) ? ch : '.');
        }
        printf("|\n");

        offset += 16;
    }
    fclose(file);

    // Print the file summary
    printSummary(firstFourBytes, totalBytes);

    return 0;
}
