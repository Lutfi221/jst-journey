import os
import re
import subprocess
import pathlib
import shutil
import time

# --- Configuration ---
HOMEWORK_DIR = pathlib.Path("./activities/2025-05-17/")
OUTPUT_MD_FILE = pathlib.Path("expected-results.md")
IMAGE_OUTPUT_DIR = pathlib.Path("expected_turtle_images")
TEMP_PS_FILE = IMAGE_OUTPUT_DIR / "_temp_turtle_image.ps"

# Ghostscript command - try Windows version first, then generic
GS_COMMANDS = ["gswin64c", "gs"]

# --- Helper Functions ---

def find_gs_command():
    """Finds a working Ghostscript command."""
    for cmd in GS_COMMANDS:
        try:
            subprocess.run([cmd, "-h"], capture_output=True, check=True, timeout=5)
            print(f"Found Ghostscript command: {cmd}")
            return cmd
        except (subprocess.CalledProcessError, FileNotFoundError, subprocess.TimeoutExpired):
            continue
    return None

GS_COMMAND = find_gs_command()

import pathlib
import re # Still used for filename sanitization

# --- State constants for the parser ---
STATE_SEARCHING_STEP = 0
STATE_IN_STEP_SEARCHING_SOLUTION_KEYWORD = 1
STATE_IN_SOLUTION_KEYWORD_SEARCHING_DETAILS_OPEN = 2
STATE_IN_DETAILS_SEARCHING_PYTHON_FENCE_OPEN = 3
STATE_IN_PYTHON_BLOCK = 4
STATE_IN_PYTHON_BLOCK_ENDED_SEARCHING_DETAILS_CLOSE = 5

def extract_solutions(md_filepath: pathlib.Path):
    """
    Extracts solution code snippets from a Markdown file by reading line by line.
    Yields (step_title, python_code, base_image_filename)
    """
    print(f"Processing Markdown file (line-by-line): {md_filepath.name}")
    
    current_step_title = None
    current_python_code_lines = []
    state = STATE_SEARCHING_STEP
    
    file_stem = md_filepath.stem
    yielded_count = 0

    with open(md_filepath, "r", encoding="utf-8") as f:
        for line_number, raw_line in enumerate(f, 1):
            line = raw_line.strip() # Process the stripped line for logic
                                    # but store raw_line (or rstripped raw_line) for code blocks

            # Handle new step ## irrespective of current state (acts as a reset for malformed previous step)
            if line.startswith("## "):
                # If a new step starts, any ongoing collection for a previous step is abandoned if not complete
                current_step_title = line[3:].strip()
                state = STATE_IN_STEP_SEARCHING_SOLUTION_KEYWORD
                current_python_code_lines = [] # Reset for new step
                # print(f"  L{line_number}: Found Step: {current_step_title}")
                continue # Consume this line as the step header

            # --- State-specific processing ---
            if state == STATE_SEARCHING_STEP:
                # Already handled by the global "## " check above.
                # This state is effectively just waiting for a "## ".
                pass

            elif state == STATE_IN_STEP_SEARCHING_SOLUTION_KEYWORD:
                if line.startswith("### Solution"):
                    state = STATE_IN_SOLUTION_KEYWORD_SEARCHING_DETAILS_OPEN
                    # print(f"  L{line_number}: Found Solution keyword for '{current_step_title}'")
            
            elif state == STATE_IN_SOLUTION_KEYWORD_SEARCHING_DETAILS_OPEN:
                if line.lower() == "<details>": # Using .lower() for HTML tags
                    state = STATE_IN_DETAILS_SEARCHING_PYTHON_FENCE_OPEN
                    # print(f"  L{line_number}: Found <details> for '{current_step_title}'")
                # If we see "### Solution" again without <details>, it's a bit odd,
                # but current logic would just stay, waiting for <details>.
                # If not <details>, it won't proceed to find python code.

            elif state == STATE_IN_DETAILS_SEARCHING_PYTHON_FENCE_OPEN:
                # We expect <summary> here, but the core requirement is ```python inside <details>
                # Ignoring <summary> presence for this parser's objective.
                if line == "```python":
                    state = STATE_IN_PYTHON_BLOCK
                    current_python_code_lines = [] # Start fresh for this code block
                    # print(f"  L{line_number}: Found ```python for '{current_step_title}'")
                elif line.lower() == "</details>": # Details tag closed before python block found
                    # print(f"  L{line_number}: Found </details> prematurely for '{current_step_title}'. Resetting to look for Solution Keyword.")
                    state = STATE_IN_STEP_SEARCHING_SOLUTION_KEYWORD # Go back to looking for solution for current step
                                                                # or wait for a new step if this one is done.


            elif state == STATE_IN_PYTHON_BLOCK:
                if line == "```": # End of python code block
                    if current_step_title and current_python_code_lines:
                        python_code = "\n".join(current_python_code_lines)
                        
                        # Filename sanitization logic (adapted from original script)
                        step_num_match = re.search(r"Step (\d+)", current_step_title, re.IGNORECASE)
                        step_num_str = f"step-{step_num_match.group(1)}" if step_num_match else "step-unknown"
                        
                        # Extract the descriptive part of the title after "Step X:"
                        title_part_match = re.match(r"Step \d+:\s*(.*)", current_step_title, re.IGNORECASE)
                        descriptive_title_part = title_part_match.group(1).strip() if title_part_match else current_step_title

                        sanitized_title_part = re.sub(r'[^\w\s-]', '', descriptive_title_part).strip()
                        sanitized_title_part = re.sub(r'[-\s]+', '-', sanitized_title_part).lower()
                        
                        base_image_filename = f"{file_stem}-{step_num_str}-{sanitized_title_part}-solution"
                        if not sanitized_title_part: # Fallback if title part becomes empty
                             base_image_filename = f"{file_stem}-{step_num_str}-solution"

                        # print(f"  L{line_number}: Yielding solution for: {current_step_title}")
                        yield current_step_title, python_code, base_image_filename
                        yielded_count += 1
                        
                        current_python_code_lines = [] # Clear after yielding
                        state = STATE_IN_PYTHON_BLOCK_ENDED_SEARCHING_DETAILS_CLOSE
                    else:
                        # This might happen if ```python was found but no step title was active (should be prevented by logic)
                        # or if code block was empty (which is fine).
                        # print(f"  L{line_number}: Found ``` but current_step_title or code lines are missing/empty. Resetting.")
                        state = STATE_IN_DETAILS_SEARCHING_PYTHON_FENCE_OPEN # Or some other reset
                else:
                    # Add the raw line (with only trailing newline removed) to preserve indentation
                    current_python_code_lines.append(raw_line.rstrip('\n'))
            
            elif state == STATE_IN_PYTHON_BLOCK_ENDED_SEARCHING_DETAILS_CLOSE:
                if line.lower() == "</details>":
                    # print(f"  L{line_number}: Found </details> confirming end of solution block for '{current_step_title}'.")
                    # Solution block fully processed. Reset to look for the next step's ## header.
                    state = STATE_SEARCHING_STEP 
                    # current_step_title = None # No, keep current_step_title until a new ## is found
                                             # this state means we are done with *this* solution block for the current step
                                             # but there might be other text or even another solution block (unlikely per problem spec)
                                             # The main ## handler at the top will reset current_step_title.
                                             # Effectively, after </details> we go back to looking for ### Solution or a new ## Step.
                                             # So, STATE_IN_STEP_SEARCHING_SOLUTION_KEYWORD is more appropriate here.
                    state = STATE_IN_STEP_SEARCHING_SOLUTION_KEYWORD

    if yielded_count == 0:
        print(f"  No solution code blocks conforming to the expected structure were found in {md_filepath.name} using line-by-line parsing.")

