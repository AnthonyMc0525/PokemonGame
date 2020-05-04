Original pokemon game in progress.

Will be a pygames project.

All original code in src folder.

**For devs who work on the project:**

Create a virtual environment in the top level of the project:
`python3 -m venv ./venv`

To run the virtual environment run:
`source venv/bin/activate`

To leave the virtual environment:
`deactivate`

In a virtual environment install pygame and pytmx:
`pip3 install pygame`
`pip install pytmx`


To add a wall to a map, create an object layer in Tiled. It doesn't have to be named "obstacles", but doing so keeps everything uniform. draw your objects as needed, and make the name property and type property "wall".

To add an NPC to a map, make sure there's an existing sprite for the NPC already in /assets/images with their name and `_npc.png` at the end. For example: `assets/images/maple_npc.png`. Create an object in an object layer in Tiled. It should be 16 units wide and 32 units tall. Make the name property whatever you'd like, as this will be implemented if this will be developed outside of schooling. Make the type property "NPC", case sensitive. You will need to add custom properties. Add a "spawn_name" property as a string, with their name in lowercase. It should point to their file without the "\_npc.png" suffix. For example, Professor Maple's spawn_name property would simply say `maple`. Add another custom field called "interact", as a boolean. Check it if you'd like. This is another field to be implemented later on if this will be developed further, for non-interactive NPCs. Finally, add a custom property called "dialogue" as a string. Add your dialogue as you please, adding line breaks with "|" and new dialogue windows with "%".

By default, the player stays in the arena map.
