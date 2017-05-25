# rw_patchgen
It generates patchsets for rimworld weapons based on yaml files.

Requirements: Python 3.x & lxml

I threw this together because making XML patchsets for weapons is really annoying to do when you want to be granular.

This only does one thing right now, ThingDefs. It only knows how to replace items. It has a little hack to make shooting verbs easy to do, because the person I made this for was making weapon mods.

If you'd like to contribute additional features I will gladly accept them.

# How to use
rw_patchgen input.yaml output.xml
