import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import json as js
import random as rn
import re

ram_mhash = {"<params>" : 
{"<name>": "Test mhash"}}    

window = tk.Tk()

window.columnconfigure(0, minsize=80, weight=0)
window.columnconfigure(1, minsize=80, weight=1)
window.columnconfigure(2, minsize=120, weight=0)
window.rowconfigure(0, minsize=24, weight=0)
window.rowconfigure(1, minsize=400, weight=2)
window.rowconfigure(2, minsize=50, weight=1)
window.rowconfigure(3, minsize=50, weight=1)
window.rowconfigure(4, minsize=24, weight=0)

window.title("Markov Chain Demo")

# initiate frames
btns_file_frame = tk.Frame()
txts_display_frame = tk.Frame(relief=tk.RAISED, borderwidth=4, padx=2, pady=2)
btn_synapse_frame = tk.Frame(relief=tk.RAISED, borderwidth=4, padx=2, pady=2) 
entry_synapse_input_frame = tk.Frame(relief=tk.RAISED, borderwidth=4, padx=2, pady=2)
entry_sim_start_input_frame = tk.Frame(relief=tk.RAISED, borderwidth=4, padx=2, pady=2)
entry_sim_end_input_frame = tk.Frame(relief=tk.RAISED, borderwidth=4, padx=2, pady=2)
btn_sim_frame = tk.Frame(relief=tk.RAISED, borderwidth=4, padx=2, pady=2)
clamp_min_frame = tk.Frame(relief=tk.RAISED, borderwidth=4, padx=2, pady=2)
clamp_max_frame = tk.Frame(relief=tk.RAISED, borderwidth=4, padx=2, pady=2)
entry_sim_regex_frame = tk.Frame(relief=tk.RAISED, borderwidth=4, padx=2, pady=2)

var_sim_start = tk.StringVar()
var_sim_end = tk.StringVar()
var_sim_endrequired = tk.BooleanVar()
var_clamp_min = tk.IntVar()
var_clamp_max = tk.IntVar()
var_regex = tk.StringVar() 

# initiate widgets
btn_file_saveas_hashmap = tk.Button(text="Save Hashmap As...", master=btns_file_frame)
btn_file_saveas_output = tk.Button(text="Save Output Log As...", master=btns_file_frame)
btn_file_load_hashmap = tk.Button(text="Load Hashmap", master=btns_file_frame)

txt_display_hashmap_scrollbar = tk.Scrollbar(master=txts_display_frame)
txt_display_hashmap = tk.Text(bg="#ddd", state=tk.DISABLED, yscrollcommand=txt_display_hashmap_scrollbar.set, master=txts_display_frame)
txt_display_hashmap_scrollbar["command"] = txt_display_hashmap.yview

txt_display_output_scrollbar = tk.Scrollbar(master=txts_display_frame)
txt_display_output = tk.Text(bg="#ddf", state=tk.DISABLED, yscrollcommand=txt_display_output_scrollbar.set, master=txts_display_frame)
txt_display_output_scrollbar["command"] = txt_display_output.yview

entry_synapse_input_label = tk.Label(master=entry_synapse_input_frame, text="Input string:")
entry_synapse_input = tk.Entry(master=entry_synapse_input_frame)
btn_synapse = tk.Button(text="Synapse", master=btn_synapse_frame)

entry_sim_start_input_label = tk.Label(master=entry_sim_start_input_frame, text="Simulation start key:")
entry_sim_start_input = tk.Entry(master=entry_sim_start_input_frame, textvariable=var_sim_start)
entry_sim_end_input_label = tk.Label(master=entry_sim_end_input_frame, text="Simulation end key:")
entry_sim_end_input = tk.Entry(master=entry_sim_end_input_frame, textvariable=var_sim_end)
chk_sim_endrequired_label = tk.Label(master=entry_sim_end_input_frame, text="End key required?")
chk_sim_endrequired = tk.Checkbutton(master=entry_sim_end_input_frame, variable=var_sim_endrequired, onvalue=True, offvalue=False)

