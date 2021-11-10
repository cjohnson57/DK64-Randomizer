# Developed by Isotarge
# Modified for Browser/Brython by Ballaam

from hashlib import md5
from browser import window
import json

pointer_tables = [
	{
		"index": 0,
		"name": "Music MIDI",
	},
	{
		"index": 1,
		"name": "Map Geometry",
	},
	{
		"index": 2,
		"name": "Map Walls",
		"dont_overwrite_uncompressed_sizes": True,
	},
	{
		"index": 3,
		"name": "Map Floors",
		"dont_overwrite_uncompressed_sizes": True,
	},
	{
		"index": 4,
		"name": "Object Model 2 Geometry",
	},
	{
		"index": 5,
		"name": "Actor Geometry",
	},
	{
		"index": 6,
		"name": "Unknown 6",
		"dont_overwrite_uncompressed_sizes": True,
	},
	{
		"index": 7,
		"name": "Textures (Uncompressed)",
		"dont_overwrite_uncompressed_sizes": True,
	},
	{
		"index": 8,
		"name": "Map Cutscenes",
	},
	{
		"index": 9,
		"name": "Map Object Setups",
	},
	{
		"index": 10,
		"name": "Map Object Model 2 Behaviour Scripts",
	},
	{
		"index": 11,
		"name": "Animations",
		"dont_overwrite_uncompressed_sizes": True,
	},
	{
		"index": 12,
		"name": "Text",
	},
	{
		"index": 13,
		"name": "Unknown 13",
	},
	{
		"index": 14,
		"name": "Textures",
	},
	{
		"index": 15,
		"name": "Map Paths",
		"do_not_compress": True,
		"dont_overwrite_uncompressed_sizes": True,
	},
	{
		"index": 16,
		"name": "Map Character Spawners",
	},
	{
		"index": 17,
		"name": "Unknown 17",
	},
	{
		"index": 18,
		"name": "Map Loading Zones",
	},
	{
		"index": 19,
		"name": "Unknown 19",
	},
	{
		"index": 20,
		"name": "Unknown 20",
		"dont_overwrite_uncompressed_sizes": True,
	},
	{
		"index": 21,
		"name": "Map Autowalk Data",
		"do_not_compress": True,
		"dont_overwrite_uncompressed_sizes": True,
	},
	{
		"index": 22,
		"name": "Unknown 22",
	},
	{
		"index": 23,
		"name": "Map Exits",
		"do_not_compress": True,
		"dont_overwrite_uncompressed_sizes": True,
	},
	{
		"index": 24,
		"name": "Map Race Checkpoints",
	},
	{
		"index": 25,
		"name": "Textures",
	},
	{
		"index": 26,
		"name": "Uncompressed File Sizes",
		"dont_overwrite_uncompressed_sizes": True,
	},
	{
		"index": 27,
		"name": "Unknown 27",
	},
	{
		"index": 28,
		"name": "Unknown 28",
	},
	{
		"index": 29,
		"name": "Unknown 29",
	},
	{
		"index": 30,
		"name": "Unknown 30",
	},
	{
		"index": 31,
		"name": "Unknown 31",
	},
]

num_tables = len(pointer_tables)
main_pointer_table_offset = 0x101C50

# The address of the next available byte of free space in ROM
# used when appending files to the end of the ROM
#next_available_free_space = 0x1FED020
next_available_free_space = 0x2200000

# These will be indexed by pointer table index then by SHA1 hash of the data
pointer_table_files = []
for x in pointer_tables:
	pointer_table_files.append({})

force_table_rewrite = [
	# 0, # Music MIDI
	# 1, # Map Geometry
	# 2, # Map Walls
	# 3, # Map Floors
	# 4, # Object Model 2 Geometry
	# 5, # Actor Geometry
	# 7, # Textures (Uncompressed)
	# 8, # Map Cutscenes
	# 9, # Map Object Setups
	# 10, # Map Object Model 2 Behaviour Scripts
	# 11, # Animations
	# 12, # Text
	# 14, # Textures
	# 15, # Map Paths
	# 16, # Map Character Spawners
	# 18, # Map Loading Zones
	# 21, # Map Autowalk Data
	# 23, # Map Exits
	# 24, # Map Race Checkpoints
	# 25, # Textures
]

