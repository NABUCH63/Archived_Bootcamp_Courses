# **VBA Challenge Stock Analysis**

### Overview of Project

A brief analysis utilizing VBA code within excel to automate a stock analysis of the 12 provided 'tickers'. These were assesed for the total volume, starting price, and closing price for each stock. A final calculation using the starting and closing prices determined the total percent return for each stock within the chosen year. 

### Purpose

The purpose of this analysis was to summarize each stock within a specified year. The analysis determined the performance of each stock, and provide an simplified summary table with visual cues to assist quick reviews. 

In addition, the VBA code used in the analysis was written and refactored to determine if there were any methods to increase the efficiency of the code's run-time. 

### Analysis and Challenges

1. Analysis of Stocks 2017 and 2018

   * The analysis of 2017 and 2018 stocks can be seen in the images below. Stepped color scales were used for easy visual cues given the performance of each stock. Prior to the analysis, the stocks and date-stamps were sorted to ensure standard results in the output tables. It can be seen that 2017 saw better returns overall, but 2018 did see increased returns from "RUN" and "TERP".

    ![All Stocks 2017](/VBA_Module_02/Project_Pictures/All_Stocks_2017.png "All Stocks 2017 Summary")

    ![All Stocks 2018](/VBA_Module_02/Project_Pictures/All_Stocks_2018.png "All Stocks 2017 Summary")

2. VBA Analysis

   *  The first code written used two for-next loops to cycle through all tickers assigned within the array, and through all rows in the worksheet. The output of each stock's volume, starting, and closing prices were output to the sumamry table within the loop, as well as the formatting of the 'return' cells based on value. Part of this code can be seen in the image below.

    ![Original For-Next Loop](/VBA_Module_02/Project_Pictures/Original_For_Loop_Code.png "Example of the original code")

   *  In an effort to determine what could be more efficient, the For-Next loop that cycled through the ticker array was removed and replaced with a variable. This variable increased as each ending price was determined, allowing for each ticker to be assessed. Removing the second for-next loop required the program to only run through the data one time, versus going through the data 12 times with the original code. 

    ![Refactored For-Next Loop](/VBA_Module_02/Project_Pictures/Refactored_table_outside_For_Loop.png "Example of the refactored code loop")

    ![Refactored End of Code](/VBA_Module_02/Project_Pictures/Refactored_formatting_outside_For_loop.png "Example of the output code and formatting")

    * The runtimes for 2017's analysis was improved by .6894531 seconds. The runtimes for 2017 can be seen below.

    ![2017 Original Code](/VBA_Module_02/Project_Pictures/Original_2017.png "2017 Original code runtime")

    ![2017 Refactored Code](/VBA_Module_02/Project_Pictures/refactored_2017.png "2017 Refactored code runtime")

   *  The runtimes for 2018's analysis was improved by .7128906 seconds. The runtimes for 2018 can be seen below.


     ![2018 Original Code](/VBA_Module_02/Project_Pictures/Original_2018.png "2018 Original code runtime")

     ![2018 Refactored Code](/VBA_Module_02/Project_Pictures/refactored_2018.png "2018 Refactored code runtime")

3. Challenges

    Pros and Cons of Refactoring code

      * Pros - A significant amount of runtime can be removed by refactoring code to be more efficient. Larger datasets will have a greater need to ensure an efficient code to minimize the runtime. 

      * Cons - Smaller datasets do not see a significant change in runtime when refactoring code. The difference of fractions of seconds ultimately does not effect the efficiency of the analysis, and sacrifices time spent by the analyst.

    Pros and Cons of this analysis

      * Pros - The refactored code did show a significant relative change in runtime. The tickerindex variable was an easy replacement for the first for-next loop. 

      * Cons - Removing the for-next loop that cycled through the ticker array required the output and formatting sections of code to be shifted to the end of the subroutine, with each output coded for each ticker (versus a single line of code for each variable). This was laborsome to write, and will require manual changes should any additional tickers be added to the dataset 

### Summary

Refactoring code to be more efficient is beneficial to larger datasts, but potentially removes any ability to readily apply the code to larger datasets. Smaller datasets see minimal improvements. Refactoring code requires additional time from the analyst to rewrite and ammend the existing subroutine, and may not be necessary to increase the workload of the project.