btn_sim_generate = tk.Button(text="Generate Sim", master=btn_sim_frame)
spin_sim_generate_n = tk.Spinbox(from_=1, to=1000, master=btn_sim_frame)

clamp_min_label = tk.Label(master=clamp_min_frame, text="Clamp minimum:")
clamp_min = tk.Entry(master=clamp_min_frame, textvariable=var_clamp_min)
clamp_max_label = tk.Label(master=clamp_max_frame, text="Clamp maximum:")
clamp_max = tk.Entry(master=clamp_max_frame, textvariable=var_clamp_max)

entry_sim_regex_label = tk.Label(master=entry_sim_regex_frame, text="Regex string:")
entry_sim_regex = tk.Entry(master=entry_sim_regex_frame, textvariable=var_regex)

# place frames on the grid
btns_file_frame.grid(row=0, column=0, sticky="se")
txts_display_frame.grid(row=1, column=0, columnspan=3, sticky="nsew")
btn_synapse_frame.grid(row=2, column=2, sticky="nesw")
entry_synapse_input_frame.grid(row=2, column=0, columnspan=2, sticky="nsew")
entry_sim_start_input_frame.grid(row=4, column=0, sticky="nse")
entry_sim_end_input_frame.grid(row=4, column=1, sticky="nsw")
btn_sim_frame.grid(row=4, column=2, sticky="nsew")
clamp_min_frame.grid(row=5, column=0, sticky="ne")
clamp_max_frame.grid(row=5, column=1, sticky="nw")
entry_sim_regex_frame.grid(row=5, column=2, sticky="new")

# place widgets in their respective frame
btn_file_saveas_output.pack(side = tk.RIGHT)
btn_file_saveas_hashmap.pack(side = tk.RIGHT)
btn_file_load_hashmap.pack(side = tk.RIGHT)

# mhash display
txt_display_hashmap.pack(side=tk.LEFT, fill=tk.BOTH)
txt_display_hashmap_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
# output log display
txt_display_output.pack(side=tk.LEFT, fill=tk.BOTH)
txt_display_output_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

entry_synapse_input_label.pack()
entry_synapse_input.pack(fill=tk.X)
btn_synapse.pack(side = tk.LEFT)

entry_sim_start_input_label.pack()
entry_sim_start_input.pack()
entry_sim_end_input_label.pack()
entry_sim_end_input.pack()
chk_sim_endrequired_label.pack(side = tk.LEFT)
chk_sim_endrequired.pack(side = tk.LEFT)

btn_sim_generate.pack(side = tk.LEFT)
spin_sim_generate_n.pack(side = tk.LEFT)

clamp_min_label.pack()
clamp_max_label.pack()
clamp_min.pack(fill=tk.X)
clamp_max.pack(fill=tk.X)
entry_sim_regex_label.pack(fill=tk.X)
entry_sim_regex.pack(fill=tk.X)

# start focused on the synapse input box
entry_synapse_input.focus()

# compiles words seperated by <space> into an mhash (markov hashmap)
def synapse_str(self, str):
    print("Beginning synapse of str: {}".format(str))
    mhash = {}
    fail_index_curr = [] #save failed indices to recheck them at the end after all keys have been initiated at both levels
    fail_index_next = [] 
    str_list = str.split()

    for i in range(len(str_list)): #dive into each part of the str as a list so that the "next" index may be referenced
        _curr = str_list[i] #current part of str
        try:
            _next = str_list[i + 1] #next part of str or "<end>" if string completed
        except IndexError:
            _next = "<end>"

        try:
            mhash[_curr][_next] = mhash[_curr][_next] + 1 #increases occurences by one if both dict keys (1d and 2d) are initiated

        except KeyError:
            fail_index_curr.append(_curr) #saves indices for recheck after all keys have been initiated
            fail_index_next.append(_next)

            try:
                mhash[_curr][_next] = 1 #tries to initiate the 2d key with a one, unless 2d key is not initiated
                fail_index_curr.pop() #pop off fail rechecks if we were able to just initiate the key
                fail_index_next.pop()

            except KeyError:
                try:
                    mhash[_curr] = {} #initiates 1d key with a blank dict
                except KeyError:
                    pass
    
    for i in range(len(fail_index_curr)): #rechecking failed indices after at least all 1d keys have been initiated
        try:
            mhash[fail_index_curr[i]][fail_index_next[i]] = mhash[fail_index_curr[i]][fail_index_next[i]] + 1 #increases 2d key
        except KeyError:
            mhash[fail_index_curr[i]][fail_index_next[i]] = 1 #initiates 2d key
    
    return mhash