def lstToInt(lst):
    total = 0;
    for x in lst:
        total *= 256;
        total += x;
    return total

def reverse(lst):
    return [ele for ele in reversed(lst)]

def intToLst(int_,cap):
    lst = [];
    while (cap > 0):
        offset = int_ % 256;
        lst.append(offset)
        int_ -= offset;
        int_ /= 256;
        cap -= 1;
    return reverse(lst)

def make_safe_filename(s : str):
    def safe_char(c : str):
        if c.isalnum():
            return c
        else:
            return "_"
    return "".join(safe_char(c) for c in s).rstrip("_")

def simple_hash(lst):
	hsh = 0;
	for x in range(lst):
		hsh += (lst[x] * x);
	return hex(hsh % 0xFFFFFFF);


def getOriginalUncompressedSize(pointer_table_index : int, file_index : int):
	global pointer_tables

	if "dont_overwrite_uncompressed_sizes" in pointer_tables[pointer_table_index]:
		return 0

	ROMAddress = pointer_tables[26]["entries"][pointer_table_index]["absolute_address"] + file_index * 4

	# print("Reading size for file " + str(pointer_table_index) + "->" + str(file_index) + " from ROM address " + hex(ROMAddress))

	window.patchedRom.seek(ROMAddress)
	return lstToInt(window.patchedRom.readBytes(4))

# Write the new uncompressed size back to ROM to prevent malloc buffer overruns when decompressing
def writeUncompressedSize(pointer_table_index : int, file_index : int, uncompressed_size : int):
	global pointer_tables

	if "dont_overwrite_uncompressed_sizes" in pointer_tables[pointer_table_index]:
		return 0

	ROMAddress = pointer_tables[26]["entries"][pointer_table_index]["absolute_address"] + file_index * 4

	print(" - Writing new uncompressed size " + hex(uncompressed_size) + " for file " + str(pointer_table_index) + "->" + str(file_index) + " to ROM address " + hex(ROMAddress))

	window.patchedRom.seek(ROMAddress)
	window.patchedRom.writeBytes(lstToInt(uncompressed_size, 4))

