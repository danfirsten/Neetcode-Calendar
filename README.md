
# NeetCode Roadmap Calendar Generator

This Python script generates a study calendar based on the NeetCode roadmap, organizing tasks to be completed on weekdays. It outputs an `.ics` file that can be imported into any calendar application (e.g., Google Calendar, Outlook) for structured tracking of your study schedule.

---

## Features

- **Tasks Only on Weekdays**: Automatically skips weekends, extending the timeline if necessary.
- **Customizable Topics**: Covers foundational, intermediate, and advanced data structures and algorithms.
- **Exportable Format**: Outputs an `.ics` file for easy import into calendar apps.
- **Structured Events**: Each event includes:
  - A title for the topic.
  - A description with detailed tasks to complete.
  - A default duration of 2 hours (customizable).

---

## Requirements

1. **Python 3.7 or higher**
2. **`ics` Library**: Install it using the following command:
   ```bash
   pip install ics 
   ```
 
 ---

## How to Use

-   **Download or Copy the Script**: Save the script to a `.py` file (e.g., `calendar_generator.py`).
-   **Run the Script**: Execute the script in your terminal or IDE:
    
    ```bash   
    `python calendar_generator.py
    ``` 
    
-   **Import the Calendar**: The script generates a file named `NeetCode_Roadmap_Calendar.ics`. Import this file into your preferred calendar app:
    -   **Google Calendar**:
	    -   Go to `Settings > Add Calendar > Create New Calendar`
	    -   Name the new calendar ( e.g. 'Interview Prep') 
        -   Go to `Settings > Import & Export > Import`.
	        -  Make sure your new calendar is selected
        -   Upload the `.ics` file.
    -   **Outlook**:
        -   Go to `File > Open & Export > Import/Export`.
        -   Select the `.ics` file to import.

---

## Customization

-   **Adjust Task Duration**: Modify the event duration by changing the `timedelta(hours=2)` parameter.
-   **Change Start Date**: Update the `start_date` variable to set a custom starting date.
-   **Add/Edit Topics**: Modify the `tasks` list in the script to add new topics or adjust existing ones.

---

## License

This script is open-source and is provided under the MIT License. You are free to use, modify, and distribute it for personal and educational purposes.