# dict_a recommended to be larger dict
# THIS ONLY WORKS ON ONE DIMENSIONAL DICTS WITH INTS, USE merge_mhashs to combine mhashes
def merge_dicts(dict_a, dict_b):
    output_dict = {}

    for key in dict_a: #here we start by assigning each key in dict_a to the output_dict
        try:
            output_dict[key] = dict_a[key]
        except KeyError as e:
            print("Error at {}:{}".format(key, e)) #should be no errors, but here just to be safe for a second

    for key in dict_b: #here we will actually merge dict_a into dict_b
        try:
            output_dict[key] = output_dict[key] + dict_b[key] #checks if key exists in output_dict and if so adds dict_b's occurence
        except KeyError as e:
            output_dict[key] = dict_b[key] #here it would create a new key in case there is a key in dict_b that was not in dict_a

    return output_dict

# Mhash (markov hashmap) only contains occurences of each outcome, probabilities to be generated at simulation level
# Merges hash_b INTO hash_a, all keys that are found in hash_a plus keys only found in hash_b will be returned in an mhash
def merge_mhashs(hash_a, hash_b)  :  
    output_dict = hash_a #start by copying hash_a to our output, so that we can just merge common keys and create new keys within it
    ab_common_keys = [] #a running list of keys that are found in both A and B

    for keys_a in hash_a:   #runs through each primary key in hash_a WILL ONLY DETECT KEYS COMMON WITH B OR UNCOMMON WITH B, WILL NEED TO RUN THROUGH B AS WELL TO DETECT THOSE UNCOMMON WITH A, we can flag all those in b found to be common with a simply skip them
                            #[keys_a] is the top-level KEY in hash_a
                            #[hash_a[keys_a]] is the OCCURENCE DICT of that KEY (all we need to merge_dict)

        try:                #tries to open each primary key of hash_a IN hash_b to see if it is common; if it is, it is added as a common key to the running list
                            #[hash_b[keys_a]] is the OCCURENCE DICT of the current key [keys_a] in hash_b (to merge_dict)
            output_dict[keys_a] = merge_dicts(hash_a[keys_a], hash_b[keys_a]) #this will merge all keys that are common to a and b, DOES NOT INCLUDE KEYS UNCOMMON TO A AND B THAT ARE ONLY FOUND IN B
            ab_common_keys.append(keys_a) #marks this key as common and will thus be skipped over in the hash_b check

        except KeyError: #throws if an uncommon key is found in hash_a, this is OKAY because hash_b is to be "added" into hash_a
            pass

    for keys_b in hash_b: #runs through each key in hash_b
        if keys_b not in ab_common_keys: #only cares about keys that were uncommon to hash_a
            output_dict[keys_b] = hash_b[keys_b] #creates new key in output_dict with the uncommon key and fills it with hash_b's OCCURENCE DICT of that key

    return output_dict