def parsePointerTables():
	global pointer_tables
	global main_pointer_table_offset
	global num_tables

	# Read pointer table addresses
	print("Reading Pointer Table Addresses")
	offset = 0;
	for x in pointer_tables:
		window.patchedRom.seek(main_pointer_table_offset + offset)
		offset += 4;
		absolute_address = lstToInt(window.patchedRom.readBytes(4)) + main_pointer_table_offset
		x["absolute_address"] = absolute_address
		x["new_absolute_address"] = absolute_address

	# Read pointer table lengths
	print("Reading Pointer Table Lengths")
	window.patchedRom.seek(main_pointer_table_offset + num_tables * 4)
	offset = 0;
	for x in pointer_tables:
		window.patchedRom.seek(main_pointer_table_offset + (num_tables * 4) + offset)
		offset += 4;
		x["num_entries"] = lstToInt(window.patchedRom.readBytes(4))
		x["entries"] = []

	# Read pointer table entries
	print("Reading Pointer Table Entries")
	for x in pointer_tables:
		if x["num_entries"] > 0:
			for i in range(x["num_entries"]):
				# Compute address and size information about the pointer
				window.patchedRom.seek(x["absolute_address"] + i * 4)
				raw_int = lstToInt(window.patchedRom.readBytes(4))
				absolute_address = (raw_int & 0x7FFFFFFF) + main_pointer_table_offset
				window.patchedRom.seek(x["absolute_address"] + (i * 4) + 4)
				next_absolute_address = (lstToInt(window.patchedRom.readBytes(4)) & 0x7FFFFFFF) + main_pointer_table_offset
				x["entries"].append({
					"index": i,
					"pointer_address": hex(x["absolute_address"] + i * 4),
					"absolute_address": absolute_address,
					"new_absolute_address": absolute_address,
					"next_absolute_address": next_absolute_address,
					"bit_set": (raw_int & 0x80000000) > 0,
					"original_sha1": "",
					"new_sha1": "",
				})

	# Read data and original uncompressed size
	# Note: Needs to happen after all entries are read for annoying reasons
	print("Reading Data and uncompressed size")
	for x in pointer_tables:
		if x["num_entries"] > 0:
			for y in x["entries"]:
				if not y["bit_set"]:
					absolute_size = y["next_absolute_address"] - y["absolute_address"]
					if absolute_size > 0:
						file_info = addFileToDatabase(y["absolute_address"], absolute_size, x["index"], y["index"])

	# Go back over and look up SHA1s for the bit_set entries
	# Note: Needs to be last because it's possible earlier entries point to later entries that might not have data yet
	print("Cross-Referencing Hash")
	for x in pointer_tables:
		if x["num_entries"] > 0:
			for y in x["entries"]:
				if y["bit_set"]:
					window.patchedRom.seek(y["absolute_address"])
					lookup_index = lstToInt(window.patchedRom.readBytes(2))
					file_info = getFileInfo(x["index"], lookup_index)
					if file_info:
						y["original_sha1"] = file_info["sha1"]
						y["new_sha1"] = file_info["sha1"]
						#y["bit_set"] = False # We'll turn this back on later when recomputing pointer tables
	window.pointer_tables = json.dumps(pointer_tables);

def addFileToDatabase(absolute_address : int, absolute_size: int, pointer_table_index : int, file_index : int):
	global pointer_tables
	global pointer_table_files

	# TODO: Get rid of this check
	for x in pointer_tables:
		if x["absolute_address"] == absolute_address:
			print("WARNING: POINTER TABLE " + str(x["index"]) + " BEING USED AS FILE!")
			return

	window.patchedRom.seek(absolute_address)
	data = window.patchedRom.readBytes(absolute_size)
	dataSHA1Hash = simple_hash(data);

	pointer_tables[pointer_table_index]["entries"][file_index]["original_sha1"] = dataSHA1Hash
	pointer_tables[pointer_table_index]["entries"][file_index]["new_sha1"] = dataSHA1Hash

	pointer_table_files[pointer_table_index][dataSHA1Hash] = {
		"new_absolute_address": absolute_address,
		"data": data,
		"sha1": dataSHA1Hash,
		"uncompressed_size": getOriginalUncompressedSize(pointer_table_index, file_index),
	}
	return pointer_table_files[pointer_table_index][dataSHA1Hash]

def getFileInfo(pointer_table_index : int, file_index : int):
	global pointer_tables
	global pointer_table_files
	if not pointer_table_index in range(len(pointer_tables)):
		return

	if not file_index in range(len(pointer_tables[pointer_table_index]["entries"])):
		return

	if not pointer_tables[pointer_table_index]["entries"][file_index]["new_sha1"] in pointer_table_files[pointer_table_index]:
		return

	return pointer_table_files[pointer_table_index][pointer_tables[pointer_table_index]["entries"][file_index]["new_sha1"]]

