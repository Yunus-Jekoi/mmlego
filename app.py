import streamlit as st

# Initialize session state for blocks
if 'blocks' not in st.session_state:
    st.session_state['blocks'] = []

# Function to add a block
def add_block(goal, color):
    st.session_state['blocks'].append({'goal': goal, 'color': color})

# Function to remove a block
def remove_block(index):
    if 0 <= index < len(st.session_state['blocks']):
        st.session_state['blocks'].pop(index)

# Function to edit a block
def edit_block(index, goal, color):
    if 0 <= index < len(st.session_state['blocks']):
        st.session_state['blocks'][index] = {'goal': goal, 'color': color}

# Main title and instructions
st.title("Monk Mode - LEGO Goals")
st.write("Click on a block to edit or remove it.")

# Center-aligning the entire app
st.markdown("""
    <style>
    .stApp {
        display: flex;
        justify-content: center;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar for adding/editing blocks
with st.sidebar:
    st.header("Add/Edit Block")
    block_index = st.selectbox("Select Block", ["Add New"] + [f"Block {i+1}" for i in range(len(st.session_state['blocks']))], 0)
    if block_index == "Add New":
        goal = st.text_input("Enter Goal")
        color = st.color_picker("Block Color", "#FFD700")
        if st.button("Add Block"):
            if goal:
                add_block(goal, color)
    elif block_index != 0:
        index = int(block_index.split()[-1]) - 1
        goal = st.text_input("Enter Goal", st.session_state['blocks'][index]['goal'])
        color = st.color_picker("Block Color", st.session_state['blocks'][index]['color'])
        edit_block(index, goal, color)

# Display LEGO blocks
for i, block in enumerate(st.session_state['blocks']):
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if st.button(f"Block {i+1}", key=f"block-{i}", help=f"Click to edit Block {i+1}"):
            goal = st.text_input("Edit Goal", block['goal'])
            color = st.color_picker("Edit Color", block['color'])
            if st.button("Save Changes"):
                edit_block(i, goal, color)
        else:
            st.markdown(f"""
                <div style="display: flex; justify-content: center; align-items: center; height: 120px;
                            width: 200px; background-color: {block['color']}; border-radius: 10px; box-shadow: 3px 3px 8px rgba(0,0,0,0.2);
                            cursor: pointer; transition: transform 0.2s ease-in-out;">
                    {block['goal']}
                </div>
            """, unsafe_allow_html=True)
    with col2:
        pass  # No need to display goal or color
    with col3:
        if st.button(f"Delete Block {i}"):
            remove_block(i)

# Displaying this note to guide the user
st.sidebar.markdown("* You can add, edit, and remove LEGO blocks using the sidebar.")