# Simulates a single markov outcome, the basis of all simulations
def markov(mhash, key):
    try:
        outcomes = [] # this will be a list of each possible outcome and each outcome will occur the number of times in the mhash
        i = -1 # start at -1 so that it lines up with 0 indexed list
        for outcome in mhash[key]:
            try: # will catch TypeErrors generated by a failed markov sim upstream
                for j in range((mhash[key][outcome] + i) - i): # this calculates the number of occurences and appends it to the occurences list that many times
                    outcomes.append(outcome)
                    j = j #TODO: if anyone knows of a better way to get the warning to shut up I welcome it lol

                i = (mhash[key][outcome] + i) # increases i by the number of times the outcome occurred 
            except TypeError as e:
                print(f"[markov({mhash}, {key})] TypeError: outcomes list {outcomes}, mhash[key] {mhash[key]}: {e}") # if a TypeError is caught, likely due to a failed sim upstream
                return False

        rand_int = rn.randint(0, len(outcomes)-1) 

        try:
            return outcomes[rand_int] # gets a random outcome from outcomes 
        except IndexError as e:
            print(f"[markov({mhash}, {key})] IndexError: outcomes list {outcomes}, random {rand_int}: {e}") # if out of range for some reason (empty list)
            return False
        
    except KeyError:
        return False

# attempts to generate a solution with the given parameters
# mhash: Hashmap to use for simulation
# start: Key to start with, DEFAULT a random key from hashmap 
# end:   Key to end sim at, DEFAULT "<end>"
# minlength: Minimum length of solution, returns False if solution doesn't meet it
# maxlength: Maximum length of solution, cuts simulation off if this number is reached (SEE NEXT)
# endrequired: If True, solution will only be accepted if the maxlength is met AND the end key is met
# regex: A regular expression, solution will only be accepted if regex returns 1 or more on findall operation IS LAST CHECK, STACKS WITH OTHER PARAMS
# seperator: string to combine outcome keys with into string, DEFAULT space
def generate_simulation(mhash, start=False, end="<end>", minlength=-1, maxlength=100, endrequired=False, regex=False, seperator=" "): 
    potential_outcome = []

    if start:                                                           # triggers if we have a start key
        potential_outcome.append(start) # adds start key to potential outcome
        while potential_outcome[len(potential_outcome) - 1] != end and len(potential_outcome) < maxlength: # run the loop until maxlength is reached or the end key is found at the last index of potential_outcome
            potential_outcome.append(markov(mhash, potential_outcome[len(potential_outcome) - 1]))
        
    else:                                                               # triggers with no start key
        possible_keys = [] # find a random start key
        for key in mhash:
            possible_keys.append(key)

        start = possible_keys[rn.randint(0,len(possible_keys)-1)] # sets start to random key
        potential_outcome.append(start) # adds start key to potential outcome
        while potential_outcome[len(potential_outcome) - 1] != end and len(potential_outcome) < int(maxlength): # run the loop until maxlength is reached or the end key is found at the last index of potential_outcome
            potential_outcome.append(markov(mhash, potential_outcome[len(potential_outcome) - 1]))

    if endrequired and potential_outcome[len(potential_outcome) - 1] != end: # if the endrequired param is True and end key is wrong, returns False 
        return False

    if minlength > 0 and len(potential_outcome) < minlength: # if the minlength is set proper, returns false if not met
        return False

    try:
        final_outcome_string = seperator.join(potential_outcome) # combines keys into outcome using seperator param
    except TypeError as e:
        print(f"Simulation Failure: while trying to process outcomes to string. {e}")
        return False
    
    if regex:
        if len(re.findall(regex, final_outcome_string)) < 1: # only passes if the regex findall returns 1 or more 
            return False
    
    return final_outcome_string

# this is the function called when the "Synapse" button is clicked
# Synapses the input string, merges it with the mhash stored in the txt_display_hashmap, and clears everything
def syn_entry_synapse_input(self):
    txt_display_hashmap["state"] = tk.NORMAL # makes the text display box interactable which we need
    temp = merge_mhashs(js.loads(txt_display_hashmap.get("1.0", tk.END)), synapse_str(0, entry_synapse_input.get())) # pulls the json dict stored in the text display box and combines it with a synapse of the text in the entry box
    
    json_mhash = js.dumps(temp) # packs the combined mhashs into json
    txt_display_hashmap.delete("1.0", tk.END) # clear text display
    entry_synapse_input.delete(0, tk.END) # clears input box
    txt_display_hashmap.insert("1.0", json_mhash) # dumps the combined mhashs into the display text box
    txt_display_hashmap["state"] = tk.DISABLED # turns text display off again

