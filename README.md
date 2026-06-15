# BJJ Membership Retention and Lifetime Value Analysis

## Background & Overview

Member retention is one of the most important drivers of long-term revenue for martial arts academies. While acquiring new students is essential for growth, maintaining existing memberships often has a greater impact on profitability due to the recurring nature of membership-based businesses. Understanding which member segments remain enrolled the longest and generate the greatest lifetime value can help gym management make more informed decisions regarding sales, retention, and marketing strategies.

This project analyzes membership data from a Brazilian Jiu-Jitsu academy to identify factors associated with member retention and revenue generation. Using SQL Server for data preparation and Python for analysis and visualization, the project evaluates membership duration, lifetime value, billing hold behavior, and demographic trends. The objective is to provide actionable insights that can help academy leadership improve member retention and maximize long-term revenue.

---

## Data Structure Overview

The dataset consists of membership records containing demographic information, membership status, billing hold information, and revenue-related metrics. Data cleaning and feature engineering were performed using SQL Server before being imported into Python for analysis.

Key fields include:

* Membership_Type (1x per week or Full Access)
* Age
* Age_Group
* Current_Member
* Hold_Status
* Hold_Duration_Days
* Membership_Duration_Days
* Monthly_Dues
* Lifetime Value (LTV)

Several calculated metrics were created to support the analysis, including membership duration, member lifetime value, churn rate, and average hold duration. These metrics were aggregated by membership type and age group to evaluate retention and revenue trends across member segments.

---

## Executive Summary

The analysis found that Full Access memberships generate substantially greater revenue than 1x-per-week memberships while exhibiting nearly identical retention performance. Full Access members produce an average lifetime value of approximately $2,351 compared to $1,520 for 1x-per-week members, representing a difference of roughly 55%. Despite this significant revenue gap, both membership plans display similar membership durations and churn rates.

Adult members emerged as the academy's most valuable customer segment. Adults demonstrated the highest average lifetime value and the longest average membership duration compared to children and toddlers. These findings suggest that adult members contribute disproportionately to both retention and revenue outcomes.

The analysis also identified a relationship between billing holds and membership duration. Members currently on hold exhibited shorter average membership tenures than members who were not on hold. While additional historical data is required to determine whether holds directly contribute to member cancellations, the results suggest that hold activity may serve as an indicator of members at greater risk of leaving the academy.

---

## KPI Summary

| KPI                         | 1x per Week | Full Access |
| --------------------------- | ----------- | ----------- |
| Average Membership Duration | 285 Days    | 294 Days    |
| Churn Rate                  | 54.25%      | 53.09%      |
| Average Lifetime Value      | $1,520      | $2,351      |
| Average Hold Duration       | 47 Days     | 49 Days     |

Key observations include:

* Membership duration is nearly identical across membership types.
* Churn rates differ by only approximately one percentage point.
* Full Access members generate approximately 55% greater lifetime value.
* Hold durations are consistent across membership plans.

These findings suggest that membership type has a much greater impact on revenue generation than on retention outcomes.

---

## Recommendations

### Promote Full Access Memberships

Full Access memberships generate significantly greater lifetime value while maintaining retention rates comparable to 1x-per-week memberships. Management should consider emphasizing Full Access memberships during the sales process and evaluating opportunities to encourage existing members to upgrade.

### Focus Retention Efforts on Adult Members While Improving Youth Retention

Adult members demonstrate the highest lifetime value and longest membership duration of any age segment. Understanding the factors contributing to strong adult retention may help identify opportunities to improve retention among children and toddlers.

### Improve Hold and Cancellation Tracking

Members currently on hold exhibit shorter average membership durations than members not on hold. Collecting additional information regarding hold reasons, hold frequency, and cancellation motivations would enable more detailed retention analysis and support the development of targeted intervention strategies for at-risk members.
