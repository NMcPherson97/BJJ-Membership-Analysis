USE BJJMEMBERS;

-- Clean null and nonsensical ages (126 and -1)
UPDATE dbo.membership 
SET AGE = CASE 
    WHEN AGE IS NULL THEN 0 
    WHEN Age < 0 THEN 0 
    WHEN Age = 126 THEN 0 
    ELSE Age 
END;

-- Calculate membership duration in days, using current date for active memberships
UPDATE dbo.membership
SET Membership_Duration_Days =
    DATEDIFF(
        DAY,
        Sign_Up_Date,
        ISNULL(Cancellation_Date, GETDATE())
    );

--Calculate Age group column
SELECT * ,
CASE
    WHEN Age >= 0 AND  Age < 6 THEN 'Toddler'
    WHEN Age >= 6 AND Age <= 13 THEN 'Child'
    WHEN Age >= 14 THEN 'Adult'
END AS Age_Group
FROM dbo.membership; 

--Monthly Dues column
SELECT *,
CASE
    WHEN Membership_Type = '1x per week' THEN 160
    WHEN Membership_Type = 'Full Access' THEN 240
END AS Monthly_Dues
FROM dbo.membership;

--Analysis View 
GO
CREATE OR ALTER VIEW member_analysis AS
SELECT
    Membership_Type,
    Current_Member,
    Hold_Status,
    Hold_Duration_Days,
    Age,
    Age_Group,
    Membership_Duration_Days,
    Monthly_Dues,
    Sign_Up_Date,
    Cancellation_Date
FROM dbo.membership;
GO

SELECT TOP 10 *
FROM member_analysis;


