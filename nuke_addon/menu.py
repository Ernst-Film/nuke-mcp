"""Nuke menu integration for NukeMCP.

Place this file (and nuke_mcp_addon.py) in your .nuke directory or NUKE_PATH.
"""

import nuke

toolbar = nuke.menu("Nodes")
nuke_mcp_menu = toolbar.addMenu("NukeMCP")
nuke_mcp_menu.addCommand(
    "Start Server",
    "import nuke_mcp_addon; nuke_mcp_addon.start()",
)

# Start the server in the background as soon as Nuke's GUI comes up, so an MCP
# client can connect without anyone opening the panel. "Start Server" above
# still opens the panel (and takes the port over).
import nuke_mcp_addon
nuke_mcp_addon.autostart()
