"""The interface code is here, encapsulated into a class."""

import copy
import json
import re
import os
import sys
from tkinter import ttk, N, S, E, W, BooleanVar, StringVar, Menu
import comics

class Interface:
    """Creates and manages the interface of the program."""
    def __init__(self, master):
        self.validate_entry_wrapper = (master.register(self.validate_entry), "%P", "%V")

        # Set up root.
        self.master = master
        self.master.minsize(800, 500)
        self.master.geometry('800x400+50+50')
        menubar = Menu(self.master)
        self.master["menu"] = menubar
        master.title("Comic Downloader")

        # Set up style rules for disabled entry fields.
        s = ttk.Style()
        s.map('TEntry', background=[('disabled', '#d9d9d9')])

        # Set up the two main frames.
        self.content_frame = ttk.Frame(master, padding=(3, 3, 12, 12))
        self.input_frame = ttk.Frame(
            self.content_frame,
            borderwidth=5,
            padding=(5, 5, 5, 5),
            relief="ridge"
        )

        # Entry labels.
        self.abstruse_lbl = ttk.Label(self.input_frame, text="Abstruse Goose")
        self.cyanide_lbl = ttk.Label(self.input_frame, text="Cyanide & Happiness")
        self.lfg_lbl = ttk.Label(self.input_frame, text="Looking For Group")
        self.lovenstein_lbl = ttk.Label(self.input_frame, text="Lovenstein")
        self.stick_lbl = ttk.Label(self.input_frame, text="Order of the Stick")
        self.chapel_lbl = ttk.Label(self.input_frame, text="The Chapel")
        self.wukrii_lbl = ttk.Label(self.input_frame, text="Wukrii")
        self.xkcd_lbl = ttk.Label(self.input_frame, text="XKCD")

        # String variables for entry fields.
        self.abstruse_entry_value = StringVar(value=self.entry_value("ABSTRUSE"))
        self.cyanide_entry_value = StringVar(value=self.entry_value("CYANIDE"))
        self.lfg_entry_value = StringVar(value=self.entry_value("LFG"))
        self.lovenstein_entry_value = StringVar(value=self.entry_value("LOVENSTEIN"))
        self.stick_entry_value = StringVar(value=self.entry_value("STICK"))
        self.chapel_entry_value = StringVar(value=self.entry_value("CHAPEL"))
        self.wukrii_entry_value = StringVar(value=self.entry_value("WUKRII"))
        self.xkcd_entry_value = StringVar(value=self.entry_value("XKCD"))

        # Entry fields
        self.abstruse_entry = ttk.Entry(
            self.input_frame,
            state=self.entry_state(comic="ABSTRUSE"),
            textvariable=self.abstruse_entry_value,
            justify="right",
            validate="all",
            validatecommand=self.validate_entry_wrapper
        )
        self.cyanide_entry = ttk.Entry(
            self.input_frame,
            state=self.entry_state(comic="CYANIDE"),
            textvariable=self.cyanide_entry_value,
            justify="right",
            validate="all",
            validatecommand=self.validate_entry_wrapper
        )
        self.lfg_entry = ttk.Entry(
            self.input_frame,
            state=self.entry_state(comic="LFG"),
            textvariable=self.lfg_entry_value,
            justify="right",
            validate="all",
            validatecommand=self.validate_entry_wrapper
        )
        self.lovenstein_entry = ttk.Entry(
            self.input_frame,
            state=self.entry_state(comic="LOVENSTEIN"),
            textvariable=self.lovenstein_entry_value,
            justify="right",
            validate="all",
            validatecommand=self.validate_entry_wrapper
        )
        self.stick_entry = ttk.Entry(
            self.input_frame,
            state=self.entry_state(comic="STICK"),
            textvariable=self.stick_entry_value,
            justify="right",
            validate="all",
            validatecommand=self.validate_entry_wrapper
        )
        self.chapel_entry = ttk.Entry(
            self.input_frame,
            state=self.entry_state(comic="CHAPEL"),
            textvariable=self.chapel_entry_value,
            justify="right",
            validate="all",
            validatecommand=self.validate_entry_wrapper
        )
        self.wukrii_entry = ttk.Entry(
            self.input_frame,
            state=self.entry_state(comic="WUKRII"),
            textvariable=self.wukrii_entry_value,
            justify="right",
            validate="all",
            validatecommand=self.validate_entry_wrapper
        )
        self.xkcd_entry = ttk.Entry(
            self.input_frame,
            state=self.entry_state(comic="XKCD"),
            textvariable=self.xkcd_entry_value,
            justify="right",
            validate="all",
            validatecommand=self.validate_entry_wrapper
        )

        # Boolean variables for status checkboxes.
        self.abstruse_checkbox_value = BooleanVar(value=self.checkbox_value("ABSTRUSE"))
        self.cyanide_checkbox_value = BooleanVar(value=self.checkbox_value("CYANIDE"))
        self.lfg_checkbox_value = BooleanVar(value=self.checkbox_value("LFG"))
        self.lovenstein_checkbox_value = BooleanVar(value=self.checkbox_value("LOVENSTEIN"))
        self.stick_checkbox_value = BooleanVar(value=self.checkbox_value("STICK"))
        self.chapel_checkbox_value = BooleanVar(value=self.checkbox_value("CHAPEL"))
        self.wukrii_checkbox_value = BooleanVar(value=self.checkbox_value("WUKRII"))
        self.xkcd_checkbox_value = BooleanVar(value=self.checkbox_value("XKCD"))

        # Checkboxes for enabling/disabling the entry fields.
        self.abstruse_checkbox = ttk.Checkbutton(
            self.input_frame,
            text="Tick to disable",
            variable=self.abstruse_checkbox_value,
            command=lambda e=self.abstruse_entry, s=self.abstruse_checkbox_value: self.entry_state(entry=e, state=s)
        )
        self.cyanide_checkbox = ttk.Checkbutton(
            self.input_frame,
            text="Tick to disable",
            variable=self.cyanide_checkbox_value,
            command=lambda e=self.cyanide_entry, s=self.cyanide_checkbox_value: self.entry_state(entry=e, state=s)
        )
        self.lfg_checkbox = ttk.Checkbutton(
            self.input_frame,
            text="Tick to disable",
            variable=self.lfg_checkbox_value,
            command=lambda e=self.lfg_entry, s=self.lfg_checkbox_value: self.entry_state(entry=e, state=s)
        )
        self.lovenstein_checkbox = ttk.Checkbutton(
            self.input_frame,
            text="Tick to disable",
            variable=self.lovenstein_checkbox_value,
            command=lambda e=self.lovenstein_entry, s=self.lovenstein_checkbox_value: self.entry_state(entry=e, state=s)
        )
        self.stick_checkbox = ttk.Checkbutton(
            self.input_frame,
            text="Tick to disable",
            variable=self.stick_checkbox_value,
            command=lambda e=self.stick_entry, s=self.stick_checkbox_value: self.entry_state(entry=e, state=s)
        )
        self.chapel_checkbox = ttk.Checkbutton(
            self.input_frame,
            text="Tick to disable",
            variable=self.chapel_checkbox_value,
            command=lambda e=self.chapel_entry, s=self.chapel_checkbox_value: self.entry_state(entry=e, state=s)
        )
        self.wukrii_checkbox = ttk.Checkbutton(
            self.input_frame,
            text="Tick to disable",
            variable=self.wukrii_checkbox_value,
            command=lambda e=self.wukrii_entry, s=self.wukrii_checkbox_value: self.entry_state(entry=e, state=s)
        )
        self.xkcd_checkbox = ttk.Checkbutton(
            self.input_frame,
            text="Tick to disable",
            variable=self.xkcd_checkbox_value,
            command=lambda e=self.xkcd_entry, s=self.xkcd_checkbox_value: self.entry_state(entry=e, state=s)
        )

        # Instructions label.
        self.instructions_msg_text = (
            "For each comic, enter the page you are currently on " +
            "then press done to download all the new comics.\n\n" +
            "Tick a box next to the comic to ignore it.\n\n" +
            "The comics will be downloaded in the same location " +
            "as this program, grouped into folders."
        )
        self.instructions_msg_lbl = ttk.Label(
            self.content_frame,
            wraplength=200,
            justify="left",
            text=self.instructions_msg_text
        )

        # Progress label.
        self.progress_msg_lbl_frame = ttk.Labelframe(
            self.content_frame,
            text="Status",
            width=210,
            height=180
        )
        self.progress_msg_value = StringVar()
        self.progress_msg_lbl = ttk.Label(
            self.progress_msg_lbl_frame,
            wraplength=200,
            justify="center",
            textvariable=self.progress_msg_value
        )

        # Error message label.
        self.error_msg_value = StringVar()
        self.error_msg_text = "Only numbers are accepted as input."
        self.error_msg_lbl = ttk.Label(
            self.input_frame,
            font='TkCaptionFont',
            foreground='red',
            textvariable=self.error_msg_value
        )

        # Done and quit buttons.
        self.entries = [
            self.abstruse_entry, self.cyanide_entry, self.lfg_entry,
            self.lovenstein_entry, self.stick_entry, self.chapel_entry,
            self.wukrii_entry, self.xkcd_entry
        ]
        self.checkboxes = [
            self.abstruse_checkbox_value, self.cyanide_checkbox_value,
            self.lfg_checkbox_value, self.lovenstein_checkbox_value,
            self.stick_checkbox_value, self.chapel_checkbox_value,
            self.wukrii_checkbox_value, self.xkcd_checkbox_value
        ]
        self.download = ttk.Button(
            self.content_frame,
            text="Download",
            command=lambda entries=self.entries, checkboxes=self.checkboxes: self.download_and_save(entries, checkboxes)
        )
        self.quit = ttk.Button(self.content_frame, text="Quit", command=self.quit_application)

        # Layout of the main content frame.
        self.content_frame.grid(column=0, row=0, sticky=(N, S, E, W))
        self.instructions_msg_lbl.grid(column=3, columnspan=2, row=0, padx=10, pady=10, sticky=(N))
        self.progress_msg_lbl_frame.grid(column=3, columnspan=2, row=1, padx=10, pady=10, sticky=("nsew"))
        self.progress_msg_lbl_frame.grid_propagate(0)
        self.progress_msg_lbl.place(x=103, y=85, anchor="center")
        self.error_msg_lbl.grid(column=3, columnspan=2, row=2, padx=5, pady=5, sticky=(N))
        self.download.grid(column=3, row=3, padx=5)
        self.quit.grid(column=4, row=3, padx=5)

        # Layout of the input frame, which holds al of the entry fields.
        self.input_frame.grid(column=0, row=0, columnspan=3, rowspan=3, sticky=(N, S, E, W))
        self.abstruse_lbl.grid(column=0, row=0, sticky=(E))
        self.abstruse_entry.grid(column=1, row=0, sticky=(W))
        self.abstruse_checkbox.grid(column=2, row=0, sticky=(W))
        self.cyanide_lbl.grid(column=0, row=1, sticky=(E))
        self.cyanide_entry.grid(column=1, row=1, sticky=(W))
        self.cyanide_checkbox.grid(column=2, row=1, sticky=(W))
        self.lfg_lbl.grid(column=0, row=2, sticky=(E))
        self.lfg_entry.grid(column=1, row=2, sticky=(W))
        self.lfg_checkbox.grid(column=2, row=2, sticky=(W))
        self.lovenstein_lbl.grid(column=0, row=3, sticky=(E))
        self.lovenstein_entry.grid(column=1, row=3, sticky=(W))
        self.lovenstein_checkbox.grid(column=2, row=3, sticky=(W))
        self.stick_lbl.grid(column=0, row=4, sticky=(E))
        self.stick_entry.grid(column=1, row=4, sticky=(W))
        self.stick_checkbox.grid(column=2, row=4, sticky=(W))
        self.chapel_lbl.grid(column=0, row=5, sticky=(E))
        self.chapel_entry.grid(column=1, row=5, sticky=(W))
        self.chapel_checkbox.grid(column=2, row=5, sticky=(W))
        self.wukrii_lbl.grid(column=0, row=6, sticky=(E))
        self.wukrii_entry.grid(column=1, row=6, sticky=(W))
        self.wukrii_checkbox.grid(column=2, row=6, sticky=(W))
        self.xkcd_lbl.grid(column=0, row=7, sticky=(E))
        self.xkcd_entry.grid(column=1, row=7, sticky=(W))
        self.xkcd_checkbox.grid(column=2, row=7, sticky=(W))
        self.error_msg_lbl.grid(column=1, row=8, sticky=(W))

        # Further layout code, adding weights to columns and rows.
        master.columnconfigure(0, weight=1)
        master.rowconfigure(0, weight=1)
        self.content_frame.columnconfigure(0, weight=3)
        self.content_frame.columnconfigure(1, weight=1)
        self.content_frame.columnconfigure(2, weight=1)
        self.content_frame.rowconfigure(0, weight=1)
        self.content_frame.rowconfigure(1, weight=1)
        self.content_frame.rowconfigure(2, weight=1)
        self.input_frame.columnconfigure(2, weight=1)
        self.input_frame.rowconfigure(0, weight=0)

    def quit_application(self):
        """Exits the application."""
        sys.exit()

    def entry_value(self, comic):
        """Sets the values in the entry fields."""
        program_abs_path = os.path.abspath(os.getcwd())
        comic_tracker_path = os.path.join(program_abs_path, "comic_tracker.txt")
        if os.path.exists(comic_tracker_path):
            with open("comic_tracker.txt") as json_file:
                comic_tracker = json.load(json_file)
            return comic_tracker[comic][0]
        else:
            return 1

    def entry_state(self, **kwargs):
        """Modifies the state of each entry field."""
        if "state" in kwargs:
            if kwargs["state"].get():
                kwargs["entry"].configure(state="disabled")
            else:
                kwargs["entry"].configure(state="normal")
        else:
            program_abs_path = os.path.abspath(os.getcwd())
            tracker_file_path = os.path.join(program_abs_path, "comic_tracker.txt")
            if os.path.exists(tracker_file_path):
                with open("comic_tracker.txt") as json_file:
                    comic_tracker = json.load(json_file)
                if comic_tracker[kwargs["comic"]][1]:
                    return "disabled"
                return "normal"
            return "normal"

    def checkbox_value(self, comic):
        """Sets the initial state of the checkboxes."""
        program_abs_path = os.path.abspath(os.getcwd())
        tracker_file_path = os.path.join(program_abs_path, "comic_tracker.txt")
        if os.path.exists(tracker_file_path):
            with open("comic_tracker.txt") as json_file:
                comic_tracker = json.load(json_file)
            return comic_tracker[comic][1]
        else:
            return 0

    def validate_entry(self, newval, op):
        """Validates the code in the entry field. Only numbers allowed."""
        self.error_msg_value.set('')
        valid = re.match('^[0-9]*$', newval) is not None
        if op == "key":
            ok_so_far = re.match('^[0-9]*$', newval) is not None
            if not ok_so_far:
                self.error_msg_value.set(self.error_msg_text)
            return ok_so_far
        if op == 'focusout':
            if not valid:
                self.error_msg_value.set(self.error_msg_text)
        return valid

    def download_and_save(self, entries, checkboxes):
        """Calls the download_comics() funciton and saves comic information as a json file.

        Creates a comic-tracker variable to keep track of comic data, calls download_comics()
        function passing it the comic-tracker variable, and saves the variable as a json file."""
        comic_options = ["ABSTRUSE", "CYANIDE", "LFG", "LOVENSTEIN", "STICK", "CHAPEL", "WUKRII", "XKCD"]
        comic_tracker = dict.fromkeys(comic_options, 0)
        comic_tracker["ABSTRUSE"] = [int(entries[0].get()), checkboxes[0].get()]
        comic_tracker["CYANIDE"] = [int(entries[1].get()), checkboxes[1].get()]
        comic_tracker["LFG"] = [int(entries[2].get()), checkboxes[2].get()]
        comic_tracker["LOVENSTEIN"] = [int(entries[3].get()), checkboxes[3].get()]
        comic_tracker["STICK"] = [int(entries[4].get()), checkboxes[4].get()]
        comic_tracker["CHAPEL"] = [int(entries[5].get()), checkboxes[5].get()]
        comic_tracker["WUKRII"] = [int(entries[6].get()), checkboxes[6].get()]
        comic_tracker["XKCD"] = [int(entries[7].get()), checkboxes[7].get()]

        self.download_comics(comic_tracker)

        with open("comic_tracker.txt", "w")  as outfile:
            json.dump(comic_tracker, outfile)

    def download_comics(self, comic_tracker):
        """Calls webscrapping code, calls update_progress() and updates comic_tracker."""
        program_abs_path = os.path.abspath(os.getcwd())
        comic_tracker_copy = copy.deepcopy(comic_tracker)
        if not comic_tracker["ABSTRUSE"][1]:
            self.update_progress("ABSTRUSE", comic_tracker, comic_tracker_copy)
            self.master.update()
            comic_tracker["ABSTRUSE"][0] = comics.download_abstruse_goose(program_abs_path, comic_tracker["ABSTRUSE"][0])
        if not comic_tracker["CYANIDE"][1]:
            self.update_progress("CYANIDE", comic_tracker, comic_tracker_copy)
            self.master.update()
            comic_tracker["CYANIDE"][0] = comics.download_cyanide_and_happiness(program_abs_path, comic_tracker["CYANIDE"][0])
        if not comic_tracker["LFG"][1]:
            self.update_progress("LFG", comic_tracker, comic_tracker_copy)
            self.master.update()
            comic_tracker["LFG"][0] = comics.download_lfg(program_abs_path, comic_tracker["LFG"][0])
        if not comic_tracker["LOVENSTEIN"][1]:
            self.update_progress("LOVENSTEIN", comic_tracker, comic_tracker_copy)
            self.master.update()
            comic_tracker["LOVENSTEIN"][0] = comics.download_lovenstein(program_abs_path, comic_tracker["LOVENSTEIN"][0])
        if not comic_tracker["STICK"][1]:
            self.update_progress("STICK", comic_tracker, comic_tracker_copy)
            self.master.update()
            comic_tracker["STICK"][0] = comics.download_order_of_the_stick(program_abs_path, comic_tracker["STICK"][0])
        if not comic_tracker["CHAPEL"][1]:
            self.update_progress("CHAPEL", comic_tracker, comic_tracker_copy)
            self.master.update()
            comic_tracker["CHAPEL"][0] = comics.download_chapel(program_abs_path, comic_tracker["CHAPEL"][0])
        if not comic_tracker["WUKRII"][1]:
            self.update_progress("WUKRII", comic_tracker, comic_tracker_copy)
            self.master.update()
            comic_tracker["WUKRII"][0] = comics.download_wukrii(program_abs_path, comic_tracker["WUKRII"][0])
        if not comic_tracker["XKCD"][1]:
            self.update_progress("XKCD", comic_tracker, comic_tracker_copy)
            self.master.update()
            comic_tracker["XKCD"][0] = comics.download_xkcd(program_abs_path, comic_tracker["XKCD"][0])
        os.chdir(program_abs_path)
        self.update_progress(None, comic_tracker, comic_tracker_copy)

    def update_progress(self, comic, comic_tracker, comic_tracker_copy):
        """Updates text for the progress label."""
        comic_names = {"ABSTRUSE":"Abstruse Goose", "CYANIDE":"Cyanide & Happiness",
                       "LFG":"LFG", "LOVENSTEIN":"Lovenstein", "STICK":"Order of the Stick",
                       "CHAPEL":"The Chapel", "WUKRII":"Wukrii", "XKCD":"XKCD",
                       None:None}
        comic = comic_names[comic]
        if comic is None:
            result = ["All downloads are now finished."]
            for comic_name in comic_tracker:
                new_comics = comic_tracker[comic_name][0] - comic_tracker_copy[comic_name][0]
                if comic_tracker[comic_name][1]:
                    continue
                if new_comics == 0:
                    result.append(f"{comic_names[comic_name]}: 0")
                else:
                    result.append(f"{comic_names[comic_name]}: {new_comics}")
            result = "\n".join(result)
            self.progress_msg_value.set(result)
        else:
            self.progress_msg_value.set(f"Downloading {comic} comics...")
