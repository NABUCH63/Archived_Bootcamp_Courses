# **Kickstarting with Excel**

## Overview of Project

A brief analysis into what Kickstarter projects were created, their goals, pledge results, and level of success. This analysis broke down the 'theater' category based on the project creation and the level of funding recieved.

### Purpose

The purpose of this analysis was to summarize the trends between the time of year and the outcomes of Kickstarter projects listed under the category 'theater'. An aditional analysis broke down the level of funding provided specifically to the subcategory 'plays'. 

## Analysis and Challenges

1. Analysis of Outcomes Based on Launch Date

    The analysis of outcomes versus launch dates summarized the frequency of the outcomes "successful", "failed", and "canceled" to the months theater projects were launched (across all years of data available). A pivot table was created representing the full dataset, and was filtered down to represent only those projects within the 'theater' category. The table can be found in the "Kickstarter" workbook under the "Theater_Outcomes_By_Launch_Date" worksheet. The chart can be seen below.

    ![Outcomes vs Launch Date](/Excel_Module_01/Project_Pictures/Theater_Outcomes_vs_Launch_Date.png "Outcomes Vs Launch Date Chart")


2. Analysis of Outcomes Based on Goals

    The analysis of outcomes based on goals summarized the level of success of the outcomes "successful", "failed", and "canceled" for any 'plays' within the 'theater' category. The summary was simplified to bins ranging from less than $1000 goals to more than $50000 goals, at roughly $5000 steps. The number falling into those criteria were determined, and the total number of projects for each bin. The percentage of the outcomes in each bin were determined and plotted. The chart can be seen below. 

    ![Outcomes vs Goals](/Excel_Module_01/Project_Pictures/Outcomes_vs_Goals.png "Outcomes Vs Project Goals")

 3. Challenges and Difficulties Encountered

    A few challenges were met in this analysis. When searching the data by criteria, it was a challenge to validate if the results of the "canceled" plays were truly zero across all goal amounts. After assessing the cell formulas, it took physically filtering the data down manually to determine that there were no data points that fell within to those criteria. 

## Results

1. Analysis of Outcomes based on Launch Dates

    The resulting chart showed that the summer months did see a trend of more project successes, with a peak in the month of May. This was interesting to compare to the level of failed and canceled outcomes, which remained relatively steady throughout the calendar year. It can be concluded that the increase in overall projects started in the summmer does not directly influnce the increase in successful projects, as the failed and canceled projects do not see the same level of influence from the summer fluctuation. 

2. Analysis of Outcomes based on Goals

    The resulting table and chart showed that the majority of project goals were less than $5000. The trend seen as the goal amount increased was a decline in success (with a rise in failure). The exception to this was seen within the range of $35000 to $44999, where the percent of success again rose above the percent failure. Projects above $45000 saw very high trends of failure. No projects within the 'plays' criteria saw any cancelations, regardless of goal set.

3. Overall Results

    It could be seen through both analyses that the 'theater' category saw a spike in the number of overall projects, and the number of successes. When the 'plays' were isolated, it was determined that the majority of the projects fell below $5000 and saw more successful funding if the goal was below $15000. 

4. Limitations

    This analysis was limited to overall trends, and did not look into the length of campaigns nor the rate they were funded. 

    The dataset does not include the time pledges were recieved, if the projects that were successfully funded resulted in a final product, or what the "spotlight" and "staffpick" categories signify (if any additional attention was provided to certain project campaigns over others).

5. Other Possibilities

    Other deliverables that could be beneficial to this project could include tables showing the total campaign time compared to the goal, the number of backers, and the amount pledged. 
