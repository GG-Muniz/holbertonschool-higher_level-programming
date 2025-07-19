#!/usr/bin/env python3
"""
Task 00: Template Generation with Error Handling
"""

import os


def generate_invitations(template, attendees):
    """
    Generate invitation files from a template and list of attendees.
    
    Args:
        template (str): The template string with placeholders
        attendees (list): List of dictionaries containing attendee data
    
    Returns:
        None: Creates output files or logs errors
    """
    # Check if template is a string
    if not isinstance(template, str):
        print("Error: Template must be a string")
        return
    
    # Check if attendees is a list of dictionaries
    if not isinstance(attendees, list):
        print("Error: Attendees must be a list")
        return
    
    # Check if template is empty
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    
    # Check if attendees list is empty
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    # Process each attendee
    for i, attendee in enumerate(attendees, 1):
        if not isinstance(attendee, dict):
            print(f"Error: Attendee at index {i-1} is not a dictionary")
            continue
        
        # Create a copy of the template for this attendee
        personalized_template = template
        
        # Replace placeholders with attendee data
        # Use get() method to handle missing keys with "N/A" as default
        personalized_template = personalized_template.replace("{name}", str(attendee.get("name", "N/A")))
        personalized_template = personalized_template.replace("{event_title}", str(attendee.get("event_title", "N/A")))
        personalized_template = personalized_template.replace("{event_date}", str(attendee.get("event_date", "N/A")))
        personalized_template = personalized_template.replace("{event_location}", str(attendee.get("event_location", "N/A")))
        
        # Write to output file
        output_filename = f"output_{i}.txt"
        try:
            with open(output_filename, 'w') as file:
                file.write(personalized_template)
        except Exception as e:
            print(f"Error writing file {output_filename}: {e}")


if __name__ == "__main__":
    # Example usage
    template_content = """Hello {name},

You are invited to the {event_title} on {event_date} at {event_location}.

We look forward to your presence.

Best regards,
Event Team"""

    attendees = [
        {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
    ]

    generate_invitations(template_content, attendees) 