def generate_image_from_code(python_code: str, ps_filepath: pathlib.Path, png_filepath: pathlib.Path):
    """
    Executes turtle code, saves to PS, and converts to PNG.
    Returns True on success, False on failure.
    """
    if not GS_COMMAND:
        print("Error: Ghostscript command not found. Cannot convert PS to PNG.")
        return False

    # Modify code: remove turtle.done(), add saving and closing
    modified_code = python_code.replace("turtle.done()", "# turtle.done() removed by script")
    
    # Ensure turtle is available in the exec scope if not imported by snippet
    # Snippets provided do import turtle, so this is mostly a safeguard or for other contexts
    # if "import turtle" not in modified_code:
    #    modified_code = "import turtle\n" + modified_code
    # if "import random" not in modified_code and "random." in modified_code:
    #    modified_code = "import random\n" + modified_code


    # Add saving logic.
    # It's crucial to get the screen instance. Some snippets assign it to 's', others don't.
    # We'll try to get it generally.
    # Also, tracer(0,0) means we need update() before saving.
    save_code = f"""
# Added by script for saving
_screen_to_save = turtle.Screen()
_screen_to_save.update() # Ensure drawing is complete if tracer(0,0) was used
_canvas_to_save = _screen_to_save.getcanvas()
_canvas_to_save.postscript(file=r"{ps_filepath.resolve()}", colormode='color')
turtle.bye() # Close turtle window
"""
    modified_code += save_code
    
    # print("\n--- Modified code to execute ---")
    # print(modified_code)
    # print("------------------------------\n")

    try:
        # Using a fresh globals/locals dict for each exec might be safer
        # to avoid pollution, but turtle itself has global state.
        # The key is turtle.bye() and re-initialization if needed.
        global_namespace = {} # Fresh namespace
        exec(modified_code, global_namespace)
        
        # Brief pause for file system
        time.sleep(0.5) 

        if not ps_filepath.exists() or ps_filepath.stat().st_size == 0:
            print(f"Error: PostScript file {ps_filepath.name} was not created or is empty.")
            return False

    except Exception as e:
        print(f"Error executing Turtle code for {png_filepath.stem}: {e}")
        # Clean up potentially empty PS file
        if ps_filepath.exists() and ps_filepath.stat().st_size == 0:
            try:
                ps_filepath.unlink()
            except OSError:
                pass # Ignore if it can't be deleted immediately
        return False

    # Convert PS to PNG
    try:
        # Ensure output directory for PNG exists
        png_filepath.parent.mkdir(parents=True, exist_ok=True)

        # Ghostscript command
        # -dSAFER is good practice
        # -r150 for reasonable resolution/file size balance for web
        gs_args = [
            GS_COMMAND,
            "-dNOPAUSE",
            "-dBATCH",
            "-dSAFER",
            "-sDEVICE=pngalpha", # For transparency
            "-r150",
            f"-sOutputFile={png_filepath.resolve()}",
            str(ps_filepath.resolve())
        ]
        print(f"  Converting PS to PNG: {png_filepath.name}")
        process = subprocess.run(gs_args, capture_output=True, text=True, timeout=30)
        if process.returncode != 0:
            print(f"Error converting PS to PNG for {png_filepath.stem}:")
            print(f"  GS Output: {process.stdout}")
            print(f"  GS Error: {process.stderr}")
            return False
        
        # Brief pause for file system
        time.sleep(0.2) 
        if not png_filepath.exists() or png_filepath.stat().st_size == 0:
            print(f"Error: PNG file {png_filepath.name} was not created or is empty after conversion.")
            return False

        return True
    except subprocess.TimeoutExpired:
        print(f"Error: Ghostscript timed out while converting {ps_filepath.name}")
        return False
    except Exception as e:
        print(f"Error during PS to PNG conversion for {png_filepath.stem}: {e}")
        return False
    finally:
        # Clean up the temporary PS file
        if ps_filepath.exists():
            try:
                ps_filepath.unlink()
            except OSError:
                print(f"Warning: Could not delete temporary PS file {ps_filepath.name}")