# this is the function called when the "Generate simulation" button is clicked
# takes in all parameters from entry fields, runs generate_simulation until specified number of solutions are successfully generated.
# successful solutions are stored in the output log
def run_simulation_params(self):
    killat = 10000
    attempts = 0
    successes = 0

    txt_display_output["state"] = tk.NORMAL # allows us to edit the output display, TODO: try and break this, I don't want to have to put it in the while loop but I will if I have to

    while successes < int(spin_sim_generate_n.get()) and attempts < killat: # hardocded to kill the sim at "killat iterations
        attempts = attempts + 1

        outcome = generate_simulation(
            js.loads(txt_display_hashmap.get("1.0", tk.END)),
            start=var_sim_start.get(),
            end=var_sim_end.get(),
            endrequired=var_sim_endrequired.get(),
            minlength=var_clamp_min.get(),
            maxlength=var_clamp_max.get(),
            regex=var_regex.get()
            )

        if outcome:
            txt_display_output.insert(tk.END, "\n{}".format(outcome))
            successes = successes + 1

    if attempts >= killat:
        print(f"Simulation could not find solution after {attempts} iterations (0 percent success rate)")
    else:
        print("Completed requested simulations, {}, in {} attempts ({} percent success rate)".format(successes, attempts, int((successes/attempts) * 100)))
    
    txt_display_output["state"] = tk.DISABLED

# save your current hashmap to a .json file
def file_save_mhash(self):
    save_path = tk.filedialog.asksaveasfilename(defaultextension="json", filetypes=[("JSON Files", "*.json"), ("All Files", "*.*")])

    if not save_path:
        return False

    with open(save_path, "w") as output_file:
        str_ = txt_display_hashmap.get("1.0", tk.END)
        output_file.write(str_)

# load a saved hashmap from a .json file
def file_open_mhash(self):
    file_path = tk.filedialog.askopenfilename(filetypes=[("JSON Files", "*.json"), ("All Files", "*.*")])

    if not file_path:
        return False
    
    txt_display_hashmap["state"] = tk.NORMAL # makes the text display box interactable which we need
    txt_display_hashmap.delete("1.0", tk.END) # clear it to make way for the new

    with open(file_path, "r") as to_load:
        str_ = to_load.read()
        txt_display_hashmap.insert(tk.END, str_)
        txt_display_hashmap["state"] = tk.DISABLED # text display uneditable again

# puts the ram_mhash into the text display box
txt_display_hashmap["state"] = tk.NORMAL # makes the text display box interactable which we need
json_mhash = js.dumps(ram_mhash) # packs the ram_mhash dict into json
txt_display_hashmap.delete("1.0", tk.END) # clear text display (shouldn't be neccesary but whatevs)
txt_display_hashmap.insert("1.0", json_mhash) # dumps the ram_mhash into the display text box
txt_display_hashmap["state"] = tk.DISABLED # turns text display off again

btn_synapse.bind("<Button-1>", syn_entry_synapse_input)
btn_sim_generate.bind("<Button-1>", run_simulation_params)
btn_file_saveas_hashmap.bind("<Button-1>", file_save_mhash)
btn_file_load_hashmap.bind("<Button-1>", file_open_mhash)

# quick little QOL that allows you to hit enter to synapse while editing the input
def synapse_input_keys(event):
    try:
        if event.keycode == 2359309:
            syn_entry_synapse_input(0)   
    except:
        pass
entry_synapse_input.bind("<Key>", synapse_input_keys)

window.mainloop()
print("Window closed.")