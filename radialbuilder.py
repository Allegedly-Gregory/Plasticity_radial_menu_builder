import json
import difflib

class RadialMenuBuilder:
    def __init__(self):
        self.menu_config = {
            "name": "",
            "command": "",
            "items": []
        }

    def set_title(self, title):
        self.menu_config["name"] = title
        self.menu_config["command"] = f"{title}:menu"

    def add_slice(self, command, label):
        icon = str(command[8:])
        # label = str(command[8:]).replace(":", "-")
        slice_config = {
            "command": command,
            "icon": icon,
            "label": label
        }
        self.menu_config["items"].append(slice_config)

    def generate_label(self, command):
        words = [word.capitalize() for word in command[8:].split('-')]
        return ' '.join(words)

    def export_to_json(self):
        if not self.menu_config["name"]:
            print("Error: Please set a title for the radial menu.")
            return

        json_filename = f"{self.menu_config['name']}.radial.json"

        with open(json_filename, 'w') as json_file:
            json.dump(self.menu_config, json_file, indent=2)

        print(f"Radial menu configuration saved to {json_filename}")

    def build_menu_interactively(self):
        title = input("Enter the title for the radial menu: ")
        self.set_title(title)

        while True:
            print("Available commands:")
            for i, command in enumerate(self.available_commands, start=1):
                print(f"{i}. {command}")

            partial_input = input("Select commands by number, name, or range (e.g., 1,3,5-8), or type at least 3 letters to narrow down: ").lower()

            if ',' in partial_input or '-' in partial_input:
                # User entered a list or range
                selected_numbers = self.parse_selection(partial_input)
                for selected_number in selected_numbers:
                    self.handle_selection(selected_number)
            elif partial_input.isdigit():
                # User entered a single number
                selected_number = int(partial_input)
                self.handle_selection(selected_number)
            elif len(partial_input) >= 3:
                # User started typing, narrow down the list
                matching_commands = self.get_matching_commands(partial_input)
                if matching_commands:
                    print("Matching commands:")
                    for i, command in enumerate(matching_commands, start=1):
                        print(f"{i}. {command}")

                    selected_numbers_input = input("Select commands by number or range (e.g., 1,3,5-8): ")
                    matching_numbers = self.parse_selection(selected_numbers_input, matching_commands)
                    for selected_number in matching_numbers:
                        self.handle_selection(selected_number, matching_commands)
                elif partial_input.startswith('fin'):
                    self.export_to_json()
                    print("Exiting the menu builder.")
                    return  # Exit the loop
                else:
                    print("No matching commands found.")
            else:
                print("Invalid input. Please enter numbers, names, or ranges (e.g., 1,3,5-8 or 'finished').")

    def handle_selection(self, selected_number, command_list=None):
        if command_list is None:
            command_list = self.available_commands

        try:
            selected_index = int(selected_number) - 1
            if 0 <= selected_index < len(command_list):
                selected_command = command_list[selected_index]
                label = input(f"Enter the label for '{selected_command}' (or press Enter to use the default): ")
                if not label:
                    label = self.generate_label(selected_command)
                self.add_slice(selected_command, label)
            else:
                raise ValueError()
        except ValueError:
            print("Invalid number. Please choose a number from the list.")

    def get_matching_commands(self, partial_input):
        close_matches = difflib.get_close_matches(partial_input, self.available_commands, n=5, cutoff=0.6)
        return [cmd for cmd in self.available_commands if self.match_substring(partial_input, cmd)]

    def match_substring(self, partial_input, full_string):
        partial_input = partial_input.lower()
        full_string = full_string.lower()
        return partial_input in full_string

    def parse_selection(self, selection_input, command_list=None):
        if ',' in selection_input:
            # User entered a comma-separated list
            selection_numbers = selection_input.split(',')
        elif '-' in selection_input:
            # User entered a range
            start, end = map(int, selection_input.split('-'))
            selection_numbers = map(str, range(start, end + 1))
        else:
            # User entered a single number
            selection_numbers = [selection_input]

        if command_list is None:
            return selection_numbers
        else:
            # Check if the entered numbers are valid indices in the command list
            valid_numbers = [num for num in selection_numbers if 1 <= int(num) <= len(command_list)]
            return valid_numbers

    @property
    def available_commands(self):
        return [
"command:alternative-duplicate",
"command:boolean",
"command:bridge",
"command:bridge-curve",
"command:bridge-edge",
"command:bridge-surface",
"command:bridge-vertex",
"command:center-box",
"command:center-circle",
"command:center-point-arc",
"command:center-rectangle",
"command:check",
"command:constrained-surface",
"command:control-point-curve",
"command:convert-vertex",
"command:corner-box",
"command:corner-rectangle",
"command:create-solid-from-faces",
"command:create-viewspace-construction-plane",
"command:create-viewspace-construction-plane-at-origin",
"command:curve",
"command:curve-array",
"command:cut",
"command:cut-curve",
"command:cylinder",
"command:delete",
"command:delete-control-point",
"command:delete-edge",
"command:delete-face",
"command:delete-group",
"command:delete-redundant-topology",
"command:deselect-all",
"command:dissolve",
"command:dissolve-face",
"command:draft-face",
"command:duplicate",
"command:duplicate-curve-and-project",
"command:unjoin",
"command:unjoin-curves",
"command:unjoin-faces",
"command:unjoin-shells",
"command:export-cad",
"command:export-obj",
"command:export-stl",
"command:extend",
"command:extend-curve",
"command:extend-edge",
"command:extend-sheet",
"command:extrude",
"command:fillet",
"command:fillet-curve",
"command:fillet-shell",
"command:fillet-vertex",
"command:find-boundary-edges",
"command:focus",
"command:freestyle-mirror",
"command:freestyle-move",
"command:freestyle-move-item",
"command:freestyle-offset-planar-curve",
"command:freestyle-rotate",
"command:freestyle-rotate-item",
"command:freestyle-scale",
"command:freestyle-scale-item",
"command:group-selected",
"command:hide-selected",
"command:hide-unselected",
"command:hollow",
"command:hollow-solid",
"command:imprint",
"command:imprint-body-body",
"command:imprint-curve-body",
"command:invert-hidden",
"command:invert-selection",
"command:isoparam",
"command:join",
"command:join-curves",
"command:join-sheets",
"command:line",
"command:lock-selected",
"command:loft",
"command:loft-guide",
"command:match-face",
"command:mirror",
"command:move",
"command:move-control-point",
"command:move-empty",
"command:move-face",
"command:move-item",
"command:offset-curve",
"command:offset-edge",
"command:offset-face",
"command:offset-face-loop",
"command:offset-planar-curve",
"command:offset-region",
"command:patch",
"command:pipe",
"command:place",
"command:polygon",
"command:project",
"command:project-body-body",
"command:project-curve-body",
"command:project-curve-curve",
"command:push-face",
"command:radial-array",
"command:rebuild",
"command:rebuild-curve",
"command:rebuild-face",
"command:rectangular-array",
"command:refillet-face",
"command:remove-fillets-from-shell",
"command:remove-item",
"command:remove-material",
"command:revolve",
"command:rotate",
"command:rotate-control-point",
"command:rotate-empty",
"command:rotate-face",
"command:rotate-item",
"command:scale",
"command:scale-control-point",
"command:scale-empty",
"command:scale-face",
"command:scale-item",
"command:select-adjacent",
"command:select-all",
"command:select-all-curves",
"command:set-material",
"command:smart-command",
"command:sphere",
"command:spiral",
"command:split-segment",
"command:subdivide-curve",
"command:sweep",
"command:sweep-tool",
"command:text",
"command:thicken",
"command:thicken-sheet",
"command:three-point-arc",
"command:three-point-box",
"command:three-point-circle",
"command:three-point-rectangle",
"command:trim",
"command:two-point-circle",
"command:ungroup-selected",
"command:unhide-all",
"command:untrim",
"command:unwrap-face",
"command:wrap-face",
"edit:repeat-last-command",
"file:export",
"file:import",
"file:new",
"file:open",
"file:save",
"file:save-as",
"file:save-as-startup",
"file:save-version",
"selection:convert:edge",
"selection:convert:face",
"selection:convert:solid",
"selection:mode:set:all",
"selection:mode:set:control-point",
"selection:mode:set:edge",
"selection:mode:set:face",
"selection:mode:set:solid",
"selection:toggle:control-point",
"selection:toggle:edge",
"selection:toggle:face",
"selection:toggle:solid",
"snaps:toggle-grid",
"snaps:toggle-snaps",
"view:radial:selection:mode",
"view:radial:viewport:settings",
"view:sidebar:toggle",
"viewport:cplane:selection",
"viewport:focus",
"viewport:grid:decr",
"viewport:grid:incr",
"viewport:navigate:back",
"viewport:navigate:bottom",
"viewport:navigate:front",
"viewport:navigate:left",
"viewport:navigate:right",
"viewport:navigate:selection",
"viewport:navigate:top",
"viewport:toggle-edges",
"viewport:toggle-faces",
"viewport:toggle-orthographic",
"viewport:toggle-overlays",
"viewport:toggle-x-ray"
        ]

# Example usage:
if __name__ == "__main__":
    radial_menu_builder = RadialMenuBuilder()
    radial_menu_builder.build_menu_interactively()