def replaceROMFile(pointer_table_index : int, file_index : int, data: bytes, uncompressed_size : int):
	global pointer_tables
	global pointer_table_files

	# TODO: Get this working
	if pointer_table_index == 8 and file_index == 0:
		print(" - WARNING: Tried to replace Test Map cutscenes. This will replace global cutscenes, so it has been disabled for now to prevent crashes.")
		return

	# Align data to 2 byte boundary for DMA
	if (len(data) % 2 == 1):
		data_array = bytearray(data)
		data_array.append(0)
		data = bytes(data_array)

	# Insert the new data into the database
	dataSHA1Hash = simple_hash(data)
	pointer_table_files[pointer_table_index][dataSHA1Hash] = {
		"data": data,
		"sha1": dataSHA1Hash,
		"uncompressed_size": uncompressed_size,
	}

	# Update the entry in the pointer table to point to the new data
	pointer_tables[pointer_table_index]["entries"][file_index]["new_sha1"] = dataSHA1Hash

def shouldWritePointerTable(index : int):
	global pointer_tables

	# Table 6 is nonsense.
	# Table 26 is a special case, it should never be manually overwritten
	# Instead, it should be recomputed based on the new uncompressed file sizes of the replaced files
	# This fixes heap corruption caused by a buffer overrun when decompressing a replaced file into a malloc'd buffer
	if index in [6, 26]:
		return False

	# No need to recompute pointer tables with no entries in them
	if pointer_tables[index]["num_entries"] == 0:
		return False

	if index in force_table_rewrite:
		return True

	# TODO: Better logic for this
	if pointer_tables[index]:
		for y in pointer_tables[index]["entries"]:
			if y["original_sha1"] != y["new_sha1"]:
				return True

	return False

def writeModifiedPointerTablesToROM():
	global next_available_free_space
	global pointer_tables
	global main_pointer_table_offset

	# Reserve pointer table space and write new data
	for x in pointer_tables:
		if not shouldWritePointerTable(x["index"]):
			continue

		# Reserve free space for the pointer table in ROM
		space_required = x["num_entries"] * 4 + 4
		should_relocate = shouldWritePointerTable(x["index"])
		earliest_file_address = 0
		if should_relocate:
			x["new_absolute_address"] = next_available_free_space
			next_available_free_space += space_required
			earliest_file_address = next_available_free_space

		# Append all files referenced by the pointer table to ROM
		for y in x["entries"]:
			file_info = getFileInfo(x["index"], y["index"])
			if file_info:
				if len(file_info["data"]) > 0:
					if should_relocate:
						# Append the file to the ROM at the address of the next available free space
						y["new_absolute_address"] = next_available_free_space
						# Move the free space pointer along
						next_available_free_space += len(file_info["data"])
					window.patchedRom.seek(y["new_absolute_address"])
					window.patchedRom.writeBytes(file_info["data"])

	# Recompute the pointer tables using the new file addresses and write them in the reserved space
	for x in pointer_tables:
		if not shouldWritePointerTable(x["index"]):
			continue

		adjusted_pointer = 0
		next_pointer = 0
		for y in x["entries"]:
			file_info = getFileInfo(x["index"], y["index"])
			if file_info:
				# Pointers to regular files calculated as normal
				adjusted_pointer = y["new_absolute_address"] - main_pointer_table_offset
				next_pointer = y["new_absolute_address"] + len(file_info["data"]) - main_pointer_table_offset

				# Update the uncompressed filesize
				if y["original_sha1"] != y["new_sha1"]:
					writeUncompressedSize(x["index"], y["index"], file_info["uncompressed_size"])
			else:
				adjusted_pointer = next_pointer

			# Fix for tables with no entry at slot 0
			if adjusted_pointer == 0:
				adjusted_pointer = earliest_file_address - main_pointer_table_offset
				next_pointer = earliest_file_address - main_pointer_table_offset

			# Update the pointer
			window.patchedRom.seek(x["new_absolute_address"] + y["index"] * 4)
			window.patchedRom.writeBytes(intToLst(adjusted_pointer,4))
			window.patchedRom.writeBytes(intToLst(next_pointer,4))

		# Redirect the global pointer to the new table
		window.patchedRom.seek(main_pointer_table_offset + x["index"] * 4)
		window.patchedRom.writeBytes(intToLst((x["new_absolute_address"] - main_pointer_table_offset),4))