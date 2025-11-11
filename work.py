import streamlit as st
import random

def delegate_rows(total_rows):
    # People and their corresponding colors
    people_colors = {
        "Jim": "Yellow",
        "Kristy": "Orange",
        "Austin": "Purple",
        "Kiran": "Green"
    }

    people = list(people_colors.keys())
    num_people = len(people)

    assignable_rows = total_rows - 1  # Subtract 1 for header row

    base_rows = assignable_rows // num_people
    remainder = assignable_rows % num_people

    extra_people = random.sample(people, remainder) if remainder > 0 else []

    assignments = {}
    current_row = 2  # Start at row 2 since row 1 is the header

    for person in people:
        rows_for_this_person = base_rows + (1 if person in extra_people else 0)
        start_row = current_row
        end_row = current_row + rows_for_this_person - 1
        assignments[person] = (start_row, end_row, rows_for_this_person)
        current_row = end_row + 1

    st.write(f"Each person has at least **{base_rows}** rows today.\n")

    for person, (start, end, count) in assignments.items():
        color = people_colors[person]
        st.write(f"**{person}** ({color}): rows {start}–{end}")

def main():
    st.title("Row Delegation App")

    total_rows = st.number_input("Enter the total number of rows (including header):", min_value=1, step=1)

    if st.button("Delegate Rows"):
        delegate_rows(total_rows)

if __name__ == "__main__":
    main()
