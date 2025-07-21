# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# DISCLAIMER: This software is provided "as is" without any warranty,
# express or implied, including but not limited to the warranties of
# merchantability, fitness for a particular purpose, and non-infringement.
#
# In no event shall the authors or copyright holders be liable for any
# claim, damages, or other liability, whether in an action of contract,
# tort, or otherwise, arising from, out of, or in connection with the
# software or the use or other dealings in the software.
# -----------------------------------------------------------------------------

# @Author  : Tek Raj Chhetri
# @Email   : tekraj@mit.edu
# @Web     : https://tekrajchhetri.com/
# @File    : main.py
# @Software: PyCharm
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Resources")

@mcp.resource("inventory://overview")
def get_inventory_overview() -> str:
    """
    Returns overview of inventory
    """
    # Sample inventory overview
    overview = """
    Inventory Overview:
    - Coffee
    - Tea
    - Cookies
    """
    return overview.strip()

inventory_id_to_price = {
    "123": "6.99",
    "456": "17.99",
    "789": "84.99"
}

inventory_name_to_id = {
    "Coffee": "123",
    "Tea": "456",
    "Cookies": "789"
}

@mcp.resource("inventory://{inventory_id}/price")
def get_inventory_price_from_inventory_id(inventory_id: str) -> str:
    """
    Returns price from inventory id
    """
    return inventory_id_to_price[inventory_id]

@mcp.resource("inventory://{inventory_name}/id")
def get_inventory_id_from_inventory_name(inventory_name: str) -> str:
    """
    Returns id from inventory name
    """
    return inventory_name_to_id[inventory_name]


if __name__ == "__main__":
    mcp.run()