# --- Main Script ---
def main():
    if not HOMEWORK_DIR.exists() or not HOMEWORK_DIR.is_dir():
        print(f"Error: Homework directory '{HOMEWORK_DIR}' not found.")
        return

    if not GS_COMMAND:
        print("Critical Error: Ghostscript is not installed or not found in PATH.")
        print("Please install Ghostscript and ensure it's accessible.")
        print(f"(Tried: {', '.join(GS_COMMANDS)})")
        return

    # Create/clear image output directory
    if IMAGE_OUTPUT_DIR.exists():
        # Optional: Clear old images. Be careful with this.
        # For safety, we'll just let it overwrite or add.
        # shutil.rmtree(IMAGE_OUTPUT_DIR)
        pass
    IMAGE_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # Ensure temp PS file's directory exists for its path resolution
    TEMP_PS_FILE.parent.mkdir(parents=True, exist_ok=True)


    md_files = sorted(list(HOMEWORK_DIR.glob("*.md")))
    if not md_files:
        print(f"No Markdown files found in {HOMEWORK_DIR}")
        return

    generated_content = ["# Expected Turtle Art Results\n\n"]

    for md_file_path in md_files:
        generated_content.append(f"## Results from: `{md_file_path.name}`\n\n")
        
        for step_title, code, base_img_name in extract_solutions(md_file_path):
            png_filename = base_img_name + ".png"
            png_filepath_abs = IMAGE_OUTPUT_DIR / png_filename
            
            # Relative path for Markdown link
            png_filepath_rel = IMAGE_OUTPUT_DIR.name + "/" + png_filename

            generated_content.append(f"### {step_title}\n\n")
            
            print(f"Attempting to generate image: {png_filepath_abs.name}")
            if generate_image_from_code(code, TEMP_PS_FILE, png_filepath_abs):
                generated_content.append(f"![{step_title}]({png_filepath_rel})\n\n")
                print(f"  Successfully generated {png_filepath_abs.name}")
            else:
                generated_content.append(f"*Failed to generate image for {step_title}*\n\n")
                print(f"  Failed to generate {png_filepath_abs.name}")
            
            # A small delay to help turtle reset between executions if necessary,
            # and to prevent overwhelming the system.
            time.sleep(0.5) 

    with open(OUTPUT_MD_FILE, "w", encoding="utf-8") as f:
        f.write("".join(generated_content))

    print(f"\nGenerated '{OUTPUT_MD_FILE}' and images in '{IMAGE_OUTPUT_DIR}'.")
    if not GS_COMMAND:
         print("\nWARNING: Ghostscript was not found. PNG conversion might have failed for all images.")

if __name__ == "__main__":
    main()