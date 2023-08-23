#include <iostream>
using namespace std;

class Solution
{
public:
    string convert(string s, int numRows)
    {
        if (numRows == 1 || s.length() <= numRows)
        {
            return s;
        }

        int totalChars = s.length();
        char zigzagMatrix[numRows][totalChars];

        // Initialize the zigzagMatrix with empty spaces
        for (int row = 0; row < numRows; row++)
        {
            for (int col = 0; col < totalChars; col++)
            {
                zigzagMatrix[row][col] = ' ';
            }
        }

        int charIndex = 0;
        int currentRow = 0, currentCol = 0;

        // Fill the zigzagMatrix with characters from the input string
        while (charIndex != totalChars)
        {
            // Moving down in the zigzag pattern
            for (int i = 0; i < numRows - 1 && charIndex != totalChars; i++)
            {
                zigzagMatrix[currentRow++][currentCol] = s[charIndex++];
            }
            if (charIndex == totalChars)
            {
                break;
            }
            
            // Moving up-right in the zigzag pattern
            zigzagMatrix[currentRow][currentCol] = s[charIndex++];
            for (int i = 0; i < numRows - 2 && charIndex != totalChars; i++)
            {
                zigzagMatrix[--currentRow][++currentCol] = s[charIndex++];
            }
            currentRow--;
            currentCol++;
        }

        string result;
        // Construct the result string from the zigzagMatrix
        for (int row = 0; row < numRows; row++)
        {
            for (int col = 0; col < totalChars; col++)
            {
                if (zigzagMatrix[row][col] != ' ')
                {
                    result += zigzagMatrix[row][col];
                }
            }
        }
        return result;
    }
};

int main()
{
    Solution solution;

    string input;
    cout << "Enter the string: ";
    getline(cin, input);

    int numRows;
    cout << "Enter the number of rows: ";
    cin >> numRows;

    string converted = solution.convert(input, numRows);
    cout << "Converted string in zigzag pattern: " << converted << endl;

    return 0;
}
