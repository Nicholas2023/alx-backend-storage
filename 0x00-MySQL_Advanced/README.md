# MySQL Advanced Tasks :wink:

This repository contains SQL scripts and operations to perform advanced tasks in MySQL. Each task is designed to showcase specific SQL functionalities and operations.

## Task Descriptions

### Task 0: Unique Users Table Creation
- Creates a table named `users` with specific attributes (`id`, `email`, `name`) and unique constraints.
- Ensures uniqueness in the `email` field to avoid duplicate entries.

### Task 1: Country Users Table with Enumeration
- Creates a `users` table with additional attributes (`country`) as an enumeration of specific countries (`US`, `CO`, `TN`).
- Implements default values and constraints to manage country enumeration effectively.

### Task 2: Band Country Origins and Fans Ranking
- Ranks country origins of bands based on the number of fans they have.
- Utilizes a provided table dump (`metal_bands.sql.zip`) to compute and order band origins by fan count.

### Task 3: Glam Rock Bands Longevity Listing
- Lists bands specializing in Glam rock along with their lifespans, calculated based on the `formed` and `split` attributes from a provided table dump (`metal_bands.sql.zip`).

### Task 4: Trigger to Decrease Item Quantity on Order
- Implements a trigger to decrease the quantity of an item after adding a new order.
- Helps maintain accurate item quantities without manual intervention.

### Task 5: Trigger for Email Validation on User Update
- Creates a trigger to reset the `valid_email` attribute only when the email has been changed for a user.
- Offers a mechanism to validate user emails directly in the database.

### Task 6: Stored Procedure to Add Bonus Correction for Students
- Develops a stored procedure (`AddBonus`) that adds a new correction for a student.
- Takes inputs for `user_id`, `project_name`, and `score`, incorporating logic to handle existing and new projects.

### Task 7: Stored Procedure for Computing Average Score
- Implements a stored procedure (`ComputeAverageScoreForUser`) to compute and store the average score for a student.
- Takes `user_id` as input and calculates the average score based on provided corrections.

### Task 8: Indexing for Simple Search Optimization
- Creates an index (`idx_name_first`) on a table (`names`) to optimize simple search based on the first letter of the name.
- Improves search efficiency for queries filtering names starting with specific letters.

### Task 9: Indexing for Search and Score Optimization
- Enhances search performance by creating an index (`idx_name_first_score`) on a table (`names`) using the first letter of the name and the score.
- Optimizes search queries filtering names and specific score ranges.

### Task 10: Function for Safe Division
- Develops a function (`SafeDiv`) that performs division and handles zero division errors.
- Takes two arguments (`a`, `b`) and returns `a / b` or 0 if `b` is equal to 0.

### Task 11: View Creation for Students Needing Meetings
- Creates a view (`need_meeting`) listing students needing meetings based on specific criteria (`score < 80` and no recent meetings).
- Offers a quick glance at students requiring attention or follow-up meetings.

### Task 12: Stored Procedure for Average Weighted Score
- Designs a stored procedure (`ComputeAverageWeightedScoreForUser`) to compute and store the average weighted score for a student.
- Considers weights assigned to different projects for calculating the average score.

## Files and Execution
- Each task's SQL script is provided in the respective files within this repository.
- To execute a task, use the provided SQL files and ensure a MySQL environment setup for testing.

## Note
- The tasks are designed for educational purposes and demonstrate various MySQL functionalities and best practices.
